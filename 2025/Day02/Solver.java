package Day02;
import helper.FileReader;

public class Solver{
    public static boolean isValidP1(String id){
        int length = id.length();
        String s1 = id.substring(0, (int)length/2);
        String s2 = id.substring((int)length/2);
        return s1.equals(s2);
    }
    
    public static boolean isValidP2(String id){
        int length = id.length();
        for (int numL = 1; numL <= (int)length/2; numL++){
            if (length%numL != 0) continue;
            String part1 = id.substring(0, numL);
            if (id.equals(part1.repeat((int) length/numL))) 
                return true;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader(args);
        String[] ranges = fr.readCSV();

        long p1 = 0;
        long p2 = 0;
        for (String idRange : ranges){
            String[] parts = idRange.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);
            for (long id=start; id<=end; id++){
                String idStr = ""+id;
                if (isValidP1(idStr)) p1+=id;
                if (isValidP2(idStr)) p2+=id;
            }
        }

        System.out.println("Part 1: "+ p1);
        System.out.println("Part 2: "+ p2);
    }
}