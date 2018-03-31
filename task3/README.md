# Programming II

## Problem  
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the
following properties:
* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.

## Example,
Consider the following matrix:
 <br />
 [ <br />
 [1, 4, 7, 11, 15], <br />
 [2, 5, 8, 12, 19], <br />
 [3, 6, 9, 16, 22], <br />
 [10, 13, 14, 17, 24], <br />
 [18, 21, 23, 26, 30] <br />
 ] <br />
Given target = 5, return true. <br />
Given target = 20, return false. <br />

## Input
* Rows Columns
* Array sorted left to right and top to bottom
* Element x to be searched 
## Output
  Returns true if element searched is found, else it returns false.
### Example:
    Input:
    5 5 
    1  4  7  11 15
    2  5  8  12 19
    3  6  9  16 22 
    10 13 14 17 24 
    18 21 23 26 30 
    5 
    Output:
    true

## Algorithm
1. Start with top right element.
2. Compare the element val with x. <br />
   a) If they are equal then return true. <br />
   b) val < x then move it to down. <br />
   c) val > x then move it to left. <br />
 3. Repeat step 2 till you find element or till all rows and columns are traversed.
 4. If x is not found return false.
