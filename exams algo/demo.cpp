#include<iostream>
using namespace std;
void d(int& m)
{
    cout<<m;
    int n=m+2;
    m=n;
}

int main()
{
    int max=12;
    d(max);
    cout<<max;
}