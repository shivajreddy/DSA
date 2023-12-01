"""
Recursion
"""


def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n < 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    print(memo)
    return memo[n]


"""
Binary Relationships

A recurrence relationship is usually expressed as a math function.
A binary string is a string with 0's and 1's

if a binary string has length n-1. say string = 0011
Then we create 2 different binary by adding either 1 or 0 at the end
so, new string = 00110 or 00111

# of binary string of length n = len(n-1) * 2
Base case: f(0) = 1
Recurrence: f(n) = 2 x f(n-1)
"""

"""
Closed Forms

Its a mathematical expression/formula, that can be used to find the output,
for a given input.
- we can understand the properties of a function or sequence better, with closed forms

For above binary string example, f(n) = 2^n
if n = 0, f(0) = 1
if n = 1, f(1) = 2
if n = 2, f(2) = 4
if n = 3, f(2) = 8
So it's easy to understand runtimes, and find actual outputs for any input


f(0) = 1 (base case)
f(1) = 2
f(2) = 2*f(1) = 4       => 2*2 because f(1)=2
f(3) = 2 * f(2) = 8     => 2*2*2 because f(2)=2*2
f(4) = 2*f(3) = 16      => 2*2*2*2
f(5) = 2*f(4) = 32      => 2*2*2*2*2
f(n) => 2*2*2...n-times => 2^n

"""
