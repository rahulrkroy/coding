import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.util.*;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

class fileexample1
{
    public static void main(String[] args) throws IOException {
        Scanner in=new Scanner(System.in);
        File f1=new File("best.c");
        System.out.println(f1.exists());
        //f1.createNewFile();
        System.out.println(f1.getName());
        System.out.println(f1.canWrite());
        System.out.println(f1.length());
       
       /* FileOutputStream fout=new FileOutputStream(f1,true);
        String s=in.next();
        char c[]=s.toCharArray();
        for(char ch : c)
        {
            fout.write(ch);
        }
        fout.close();
        */

       /* FileInputStream fin=new FileInputStream(f1);
        int i=0;
        while(i!=-1){
            i=fin.read();
            if(i!=-1)
            System.out.print((char)i);
        }
        fin.close();
        */


        /*BufferedWriter br=new BufferedWriter(new FileWriter(f1,true));
        String s=in.next()+in.nextLine();
        br.write(s);
        br.close();
        */

        
        /*
        BufferedReader br=new BufferedReader(new FileReader(f1));
        
        // int i=0;
        // while((i=br.read())!=-1){
        //     if(i!=-1)
        //     System.out.print((char)i);
        // }
        
        //  String s1;
        // while((s1=br.readLine())!=null)
        //     System.out.println(s1);
        // br.close();

        char s[]=new char[20];
        br.read(s,2,5);
        System.out.println(s);

        */

        System.out.println();
    }
} 