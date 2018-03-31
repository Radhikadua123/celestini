# Programming 

## Problem  
Given two sparse matrices A and B, perform multiply and convolution operation of the matrices
in their sparse form itself. The result should consist of two sparse matrices, one obtained by
multiplying the two input matrices, and the other obtained by convolution of the two matrices.
### Sparse matrices
A sparse matrix is a matrix in which most of the elements are zero. In the program, the sparse matrix used anywhere is sorted according to its row values. Two elements with the same row values are further sorted according to their column values.
### Convolution
Convolution is the process of adding each element one matrix to its local neighbors, weighted by the second matrix. This is related to a form of mathematical convolution. 
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
    

## Approach for multiplication of two sparse matrices
### To Multiply two sparse matrices: <br />
 1. First calculate transpose of the second matrix to simply our comparisons and maintain the sorted order. <br /> 
 2. Traversing both matrices and summing the appropriate multiplied values. <br />

Resultant matrix obtained after multiplying two sparse matrices is represented by '''mul_mat'''. <br />
Any element mul_mat[x][y] of the resultant matrix is obtained by multiplying all elements with row value equal to x in the first matrix and elements with row value equal to y in the second matrix (transposed one) and having the same column value in both matrices and  then adding them.
### To Convolve two sparse matrices: <br />
 1. Start from row 2 of matrix 1 and 2. Initialize sum with 0. <br /> 
 2. Compare row_no of element in both matrix 1 and 2: <br />
    a) if row_no both matrices are equal, compare column_no of element in both matrix 1 and 2:
      i) if they are equal, then multiply them and add it in the sum variable.  <br /> 
      ii)if column_no of matrix 1 is greater than column_no of matrix 2, then increment the row of sparse matrix 2.
      iii) else increment the row of sparse matrix 1.
    b)if row_no of matrix 1 is greater than row_no of matrix 2, then increment the row of sparse matrix 2.
    c) else increment the row of sparse matrix 1 .
  3. The sum is the convolution of two matrices.




