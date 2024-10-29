"""
Key Insights  
Sequential Generation:  
    - Ugly numbers can be generated in ascending order by multiplying previous 
      ugly numbers by 2, 3, or 5.  
    - The sequence starts with 1, and each subsequent ugly number is the smallest possible number that 
      can be obtained by multiplying an existing ugly number by 2, 3, or 5.  

Multiple Pointers Technique:  
    - To efficiently generate ugly numbers without duplicates, we can use three 
      pointers (`p2`, `p3`, `p5`) corresponding to multiples of 2, 3, and 5.  
    - These pointers track the position in the ugly number list that needs to be multiplied 
      by 2, 3, or 5 to find the next candidate ugly number.  

Avoiding Duplicates:  
    - By maintaining separate pointers for each prime factor and always choosing the minimum 
      among the candidates, we ensure that duplicates are avoided.  
    - For instance, 6 can be obtained by both 2 * 3 and 3 * 2. Using pointers ensures it's 
      added only once.  

Dynamic Programming (DP) Array:  
    - We'll use a DP array to store the sequence of ugly numbers up to the n-th number.  
    - Each position in the DP array is filled by selecting the minimum of the current 
      multiples of 2, 3, and 5.  


Detailed Plan  
    Initialize the DP Array:  
        - Create an array `ugly` of size n, where `ugly[i]` will hold the (i+1)-th ugly number.  
        - Initialize `ugly[0] = 1` as the first ugly number.  

    Initialize Pointers for 2, 3, and 5:  
        - `p2 = 0`, `p3 = 0`, `p5 = 0`: These pointers represent the current position in 
          the `ugly` array for multiplying by 2, 3, and 5 respectively.  

Iterate to Fill the DP Array:  
    - For each index `i` from 1 to n-1:  
    - Calculate the next multiples:  
        - `next_multiple_of_2 = ugly[p2] * 2`  
        - `next_multiple_of_3 = ugly[p3] * 3`  
        - `next_multiple_of_5 = ugly[p5] * 5`  
    - Select the minimum among these multiples as the next ugly number:  
        - `ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)`  
    - Increment the pointer(s) whose multiple matched the selected minimum to avoid duplicates:  
        - If `ugly[i] == next_multiple_of_2`, increment `p2`.  
        - If `ugly[i] == next_multiple_of_3`, increment `p3`.  
        - If `ugly[i] == next_multiple_of_5`, increment `p5`.  

Return the n-th Ugly Number:  
    - After filling the DP array, return `ugly[n-1]` as the n-th ugly number.  


Time and Space Complexity  
    Time Complexity: O(n)  
        - We perform a single pass through the array to generate the first n ugly numbers.  
    Space Complexity: O(n)  
        - We use an array of size n to store the ugly numbers.

"""


from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize the DP array
        ugly = [0] * n
        ugly[0] = 1  # The first ugly number is 1

        # Initialize pointers for multiples of 2, 3, and 5
        p2 = p3 = p5 = 0

        # Initialize the next multiples of 2, 3, and 5
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1, n):
            # Choose the smallest next multiple
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly[i] = next_ugly

            # Increment the pointer(s) for which the multiple was used
            if next_ugly == next_multiple_of_2:
                p2 += 1
                next_multiple_of_2 = ugly[p2] * 2
            if next_ugly == next_multiple_of_3:
                p3 += 1
                next_multiple_of_3 = ugly[p3] * 3
            if next_ugly == next_multiple_of_5:
                p5 += 1
                next_multiple_of_5 = ugly[p5] * 5

        # The last element in the array is the n-th ugly number
        return ugly[-1]

