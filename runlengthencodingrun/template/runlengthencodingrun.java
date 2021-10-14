import java.util.*;

public class runlengthencodingrun {
    // You will need to implement both of the following methods
    private static String encode(String message) {
        return "";
    }

    private static String decode(String message) {
        return "";
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String type = in.next();
        String msg = in.next();
        in.close();
        System.out.println(type.equals("E") ? encode(msg) : decode(msg));
    }
}