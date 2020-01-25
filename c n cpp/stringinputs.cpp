#include<bits/stdc++.h>
#include<string>
using namespace std;
typedef long long int lli;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    cin.ignore();
    cout<<sizeof(lli);
    //method 1
    
    while(t--)
    {
    char s1[100];
    cin.getline(s1,100);
    char s2[100];
    cin.getline(s2,100);
    cout<<s1<<"\n"<<s2<<endl;
    
    
    
    // method 2
    
    // string s;
    // getline(cin,s);
    // cout<<"s="<<s;
    }
    
    return 0;
}
