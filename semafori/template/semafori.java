// comment out the next line
package kattis.semafori.template;

import java.util.*;

public class semafori {
    
    // lights is an n x 3 array, where lights[i] = {di, ri, gi} (the ith traffic light information)
    public static int solve(int n, int l, int[][] lights) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int l = in.nextInt();
        int[][] lights = new int[n][3];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                lights[i][j] = in.nextInt();
            }
        }
        in.close();

        System.out.println(solve(n, l, lights));
    }

}
