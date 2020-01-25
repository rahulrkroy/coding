#include<stdio.h>
void knapsack(int n,int cap, float weight[],float profit[])
{
    float x[20],tp=0;
    int i,j;

    for(i=0;i<n;i++)
        x[i]=0;
    
    for(i=0;i<n;i++)
    {
        if(weight[i]>cap)
        {
            break;
        }
        else
        {
            x[i]=1;
            tp=tp+profit[i];
            cap=cap-weight[i];
        } 
    }
    if(i<n)
        x[i]=cap/weight[i];

    tp=tp+(x[i]*profit[i]);

    printf("The result vector is :- ");
    for(i=0;i<n;i++)
    printf("%f\t",x[i]);

    printf("Maximum profit is :- %f",tp);
}

int main()
{
    float profit[200],ratio[200],weight[200],temp;
    int n,cap,i,j;
    printf("Enter the number of objects\n");
    scanf("%d",&n);
    printf("Enter the weights and profits of each objects:- \n");
    for(i=0;i<n;i++)
        scanf("%f%f",&weight[i],&profit[i]);
    printf("Enter capacity of knapsack:- ");
    scanf("%d",&cap);

    for(i=0;i<n;i++)
        ratio[i]=profit[i]/weight[i];
    
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(ratio[j]>ratio[i])
            {
                temp=ratio[i];
                ratio[i]=ratio[j];
                ratio[j]=temp;

                temp=profit[i];
                profit[i]=profit[j];
                profit[j]=temp;

                temp=weight[i];
                weight[i]=weight[j];
                weight[j]=temp;
            }
        }
    }
    knapsack(n,cap,weight,profit);
    return 0;
}