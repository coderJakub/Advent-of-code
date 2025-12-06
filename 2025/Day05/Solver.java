package Day05;
import helper.FileReader;
import java.util.*;

public class Solver{
    public static int getPart1Solution(String[] freshIngredients, String[] availableIngredients){
        int res = 0;
        for (String ai : availableIngredients){
            long id = Long.parseLong(ai);
            for (String range : freshIngredients){
                String[] parts = range.split("-");
                if (Long.parseLong(parts[0]) <= id && id <= Long.parseLong(parts[1])){
                    res++;
                    break;
                }
            }
        }
        return res;
    }

    public static long[][] getSortedLongArray(String[] stringList){
        long[][] intList = new long[stringList.length][];
        for (int i=0; i<stringList.length; i++){
            String[] parts = stringList[i].split("-");
            long[] partI = new long[]{Long.parseLong(parts[0]),Long.parseLong(parts[1])};
            intList[i] = partI;
        }
        Arrays.sort(intList, (a, b) -> Long.compare(a[0], b[0]));
        return intList;
    }

    public static long getPart2Solution(String[] freshIngredientsS){
        long res = 0;
        long[][] freshIngredients = getSortedLongArray(freshIngredientsS);
        List<long[]> distinctRanges = new LinkedList<>();
        
        for (long[] range : freshIngredients){   
            if (!distinctRanges.isEmpty() && range[0] <= distinctRanges.getLast()[1]){
                long newEnd = Math.max(range[1], distinctRanges.getLast()[1]);
                distinctRanges.getLast()[1] = newEnd;
            }
            else distinctRanges.add(range);
        }
        for (long[] range : distinctRanges) res += range[1] - range[0] + 1;
        return res;
    }

    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader(args);
        String[][] blocks = fr.readBlocks();

        int p1 = getPart1Solution(blocks[0], blocks[1]); 
        long p2 = getPart2Solution(blocks[0]); 

        System.out.println("Part 1: "+ p1);
        System.out.println("Part 2: "+ p2);
    }
}