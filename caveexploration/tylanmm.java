import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashSet;

public class caveexploration {
    private static HashSet<Integer>[] g;
    private static int[] num;
    private static int[] low;
    private static int[] parent;
    private static int visited = 0;
    private static ArrayList<int[]> bridges;
    private static int[] comp;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        g = new HashSet[n];
        for (int i = 0; i < m; i++) {
            int u = in.nextInt();
            int v = in.nextInt();
            if (g[u] == null) {
                g[u] = new HashSet<Integer>();
            }
            if (g[v] == null) {
                g[v] = new HashSet<Integer>();
            }
            g[u].add(v);
            g[v].add(u);
        }
        in.close();

        num = new int[n];
        low = new int[n];
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            num[i] = -1;
            low[i] = 0;
            parent[i] = -1;
        }

        bridges = new ArrayList<int[]>();
        artPointBridge(0);
        for (int[] bridge : bridges) {
            g[bridge[0]].remove(bridge[1]);
            g[bridge[1]].remove(bridge[0]);
        }
        
        comp = new int[n];
        dfs(0);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (comp[i] == 1) {
                ans++;
            }
        }
        System.out.println(ans);
    }

    private static void artPointBridge(int u) {
        num[u] = visited++;
        low[u] = num[u];
        for (int v : g[u]) {
            if (num[v] == -1) {
                parent[v] = u;
                artPointBridge(v);
                if (num[u] < low[v]) {
                    bridges.add(new int[] {u, v});
                }
                low[u] = Math.min(low[u], low[v]);
            } else if (v != parent[u]) {
                low[u] = Math.min(low[u], num[v]);
            }
        }
    }

    private static void dfs(int u) {
        comp[u] = 1;
        for (int v : g[u]) {
            if (comp[v] == 0) {
                dfs(v);
            }
        }
    }
}