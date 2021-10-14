import java.util.*;

public class eventplanning {
    // n, b, h, and w are as described in the problem
    // price[i] = price for one person staying the weekend at hotel i
    // beds[i][w] = number of available beds at hotel i on weekend w
    // return nothing: print the minimum cost, or 'stay home'
    private static void solve(int n, int b, int h, int w, int[] price, int[][] beds) {

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int b = in.nextInt();
        int h = in.nextInt();
        int w = in.nextInt();
        int[] price = new int[h];
        int[][] beds = new int[h][w];
        for (int i = 0; i < h; i++) {
            price[i] = in.nextInt();
            for (int j = 0; j < w; j++) {
                beds[i][j] = in.nextInt();
            }
        }

        in.close();
        solve(n, b, h, w, price, beds);
    }
}
