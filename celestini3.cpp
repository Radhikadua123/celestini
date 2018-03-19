#include<iostream>
using namespace std;

bool search(int A[100][100], int p, int q, int item);

int main()
{
	int m,n,item;
	cout<<" Number of elements in array \n";
	cin>>m>>n;
	int A[100][100];
	cout<<"Enter the elemnts of the array \n";
	for(int i = 0;i < m;i++)
	for(int j = 0;j < m;j++)
	 	cin>> A[i][j];
	cout<<" Enter the element to be searched \n";
	cin>>item;
	cout<<"The array is \n";
	for(int i = 0;i < m;i++)
	{
	for(int j = 0;j < m;j++)
	 	cout<< A[i][j]<<" ";
	cout<<"\n";
	
	}
	int p = m-1;
	int q = n-1;
	bool ans = search(A, p, q, item);
	cout<<ans<<"\n";
	return 0;
}

bool search(int A[100][100], int p, int q, int item)
{	int flag = 0,r=0;
	while(p>=0 && r<q)
	{
		if(A[p][r] == item)
		{	flag = 1;
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
			

