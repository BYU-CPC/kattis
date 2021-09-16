import java.util.*;

public class commercials {

    private static int solve(int n, int p, int[] nums) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int p = in.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
        }

        in.close();

        System.out.println(solve(n, p, nums));
    }
    
}