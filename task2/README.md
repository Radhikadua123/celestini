# Programming 

## Problem  
Given two sparse matrices A and B, perform multiply and convolution operation of the matrices
in their sparse form itself. The result should consist of two sparse matrices, one obtained by
multiplying the two input matrices, and the other obtained by convolution of the two matrices.
### Sparse matrices
A sparse matrix is a matrix in which most of the elements are zero. 
## Input
 * Row 1 has 3 entries <br />
  No_rows: Number of rows in sparse matrix <br />
  No_columns: Number of columns in sparse matrix <br />
  Non-zero_elements: Number of elements in sparse matrix with non-zero values <br />
 * Row 1 to Non-zero_elements. Each input row has 3 entries. <br />
  i) Row: Index of row, where non-zero element is located <br />
  ii) Column: Index of column, where non-zero element is located <br />
  iii) Value: Value of the non zero element located at index – (row,column) <br />
 
## Example:
### Input:
#### Sparse matrix 1:
    Row Column Value
    4   4       5
    1   2       10
    1   4       12
    3   3       5
    4   1       15
    4   2       12
    
#### Sparse matrix 2:
    Row Column Value
    4   4      5
    1   3       8
    2   4       23
    3   3       9
    4   1       20
    4   2       25
   
### Output:
#### Result of Multiplication:
    Row Column Value
    4   4      6
    1   1      240
    1   2      300
    1   4      230
    3   3      45
    4   3      120
    4   4      276
#### Result of Convolution:
    Row Column Value
    1   1      1
    1   1      645
    

## Algorithm for multiplication of two sparse matrices
1. Start with top right element.
2. Compare the element val with x. <br />
   a) If they are equal then return true. <br />
   b) val < x then move it to down. <br />
   c) val > x then move it to left. <br />
 3. Repeat step 2 till you find element or till all rows and columns are traversed.
 4. If x is not found return false.
