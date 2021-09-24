import java.io.*;
import java.util.*;

public class bikegears2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int f = in.nextInt();

        while (f != 0) {
            // read rest of input
            int r = in.nextInt();
            int[] front = new int[f];
            for (int i = 0; i < f; i++) front[i] = in.nextInt();
            int[] rear = new int[r];
            for (int i = 0; i < r; i++) rear[i] = in.nextInt();
            
            // create all pairs
            int[][] pairs = new int[f*r][2];
            for (int i = 0; i < f; i++) {
                for (int j = 0; j < r; j++) {
                    pairs[j+i*r][0] = front[i];
                    pairs[j+i*r][1] = rear[j];
                }
            }
            
            // sort by drive ratio
            // r1/f1 < r2/f2 --> r1*f2 < f1*r2 --> r1*f2 - f1*r2 < 0
            Arrays.sort(pairs, (a, b) -> { 
                return a[1]*b[0] - a[0]*b[1];
            });
            
            // calculate spread between every pair
            // spread = r2/f2 / r1/f1 = r2*f1 / f2*r1
            double hi = 0;
            for (int i = 1; i < pairs.length; i++) {
                double spread = (pairs[i][1]*pairs[i-1][0]) / ((double) pairs[i][0]*pairs[i-1][1]);
                hi = Math.max(hi, spread);
            }
            
            System.out.printf("%.2f\n", Math.round(hi*100) / 100.0);
            f = in.nextInt();
        }

        in.close();
    }
}