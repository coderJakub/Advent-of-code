import java.util.*;

public class Day3{
    public static void main(String[] args){
        ReadInput reader = new ReadInput();
        ArrayList<String> lines = reader.readLines("input.txt");

        int gamma = 0;
        int epsilon = 0;
        int numLength = lines.get(0).length();
        for(int i = 0; i<numLength; i++){
            int count = 0;
            for(String line : lines)if(line.charAt(i)=='1')count++;
            if(count>lines.size()/2)
                gamma += Math.pow(2, numLength-i-1);
            else
                epsilon += Math.pow(2, numLength-i-1);
        }
        ArrayList<String> lines2 = lines;
        for (int i = 0; i<numLength; i++){
            for(boolean ox : new boolean[]{true,false}){
                int count = 0;
                ArrayList<String> newList = new ArrayList<String>();
                ArrayList<String> l = ox?lines:lines2;
                if(l.size()==1)continue;
                for(String line : l)if(line.charAt(i)=='1')count++;
                for(String line : l){
                    if(count*2>=l.size()){
                        if(ox && line.charAt(i)=='1')newList.add(line);
                        if(!ox && line.charAt(i)=='0')newList.add(line);
                    }else{
                        if(ox && line.charAt(i)=='0')newList.add(line);
                        if(!ox && line.charAt(i)=='1')newList.add(line);
                    }
                }
                if(ox)lines = newList;
                else lines2 = newList;
            }
            
        }
        int ox = Integer.parseInt(lines.get(0),2);
        int oy = Integer.parseInt(lines2.get(0),2);
        System.out.println("Part 1: "+gamma*epsilon);
        System.out.println("Part 2: "+ox*oy);
    }
}