m, n

2x1 1x2

- main logic is, if atleast m or n is even, then we can place the domino
  aligned to that even row/col

  Ex: 1x4   (xx)(xx) with 1 row  => 4/2 * 1 = 2
      2x4   (xx)(xx) with 2 rows => 4/2 * 2 = 4
      3x4   (xx)(xx) with 3 rows => 4/2 * 3 = 6
      6x2   (xx) with 6 rows     => 2/2 * 6 = 6

- the only other possibility is both being odd
  - such as 1x1, 1x3, 3x5
- odd sized grids, have even x even sub grid
XXXXX   XXXX       X
XXXXX = XXXX +     X
XXXXX          XXXXX

  NOTE: for 1x3, there is no even sub grid

                   X                    X
                   X    =           +   X
               XXXXX       XXXXX        X

  NOTE: the bottom right is counted twice, thats ok,
  because remaining area is m/2 + n/2
  so total = subgrid + m/2 + n/2

