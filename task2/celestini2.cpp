//Celestini program 2
#include<iostream>
#define MAX 100
using namespace std;

void print_sparse_matrix(int b[MAX][3]);
void read_sparse_matrix(int b[MAX][3]);
void multiply(int mat1[MAX][3], int mat2[MAX][3], int result_mul[MAX][3]);
void fast_transpose(int B1[MAX][3], int trans_mat[MAX][3]);
void convolution(int mat1[MAX][3], int mat2[MAX][3], int conv_mat[MAX][3]);

int main() {
  int matrix1[MAX][3], matrix2[MAX][3], result_mul[MAX][3], result_conv[MAX][3];
  read_sparse_matrix(matrix1);
  read_sparse_matrix(matrix2);
  multiply(matrix1, matrix2, result_mul);
  print_sparse_matrix(result_mul);
  convolution(matrix1, matrix2, result_conv);
  print_sparse_matrix(result_conv);
  return 0;
}

/* Function to input a sparse matrix
 * Row 1 has 3 entries
 * No_rows: Number of rows in sparse matrix
 * No_columns: Number of columns in sparse matrix
 * Non-zero_elements: Number of elements in sparse matrix with non-zero values
 * Row 1 to Non-zero_elements. Each input row has 3 entries.
 * i) Row: Index of row, where non-zero element is located
 * ii) Column: Index of column, where non-zero element is located
 * iii) Value: Value of the non zero element located at index – (row,column)
 */

void read_sparse_matrix(int matrix[MAX][3]) {
  int non_zero_elements;
  cout<<"\nEnter size of the matrix:";
  cin>>matrix[0][0]>>matrix[0][1];
  cout<<"\nEnter no. of non-zero elements:";
  cin >> non_zero_elements;
  matrix[0][2] = non_zero_elements;
  for(int i = 1; i <= non_zero_elements; i++) {
    cout<<"\n Enter the next triple(row,column,value) :";
    cin>>matrix[i][0]>>matrix[i][1]>>matrix[i][2];
  }
}

//Function to display a sparse matrix in array representation
void print_sparse_matrix(int matrix[MAX][3]) {
  int non_zero_elements = matrix[0][2];
  cout<<"\nrows ="<<matrix[0][0]<<"\tcolumns = "<<matrix[0][1]<<"\n";
  for(int i = 1; i <= non_zero_elements; i++)
    cout<<matrix[i][0]<<" "<<matrix[i][1]<<" "<<matrix[i][2]<<"\n";
}

//Function to Multiply two sparse matrices
void multiply(int matrix1[MAX][3], int matrix2[MAX][3], int result_mul[MAX][3]) {
  int transpose_matrix[MAX][3];
  int i, j, k, matrix1rno, matrix2colno, i1, sum;
  int matrix1_non_zero_elements = matrix1[0][2], matrix2_non_zero_elements = matrix2[0][2];
  //Condition for matrix multiplication i.e number of columns in matrix 1 = number of columns in matrix 2
  if(matrix1[0][1] != matrix2[0][0]) {
    cout<<"Matrices cannot be multiplied \n";
    exit(0);
  }
  fast_transpose(matrix2, transpose_matrix);  //Transpose the matrix2
  k = 1;       //Index for result_mul
  i = 1;
  while(i <= matrix1_non_zero_elements) {
    i1 = i;
    j = 1;
    while(j <= matrix2_non_zero_elements) {
      matrix1rno = matrix1[i][0];
      matrix2colno = transpose_matrix[j][0];
      sum = 0;

      while(i <= matrix1_non_zero_elements && j <= matrix2_non_zero_elements && matrix1rno == matrix1[i][0] && matrix2colno == transpose_matrix[j][0]) {
        if(matrix1[i][1] == transpose_matrix[j][1]) {
          sum = sum + matrix1[i][2] * transpose_matrix[j][2];
          i++; j++;
        }
        else
          if(matrix1[i][1] < transpose_matrix[j][1])
            i++;
          else
            j++;
      }
      if(sum != 0) {
        result_mul[k][0] = matrix1rno;
        result_mul[k][1] = matrix2colno;
        result_mul[k][2] = sum;
        k++;
      }
      if(j <= matrix2_non_zero_elements)
        i = i1;
      while(matrix2colno == transpose_matrix[j][0] && j <= matrix2_non_zero_elements)
        j++;
    }
    while(matrix1rno == matrix1[i][0] && i <= matrix1_non_zero_elements)
      i++;
  }
  result_mul[0][0] = matrix1[0][0];
  result_mul[0][1] = transpose_matrix[0][0];
  result_mul[0][2] = k-1;
}

//Function to transpose a matrix
void fast_transpose(int matrix[MAX][3], int transpose_matrix[MAX][3]) {
  int column_number, location;
  int total[MAX], index[MAX];
  int rows = matrix[0][0], columns = matrix[0][1], non_zero_elements = matrix[0][2];
  transpose_matrix[0][0] = rows, transpose_matrix[0][1] = columns, transpose_matrix[0][2] = non_zero_elements;
  for(int i = 0; i < columns; i++)
    total[i] = 0;
  for(int i = 1; i <= non_zero_elements; i++) {
    column_number = matrix[i][1];
    total[column_number]++;
  }
  index[0] = 1;
  for(int i = 1; i <= columns; i++)
    index[i] = index[i-1] + total[i-1];

  for(int i = 1; i <= non_zero_elements; i++) {
    column_number = matrix[i][1];
    location = index[column_number];
    index[column_number]++;
    transpose_matrix[location][0] = matrix[i][1];
    transpose_matrix[location][1] = matrix[i][0];
    transpose_matrix[location][2] = matrix[i][2];
  }
} 


//Function to convolve two matrices
void convolution(int mat1[MAX][3], int mat2[MAX][3], int conv_mat[MAX][3]) {
  int i, j, sum;
  i = 1; j = 1; sum = 0; //i and j are the indices for the sparse matrices i.e mat1[][] and mat2[][] respectively.
  while(i <= mat1[0][2] && j <= mat2[0][2])
  {
    if(mat1[i][0] == mat2[j][0]){
      if( mat1[i][1] == mat2[j][1]){
        sum = sum + mat1[i][2]*mat2[j][2];
        i++;
        j++;
      }
      else if( mat1[i][1] > mat2[j][1])
        j++;
      else
        i++;
    }
    else if(mat1[i][0] > mat2[j][0])
      j++;
    else 
      i++;
  }
  conv_mat[0][0] = 1;
  conv_mat[0][1] = 1;
  conv_mat[0][2] = 1;
  conv_mat[1][0] = 1;
  conv_mat[1][1] = 1;
  conv_mat[1][2] = sum;
}
