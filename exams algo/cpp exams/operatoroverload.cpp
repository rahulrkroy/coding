#include<iostream>
using namespace std;

class abc{
    int x;
    public:
    abc()
    {}
    abc(int a)
    {
        x=a;
    }
    abc operator +(abc obj)
    {
        abc obj1;
        obj1.x=x+obj.x;
        return obj1;
    }
    void display()
    {
        cout<<"x= "<<x<<endl;
    }
};
int main()
{
    abc ob1(5);
    abc ob2(2);
    abc ob3;
    ob3=ob1 +ob2;
    ob3.display();
}