#include<stdio.h>
void main()
{
    int a[10][10],i,j,k,n,y;
    printf("Enter dimension of the matrix:- ");
    scanf("%d",&n);
    printf("Enter the matrix elements:-\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
            if(i!=j && a[i][j]==0)
            a[i][j]=999;
        }
    }
    //algorithm starts
    for(k=0;k<n;k++)
    {
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                y=a[i][k]+a[k][j];
                if(a[i][j]>y)
                    a[i][j]=y;
            }
        }
    }

    // printing the result
    printf("The solution matrix is:-\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
         printf("%d\t",a[i][j]);
        printf("\n");
    }
}