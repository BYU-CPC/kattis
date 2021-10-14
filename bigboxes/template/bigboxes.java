import java.util.*;

public class bigboxes {
    // return the minimum possible weight of the heaviest box
    private static int solve(int n, int k, int[] items) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] items = new int[n];
        for (int i = 0; i < n; i++) {
            items[i] = in.nextInt();
        }
        
        in.close();
        System.out.println(solve(n, k, items));
    }
}