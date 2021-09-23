// comment out the next line
package kattis.financialplanning;

import java.util.*;

public class financialplanning {

    public static int solve(int n, int m, int[][] opportunities) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[][] opportunities = new int[n][2];
        for (int i = 0; i < n; i++) {
            opportunities[i][0] = in.nextInt();
            opportunities[i][1] = in.nextInt();
        }
        in.close();

        System.out.println(solve(n, m, opportunities));
    }
    
}
