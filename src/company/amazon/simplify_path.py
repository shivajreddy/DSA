"""
Key Insights  
    Using a Stack to Manage Directories:  
    - Stack Data Structure is ideal for managing directories because it follows the
      Last-In-First-Out (LIFO) principle, which aligns with navigating
      directories (entering and exiting directories).  

Parsing the Path:  
    - Split the input path by slashes `'/'` to process each component (directory name, '.', '..').  
    - Ignore empty strings resulting from consecutive slashes `'//'`.  

Handling Special Symbols:  
    - Single Period `.`: Represents the current directory. No action needed.  
    - Double Period `..`: Represents moving up one directory. Pop the last directory from the
      stack if it's not empty.  
    - Directory Names: Push onto the stack as they represent navigating into a directory.  

Reconstructing the Simplified Path:  
    - After processing all components, join the stack elements with slashes `'/'` to
    form the canonical path.  
    - Ensure the path starts with a slash `'/'`.  
    - If the stack is empty, the canonical path is the root `'/'`.  

Time and Space Efficiency:  
    - Time Complexity: O(n), where n is the length of the input path, as we traverse the string once.  
    - Space Complexity: O(n), in the worst case where all components are valid directory names.  

Detailed Plan  
Initialize an Empty Stack:  
    - This stack will store the valid directory names as we parse through the path.  

Split the Path:  
    - Use the `split('/')` method to divide the path into components separated by slashes.  

Process Each Component:  
    - If the component is empty or `.`: Do nothing (continue to the next component).  
    - If the component is `..`:  
    - Pop the top element from the stack if it's not empty (move up one directory).  
    - Otherwise (Valid Directory Name):  
        - Push the directory name onto the stack.  

Reconstruct the Canonical Path:  
    - Join the elements in the stack with slashes `'/'`.  
    - Prepend a leading slash `'/'` to form the absolute path.  
    - If the stack is empty, return `'/'`.  

Edge Case Handling:  
    - Empty Path: Although the problem states that the path has at least one character,
      ensure that an empty path returns `'/'`.  
    - Path Ending with Slash: The final path should not end with a trailing slash unless it's the root.  

Time and Space Complexity  
    - Time Complexity: O(n)  
        - We traverse the input path once, performing constant-time operations for each component.  
    - Space Complexity: O(n)  
        - In the worst-case scenario, the stack can store all directory names
          if there are no `'..'` or `'.'` components.  
"""

from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        """ Simplifies the given Unix-style absolute path to its canonical form. """
        # Step 1: Initialize an empty stack to store valid directory names
        stack: List[str] = []

        # Step 2: Split the path by '/' to process each component
        components = path.split('/')

        # Step 3: Iterate through each component in the path
        for component in components:
            if not component or component == '.':
                # Ignore empty components and current directory symbol
                continue
            elif component == '..':
                # Pop the last valid directory from the stack if possible
                if stack:
                    stack.pop()
            else:
                # Push the valid directory name onto the stack
                stack.append(component)

        # Step 4: Reconstruct the canonical path from the stack
        canonical_path = '/' + '/'.join(stack)

        # Step 5: Return the canonical path
        return canonical_path


