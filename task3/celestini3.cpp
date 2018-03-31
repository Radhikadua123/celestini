#include<iostream>
#include<vector>
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

bool search(vector<vector<int>> &array, int p, int q, int item);

int main() {
  int rows, columns,item;
  // Enter rows and columns
  cin>>rows>>columns;
  vector<vector<int>> array;
  // Enter elements of array
  for(int i = 0; i < rows; i++) {
    vector<int> row;
    for(int j = 0; j < columns; j++) {
      int temp; cin>>temp;
      row.push_back(temp);
     }
    array.push_back(row);
  }
  // Enter element to be searched
  cin>>item;
  bool ans = search(array, rows - 1, columns - 1, item);
  if(ans)
	cout<<"true"<<"\n";
  else
	cout<<"false"<<"\n";
  return 0;
}

// Algorithm details are provided in the README.md for task 3.
bool search(vector<vector<int>> &array, int p, int q, int item){
  int rowIndex = 0, colIndex = q;
  while(rowIndex < p && colIndex >= 0) {
    if(array[rowIndex][colIndex] == item)
      return true;
    else if(array[rowIndex][colIndex] > item)
      colIndex--;
    else
      rowIndex++;
  }
  return false;
}

