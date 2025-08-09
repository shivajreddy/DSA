even numbers
split into evens
need not be equal
1 <= w <= 100

edge case:
w = 1
NO

edge case: 
w = 2
NO

- when split if one is even, the other will always be even  
- min weight to split is 2, and splitting 2 results in [1,1] they are odd, so NO  
- from 3..100 all even are YES, all odd are NO
