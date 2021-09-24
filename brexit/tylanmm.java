import java.util.*;
import java.io.*;

public class brexit {
    static int c, p, x, l;
    static ArrayList<Integer>[] adj;
    static ArrayDeque<Integer> queue;

    public static void main(String[] args) throws IOException {
        // read the input
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer line = new StringTokenizer(in.readLine());
        c = Integer.parseInt(line.nextToken());
        p = Integer.parseInt(line.nextToken());
        x = Integer.parseInt(line.nextToken()) - 1;
        l = Integer.parseInt(line.nextToken()) - 1;

        // build the graph
        adj = new ArrayList[c];
        for (int i = 0; i < c; i++) adj[i] = new ArrayList<Integer>();
        for (int i = 0; i < p; i++) {
            line = new StringTokenizer(in.readLine());
            int a = Integer.parseInt(line.nextToken()) - 1;
            int b = Integer.parseInt(line.nextToken()) - 1;
            adj[a].add(b);
            adj[b].add(a);
        }

        // run kinda Kahn's?
        queue = new ArrayDeque<Integer>();
        queue.add(l);
        int[] rem = new int[c];
        rem[l] = -1;
        while (!queue.isEmpty()) {
            int country = queue.poll();

            for (int partner : adj[country]) {
                if (rem[partner] == -1) continue;
                rem[partner]++;
                if (adj[partner].size() <= rem[partner] * 2) {
                    queue.add(partner);
                    rem[partner] = -1;
                }
            }
        }
        
        System.out.println(rem[x] == -1 ? "leave" : "stay");
    }
}