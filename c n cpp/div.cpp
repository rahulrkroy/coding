#include<bits/stdc++.h>
using namespace std;

int convert(long int n)
{
    int p,r;
    while(n>0)
    {
        r=n/12;
        
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int sum,t;
    long int n;
    int r,p;
    cin>>t;
    // cin.ignore();
    while(t--)
    {
        cin>>n;
        p=0;r=0;
        while(n>0)
        {
            p=p*10+(n/26);
            r=n%26;
            n=n/26;
        }
        cout<<r<<endl;
        cout<<p<<endl;
        // if(n>0)
        //     cout<<(char)(n+64);
        // cout<<'\n';
    }
}