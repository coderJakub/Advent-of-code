import java.io.*;
import java.util.*;

public class R2 {
  public static void main(String args[]){
        File f = new File(args[0]);
        int res=0;
        String numbers[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        try{
            Scanner reader = new Scanner(f);
            //Pick each line
            while(reader.hasNextLine()){
                String data = reader.nextLine();
                String num="";

                //Find first num
                for(int i=0; i<data.length(); i++){
                    if(Character.isDigit(data.charAt(i))){
                        num+=data.charAt(i);break;
                    }
                    boolean check = false;
                    for(int j=0; j<i; j++){
                        for(int k=0; k<numbers.length; k++)if(data.substring(j, i+1).equals(numbers[k])){
                                num+=k+1; check=true; break;
                        }
                        if(check)break;
                    }
                    if(check)break;
                }
                    
                //Find last num
                for(int i=data.length()-1; i>=0; i--){
                    if(Character.isDigit(data.charAt(i))){
                        num+=data.charAt(i);break;
                    }
                    boolean check = false;
                    for(int j=data.length()-1; j>i; j--){
                        for(int k=0; k<numbers.length; k++)if(data.substring(i, j+1).equals(numbers[k])){
                                num+=k+1; check=true; break;
                        }
                        if(check)break;
                    }
                    if(check)break;
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
