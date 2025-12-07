package Day06;
import helper.FileReader;
import java.util.*;

public class Solver{
    public static long calcSolution(int startBlock, int endBlock, String[] lines, boolean vertical){
        char op = lines[lines.length-1].charAt(startBlock);
        long num = op=='*'?1:0;

        int startA = vertical ? 0 : startBlock;
        int endA = vertical ? lines.length-1 : endBlock;
        int startB = vertical ? startBlock : 0;
        int endB = vertical ? endBlock : lines.length-1;

        for (int i=startA; i<endA; i++){
            long curr = 0;
            for (int j=startB; j<endB; j++){
                char c = vertical?lines[i].charAt(j):lines[j].charAt(i);
                if (c != ' ') curr = curr * 10 + (c-'0');
            }
            if (op=='*') num*=curr;
            else num+=curr;
        }
        return num;
    }

    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader(args);
        String[] lines = fr.readLines();

        long p1 = 0;
        long p2 = 0;

        int idx = 0;
        int R = lines.length;
        int C = lines[0].length();
        while (idx<C){
            int start = idx;
            while (idx+1==C || idx+1<C && lines[R-1].charAt(idx+1) == ' ')idx++;
            p1 += calcSolution(start, idx, lines, true);
            p2 += calcSolution(start, idx, lines, false);
            idx++;
        }

        System.out.println("Part 1: "+ p1);
        System.out.println("Part 2: "+ p2);
    }
}