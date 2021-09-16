import java.util.*;

public class prva {

    private static String solve(int r, int c, char[][] grid) {
        return "";
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int r = in.nextInt();
        int c = in.nextInt();
        char[][] g = new char[r][c];
        
        for (int i = 0; i < r; i++) {
            String row = in.next();
            for (int j = 0; j < c; j++) {
                g[i][j] = row.charAt(j);
            }
        }
        
        in.close();

        System.out.println(solve(r, c, g));
    }
    
}