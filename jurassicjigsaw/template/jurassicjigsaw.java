// comment out the next line
package kattis.jurassicjigsaw.template;

import java.util.*;

public class jurassicjigsaw {
    
    public static void solve(int n, int k, String[] edges) {
        // print your output here using System.out.print, .println, and/or .printf
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        String[] edges = new String[n-1];
        for (int i = 0; i < n-1; i++) {
            edges[i] = in.next();
        }
        in.close();
        
        solve(n, k, edges);
    }
}
