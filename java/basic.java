import java.util.*;


interface b{}
interface a{
   public void abc();
}
class basic implements a,b
{
    int x;
   public void abc()
    {
        System.out.println("hello");
        x=5;
    }
    public static void main(String[] args) {
        System.out.println("hello");
        basic ob=new basic();
        ob.abc();
        if(ob instanceof b){
            System.out.println(ob);
        }
    }
    public void kill()
    {
        System.out.println();
    }
}
