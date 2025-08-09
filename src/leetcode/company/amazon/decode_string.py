"""
Constraints:
1 <= digit <= 300
1 <= n <= 30

Scope & Assumptions:
no leading 0 digits
input only contains lower case english letters, digits, [, ]
input’s encodings are all valid i.e, there is nothing like 3[a   or  3a]

Observations:
there can be nested encodings.
Left most encoding’s closing bracket is the rightmost closing bracket -> 2 pointers?

Approach:
    Dummy Node: A dummy node (dummy) is used as a placeholder to simplify list manipulation. 
    The final result will be built starting from this dummy node.

    Iteration: Both linked lists (l1 and l2) are traversed simultaneously. At each step, the 
    corresponding nodes are summed along with a carry from the previous step.

    Handling Carry: After summing the digits from both linked lists, the carry is computed for
    the next iteration. The carry is the quotient of the division by 10, and the current digit
    is the remainder.

    Edge Cases: The loop continues as long as there are nodes in either l1 or l2, or if there's
    a non-zero carry. This ensures that if one list is longer than the other, or if there's a
    carry after the last node, it is handled correctly.

    Return Result: Finally, the next node of the dummy node (dummy.next) is returned, as the
    dummy node was just a placeholder.

    Time & Space Complexity:
    Time Complexity: 
    O(max(m, n)), where m is the length of l1 and n is the length of l2. We iterate through
    both lists once.
    Space Complexity: O(max(m, n)) for the result list, since we store the sum 
    as a new linked list.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decodes an encoded string where k[encoded_string] means the string 
        inside the square brackets is repeated k times.

        Args:
        s (str): The encoded string.

        Returns:
        str: The decoded string.
        """
        stack = []
        current_number = 0
        current_substring = []

        for char in s:
            if char.isdigit():
                # Build the number that indicates how many times the next substring will be repeated
                current_number = current_number * 10 + int(char)
            elif char == '[':
                # Push the current_number and the processed part of the string onto the stack
                stack.append(current_number)
                stack.append(current_substring)
                # Reset for the new substring to be decoded
                current_number = 0
                current_substring = []
            elif char == ']':
                # Pop the processed string and the repeat factor from the stack
                previous_processed_string = stack.pop()  # The part of the string decoded up to this point
                repeat_factor = stack.pop()              # The number of times to repeat the current substring
                # Decode the current substring by repeating it and append it to the processed string
                current_substring = previous_processed_string + (repeat_factor * current_substring )
            else:
                # Append the current character to the current substring
                current_substring.append(char)

        # Join the list to form the final decoded string
        return ''.join(current_substring)

