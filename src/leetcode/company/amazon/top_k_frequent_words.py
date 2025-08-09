"""
Possible Approaches:

1. Counting Frequencies:
   - Use a hash map to count the frequency of each word.

2. Sorting:
   - Sort the words based on their frequency and lexicographical order.
   - Time complexity: O(n log n).

3. Using a Heap (Priority Queue):
   - Maintain a heap of size `k` to keep track of the top `k` elements.
   - Time complexity: O(n log k).

Choosing the Optimal Approach:
    - Since we need to sort based on frequency and lex order, and `k` can be up to 
    the number of unique words, sorting may be acceptable.
    - However, using a heap can optimize performance when `k` is much smaller than
    the number of unique words.
    - For this problem, both approaches are acceptable, but we'll implement both 
    and discuss their trade-offs.

---

Algorithm Design

Approach 1: Sorting
    1. Count Word Frequencies:
        - Use `Counter` (from `collections`) to count the frequency of each word.
    2. Sort Words:
        - Sort the words based on two criteria:
            - First Criterion: Frequency in descending order.
            - Second Criterion: Lexicographical order in ascending order.
    3. Extract Top `k` Words:
        - After sorting, take the first `k` words from the sorted list.

Time Complexity Analysis:
    - Counting frequencies: O(n), where `n` is the number of words.
    - Sorting: O(m log m), where `m` is the number of unique words.
    - Total time complexity: O(n + m log m).
Space Complexity Analysis:
    - O(m) for storing word frequencies, where `m` is the number of unique words.

---

Approach 2: Using a Heap
    1. Count Word Frequencies:
        - Use `Counter` to count the frequency of each word.
    2. Use a Min Heap:
        - Use a heap to maintain the top `k` frequent words.
        - The heap is sorted based on frequency, and for words with the same frequency,
          by lexicographical order.
        - Since Python's `heapq` is a min-heap, we invert the frequency to simulate a max-heap.
    3. Extract Top `k` Words:
        - After building the heap, extract the words and reverse the result since 
          we need the most frequent words first.

Time Complexity Analysis:
    - Counting frequencies: O(n).
    - Building the heap: O(m log k).
    - Total time complexity: O(n + m log k).
Space Complexity Analysis:
    - O(m) for storing word frequencies.
    - O(k) for the heap.

---

Summary of Trade-offs:

- Sorting Approach:
  - Simpler to implement.
  - More efficient when `k` is close to `n` (i.e., when we need many frequent words).
  
- Heap Approach:
  - More efficient when `k` is much smaller than `n` (i.e., when we only need 
    a few frequent words).
  - Slightly more complex due to the use of a heap.
"""



""" Using common library comporators, for achieving lexicographical order """
'''
from typing import List
from collections import Counter

class SolutionSorting:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        count = Counter(words)

        # Sort the words based on frequency and lex order
        sorted_words = sorted(count.items(), key=lambda x: (-x[1], x[0]))

        # Extract the top k words
        result = [word for word, _ in sorted_words[:k]]
        return result

import heapq
from typing import List
from collections import Counter

class SolutionHeap:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        count = Counter(words)

        # Use a min heap to keep the top k elements
        heap = []
        for word, freq in count.items():
            # Push a tuple with negative frequency to simulate a max heap
            heapq.heappush(heap, (-freq, word))

        # Extract the top k words from the heap
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result

# '''


""" Custom comparator for achieving lexicographical order """
# '''
from typing import List
from collections import Counter
from functools import cmp_to_key

class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        count = Counter(words)

        # Define custom comparator
        def compare_items(a, b):
            # a and b are tuples (word, frequency)
            word_a, freq_a = a
            word_b, freq_b = b

            # We need to sort by frequency descending, then lex order ascending
            if freq_a != freq_b:
                return freq_b - freq_a  # Higher frequency comes first
            else:
                if word_a < word_b:
                    return -1  # Word a comes before word b
                elif word_a > word_b:
                    return 1   # Word b comes before word a
                else:
                    return 0   # Words are the same

        # Convert the comparator to a key function
        sorted_items = sorted(count.items(), key=cmp_to_key(compare_items))

        # Extract the top k words
        result = [word for word, _ in sorted_items[:k]]
        return result

import heapq
from typing import List
from collections import Counter

class WordFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq  # Frequency is stored as positive integer

    def __lt__(self, other):
        # Compare frequencies; since we are using a min heap,
        # we want higher frequencies to come first.
        if self.freq != other.freq:
            return self.freq < other.freq  # Higher frequency comes first
        else:
            # For words with the same frequency, compare lexicographically
            return self.word > other.word  # Lexicographically smaller word comes first

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        count = Counter(words)

        # Use a min heap to keep the top k elements
        heap = []
        for word, freq in count.items():
            # Push an instance of WordFreq onto the heap
            heapq.heappush(heap, WordFreq(word, freq))
            # If heap size exceeds k, pop the smallest item
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the words from the heap and sort them
        # Since heapq returns the smallest item, we need to reverse the result
        result = []
        while heap:
            word_freq = heapq.heappop(heap)
            result.append(word_freq.word)
        result.reverse()  # Reverse to get the correct order
        return result

# '''

