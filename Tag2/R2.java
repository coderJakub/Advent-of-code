import java.io.*;
import java.util.Scanner;

public class R2 {

    static int getColor(String s){
        String col=s.split(" ")[2];
        switch (col) {
            case "blue": return 0;
            case "red" : return 1;
            case "green": return 2;
        }
        return -1;
    }
    static int[] control(String raffle){
        int col[] = new int[3];
        String cubes[] = raffle.split(",");
        for(String cube:cubes){
            col[getColor(cube)] +=Integer.parseInt(cube.split(" ")[1]);
        }
        return col;
    }
    public static void main(String[] args) {
        File f = new File(args[0]);
        int res=0;
        try{
            Scanner reader = new Scanner(f);
            //Pick each line
            while(reader.hasNextLine()){
                String data = reader.nextLine();
                String raffles[] = data.split(";");
                raffles[0] = raffles[0].split(":")[1];
                int minColor[] ={0,0,0};

                for(String i:raffles){
                    int raffleMin[] = control(i);
                    minColor[0]=(raffleMin[0]>minColor[0])?raffleMin[0]:minColor[0];
                    minColor[1]=(raffleMin[1]>minColor[1])?raffleMin[1]:minColor[1];
                    minColor[2]=(raffleMin[2]>minColor[2])?raffleMin[2]:minColor[2];
                }
                res+=minColor[0]*minColor[1]*minColor[2];
            }
            reader.close();
        }catch(FileNotFoundException e){
            System.exit(-1);
        }
        System.out.println(res);
    }
}