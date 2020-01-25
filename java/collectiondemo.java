import java.util.*;

class collectiondemo
{
    public static void main(String[] args) {
        long t1=System.currentTimeMillis();
        List <Integer> val=new  ArrayList<>();


        Comparator<Integer> cmp=new Comparator<Integer>(){
        
            @Override
            public int compare(Integer arg0, Integer arg1) {
                // TODO Auto-generated method stub
                if(arg0>arg1)
                return 1;
                else return -1;
            }
        };

        val.add(1);
        val.add(2);
        val.add(1,9);
        // Collections.sort(val, cmp);
        val.sort(cmp);
        // val.sort();
        // Collections.sort(val);
        // val.add("rahul");
        // val.remove(1);
        System.out.println(val);
        System.out.println(val.size());

        Set<Integer> ex=new HashSet<>();
        ex.add(4);
        ex.add(7);
        ex.add(4);
        for(int i:ex)
            System.out.println(i);
        System.out.println(ex);

        Map<String,Integer> m=new HashMap<>();
        m.put("one", 1);
        m.put("two", 2);
        m.put("three",3);
        System.out.println(m);

        Set <String> s=m.keySet();
        for(String key :s)
        {
            System.out.println(key+"="+m.get(key));
        }
        long t2=System.currentTimeMillis();
        System.out.println("Time taken= "+(t2-t1)+" milisecond");
    }
}