"""
To efficiently solve this problem, you can use a **Divide and Conquer strategy** or leverage **Binary Indexed Trees (Fenwick Trees)**. However, a more straightforward and commonly used method involves the following steps:


1. **Compute Prefix Sums:**
   - Calculate the prefix sums of the array to transform the problem into finding the number of pairs `(i, j)` where `i < j` and `prefix[j] - prefix[i]` falls within `[lower, upper]`.


2. **Sort the Prefix Sums:**
   - Maintain a sorted list of prefix sums encountered so far. For each new prefix sum, use binary search to find how many existing prefix sums fall within the range `[current_prefix - upper, current_prefix - lower]`.


3. **Count Valid Ranges:**
   - Use the `bisect` module in Python to perform efficient binary searches within the sorted prefix sums.


4. **Update the Sorted List:**
   - After counting, insert the current prefix sum into the sorted list to be used in future iterations.


### Explanation of the Optimized Approach:


**Prefix Sum Calculation:**
   - Compute the prefix sums and store them in the `prefix` list.


**Sorted Prefix List:**
   - Initialize an empty `sorted_prefix` list to maintain the prefix sums in sorted order.


**Counting Valid Ranges:**
   - For each prefix sum `p`, determine the range `[p - upper, p - lower]`.
   - Use `bisect_left` to find the first index where a prefix sum is `>= p - upper`.
   - Use `bisect_right` to find the first index where a prefix sum is `> p - lower`.
   - The difference `right - left` gives the number of prefix sums within the desired range.


**Insertion:**
   - Insert the current prefix sum `p` into the `sorted_prefix` list while maintaining the sorted order using `bisect.insort`.


### Time Complexity Analysis:


- **Prefix Sum Calculation:** O(n)
- **For Each Prefix Sum:**
   - **Binary Search (bisect_left and bisect_right):** O(log n)
   - **Insertion (bisect.insort):** O(n) in the worst case (since `bisect.insort` may require shifting elements)


- **Overall Time Complexity:** O(n²) in the worst case due to the insertion step, but on average, it performs better and is acceptable for moderate input sizes.


### Alternative: Using a **Binary Indexed Tree** or **Merge Sort**


For larger input sizes, where the above approach may not be efficient enough, consider using more advanced data structures like **Binary Indexed Trees (Fenwick Trees)** or **Segment Trees** combined with **Coordinate Compression**. These can bring down the time complexity significantly, but they are more complex to implement.


### Conclusion and Recommendations:


**Why Your Approach Fails:**
   - The primary issue with your current solution is the inefficiency caused by iterating through every number in the `[lower, upper]` range for each prefix sum. This results in a time complexity that is too high for large inputs.


**Optimized Solution:**
   - Utilize a sorted list with binary search (`bisect` module) to efficiently count the number of valid prefix sums within the desired range. This reduces the time complexity and avoids unnecessary iterations.


**Further Improvements:**
   - For even better performance on larger datasets, explore advanced data structures like **Binary Indexed Trees** or implement a **Divide and Conquer approach** with a modified merge sort.
"""




from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Compute prefix sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
       
        # Define the recursive merge sort function
        def merge_sort(start: int, end: int) -> int:
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid, end)
           
            j = k = mid
            for left in prefix[start:mid]:
                # Find the first index in the right half where prefix[k] - left >= lower
                while k < end and prefix[k] - left < lower:
                    k += 1
                # Find the first index in the right half where prefix[j] - left > upper
                while j < end and prefix[j] - left <= upper:
                    j += 1
                count += j - k
           
            # Merge step
            prefix[start:end] = sorted(prefix[start:end])
            return count
       
        return merge_sort(0, len(prefix))

