# A Comprehensive Guide to Monotonic Stack Problems

**NOTE**: (I use monotonic stack to explain, but same can be applied to
monotonic queue)

## Introduction

- Monotonic Datastructures, can be stack or Queue
- Properties of Monotonic Datastructures
  - A sequence of elements that maintain increasing/decreasing property
  - Since the datastructure maintains this property, it's useful to optimize
    problems from `O(n^2)` to `O(n)`
  - Can be adapted to both increasing and decreasing sequences based on the
    problem requirements.

## When to Use Monotonic Stacks

- **Next/Previous Greater/Smaller Element Problems**: When you need to find the
  next/previous element that is greater/smaller than the current element.
- **Range Calculations**: When you need to calculate spans or ranges based on
  certain conditions (e.g., stock span problems).
- **Histogram Problems**: When dealing with areas under histograms or similar
  structures (e.g., finding the largest rectangle in a histogram).

## High level outline & Observations

Outline:

- Iterate over the sequence
  - Process every element in the sequnce
    - Ensure the mono stack holds it's property with regards to current element.
    - Top of stack is the result for the current element. Update global result
    - Add current item to stack

Observations:

- We don't necesarily build a mono stack and then again go over the input
  sequence, to find next/previous greater/smaller, we do this while building the
  mono stack

## General Template for Monotonic Stack/Queue Problems

### 1. Iterate through the elements

Q: Should we traverse left to right (or) right to left for building the stack?

- We can also just use left to right traversal for finding next or previous,
  Lets look at defining the direction for being more explicit

- This is the first decision to make, what is the direction to go over hte input
  sequence, is it left to right (next'th), or right to left(previous'th)
- Answer to this, depends on what we are looking for while processing a current
  element in the sequence
- If, for every element we have to find its **next** greatest/smallest, that
  implies we are care about the elements that come after this current element,
  so while building the mono stack, we should iterate from right to left.
  Because when traversing a sequence from right to left, when we reach the
  current element we know that we have gone over all the elements that come
  after this current element
- Vice versa, if we are dealing with current element's **previous**
  greater/smaller element then for building the mono stack we would iterate from
  left to right

- Q: So how can we find the next greater element by using left-to-right
  traversal:
  - we build a decreasing mono-stack, and while processing current item, we
    ensure the mono-stack propery that is we pop off items while current item >
    top item.
  - When ever we pop off an item, that tells us that our current item was the
    popped item's next greatest number
  - And hence it is easy if our mono-stack is holding indexes, so that that we
    can go to the popped off index and we update the value at this index of
    global result

### 2. Initialize the Stack

Q: Should we build monotonic increasing or monotonic decreasing?

- Now we know the direction to go over the sequence while building the
  monostack. Next question should the stack be increasing or decreasing. (strict
  or not strict)
- If need `greater` element, the mono stack is `decreasing`
- If need `smaller` element, the mono stack is `increasing`

- If you get stuck on deciding, look at both increasing an decreasing examples,
  before adding the current elemnt to the mono stack (meaning mono stack is
  valid before adding the current element)

  - Decreasing: [ 13 9 8 5 ], current element (say 2), so top most is current  
    element's next/preious `greater` element.
  - Incresing: [ 2 4 5 8 11 ], current element (say 13), so top most is current
    element's next/previous `smaller` element compared to current element

- Decide whether you need an increasing or decreasing stack based on the
  problem.
  - **Monotonically Increasing**: Maintains elements in increasing order.
  - **Monotonically Decreasing **: Maintains elements in decreasing order.
- Initialize an empty stack (can be a simple array or deque or linked list).

- Loop through each element in the array or sequence.

### 3. Process the Stack

- **While Loop Condition**: While the stack is not empty and the current element
  breaks the monotonic condition with the element at the top of the stack.
  - If we are doing strictly increasing/decreasing:
    - For increasing stack: `while stack and array[stack[-1]] > array[i]:`
    - For decreasing stack: `while stack and array[stack[-1]] < array[i]:`
  - If we are **NOT** doing strictly increasing/decreasing:
    - For increasing stack: `while stack and array[stack[-1]] >= array[i]:`
    - For decreasing stack: `while stack and array[stack[-1]] <= array[i]:`
