import java.util.*;

public class Day1{
    public static void main(String[] args) {
        ReadInput readInput = new ReadInput();
        ArrayList<String> lines = readInput.readLines("input.txt");
        
        int p1 = 0;
        int p2 = 0;
        for(int i = 0; i<lines.size(); i++){
            if(i>0 && Integer.parseInt(lines.get(i))>Integer.parseInt(lines.get(i-1)))p1+=1;
            if(i>2 && Integer.parseInt(lines.get(i))>Integer.parseInt(lines.get(i-3)))p2+=1;
        }
        System.out.println("Part 1: "+p1);
        System.out.println("Part 2: "+p2);
    }
}