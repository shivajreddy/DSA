"""
Mergesort is O(n log n). Why Do We Need The Others?
"""

"""
Would’t it be beneficial just learning mergesort since it has faster runtime than other sorting techniques? Or 
would they actually ask us to use insertion sort or selection sort in certain scenarios? This is a great question. If 
you don't know why you're learning something, staying motivated to understand them can be difficult.

Someone will unlikely ask you to implement these approaches in an interview. If you need to sort an array in 
interviews you call arr.sort() which is O(n log n) using TimSort We cover selection sort and insertion sort to view 
sorting algorithms that can work if you are under different constraints. For example, if you have a linked list and 
cannot access the array index, you are struck with insertion sort. We're not just learning quicksort, mergesort, 
etc. They all rely on different techniques to solve the problem of sorting. Mergesort teaches that you can solve 
problems by dividing them in half and combining the resulting sub-problems. This is an O(n log n) solution and can be 
a helpful technique (divide and conquer). Many interview questions may have a similar but not the same idea. 
Quicksort is another example of divide and conquer, but it is different in that it does not divide the problem 
precisely in half, but you can still divide a problem unevenly. It's also a great example of a randomized algorithm 
where you don't know where the partition will end up. Insertion Sort is an example of an approach where you build 
incrementally to the solution. This is especially important if you cannot look ahead (the rest of the array is not 
touched); perhaps you're sorting a stream of numbers rather than an array. Selection Sort. An example of just picking 
the best element and using that right away. Although inefficient for sorting, it could be efficient for other 
problems that allow a greedy approach. Heapsort is an optimized version of selection sort because you can find the 
max element much faster.
"""
