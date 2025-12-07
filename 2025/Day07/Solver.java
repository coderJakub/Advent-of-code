package Day07;
import helper.FileReader;
import java.util.*;

public class Solver{
    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader(args);
        String[] lines = fr.readLines();

        int p1 = 0;
        long p2 = 0;

        int C = lines[0].length();

        long[] beams = new long[C];
        beams[lines[0].indexOf('S')] = 1;

        for (int layer=1; layer<lines.length; layer++){
            long[] temp = new long[C];
            for (int i=0; i<C; i++){
                if (beams[i]==0)continue;
                if (lines[layer].charAt(i)=='.')temp[i] += beams[i];
                else{
                    p1++;
                    if(i+1<C) temp[i+1] += beams[i];
                    if(i-1>=0) temp[i-1] += beams[i];
                }
            }
            beams = temp;
        }

        p2 = Arrays.stream(beams).sum();
        System.out.println("Part 1: "+ p1);
        System.out.println("Part 2: "+ p2);
    }
}