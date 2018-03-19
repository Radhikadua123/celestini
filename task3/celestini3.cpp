#include<iostream>
using namespace std;
/* 
 * Input format:
 * Rows Columns
 * Array sorted left to right and top to bottom
 * Element tp be searched

 * Output Format:
 * True/False for element found/not found.
 
 * Example:
 * 2 3
 * 1 2 3
 * 2 4 6
 * 3
 *
 * True
*/

bool search(int A[100][100], int p, int q, int item);

int main()
{
  int m, n,item;
  // Enter rows and columns
  cin>>m>>n;
  int A[m][n];
  // Enter elements of array
  for(int i = 0; i < m; i++)
    for(int j = 0; j < m; j++)
      cin>>A[i][j];
  // Enter element to be searched
  cin>>item;
  int p = m - 1, q = n - 1;
  bool ans = search(A, p, q, item);
  cout<<ans<<"\n";
  return 0;
}

// Algorithm details are provided in the README.md for task 3.
bool search(int A[100][100], int p, int q, int item){
  int flag = 0,r = 0;
  while(p > = 0 && r < q) {
    if(A[p][r] == item) {
      flag = 1;
      break;
    }
    else if(A[p][r] > item)
      p--;
    else
      r++;
  }
  if(flag)
    return true;
  return false;
}

