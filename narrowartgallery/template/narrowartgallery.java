// comment out the next line
package kattis.narrowartgallery.template;

import java.util.*;

public class narrowartgallery {
    
    public static int solve(int n, int k, int[][] gallery) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[][] gallery = new int[n][2];
        for (int i = 0; i < n; i++) {
            gallery[i][0] = in.nextInt();
            gallery[i][1] = in.nextInt();
        }
        in.close();

        System.out.println(solve(n, k, gallery));
    }
}
