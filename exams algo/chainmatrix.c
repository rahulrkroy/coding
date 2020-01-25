/* A naive recursive implementation that simply 
follows the above optimal substructure property */
#include <limits.h> 
#include <stdio.h> 

// Matrix Ai has dimension p[i-1] x p[i] for i = 1..n 
int MatrixChainOrder(int p[], int i, int j) 
{ 
	if (i == j) 
		return 0; 
	int k; 
	int min = INT_MAX; //or min=32767 
	int count; 

	// place parenthesis at different places between first 
	// and last matrix, recursively calculate count of 
	// multiplications for each parenthesis placement and 
	// return the minimum count 
	for (k = i; k < j; k++) { 
		count = MatrixChainOrder(p, i, k) + 
				MatrixChainOrder(p, k + 1, j) + 
				p[i - 1] * p[k] * p[j]; 

		if (count < min) 
			min = count; 
	} 
	// Return minimum count 
	return min; 
} 

// Driver program to test above function 
int main() 
{ 
	// int arr[] = { 5,4,6,2,7 }; 
	// int n = sizeof(arr) / sizeof(arr[0]); 
    int a[20],i,n;
    printf("Enter the number of matrices\n");
    scanf("%d",&n);
    printf("Enter nos in array\n");
    for(i=0;i<=n;i++)
        scanf("%d",&a[i]);
	printf("Minimum number of multiplications is %d ", 
		MatrixChainOrder(a, 1, n)); 

	return 0; 
} 
