import java.util.*;

public class _8queens {

    public static boolean isValid(char[][] board) {
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[][] board = new char[8][8];
        for (int i = 0; i < 8; i++) {
            String row = in.next();
            for (int j = 0; j < 8; j++) {
                board[i][j] = row.charAt(j);
            }
        }
        in.close();

        System.out.println(isValid(board) ? "valid" : "invalid");
    }

}