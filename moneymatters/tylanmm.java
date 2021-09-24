import java.util.Scanner;
import java.util.ArrayList;

public class moneymatters {
    private static int[] owed;
    private static ArrayList<Integer>[] g;
    private static boolean[] visited;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        // read amounts owed
        owed = new int[n];
        for (int i = 0; i < n; i++) {
            owed[i] = in.nextInt();
        }
        
        // read in graph
        g = new ArrayList[n];
        for (int i = 0; i < m; i++) {
            int x = in.nextInt();
            int y = in.nextInt();
            if (g[x] == null) {
                g[x] = new ArrayList<Integer>();
            }
            if (g[y] == null) {
                g[y] = new ArrayList<Integer>();
            }
            g[x].add(y);
            g[y].add(x);
        }

        in.close();

        visited = new boolean[n];
        boolean canPay = true;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int amt = dfs(i);
                if (amt != 0) {
                    canPay = false;
                    break;
                }
            }
        }
        System.out.println(canPay ? "POSSIBLE" : "IMPOSSIBLE");
    }

    private static int dfs(int f) {
        visited[f] = true;
        int total = owed[f];
        for (int friend : g[f]) {
            if (!visited[friend]) {
                total += dfs(friend);
            }
        }
        return total;
    }
}