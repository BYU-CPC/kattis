import java.util.*;

public class t9spelling {
    public static String solve(String line) {
        return "";
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());
        for (int t = 0; t < n; t++) {
            System.out.printf("Case #%d: %s\n", t+1, solve(in.nextLine()));
        }
        in.close();
    }
}