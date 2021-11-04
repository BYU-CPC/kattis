import java.util.*;

public class industrialspy {
    private static int solve(int[] digits) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        for (int i = 0; i < c; i++) {
            String line = in.next();
            int[] digits = new int[line.length()];
            for (int j = 0; j < line.length(); j++) {
                digits[j] = (int) (line.charAt(j) - 48);
            }
            System.out.println(solve(digits));
        }
        in.close();
    }
}
