import java.io.*;
import java.util.*;

public class pickupsticks {
    static ArrayList<Integer>[] adj;
    static ArrayList<Integer> topo;
    static int[] state;

    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        int n = in.nextInt();
        int m = in.nextInt();

        adj = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<Integer>();
        for (int i = 0; i < m; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            adj[b].add(a);
        }

        topo = new ArrayList<Integer>(n);
        state = new int[n+1];
        boolean possible = true;
        for (int i = 1; i <= n; i++) {
            if (state[i] == 0) {
                if (!dfs(i)) {
                    System.out.println("IMPOSSIBLE");
                    return;
                }
            }
        }

        for (int stick : topo) {
            System.out.println(stick);
        }
    }

    static boolean dfs(int stick) {
        state[stick] = 1;

        for (int under : adj[stick]) {
            if (state[under] == 0) {
                if (!dfs(under)) return false;
            } else if (state[under] == 1) {
                return false;
            }
        }
        
        state[stick] = 2;
        topo.add(stick);
        return true;
    }
}

class FastReader {
    private BufferedReader in;
    private StringTokenizer line;

    public FastReader() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
    }

    public void close() throws IOException {
        in.close();
    }

    public String nextLine() throws IOException {
        return in.readLine();
    }

    private void buffer() throws IOException {
        if (line == null || !line.hasMoreTokens()) {
            line = new StringTokenizer(in.readLine());
        }
    }

    public String next() throws IOException {
        buffer();
        return line.nextToken();
    }

    public int nextInt() throws IOException {
        String val = next();
        return Integer.parseInt(val);
    }
}