- **Process Elements**: Pop elements from the stack until the condition is
  satisfied.
- NOTE: Though we are using a while loop here, in the worst case all elements go
  into the stack popped from stack, so at most 2 times an item is touched. which
  is linear time complexity.

### 4. Perform Necessary Calculations

- **Before Pushing**: If needed, perform calculations using the indices or
  values.
- **After Popping**: Use the index or value of the popped element to compute
  results (e.g., span, area).

### 5. Push Current Element Onto Stack

- Push the current index (or value, depending on the problem) onto the stack.

### 6. Post-Processing (if necessary)

- After the loop, perform any additional calculations required by the problem.

---

## Example Problems

### Example 1: Next Greater Element

#### Problem Statement

Given an array of integers `nums`, for each element find the next element that
is greater than it. If there is no such element, use -1.

#### Solution Explanation

We will use a monotonically decreasing stack to keep track of indices whose next
greater element hasn't been found yet.

#### Implementation

```py
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        # While current element is greater than the element at index stored at
        # the top of the stack
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result
```

---

### Example 2: Largest Rectangle in Histogram

#### Problem Statement

Given an array of integers `heights` representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in
the histogram.

#### Solution Explanation

We use a monotonically increasing stack to store indices of the bars. We
calculate the area for every bar as the smallest bar in the rectangle when we
encounter a bar of smaller height.

#### Implementation

```py
def largest_rectangle_area(heights):
    heights.append(0)  # Append a zero to handle remaining bars
    stack = [-1]       # Initialize stack with sentinel value
    max_area = 0

    for i in range(len(heights)):
        # While the current bar is smaller than the last stacked bar
        while heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1  # Calculate the width
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()  # Clean up the appended zero
    return max_area
```

---

### Example 3: Trapping Rain Water

#### Problem Statement

Given `n` non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

#### Solution Explanation

We use a monotonically decreasing stack to keep track of the bars that can
potentially trap water.

#### Implementation

```py
def trap_rain_water(height):
    stack = []
    water_trapped = 0
    i = 0

    while i < len(height):
        # While current height is greater than the height at stack's top
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[bottom]
            water_trapped += distance * bounded_height
        stack.append(i)
        i += 1
    return water_trapped
```

---

### Example 4: Daily Temperatures

#### Problem Statement

Given a list of daily temperatures `T`, return a list such that, for each day in
the input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0
instead.

#### Solution Explanation

We use a monotonically decreasing stack to keep track of indices where a warmer
temperature hasn't been found yet.

#### Implementation

```py
def daily_temperatures(T):
    n = len(T)
    result = [0] * n
    stack = []

    for i in range(n):
        # While current temperature is higher than the temperature at index stored at the top of the stack
        while stack and T[i] > T[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result
```

---

### Example 5: Stock Span Problem

#### Problem Statement

Given a list of daily stock prices, calculate the span of stock’s price for all
days. The span of the stock’s price on a given day is defined as the maximum
number of consecutive days the price of the stock has been less than or equal to
its price on that day.

#### Solution Explanation

We use a monotonically decreasing stack to keep track of indices where the
current price is higher, which helps us compute the span efficiently.

#### Implementation

```py
def calculate_span(prices):
    n = len(prices)
    spans = [1] * n
    stack = []

    for i in range(n):
        # Pop elements from stack while current price is higher
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()
        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return spans
```

---

### Example 6: Shortest Subarray with Sum at Least K

#### Problem Statement

Given an array of integers `A` and an integer `K`, find the length of the
shortest, non-empty, contiguous subarray of `A` with sum at least `K`. If no
such subarray exists, return -1.

#### Solution Explanation

We use a monotonically increasing deque (double-ended queue) to maintain the
indices of the prefix sums in increasing order.

#### Implementation

```py
from collections import deque

def shortest_subarray(A, K):
    n = len(A)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i+1] = prefix_sums[i] + A[i]

    result = n + 1
    monoq = deque()  # Monotonically increasing deque

    for i in range(len(prefix_sums)):
        # Check if current prefix sum - smallest prefix sum >= K
        while monoq and prefix_sums[i] - prefix_sums[monoq[0]] >= K:
            result = min(result, i - monoq.popleft())
        # Maintain the increasing order of prefix sums
        while monoq and prefix_sums[i] <= prefix_sums[monoq[-1]]:
            monoq.pop()
        monoq.append(i)

    return result if result <= n else -1
```

