import java.util.*;

public class glitchbot {

    // target is the word you want to type
    // written is what has been written so far
    // suggestions contains the three suggestion strings
    // return the minimum number of keypresses needed
    public static int min_keypresses(String target, String written, String[] suggestions) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            String target = in.next();
            String written = in.next();
            String[] suggestions = new String[3];
            for (int j = 0; j < 3; j++) {
                suggestions[j] = in.next();
            }
            min_keypresses(target, written, suggestions);
        }
        in.close();
    }

}