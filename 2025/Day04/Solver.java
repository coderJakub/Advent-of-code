package Day04;
import helper.FileReader;

public class Solver{
    public static int countAdjecent(int i, int j, char[][] grid){
        int R = grid.length;
        int C = grid[0].length;
        int adj = 0;
        for (int ni=i-1; ni<=i+1; ni++){
            for (int nj=j-1; nj<=j+1; nj++){
                if (ni>=0 && ni<R && nj>=0 && nj<C && (ni!=i || nj!=j) && grid[ni][nj]=='@') adj++;
            }
        }
        return adj;
    }

    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader(args);
        String[] lines = fr.readLines();

        int p1 = 0;
        int p2 = 0;

        char[][] grid = new char[lines.length][lines[0].length()];
        for(int i=0; i<grid.length; i++) grid[i] = lines[i].toCharArray();
        
        boolean first = true;
        while (true){
            boolean changes = false;
            for(int i=0; i<grid.length; i++){
                for(int j=0; j<grid[i].length; j++){
                    if (grid[i][j]=='@' && countAdjecent(i, j, grid) < 4){
                        changes = true;
                        if(first) p1++;
                        else{
                            p2++;
                            grid[i][j] = '.';
                        }
                    }
                }
            }
            first = false;
            if(!changes)break;
        }

        System.out.println("Part 1: "+ p1);
        System.out.println("Part 2: "+ p2);
    }
}