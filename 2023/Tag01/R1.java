import java.io.*;
import java.util.*;

public class R1 {

    public static void main(String args[]){
        File f = new File(args[0]);
        int res=0;

        try{
            Scanner reader = new Scanner(f);

            //Pick each line
            while(reader.hasNextLine()){
                String data = reader.nextLine();
                String num="";

                //Find first num
                for(int i=0; i<data.length(); i++)if(Character.isDigit(data.charAt(i))){
                    num+=data.charAt(i);break;
                }
                //Find last num
                for(int i=data.length()-1; i>=0;i--)if(Character.isDigit(data.charAt(i))){
                    num+=data.charAt(i); break;
                }
                //Add result to the num
                res+=Integer.valueOf(num);
            }
            
            reader.close();
        }catch(FileNotFoundException e){
            System.exit(-1);
        }
        System.out.println(res);
    }
}