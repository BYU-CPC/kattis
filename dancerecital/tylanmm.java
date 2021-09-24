import java.util.*;
import java.io.*;

class dancerecital {
    static int[] dances;
    static ArrayList<Integer> order = new ArrayList();
    static boolean[] used;
    
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        int r = in.nextInt();
        dances = new int[r];
        used = new boolean[r];
        for (int i = 0; i < r; i++) {
            int n = 0;
            String dance = in.next();
            for (int j = 0; j < dance.length(); j++){
                n |= 1 << dance.charAt(j) - 'A';
            }
            dances[i] = n;
        }
        
        System.out.println(solve());
    }

    public static int solve() {
        int lo = Integer.MAX_VALUE;
        boolean end = true;
        for (int i = 0; i < used.length; i++) {
            if (!used[i]) {
                end = false;
                used[i] = true;
                order.add(dances[i]);
                lo = Math.min(lo, solve());
                used[i] = false;
                order.remove(order.size()-1);
            }
        }
        
        return end ? countChanges() : lo;
    }

    public static int countChanges() {
        int total = 0;
        for (int i = 0; i < order.size() - 1; i++) {
            int n = order.get(i) & order.get(i+1);
            while (n > 0) {
                n &= n - 1;
                total += 1;
            }
        }
        return total;
    }
}