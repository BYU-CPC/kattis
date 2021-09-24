import java.util.*;

public class palindromesubstring {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String s = in.next();
            int n = s.length();
            TreeSet<String> answer = new TreeSet<String>();
            for (int i = 0; i < n-1; i++) {
                // find even length palindromes
                int hi = Math.min(i, n-i-2);
                for (int j = 0; j <= hi; j++) {
                    if (s.charAt(i-j) == s.charAt(i+1+j)) {
                        answer.add(s.substring(i-j, i+1+j+1));
                    } else {
                        break;
                    }
                }

                // find odd length palindromes
                hi = Math.min(i, n-i-1);
                for (int j = 1; j <= hi; j++) {
                    if (s.charAt(i-j) == s.charAt(i+j)) {
                        answer.add(s.substring(i-j, i+j+1));
                    } else {
                        break;
                    }
                }
            }

            for (String word : answer) {
                System.out.println(word);
            }

            System.out.println();
        }

        in.close();
    }
}