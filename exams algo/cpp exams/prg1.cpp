#include<iostream>
using namespace std;
class abc{
    
    public:
    int a;
    abc(int x)
    {
        a=x;
    }
    abc (abc &ob)
    {
        a=ob.a;
    }
};

int main()
{
    abc ob1(10);
    abc ob2(ob1);
    cout<<ob2.a<<endl;
}
