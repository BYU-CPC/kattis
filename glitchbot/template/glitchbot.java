import java.util.*;

public class glitchbot {

    // (x, y) is the target destination
    // n is the length of instructions
    // instructions is a list of "Left" "Forward" and "Right"
    // Do not return anything: print the line number and correct instruction 
    public static void solve(int x, int y, int n, String[] instructions) {
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x = in.nextInt();
        int y = in.nextInt();
        int n = in.nextInt();
        String[] instructions = new String[n];
        for (int i = 0; i < n; i++) {
            instructions[i] = in.next();
        }
        in.close();

        solve(x, y, n, instructions);
    }

}