import java.util.*;

public class egypt {

    // return True if a, b, and c form a right triangle
    // return False otherwise
    public static boolean isRightTriangle(int a, int b, int c) {
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a, b, c;
        do {
            a = in.nextInt();
            b = in.nextInt();
            c = in.nextInt();
            System.out.println(isRightTriangle(a, b, c) ? "right" : "wrong");
        } while (a + b + c != 0);
        in.close();
    }

}