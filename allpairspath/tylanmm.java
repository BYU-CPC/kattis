import java.io.*;
import java.util.*;

public class allpairspath {
    static double[][] g;
    static int[][] p;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] line = in.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        while (n != 0) {
            int m = Integer.parseInt(line[1]), q = Integer.parseInt(line[2]);

            // set up graph
            g = new double[n][n];
            p = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    g[i][j] = Double.POSITIVE_INFINITY;
                    p[i][j] = i;
                }
            }

            // read in edges
            for (int i = 0; i < m; i++) {
                line = in.readLine().split(" ");
                int u = Integer.parseInt(line[0]);
                int v = Integer.parseInt(line[1]);
                int w = Integer.parseInt(line[2]);
                if (u != v || w < 0) {
                    g[u][v] = Math.min(g[u][v], w);
                }
            }

            // floyd warshall
            for (int k = 0; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (g[i][k] + g[k][j] < g[i][j]) {
                            g[i][j] = g[i][k] + g[k][j];
                            p[i][j] = p[k][j];
                        }
                    }
                }
            }

            // process queries
            for (int i = 0; i < q; i++) {
                line = in.readLine().split(" ");
                int u = Integer.parseInt(line[0]);
                int v = Integer.parseInt(line[1]);
                if (g[u][v] != Double.POSITIVE_INFINITY && hasNegCycle(u, v)) {
                    System.out.println("-Infinity");
                } else if (u == v) {
                    System.out.println(0);
                } else if (g[u][v] == Double.POSITIVE_INFINITY) {
                    System.out.println("Impossible");
                } else {
                    System.out.println((int) g[u][v]);
                }
            }

            // prepare for next test case
            System.out.println();
            line = in.readLine().split(" ");
            n = Integer.parseInt(line[0]);
        }
        in.close();
    }

    private static boolean hasNegCycle(int u, int v) {
        if (u != v) {
            return g[v][v] < 0 || hasNegCycle(u, p[u][v]);
        }
        return g[u][u] < 0;
    }
}