# Segment Trees: An In-Depth Exploration

## Introduction

A **segment tree** is a versatile data structure that allows for efficient querying and updating of intervals or segments within an array. It is particularly useful when dealing with problems that require frequent range queries and point updates, such as finding the sum, minimum, maximum, or greatest common divisor (GCD) over a range.

Segment trees are essential in scenarios where we have a large dataset, and we need to perform multiple queries and updates efficiently. They reduce the time complexity of these operations from `O(n)` to `O(log n)`, making them invaluable for performance-critical applications.

---

## Table of Contents

1. [Why Use Segment Trees?](#why-use-segment-trees)
2. [Fundamental Concepts](#fundamental-concepts)
3. [Building a Segment Tree](#building-a-segment-tree)
4. [Operations on Segment Trees](#operations-on-segment-trees)
    - [Range Query](#range-query)
    - [Point Update](#point-update)
5. [Detailed Example](#detailed-example)
6. [Advanced Topics](#advanced-topics)
    - [Lazy Propagation](#lazy-propagation)
    - [Persistent Segment Trees](#persistent-segment-trees)
    - [2D Segment Trees](#2d-segment-trees)
7. [LeetCode Problems Solved with Segment Trees](#leetcode-problems-solved-with-segment-trees)
    - [Problem 1: Range Sum Query - Mutable (LeetCode 307)](#problem-1-range-sum-query---mutable-leetcode-307)
    - [Problem 2: Count of Smaller Numbers After Self (LeetCode 315)](#problem-2-count-of-smaller-numbers-after-self-leetcode-315)
8. [Conclusion](#conclusion)

---

## Why Use Segment Trees?

Imagine you have an array of numbers and need to perform the following operations multiple times:

1. **Range Queries**: Compute a function (e.g., sum, minimum, maximum) over a subarray ([l, r]).
2. **Point Updates**: Update the value of an element at a specific index.

Using a simple array, these operations would have the following time complexities:

- **Range Query**: `O(n)`
- **Point Update**: `O(1)`

For multiple queries and updates, the total time complexity becomes `O(n * q)`, which is inefficient for large `n` and `q`.

**Segment trees** address this inefficiency by reducing the time complexity to `O(log n)` for both queries and updates. They achieve this by storing aggregate information about segments of the array in a tree structure, allowing for quick access and modification.

---

## Fundamental Concepts

A segment tree is a **binary tree** where:

- **Each node represents an interval (segment) of the array.**
- **The root node represents the entire array.**
- **Leaf nodes represent individual elements of the array.**
- **Internal nodes represent the aggregation of their children's intervals.**

**Properties:**

- **Height**: The height of a segment tree is `O(log n)`, where `n` is the size of the array.
- **Space Complexity**: Approximately `2 * 2^( log_2 n )` (usually `4n`) to accommodate the nodes.
- **Operations**: Both range queries and point updates have `O(log n)` time complexity.

---

## Building a Segment Tree

**Steps to Build a Segment Tree:**

1. **Start with the Root Node**: Represents the entire array range ([0, n-1]).
2. **Recursive Division**:
    - **Divide** the current segment into two halves.
    - **Conquer** by building left and right child nodes recursively.
3. **Leaf Nodes**: When the segment size becomes 1 (start == end), create a leaf node with the value from the array.
4. **Internal Nodes**: After creating left and right children, compute the value for the current node based on its children's values (e.g., sum, min, max).

**Visualization:**

Consider an array `A = [a_0, a_1, a_2, ..., a_{n-1}]`. The segment tree is built by:

- Splitting the range ([0, n-1]) into ([0, m]) and ([m+1, n-1]), where `m = lfloor (start + end) / 2 rfloor`.
- Recursively building the left and right subtrees.

---

## Operations on Segment Trees

### Range Query

To perform a range query over ([l, r]):

1. **Start at the Root Node**:
    - If the node's range is entirely within ([l, r]), return its value.
    - If the node's range is entirely outside ([l, r]), return a default value (e.g., 0 for sum).
    - If the node's range partially overlaps ([l, r]), recursively query both children.

2. **Combine Results**:
    - Aggregate the results from the left and right children based on the operation (e.g., sum, min).

**Time Complexity**: `O(log n)`

### Point Update

To update the value at index `i`:

1. **Start at the Root Node**:
    - If the node represents a range that includes `i`:
        - If it's a leaf node, update its value.
        - Otherwise, recursively update the appropriate child.

2. **Update Internal Nodes**:
    - After updating a child, update the current node's value based on its children's new values.

**Time Complexity**: `O(log n)`

---

## Detailed Example

Let's build and operate on a segment tree for the array:

[ A = [1, 3, 5, 7, 9, 11] ]

### Building the Segment Tree

**Step 1: Initialization**

- **Root Node**: Represents the range ([0, 5]).

**Step 2: Recursive Division**

- **Split ([0, 5]) into ([0, 2]) and ([3, 5])**.
- **Continue splitting until reaching single-element ranges**.

**Step 3: Constructing the Tree**

![Segment Tree Diagram](https://i.imgur.com/Tz4t0tg.png)

**Values at Each Node:**

- **Leaf Nodes**:
    - ([0,0]): 1
    - ([1,1]): 3
    - ([2,2]): 5
    - ([3,3]): 7
    - ([4,4]): 9
    - ([5,5]): 11
- **Internal Nodes**:
    - ([0,1]): `1 + 3 = 4`
    - ([0,2]): `4 + 5 = 9`
    - ([3,4]): `7 + 9 = 16`
    - ([3,5]): `16 + 11 = 27`
    - **Root ([0,5])**: `9 + 27 = 36`

### Performing a Range Query

**Query**: Calculate the sum from index 1 to 3.

**Process**:

1. **Start at Root ([0,5])**:
    - ([1,3]) overlaps with both children.
2. **Left Child ([0,2])**:
    - ([1,3]) overlaps.
    - Recurse into ([0,1]) and ([2,2]).
3. **Nodes ([0,1])**:
    - ([1,3]) overlaps with ([1,1]); include value 3.
4. **Node ([2,2])**:
    - Included; value 5.
5. **Right Child ([3,5])**:
    - ([1,3]) overlaps with ([3,3]); include value 7.
6. **Result**:
    - Sum: `3 + 5 + 7 = 15`

### Performing a Point Update

**Update**: Change the value at index 2 from 5 to 6.

**Process**:

1. **Start at Root ([0,5])**:
    - Index 2 is within the range.
2. **Recurse into ([0,2])**:
    - Index 2 is within the range.
3. **Recurse into ([2,2])**:
    - Leaf node; update value to 6.
4. **Update Internal Nodes**:
    - ([0,2]): New sum `4 + 6 = 10`.
    - Root ([0,5]): New sum `10 + 27 = 37`.

---

## Advanced Topics

### Lazy Propagation

When dealing with **range updates** (e.g., adding a value to all elements in a range), updating each node individually becomes inefficient. **Lazy propagation** postpones updates to child nodes until necessary.

**Key Concepts**:

- **Lazy Value**: Each node carries a pending update value.
- **On Query/Update**:
    - If a node has a lazy value, apply it before proceeding.
    - Propagate the lazy value to children if necessary.

**Benefits**:

- Efficiently handles range updates in `O(log n)` time.
- Reduces unnecessary updates.

### Persistent Segment Trees

**Persistent segment trees** allow access to previous versions after updates, which is useful in functional programming and certain algorithmic problems.

**Key Concepts**:

- **Immutability**: Instead of modifying nodes, create new ones.
- **Versioning**: Keep references to roots of different versions.

**Benefits**:

- Access historical data.
- Efficient memory usage due to shared unchanged nodes.

### 2D Segment Trees

Extend segment trees to two dimensions, typically used for querying over a 2D grid or matrix.

**Implementation**:

- **First Level**: Segment tree over rows.
- **Second Level**: Each node contains a segment tree over columns.

**Time Complexity**:

- Build: `O(n log n log n)`
- Query/Update: `O(log n log n)`

---

## LeetCode Problems Solved with Segment Trees

### Problem 1: Range Sum Query - Mutable (LeetCode 307)

**Problem Statement**:

Implement a class `NumArray` that supports:

- **`NumArray(int[] nums)`**: Initializes the object with the integer array `nums`.
- **`void update(int index, int val)`**: Updates the value of `nums[index]` to be `val`.
- **`int sumRange(int left, int right)`**: Returns the sum of elements between indices `left` and `right` inclusive.

**Constraints**:

- `1 leq nums.length leq 3 times 10^4`
- `-100 leq nums[i] leq 100`
- `0 leq index < nums.length`
- `-100 leq val leq 100`
- `0 leq left leq right < nums.length`
- At most `3 times 10^4` calls to `update` and `sumRange`.

**Solution Using Segment Tree**:

We need to efficiently support both point updates and range sum queries.

**Implementation Steps**:

1. **Build the Segment Tree**:
    - Each node stores the sum over a range.
    - Build recursively.

2. **Update Operation**:
    - Update the value at a specific index.
    - Update all nodes covering that index.

3. **SumRange Operation**:
    - Query the sum over a given range.

**Code Implementation (Python)**:

```python
class NumArray:

    class SegmentTreeNode:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.left = None
            self.right = None
            self.sum = 0

    def buildTree(self, nums, l, r):
        node = self.SegmentTreeNode(l, r)
        if l == r:
            node.sum = nums[l]
        else:
            mid = (l + r) // 2
            node.left = self.buildTree(nums, l, mid)
            node.right = self.buildTree(nums, mid + 1, r)
            node.sum = node.left.sum + node.right.sum
        return node

    def updateTree(self, node, index, val):
        if node.start == node.end:
            node.sum = val
        else:
            mid = (node.start + node.end) // 2
            if index <= mid:
                self.updateTree(node.left, index, val)
            else:
                self.updateTree(node.right, index, val)
            node.sum = node.left.sum + node.right.sum

    def queryTree(self, node, l, r):
        if node.start == l and node.end == r:
            return node.sum
        mid = (node.start + node.end) // 2
        if r <= mid:
            return self.queryTree(node.left, l, r)
        elif l > mid:
            return self.queryTree(node.right, l, r)
        else:
            return self.queryTree(node.left, l, mid) + self.queryTree(node.right, mid + 1, r)

    def __init__(self, nums):
        if nums:
            self.root = self.buildTree(nums, 0, len(nums) - 1)
        else:
            self.root = None

    def update(self, index, val):
        self.updateTree(self.root, index, val)

    def sumRange(self, left, right):
        return self.queryTree(self.root, left, right)
```

---

### Problem 2: Count of Smaller Numbers After Self (LeetCode 315)

**Problem Statement**:

Given an integer array `nums`, return an integer array `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

**Example**:

```plaintext
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

**Constraints**:

- `1 leq nums.length leq 10^5`
- `-10^4 leq nums[i] leq 10^4`

**Solution Using Segment Tree**:

We need to count, for each element, the number of smaller elements to its right.

**Approach**:

1. **Normalize the Numbers**:
    - Map the numbers to a range `[0, N]` using their ranks after sorting to handle negative numbers.

2. **Process from Right to Left**:
    - At each step, count the number of elements smaller than the current element that have been seen so far.

3. **Use a Segment Tree**:
    - The segment tree nodes will store counts of numbers within a range.
    - For each number, query the segment tree for counts of numbers less than it.
    - Update the segment tree to include the current number.

**Code Implementation (Python)**:

```python
class Solution:
    def countSmaller(self, nums):
        # Normalize the nums
        sorted_unique_nums = sorted(set(nums))
        num_to_index = {num: idx for idx, num in enumerate(sorted_unique_nums)}
        size = len(sorted_unique_nums)
        
        class SegmentTreeNode:
            def __init__(self, l, r):
                self.left = None
                self.right = None
                self.l = l
                self.r = r
                self.count = 0

        def build(l, r):
            node = SegmentTreeNode(l, r)
            if l == r:
                return node
            mid = (l + r) // 2
            node.left = build(l, mid)
            node.right = build(mid + 1, r)
            return node

        def update(node, index):
            if node.l == node.r:
                node.count += 1
            else:
                mid = (node.l + node.r) // 2
                if index <= mid:
                    update(node.left, index)
                else:
                    update(node.right, index)
                node.count = node.left.count + node.right.count

        def query(node, l, r):
            if node.l > r or node.r < l:
                return 0
            if l <= node.l and node.r <= r:
                return node.count
            return query(node.left, l, r) + query(node.right, l, r)

        root = build(0, size - 1)
        res = []
        for num in reversed(nums):
            idx = num_to_index[num]
            count = query(root, 0, idx - 1) if idx > 0 else 0
            res.append(count)
            update(root, idx)
        return res[::-1]
```

---

## Conclusion

Segment trees are powerful and efficient data structures for handling range queries and updates on arrays. By understanding their construction and operation, you can solve a variety of complex algorithmic problems that require efficient querying and updating of intervals.

**Key Takeaways**:

- **Efficiency**: Segment trees reduce query and update times from `O(n)` to `O(log n)`.
- **Versatility**: They can handle different operations like sum, min, max, and even more complex functions.
- **Advanced Techniques**: Concepts like lazy propagation and persistent segment trees extend their applicability.

**When to Use Segment Trees**:

- When you need to perform frequent range queries and updates on an array.
- When the array size is large, and `O(n)` operations are too slow.
- In competitive programming and coding interviews for efficient solutions.

By mastering segment trees, you equip yourself with a tool that is both powerful and widely applicable in the field of computer science and software engineering.

---

Feel free to experiment with the provided code examples and explore more problems where segment trees can be applied!
