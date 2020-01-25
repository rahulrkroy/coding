#include<bits/stdc++.h>
#include<stack>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i;
    stack<int> s;
    int a[]={1,2,3,4,5};
    for(i=0;i<5;i++)
    s.push(a[i]);
    cout<<s.size()<<endl;
    while(!s.empty())
    {
        cout<<s.top()<<endl;
        s.pop();
    }
    cout<<s.empty()<<endl;
}