class oa
{
    void display(){
        System.out.println("display called");
    }
    static void abc()
    {
        oa obj=new oa();
        obj.display();
    }
    @Override
    protected void finalize() throws Throwable {
        System.out.println("finalize called");
    }
    public static void main(String[] args) {
        oa.abc();
        System.gc();
        int a[]={1,2,3,4,5,6,7,8,9,0};
        for(int i:a)
        System.out.println(i);
    }
}