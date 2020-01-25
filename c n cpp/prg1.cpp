#include <bits/stdc++.h>1
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int a[]={6,2,5,5,4,5,6,3,7,6};
    
    int t,i;
    long p,q,s;
    cin>>t;
    while(t--)
    {
        cin>>p>>q;
        s=p+q;
        i=0;
        while(s>0)
        {
            i=i+a[s%10];
            s=s/10;
        }
        cout<<i<<"\n";
    }
    return 0;
}