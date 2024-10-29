from collections import Counter, defaultdict
import heapq
from typing import List
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # Move pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[i], unique[store_index] = unique[store_index], unique[i]
                    store_index += 1

            # Move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left: int, right: int, k_smallest: int) -> None:
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k :]


# Example usage
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = solution.topKFrequent(nums, k)
print(result)  # Output: [1, 2]


class Solutiongpt:
    """
    Time :
    Space:
    """

    def topKFrequent(self, nums, k):
        # Step 1: Build frequency map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Convert count map to a list of (element, frequency) tuples
        unique_elements = list(count.keys())

        # Step 3: Define partition function
        def partition(left, right, pivot_index):
            pivot_frequency = count[unique_elements[pivot_index]]
            # Move pivot to end
            unique_elements[pivot_index], unique_elements[right] = (
                unique_elements[right],
                unique_elements[pivot_index],
            )
            store_index = left
            # Move all elements with greater frequency to the left
            for i in range(left, right):
                if count[unique_elements[i]] > pivot_frequency:
                    unique_elements[store_index], unique_elements[i] = (
                        unique_elements[i],
                        unique_elements[store_index],
                    )
                    store_index += 1
            # Move pivot to its final place
            unique_elements[right], unique_elements[store_index] = (
                unique_elements[store_index],
                unique_elements[right],
            )
            return store_index

        # Step 4: Quickselect function
        def quickselect(left, right, k_smallest):
            """
            Sort a list within left..right till k_smallest index
            """
            if left == right:  # If the list contains only one element
                return

            # Select a random pivot_index
            pivot_index = random.randint(left, right)

            # Find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # The pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
            # Go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # Go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        # Step 5: Perform quickselect on the unique_elements array
        n = len(unique_elements)
        quickselect(0, n - 1, k - 1)

        # Step 6: Return the top k elements
        return unique_elements[:k]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        unique_nums = list(count.keys())

        def partition(left, right, pivot_idx):
            pivot_frequency = count[unique_nums[pivot_idx]]

            # Swap num @ pivot_index with num @ right index
            unique_nums[pivot_idx], unique_nums[right] = (
                unique_nums[right],
                unique_nums[pivot_idx],
            )

            store_index = left

            # Move all elements with greater frequency to the left
            for i in range(left, right):
                if count[unique_nums[i]] > pivot_frequency:
                    unique_nums[store_index], unique_nums[i] = (
                        unique_nums[i],
                        unique_nums[store_index],
                    )
                    store_index += 1

            # Move pivot to its final place
            unique_nums[right], unique_nums[store_index] = (
                unique_nums[store_index],
                unique_nums[right],
            )

            return store_index

        # Sort list within left..right till k_smallest, in descending order
        def quick_select(left, right, k_smallest):
            if left == right:
                return

            # Select a random idx b/w left & right and use that as pivot idx
            pivot_idx = random.randint(left, right)

            # Find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_idx)

            # Pivot reached its final position
            if k_smallest == pivot_idx:
                return
            # Go left
            elif k_smallest < pivot_idx:
                quick_select(left, pivot_idx - 1, k_smallest)
            # Go right
            else:
                quick_select(pivot_idx + 1, right, k_smallest)

        n = len(nums)
        quick_select(0, n - 1, k - 1)

        return unique_nums[:k]


class Solution2:
    """
    Approach: Max-heap

    Time : O(n + k.log(n)), where k is the top k elements asked for
    Space: O(n) for creating the frequency & heap
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Frequency of given numbers
        num_frequency = defaultdict(int)
        for num in nums:
            num_frequency[num] += 1

        # Create Max-heap of numbers frequency
        max_freq_heap = [(-count, num) for num, count in num_frequency.items()]
        heapq.heapify(max_freq_heap)  # O(n) for creating heap

        res = []

        # Extract top k elements: O(k. log n)
        while len(res) < k:
            _, num = heapq.heappop(max_freq_heap)
            res.append(num)

        return res


class Solution3:
    """
    Time : O(n + k.log(n)), where k is the top k elements asked for
    Space: O(n) for creating the frequency & heap
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_frequency = Counter(nums)

        min_heap = []

        for num, count in num_frequency.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, num))
            else:
                heapq.heappushpop(min_heap, (count, num))

        return [num for _, num in min_heap]
