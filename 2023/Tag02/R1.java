import java.io.*;
import java.util.Scanner;

public class R1 {

    static int getColor(String s){
        String col=s.split(" ")[2];
        switch (col) {
            case "blue": return 0;
            case "red" : return 1;
            case "green": return 2;
        }
        return -1;
    }
    static boolean control(String raffle){
        int col[] = new int[3];
        String cubes[] = raffle.split(",");
        for(String cube:cubes){
            col[getColor(cube)] +=Integer.parseInt(cube.split(" ")[1]);
        }
        if(col[0]>14 || col[1]>12 || col[2]>13)return false;
        else return true;
    }
    public static void main(String[] args) {
        File f = new File(args[0]);
        int id = 1;
        int res=0;
        try{
            Scanner reader = new Scanner(f);
            //Pick each line
            while(reader.hasNextLine()){
                String data = reader.nextLine();
                String raffles[] = data.split(";");
                raffles[0] = raffles[0].split(":")[1];
                boolean legal=true;
                for(String i:raffles){
                    legal =control(i);
                    if(!legal)break;
                }
                if(legal)res+=id;
                id++;
            }
            reader.close();
        }catch(FileNotFoundException e){
            System.exit(-1);
        }
        System.out.println(res);
    }
}