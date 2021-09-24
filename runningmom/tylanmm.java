import java.io.*;
import java.util.*;

public class runningmom {
    static int n;
    static HashMap<String, ArrayList<String>> adj = new HashMap<String, ArrayList<String>>();
    static HashMap<String, Integer> state = new HashMap<String, Integer>();
    static HashMap<String, Boolean> canReachCycle = new HashMap<String, Boolean>();

    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        n = in.nextInt();
        for (int i = 0; i < n; i++) {
            String o = in.next();
            String d = in.next();
            adj.putIfAbsent(o, new ArrayList<String>());
            adj.putIfAbsent(d, new ArrayList<String>());
            adj.get(o).add(d);
        }

        for (String city : adj.keySet()) {
            state.put(city, 0);
            canReachCycle.put(city, false);
        }

        for (String city : adj.keySet()) {
            if (state.get(city) == 0) {
                dfs(city);
            }
        }

        String line = in.in.readLine();
        while (line != null) {
            System.out.printf("%s %s\n", line, canReachCycle.get(line) ? "safe" : "trapped");
            line = in.in.readLine();
        }

        in.close();
    }

    static void dfs(String city) {
        state.put(city, 1);
        for (String destination : adj.get(city)) {
            if (state.get(destination) == 0) {
                dfs(destination);
                if (canReachCycle.get(destination)) {
                    canReachCycle.put(city, true);
                }
            } else if (state.get(destination) == 1) {
                canReachCycle.put(city, true);
            } else {
                if (canReachCycle.get(destination)) {
                    canReachCycle.put(city, true);
                }
            }
        }
        state.put(city, 2);
    }
}

class FastReader {
    public BufferedReader in;
    private StringTokenizer line;

    public FastReader() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
    }

    public void close() throws IOException {
        in.close();
    }

    private void buffer() throws IOException {
        if (line == null || !line.hasMoreTokens()) {
            line = new StringTokenizer(in.readLine());
        }
    }

    public String nextLine() throws IOException {
        return in.readLine();
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