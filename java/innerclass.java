interface prg
{
   public void show();
}
class innerclass
{
    
    public static void main(String[] args) {

        //anonnymous inner class
        
        // prg ob=new prg()
        // {
        //     public void show()
        //     {
        //         System.out.println("hello");
        //     }
        // };

        //lambda expression
        prg ob=()->
            {
                System.out.println("hello");
            };

        ob.show();


        // a obj=new a();
        // a.b obj2=obj.new b();

        a.b obj2=new a.b();
        obj2.show();
    }
}

class a{
    void show()
    {
        System.out.println("a class");
    };

    static class b{
    void show()
    {
        System.out.println("b class");
    }
    }

}