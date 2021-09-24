import java.util.*;

public class millionairemadness {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int n = in.nextInt();
        int[][] grid = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = in.nextInt();
            }
        }
        in.close();

        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) -> { return a[0] - b[0];});
        pq.add(new int[] {0, 0, 0});
        int hi = 0;
        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            int d = top[0], i = top[1], j = top[2];
            if (grid[i][j] == -1) continue;
            hi = Math.max(hi, d);
            if (i == m-1 && j == n-1) break;

            if (i > 0) pq.add(new int[] {grid[i-1][j] - grid[i][j], i-1, j});
            if (j > 0) pq.add(new int[] {grid[i][j-1] - grid[i][j], i, j-1});
            if (i + 1 < m) pq.add(new int[] {grid[i+1][j] - grid[i][j], i+1, j});
            if (j + 1 < n) pq.add(new int[] {grid[i][j+1] - grid[i][j], i, j+1});

            grid[i][j] = -1;
        }

        System.out.println(hi);
    }
}