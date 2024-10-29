"""
Key Insights  
    Backtracking is Ideal:  
    - Backtracking is a powerful technique for solving problems that require exploring all
      potential solutions, such as generating all possible letter combinations.  
    - It allows us to build combinations incrementally and abandon a path as soon as it determines
      that this path cannot possibly lead to a valid solution.  


Recursive Exploration:  
    - Each digit maps to a set of letters. For each digit in the input string, we need to explore all
      possible letters it can represent.  
    - By recursively building combinations, we ensure that all possible permutations are covered.  


Efficiency with Early Termination:  
    - By checking the length of the current combination against the input digits, we can terminate
      paths that have already reached the desired length, preventing unnecessary computations.  


Handling Edge Cases Gracefully:  
    - If the input string is empty, the output should be an empty list.  
    - Ensure that the solution handles digits that map to multiple letters (e.g., '7' and '9') correctly.  


Detailed Plan  
    Mapping Digits to Letters:  
    - Create a dictionary that maps each digit from 2 to 9 to its corresponding letters as per the
      telephone keypad.  


Initialize the Backtracking Process:  
    - Start with an empty combination and begin processing the digits one by one.  
    - Use a helper function (e.g., `backtrack`) to handle the recursive exploration of possible letters.  


Recursive Backtracking Function:  
    - Base Case:  
        - If the length of `current_combination` equals the length of the input digits, append the
          combination to the result list.  
    - Parameters:  
        - `index`: The current position in the input digits string.  
        - `current_combination`: The combination of letters built so far.  
    - Recursive Case:  
        - For the current digit, iterate through all its corresponding letters.  
        - For each letter, append it to the current combination and recursively call the backtracking
          function for the next digit.  
        - After returning from the recursion, remove the last letter (backtrack) to explore other possibilities.  


Return the Result:  
    - After exploring all possible combinations, return the list of valid letter combinations.  


Time and Space Complexity  
    Time Complexity:  
        - O(3^n * 4^m), where:  
        - n is the number of digits that map to 3 letters (digits 2, 3, 4, 5, 6, 8).  
        - m is the number of digits that map to 4 letters (digits 7, 9).  
        - This accounts for all possible combinations, as each digit contributes 3 or 4 possibilities.  
    Space Complexity:  
        - O(n), where n is the length of the input digits string.  
        - This space is used by the recursion stack and the `current_combination` being built.  


Given the constraints (0 <= digits.length <= 4), this approach is highly efficient and well-suited for the problem.
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Edge Case: If the input is empty, return an empty list
        if not digits:
            return []

        # Step 1: Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # Resultant list to store all valid combinations
        combinations = []

        # Step 2: Define the backtracking function
        def backtrack(index: int, current_combination: List[str]):
            """ Recursively builds letter combinations. """
            # Base Case: If the current combination is the same length as digits, add to results
            if index == len(digits):
                combinations.append("".join(current_combination))
                return

            # Get the letters that the current digit maps to
            current_digit = digits[index]
            possible_letters = digit_to_letters.get(current_digit, "")

            # Iterate through the letters and recurse
            for letter in possible_letters:
                # Append the current letter to the combination
                current_combination.append(letter)
                # Move to the next digit
                backtrack(index + 1, current_combination)
                # Backtrack by removing the last letter
                current_combination.pop()

        # Step 3: Initiate backtracking from the first digit
        backtrack(0, [])

        return combinations

