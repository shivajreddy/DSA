"""
### Approach:

#### Frequency Count:
First, count the frequency of each task using a hashmap (`hm`). This will tell 
us how often each task needs to be scheduled.

#### Max-Heap:
Since the task with the highest frequency should be scheduled first, we use a 
max-heap to always pick the task with the highest remaining frequency. We push 
the negative of the frequency into the heap to simulate a max-heap using 
Python's `heapq`, which is a min-heap by default.

#### Cooldown Management:
While scheduling, we keep track of tasks in a "cooldown" period. After picking 
a task from the heap, we add it to a list of tasks that cannot be executed for 
`n` intervals. We simulate each time unit and check if there are tasks ready to 
be executed, maintaining a count of the total intervals.

#### Edge Cases:
- If there are idle periods, we need to account for them in the result.
- If the heap becomes empty and there are still tasks in the cooldown, we must 
  still count idle intervals.

#### Time Complexity:
- **Heap Operations**: Each heap operation (insertion, deletion) is `O(log k)`, 
  where `k` is the number of unique tasks.
- **Overall Complexity**: The loop runs at most `n` times (where `n` is the 
  number of tasks). Thus, the overall complexity is `O(n log k)`.

#### Space Complexity:
The space complexity is `O(k)` where `k` is the number of unique tasks, used 
for the heap and hashmap.

"""


from typing import List
from collections import defaultdict
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Finds the minimum intervals needed to execute all the tasks given a cooldown period.

        Args:
        tasks (List[str]): List of tasks represented by characters.
        n (int): Cooldown period between the same tasks.

        Returns:
        int: The minimum number of intervals needed to complete all tasks.
        """

        # Step 1: Count frequency of each task
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        # Step 2: Create a max heap based on task frequency
        max_heap = [-count for count in task_count.values()]
        # heapq by default is a min-heap, so we use negative values to simulate max-heap
        heapq.heapify(max_heap)

        time = 0  # Total intervals (time)

        while max_heap:
            # List to keep track of tasks in cooldown
            cooldown_tasks = []
            # Process up to 'n + 1' tasks (or as many as available)
            for _ in range(n + 1):
                if max_heap:
                    task_count = heapq.heappop(max_heap)
                    # Decrease frequency of this task
                    if task_count + 1 < 0:
                        cooldown_tasks.append(task_count + 1)

                time += 1

                # If all tasks are done and the heap is empty
                if not max_heap and not cooldown_tasks:
                    return time

            # Push remaining tasks (from cooldown) back to the heap
            for task in cooldown_tasks:
                heapq.heappush(max_heap, task)

        return time
