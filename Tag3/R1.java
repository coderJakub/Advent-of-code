import java.io.*;
import java.util.*;

public class R1 {
    public static boolean checkNum(int startNum, int endNum, int line, ArrayList<String> data){
        for(int i=startNum-1; i<=endNum+1;i++){
            for(int j=line-1; j<=line+1;j++){
                if(i>=0  && j>=0 && j<data.size() && i<data.get(j).length()){
                    if(data.get(j).charAt(i)!='.' && !Character.isDigit(data.get(j).charAt(i)))return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args)throws Exception{
        File f = new File(args[0]);
        ArrayList<String> data = new ArrayList<String>();

        Scanner r = new Scanner(f);
        while(r.hasNextLine())data.add(r.nextLine());
        r.close();

        int res=0;
        int startNum=-1;
        String num="";
        for(int i=0; i<data.size(); i++){

            String line = data.get(i);

            for(int j=0; j<line.length(); j++){
                if(Character.isDigit(line.charAt(j))){
                    if(startNum==-1)startNum=j;
                    num+=line.charAt(j);
                }
                if(startNum!=-1 && (!Character.isDigit(line.charAt(j)) || j==line.length()-1)){
                    if(checkNum(startNum, (j==line.length()-1)?j:j-1, i, data))res+=Integer.parseInt(num);
                    num=""; startNum=-1;
                }
            }
        }
        System.out.println(res);
    }
}
