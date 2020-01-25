#include<iostream>
#include<string>
using namespace std;
int main()
{
    int i,t;
    cin>>t;
    long long p,n,f[60];
    f[0]=0;
    f[1]=1;
    for(i=2;i<60;i++)
    {
        f[i]=f[i-1]+f[i-2];
    }
    for(i=0;i<t;i++)
    {
        long long n;
        cin>>n;
        long long p=1;
        while(p*2<n)
        {p=p*2;}
        p=p-1;
        cout<<"p="<<p<<endl;
        cout<<"f[p]=1"<<f[p%60]<<endl;
        cout<<((f[p%60])%10)<<endl; 
    }
    return 0;
}