---

### Example 7: Sum of Subarray Minimums

#### Problem Statement

Given an array of integers `A`, find the sum of `min(B)`, where `B` ranges over
every (contiguous) subarray of `A`. Since the answer may be large, return the
answer modulo 10^9 + 7.

#### Solution Explanation

We use a monotonically increasing stack to find the previous and next less
elements for each element. This helps in calculating how many subarrays an
element is the minimum of.

#### Implementation

```py
def sum_subarray_mins(A):
    MOD = 10**9 + 7
    n = len(A)
    stack = []
    left = [0] * n  # Distance to previous less
    right = [0] * n # Distance to next less

    # Previous Less Element
    for i in range(n):
        count = 1
        while stack and stack[-1][0] > A[i]:
            count += stack.pop()[1]
        stack.append((A[i], count))
        left[i] = count

    stack = []

    # Next Less Element
    for i in range(n-1, -1, -1):
        count = 1
        while stack and stack[-1][0] >= A[i]:
            count += stack.pop()[1]
        stack.append((A[i], count))
        right[i] = count

    result = 0
    for i in range(n):
        result = (result + A[i] * left[i] * right[i]) % MOD
    return result
```

---

### Example 8: Remove K Digits

#### Problem Statement

Given a non-negative integer represented as a string `num`, remove `k` digits
from the number so that the new number is the smallest possible.

#### Solution Explanation

We use a monotonically increasing stack to build the smallest possible number by
removing digits that are greater than the current digit when possible.

#### Implementation

```py
def remove_k_digits(num, k):
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    # If k > 0, remove from the end
    final_stack = stack[:-k] if k else stack
    # Build the number and remove leading zeros
    return ''.join(final_stack).lstrip('0') or '0'
```

---

### Example 9: Asteroid Collision

#### Problem Statement

Given an array `asteroids` of integers representing asteroids in a row. For each
asteroid, the absolute value represents its size, and the sign represents its
direction (positive meaning right, negative meaning left). Find out the state of
the asteroids after all collisions.

#### Solution Explanation

We use a stack to simulate the collisions. A collision occurs when a moving
right asteroid (positive) meets a moving left asteroid (negative).

#### Implementation

```py
def asteroid_collision(asteroids):
    stack = []
    for ast in asteroids:
        while stack and ast < 0 < stack[-1]:
            if stack[-1] < -ast:
                stack.pop()
                continue
            elif stack[-1] == -ast:
                stack.pop()
            break
        else:
            stack.append(ast)
    return stack
```

---

### Example 10: Validate Stack Sequences

#### Problem Statement

Given two sequences `pushed` and `popped` with distinct values, return `True` if
and only if this could have been the result of a sequence of push and pop
operations on an initially empty stack.

#### Solution Explanation

We simulate the push and pop operations using a stack, ensuring that at each
step the next number to pop is on top of the stack.

#### Implementation

```py
def validate_stack_sequences(pushed, popped):
    stack = []
    i = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return not stack
```

---

## Conclusion

Monotonic stacks are an essential tool in algorithm design, particularly for
array and sequence manipulation problems. By maintaining a stack with elements
in a specific order (either increasing or decreasing), we can efficiently solve
problems that would otherwise require more complex or less efficient approaches.
The template provided can be adapted to a wide range of problems, making
monotonic stacks a versatile addition to your algorithmic toolkit.

---

## Tips for Using Monotonic Stacks

- **Choose the Right Type**: Decide whether you need an increasing or decreasing
  stack based on whether you're looking for next greater/smaller elements.
- **Edge Cases**: Be mindful of edge cases, such as empty stacks or the last
  elements in the array.
- **Indices vs. Values**: Often, storing indices rather than values can provide
  more flexibility, especially when you need to calculate distances or spans.
- **Stack Content**: The stack can store tuples or custom objects if you need to
  keep track of additional information.
