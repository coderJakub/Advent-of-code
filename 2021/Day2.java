import java.util.*;

public class Day2{
    public static void main(String[] args){
        ReadInput readInput = new ReadInput();
        ArrayList<String> lines = readInput.readLines("input.txt");

        int horizontal = 0;
        int depth1 = 0;
        int depth2 = 0;
        int aim = 0;

        for(String line:lines){
            String[] parts = line.split(" ");
            int x = Integer.parseInt(parts[1]);
            switch (parts[0]) {
                case "forward":
                    horizontal +=x;
                    depth2 += aim*x;
                    break;
                case "down":
                    aim += x;
                    depth1 += x;
                    break;
                case "up":
                    aim -= x;
                    depth1 -= x;
                    break;
            }
        }
        System.out.println("Part 1: "+ horizontal*depth1);
        System.out.println("Part 2: "+ horizontal*depth2);
    }
}