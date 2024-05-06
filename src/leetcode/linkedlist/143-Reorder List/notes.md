# 143 - Reorder List  
[LeetCode](https://leetcode.com/problems/reorder-list/description/)


Learnings:  
- I failed so many times on how to break the list  
    - got confused how to break if length=even vs. length=odd  
    - best way to break a list is to use slow, fast poniters
    - ** there is no need to set the middle_node.next to None**
       because when we pass the head of the right-half into the 
       reverse_list fn we are setting this nodes.next to None, since
       we initiate prev=None


Visialization of `slow`, `fast` pointers:
- slow will always point to the middle item(upper bound if odd) when
  fast pointer goes out of bound  

IN: 1 2 3 4 5
1 2 3 4 5
---------
s | | | |
f | | | |
---------
  s | | |
    f | |
---------
    s | |
        f
OUT:
1 2 3 4 5
---------
    M

1->2  x<-3<-4<-5
---   ----------
L              R


IN: 1 2 3 4 5 6
1 2 3 4 5 6
-----------
s | | | | |
f | | | | |
-----------
  s | | | |
    f | | |
-----------
    s | | |
        f |
OUT:
1 2   3 4 5 6
----  -------
      M

1->2  x<-3<-4<-5<-6
---   -------------
L                 R


Final Approach:
1. break the 

