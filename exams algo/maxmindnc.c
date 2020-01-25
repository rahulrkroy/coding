#include<stdio.h>
int a[50];
void maxmin(int i,int j,int* max,int* min)
{
    if(i==j)
    {
            *max=a[i];
            *min=a[j];
        return;
    }
    else if((j-i) == 1)
    {
        if(a[i]<a[j])
        {
            if(*max<a[j])
                *max=a[j];
            if(*min>a[i])
            *min=a[i];
        }
        else
        {
            if(*max<a[i])
            *max=a[i];
            if(*min>a[j])
            *min=a[j];
        }
        return;
    }
        int mid=(i+j)/2;
        maxmin(i,mid,max,min);
        maxmin(mid,j,max,min);
}

int main()
{
    int n,max,min;
    //int a[100];
    printf("Enter size \n");
    scanf("%d",&n);
    printf("Enter the no in array");
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    max=a[0],min=a[0];
    maxmin(0,n-1,&max,&min);
    printf("max = %d",max);
    printf("min = %d",min);
   return 0;
}
