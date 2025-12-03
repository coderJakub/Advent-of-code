package Day03;
import helper.FileReader;

public class Solver{
    public static int[] getMaxValue(String line){
        int[] maxValue = new int[]{0,0};
        for (int idx = 0; idx < line.length(); idx++){
            int num = line.charAt(idx)-'0';
            if (num > maxValue[0]) maxValue = new int[]{num, idx};
        }
        return maxValue;
    }

    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader(args);
        String[] lines = fr.readLines();

        long[] res = new long[]{0,0};
        for (String line : lines){
            for (int part=0; part<2; part++){
                long num = 0;
                int numL = part==0 ? 1 : 11;
                int start = 0;
                for (int end=numL; end>=0; end--){
                    int[] maxValue = getMaxValue(line.substring(start, line.length()-end));
                    num = num*10+maxValue[0];
                    start += maxValue[1]+1;
                }
                res[part] += num;
            }
        }

        System.out.println("Part 1: "+ res[0]);
        System.out.println("Part 2: "+ res[1]);
    }
}