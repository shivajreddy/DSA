# Segment Trees: An In-Depth Exploration (4o)

## **Introduction**

A **segment tree** is a versatile data structure that allows for efficient
querying and updating of intervals or segments within an array. It is
particularly useful when dealing with problems that require frequent range
queries and point updates, such as finding the sum, minimum, maximum, or
greatest common divisor (GCD) over a range.

Segment trees are essential in scenarios where we have a large dataset, and we
need to perform multiple queries and updates efficiently. They reduce the time
complexity of these operations from ( O(n) ) to ( O(\\log n) ), making them
invaluable for performance-critical applications.

---

## **Table of Contents**

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
   - [Problem 1: Range Sum Query \- Mutable (LeetCode 307\)](#problem-1-range-sum-query---mutable-leetcode-307)
   - [Problem 2: Count of Smaller Numbers After Self (LeetCode 315\)](#problem-2-count-of-smaller-numbers-after-self-leetcode-315)
8. [Conclusion](#conclusion)

---

## **Why Use Segment Trees?**

Imagine you have an array of numbers and need to perform the following
operations multiple times:

1. **Range Queries**: Compute a function (e.g., sum, minimum, maximum) over a
   subarray (\[l, r\]).
2. **Point Updates**: Update the value of an element at a specific index.

Using a simple array, these operations would have the following time
complexities:

- **Range Query**: ( O(n) )
- **Point Update**: ( O(1) )

For multiple queries and updates, the total time complexity becomes ( O(n \\cdot
q) ), which is inefficient for large ( n ) and ( q ).

**Segment trees** address this inefficiency by reducing the time complexity to (
O(\\log n) ) for both queries and updates. They achieve this by storing
aggregate information about segments of the array in a tree structure, allowing
for quick access and modification.

---

## **Fundamental Concepts**

A segment tree is a **binary tree** where:

- **Each node represents an interval (segment) of the array.**
- **The root node represents the entire array.**
- **Leaf nodes represent individual elements of the array.**
- **Internal nodes represent the aggregation of their children's intervals.**

**Properties:**

- **Height**: The height of a segment tree is ( O(\\log n) ), where ( n ) is the
  size of the array.
- **Space Complexity**: Approximately ( 2 \\cdot 2^{\\lceil \\log_2 n \\rceil} )
  (usually ( 4n )) to accommodate the nodes.
- **Operations**: Both range queries and point updates have ( O(\\log n) ) time
  complexity.

---

## **Building a Segment Tree**

**Steps to Build a Segment Tree:**

1. **Start with the Root Node**: Represents the entire array range (\[0, n-1\]).
2. **Recursive Division**:
   - **Divide** the current segment into two halves.
   - **Conquer** by building left and right child nodes recursively.
3. **Leaf Nodes**: When the segment size becomes 1 (start \== end), create a
   leaf node with the value from the array.
4. **Internal Nodes**: After creating left and right children, compute the value
   for the current node based on its children's values (e.g., sum, min, max).

**Visualization:**

Consider an array ( A \= \[a_0, a_1, a_2, ..., a\_{n-1}\] ). The segment tree is
built by:

- Splitting the range (\[0, n-1\]) into (\[0, m\]) and (\[m+1, n-1\]), where ( m
  \= \\lfloor (start \+ end) / 2 \\rfloor ).
- Recursively building the left and right subtrees.

---

## **Operations on Segment Trees**

### Range Query

To perform a range query over (\[l, r\]):

1. **Start at the Root Node**:

   - If the node's range is entirely within (\[l, r\]), return its value.
   - If the node's range is entirely outside (\[l, r\]), return a default value
     (e.g., 0 for sum).
   - If the node's range partially overlaps (\[l, r\]), recursively query both
     children.

2. **Combine Results**:
   - Aggregate the results from the left and right children based on the
     operation (e.g., sum, min).

**Time Complexity**: ( O(\\log n) )

### Point Update

To update the value at index ( i ):

1. **Start at the Root Node**:

   - If the node represents a range that includes ( i ):
     - If it's a leaf node, update its value.
     - Otherwise, recursively update the appropriate child.

2. **Update Internal Nodes**:
   - After updating a child, update the current node's value based on its
     children's new values.

**Time Complexity**: ( O(\\log n) )

---

## **Detailed Example**

Let's build and operate on a segment tree for the array:

\[ A \= \[1, 3, 5, 7, 9, 11\] \]

### Building the Segment Tree

**Step 1: Initialization**

- **Root Node**: Represents the range (\[0, 5\]).

**Step 2: Recursive Division**

- **Split (\[0, 5\]) into (\[0, 2\]) and (\[3, 5\])**.
- **Continue splitting until reaching single-element ranges**.

**Step 3: Constructing the Tree**

![Segment Tree Diagram][image1]

**Values at Each Node:**

- **Leaf Nodes**:
  - (\[0,0\]): 1
  - (\[1,1\]): 3
  - (\[2,2\]): 5
  - (\[3,3\]): 7
  - (\[4,4\]): 9
  - (\[5,5\]): 11
- **Internal Nodes**:
  - (\[0,1\]): ( 1 \+ 3 \= 4 )
  - (\[0,2\]): ( 4 \+ 5 \= 9 )
  - (\[3,4\]): ( 7 \+ 9 \= 16 )
  - (\[3,5\]): ( 16 \+ 11 \= 27 )
  - **Root (\[0,5\])**: ( 9 \+ 27 \= 36 )

### Performing a Range Query

**Query**: Calculate the sum from index 1 to 3\.

**Process**:

1. **Start at Root (\[0,5\])**:
   - (\[1,3\]) overlaps with both children.
2. **Left Child (\[0,2\])**:
   - (\[1,3\]) overlaps.
   - Recurse into (\[0,1\]) and (\[2,2\]).
3. **Nodes (\[0,1\])**:
   - (\[1,3\]) overlaps with (\[1,1\]); include value 3\.
4. **Node (\[2,2\])**:
   - Included; value 5\.
5. **Right Child (\[3,5\])**:
   - (\[1,3\]) overlaps with (\[3,3\]); include value 7\.
6. **Result**:
   - Sum: ( 3 \+ 5 \+ 7 \= 15 )

### Performing a Point Update

**Update**: Change the value at index 2 from 5 to 6\.

**Process**:

1. **Start at Root (\[0,5\])**:
   - Index 2 is within the range.
2. **Recurse into (\[0,2\])**:
   - Index 2 is within the range.
3. **Recurse into (\[2,2\])**:
   - Leaf node; update value to 6\.
4. **Update Internal Nodes**:
   - (\[0,2\]): New sum ( 4 \+ 6 \= 10 ).
   - Root (\[0,5\]): New sum ( 10 \+ 27 \= 37 ).

---

## **Advanced Topics**

### Lazy Propagation

When dealing with **range updates** (e.g., adding a value to all elements in a
range), updating each node individually becomes inefficient. **Lazy
propagation** postpones updates to child nodes until necessary.

**Key Concepts**:

- **Lazy Value**: Each node carries a pending update value.
- **On Query/Update**:
  - If a node has a lazy value, apply it before proceeding.
  - Propagate the lazy value to children if necessary.

**Benefits**:

- Efficiently handles range updates in ( O(\\log n) ) time.
- Reduces unnecessary updates.

### Persistent Segment Trees

**Persistent segment trees** allow access to previous versions after updates,
which is useful in functional programming and certain algorithmic problems.

**Key Concepts**:

- **Immutability**: Instead of modifying nodes, create new ones.
- **Versioning**: Keep references to roots of different versions.

**Benefits**:

- Access historical data.
- Efficient memory usage due to shared unchanged nodes.

### 2D Segment Trees

Extend segment trees to two dimensions, typically used for querying over a 2D
grid or matrix.

**Implementation**:

- **First Level**: Segment tree over rows.
- **Second Level**: Each node contains a segment tree over columns.

**Time Complexity**:

- Build: ( O(n \\log n \\log n) )
- Query/Update: ( O(\\log n \\log n) )

---

## **LeetCode Problems Solved with Segment Trees**

### Problem 1: Range Sum Query \- Mutable (LeetCode 307\)

**Problem Statement**:

Implement a class `NumArray` that supports:

- **`NumArray(int[] nums)`**: Initializes the object with the integer array
  `nums`.
- **`void update(int index, int val)`**: Updates the value of `nums[index]` to
  be `val`.
- **`int sumRange(int left, int right)`**: Returns the sum of elements between
  indices `left` and `right` inclusive.

**Constraints**:

- ( 1 \\leq nums.length \\leq 3 \\times 10^4 )
- ( \-100 \\leq nums\[i\] \\leq 100 )
- ( 0 \\leq index \< nums.length )
- ( \-100 \\leq val \\leq 100 )
- ( 0 \\leq left \\leq right \< nums.length )
- At most ( 3 \\times 10^4 ) calls to `update` and `sumRange`.

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

```py
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

### Problem 2: Count of Smaller Numbers After Self (LeetCode 315\)

**Problem Statement**:

Given an integer array `nums`, return an integer array `counts` where
`counts[i]` is the number of smaller elements to the right of `nums[i]`.

**Example**:

Input: nums \= \[5, 2, 6, 1\]

Output: \[2, 1, 1, 0\]

**Constraints**:

- ( 1 \\leq nums.length \\leq 10^5 )
- ( \-10^4 \\leq nums\[i\] \\leq 10^4 )

**Solution Using Segment Tree**:

We need to count, for each element, the number of smaller elements to its right.

**Approach**:

1. **Normalize the Numbers**:

   - Map the numbers to a range ( \[0, N\] ) using their ranks after sorting to
     handle negative numbers.

2. **Process from Right to Left**:

   - At each step, count the number of elements smaller than the current element
     that have been seen so far.

3. **Use a Segment Tree**:
   - The segment tree nodes will store counts of numbers within a range.
   - For each number, query the segment tree for counts of numbers less than it.
   - Update the segment tree to include the current number.

**Code Implementation (Python)**:

```py
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

## **Conclusion**

Segment trees are powerful and efficient data structures for handling range
queries and updates on arrays. By understanding their construction and
operation, you can solve a variety of complex algorithmic problems that require
efficient querying and updating of intervals.

**Key Takeaways**:

- **Efficiency**: Segment trees reduce query and update times from ( O(n) ) to (
  O(\\log n) ).
- **Versatility**: They can handle different operations like sum, min, max, and
  even more complex functions.
- **Advanced Techniques**: Concepts like lazy propagation and persistent segment
  trees extend their applicability.

**When to Use Segment Trees**:

- When you need to perform frequent range queries and updates on an array.
- When the array size is large, and ( O(n) ) operations are too slow.
- In competitive programming and coding interviews for efficient solutions.

By mastering segment trees, you equip yourself with a tool that is both powerful
and widely applicable in the field of computer science and software engineering.

---

# Segment Trees: A Comprehensive Guide (3.5 sonnet)

## **1\. Introduction to Segment Trees**

A segment tree is a tree data structure used for storing information about
intervals, or segments. It allows querying which of the stored segments contain
a given point. It's particularly useful for solving range query problems
efficiently.

Key features of segment trees:

- They can be used to solve range query problems in O(log n) time.
- They require O(n) space, where n is the number of elements in the input array.
- They can be easily extended to handle range updates efficiently.

## **2\. Structure of a Segment Tree**

A segment tree for an array A\[0, 1, ..., n-1\] is a binary tree where:

1. The root represents the whole array A\[0:n-1\].
2. Each leaf represents a single element A\[i\].
3. Each internal node represents a merge of its children's intervals.

For an array of n elements, the segment tree will have 2n-1 nodes in the worst
case.

## **3\. Building a Segment Tree**

To build a segment tree, we follow these steps:

1. Create a tree with 4n nodes (to ensure we have enough space).
2. Start with the entire range of the array at the root.
3. Recursively divide the range into two halves until we reach individual
   elements.
4. Compute the value for each node based on its children.

Here's a Python implementation of building a segment tree for the sum operation:

class SegmentTree:

    def \_\_init\_\_(self, arr):

        self.n \= len(arr)

        self.tree \= \[0\] \* (4 \* self.n)

        self.build(arr, 0, 0, self.n \- 1\)



    def build(self, arr, node, start, end):

        if start \== end:

            self.tree\[node\] \= arr\[start\]

            return



        mid \= (start \+ end) // 2

        self.build(arr, 2\*node+1, start, mid)

        self.build(arr, 2\*node+2, mid+1, end)

        self.tree\[node\] \= self.tree\[2\*node+1\] \+ self.tree\[2\*node+2\]

Time Complexity: O(n), where n is the number of elements in the input array.
Space Complexity: O(n) to store the segment tree.

## **4\. Querying a Segment Tree**

To query a range \[l, r\] in the segment tree, we follow these steps:

1. Start at the root of the tree.
2. If the current node's range is completely inside \[l, r\], return the node's
   value.
3. If the current node's range is completely outside \[l, r\], return the
   identity value (e.g., 0 for sum).
4. Otherwise, split the query into two parts and recurse on both children.

Here's the Python implementation for querying a sum segment tree:

def query(self, node, start, end, l, r):

    if r \< start or end \< l:

        return 0

    if l \<= start and end \<= r:

        return self.tree\[node\]



    mid \= (start \+ end) // 2

    left\_sum \= self.query(2\*node+1, start, mid, l, r)

    right\_sum \= self.query(2\*node+2, mid+1, end, l, r)

    return left\_sum \+ right\_sum

def range_sum(self, l, r):

    return self.query(0, 0, self.n-1, l, r)

Time Complexity: O(log n) per query.

## **5\. Updating a Segment Tree**

To update a single element in the segment tree, we follow these steps:

1. Start at the root of the tree.
2. Navigate to the leaf node corresponding to the element to be updated.
3. Update the leaf node.
4. Recursively update all ancestor nodes.

Here's the Python implementation for updating a sum segment tree:

def update(self, node, start, end, idx, val):

    if start \== end:

        self.tree\[node\] \= val

        return



    mid \= (start \+ end) // 2

    if idx \<= mid:

        self.update(2\*node+1, start, mid, idx, val)

    else:

        self.update(2\*node+2, mid+1, end, idx, val)

    self.tree\[node\] \= self.tree\[2\*node+1\] \+ self.tree\[2\*node+2\]

def update_value(self, idx, val):

    self.update(0, 0, self.n-1, idx, val)

Time Complexity: O(log n) per update.

## **6\. Lazy Propagation**

Lazy propagation is an optimization technique used when we need to perform range
updates. Instead of updating all nodes in a range immediately, we defer the
updates and propagate them only when necessary.

Here's a basic implementation of lazy propagation for a sum segment tree:

class LazySegmentTree:

    def \_\_init\_\_(self, arr):

        self.n \= len(arr)

        self.tree \= \[0\] \* (4 \* self.n)

        self.lazy \= \[0\] \* (4 \* self.n)

        self.build(arr, 0, 0, self.n \- 1\)



    def build(self, arr, node, start, end):

        if start \== end:

            self.tree\[node\] \= arr\[start\]

            return



        mid \= (start \+ end) // 2

        self.build(arr, 2\*node+1, start, mid)

        self.build(arr, 2\*node+2, mid+1, end)

        self.tree\[node\] \= self.tree\[2\*node+1\] \+ self.tree\[2\*node+2\]



    def push(self, node, start, end):

        if self.lazy\[node\] \!= 0:

            self.tree\[node\] \+= (end \- start \+ 1\) \* self.lazy\[node\]

            if start \!= end:

                self.lazy\[2\*node+1\] \+= self.lazy\[node\]

                self.lazy\[2\*node+2\] \+= self.lazy\[node\]

            self.lazy\[node\] \= 0



    def update\_range(self, node, start, end, l, r, val):

        self.push(node, start, end)

        if r \< start or end \< l:

            return

        if l \<= start and end \<= r:

            self.lazy\[node\] \+= val

            self.push(node, start, end)

            return



        mid \= (start \+ end) // 2

        self.update\_range(2\*node+1, start, mid, l, r, val)

        self.update\_range(2\*node+2, mid+1, end, l, r, val)

        self.tree\[node\] \= self.tree\[2\*node+1\] \+ self.tree\[2\*node+2\]



    def query(self, node, start, end, l, r):

        self.push(node, start, end)

        if r \< start or end \< l:

            return 0

        if l \<= start and end \<= r:

            return self.tree\[node\]



        mid \= (start \+ end) // 2

        left\_sum \= self.query(2\*node+1, start, mid, l, r)

        right\_sum \= self.query(2\*node+2, mid+1, end, l, r)

        return left\_sum \+ right\_sum

## **7\. LeetCode Problems Using Segment Trees**

Let's solve two LeetCode problems using segment trees:

### Problem 1: Range Sum Query \- Mutable (LeetCode 307\)

Problem Statement: Given an integer array nums, handle multiple queries of the
following types:

1. Update the value of an element in nums.
2. Calculate the sum of the elements of nums between indices left and right
   inclusive where left \<= right.

Solution using Segment Tree:

class NumArray:

    def \_\_init\_\_(self, nums: List\[int\]):

        self.n \= len(nums)

        self.tree \= \[0\] \* (4 \* self.n)

        self.build(nums, 0, 0, self.n \- 1\)



    def build(self, nums, node, start, end):

        if start \== end:

            self.tree\[node\] \= nums\[start\]

            return



        mid \= (start \+ end) // 2

        self.build(nums, 2\*node+1, start, mid)

        self.build(nums, 2\*node+2, mid+1, end)

        self.tree\[node\] \= self.tree\[2\*node+1\] \+ self.tree\[2\*node+2\]



    def update(self, index: int, val: int) \-\> None:

        def update\_tree(node, start, end, index, val):

            if start \== end:

                self.tree\[node\] \= val

                return



            mid \= (start \+ end) // 2

            if index \<= mid:

                update\_tree(2\*node+1, start, mid, index, val)

            else:

                update\_tree(2\*node+2, mid+1, end, index, val)

            self.tree\[node\] \= self.tree\[2\*node+1\] \+ self.tree\[2\*node+2\]



        update\_tree(0, 0, self.n-1, index, val)

    def sumRange(self, left: int, right: int) \-\> int:

        def query(node, start, end, l, r):

            if r \< start or end \< l:

                return 0

            if l \<= start and end \<= r:

                return self.tree\[node\]



            mid \= (start \+ end) // 2

            left\_sum \= query(2\*node+1, start, mid, l, r)

            right\_sum \= query(2\*node+2, mid+1, end, l, r)

            return left\_sum \+ right\_sum



        return query(0, 0, self.n-1, left, right)

Time Complexity:

- Constructor: O(n)
- Update: O(log n)
- SumRange: O(log n)

Space Complexity: O(n) for the segment tree.

### Problem 2: Range Minimum Query (LeetCode 1530 \- modified version)

Problem Statement: Given an array of integers, perform two types of operations:

1. Update the value of an element in the array.
2. Find the minimum value in a given range \[left, right\].

Solution using Segment Tree:

class RangeMinQuery:

    def \_\_init\_\_(self, nums: List\[int\]):

        self.n \= len(nums)

        self.tree \= \[0\] \* (4 \* self.n)

        self.build(nums, 0, 0, self.n \- 1\)



    def build(self, nums, node, start, end):

        if start \== end:

            self.tree\[node\] \= nums\[start\]

            return



        mid \= (start \+ end) // 2

        self.build(nums, 2\*node+1, start, mid)

        self.build(nums, 2\*node+2, mid+1, end)

        self.tree\[node\] \= min(self.tree\[2\*node+1\], self.tree\[2\*node+2\])



    def update(self, index: int, val: int) \-\> None:

        def update\_tree(node, start, end, index, val):

            if start \== end:

                self.tree\[node\] \= val

                return



            mid \= (start \+ end) // 2

            if index \<= mid:

                update\_tree(2\*node+1, start, mid, index, val)

            else:

                update\_tree(2\*node+2, mid+1, end, index, val)

            self.tree\[node\] \= min(self.tree\[2\*node+1\], self.tree\[2\*node+2\])



        update\_tree(0, 0, self.n-1, index, val)

    def query\_min(self, left: int, right: int) \-\> int:

        def query(node, start, end, l, r):

            if r \< start or end \< l:

                return float('inf')

            if l \<= start and end \<= r:

                return self.tree\[node\]



            mid \= (start \+ end) // 2

            left\_min \= query(2\*node+1, start, mid, l, r)

            right\_min \= query(2\*node+2, mid+1, end, l, r)

            return min(left\_min, right\_min)



        return query(0, 0, self.n-1, left, right)

Time Complexity:

- Constructor: O(n)
- Update: O(log n)
- Query_min: O(log n)

Space Complexity: O(n) for the segment tree.

## **8\. Conclusion**

Segment trees are powerful data structures that can efficiently handle various
range query problems. They offer a good balance between query time and update
time, both typically O(log n). While they require more memory than a simple
array, the trade-off is often worth it for problems involving frequent range
queries or updates.

Key points to remember:

1. Segment trees are particularly useful for range query problems.
2. They can be adapted for various operations (sum, min, max, GCD, etc.) by
   changing the merge function.
3. Lazy propagation can be used to optimize range updates.
4. The space complexity is O(n), and both query and update operations take O(log
   n) time.

When solving problems, consider using a segment tree if you see:

- Range queries on a mutable array
- Need for efficient updates and queries
- Operations that can be merged easily (like sum, min, max)

Practice implementing segment trees for different operations to become
proficient in using this powerful data structure.

[image1]:
  data:image/png;base64,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
