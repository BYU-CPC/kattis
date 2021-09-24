import java.io.*;
import java.util.*;

public class arbitrage {
    static int n;
    static HashMap<String, Integer> currencyIndices;
    static double[][] g;

    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(in.readLine());
        while (n != 0) {
            String[] currencies = in.readLine().split(" ");
            currencyIndices = new HashMap<String, Integer>();
            for (int i = 0; i < n; i++) {
                currencyIndices.put(currencies[i], i);
            }
            g = new double[n][n];

            int r = Integer.parseInt(in.readLine());
            for (int i = 0; i < r; i++) {
                String[] rule = in.readLine().split(" ");
                String[] rate = rule[2].split(":");
                g[currencyIndices.get(rule[0])][currencyIndices.get(rule[1])] = Double.parseDouble(rate[1]) / Double.parseDouble(rate[0]);
            }

            System.out.println(solve());
            n = Integer.parseInt(in.readLine());
        }
        in.close();
    }

    public static String solve() {
        for (int i = 0; i < n; i++) {
            g[i][i] = 1.0;
        }

        // modified floyd warshall
        for (int piv = 0; piv < n; piv++) {
            for (int from = 0; from < n; from++) {
                for (int to = 0; to < n; to++) {
                    g[from][to] = Math.max(g[from][to], g[from][piv] * g[piv][to]);
                    if (from == to && g[from][to] > 1) {
                        return "Arbitrage";
                    }
                }
            }
        }
        
        return "Ok";
    }
}