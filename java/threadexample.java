class threadexample
{
    public static void main(String[] args) throws Exception {
        for(int i=0;i<5;i++)
        {
            System.out.println(i);
            Thread.sleep(500);
        }
    }
}
