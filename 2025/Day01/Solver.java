package Day01;

import helper.FileReader;
import java.util.List;

public class Solver {
    
    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader(args);
        List<String> lines = fr.readLines();
        
        int dial = 50;
        int p1 = 0;
        int p2 = 0;
        for (String line : lines) {
            int incr = (line.charAt(0) == 'R') ? 1 : -1;
            int am = incr*Integer.parseInt(line.substring(1));
            dial += am;
            p2 += Math.abs((int)(dial/100)) + (dial<=0 && dial!=am? 1 : 0);
            dial = Math.floorMod(dial, 100);
            if (dial==0) p1 += 1;
        }
        System.out.println("Part 1: " + p1);
        System.out.println("Part 2: " + p2);
    }
}