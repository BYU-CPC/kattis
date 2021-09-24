import java.io.*;
import java.util.*;

public class ministryofmagic {
    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        int c = in.nextInt();
        int p = in.nextInt();

        int[] votes = new int[p];
        ArrayDeque<Integer>[] pref = new ArrayDeque[p];
        for (int i = 0; i < p; i++) {
            votes[i] = in.nextInt();
            ArrayDeque<Integer> order = new ArrayDeque<Integer>(c);
            for (int j = 0; j < c; j++) {
                order.add(in.nextInt());
            }
            pref[i] = order;
        }
        in.close();
        
        // Make entry for every candidate
        HashMap<Integer, Integer> counts = new HashMap<Integer, Integer>();
        for (int i = 1; i <= c; i++) {
            counts.put(i, 0);
        }
        
        while (true) {
            // Get the vote counts for that particular round
            for (int i = 0; i < p; i++) {
                while (!pref[i].isEmpty() && !counts.containsKey(pref[i].peek())) {
                    pref[i].pollFirst();
                }
                
                if (!pref[i].isEmpty()) {
                    int choice = pref[i].peek();
                    counts.replace(choice, counts.get(choice) + votes[i]);
                }
            }
            
            // Find the winner(s)
            ArrayList<Integer> winners = new ArrayList<Integer>();
            int winAmount = 0;
            int loser = 0;
            int loseAmount = 2000000000;
            int totalAmount = 0;
            for (int candidate : counts.keySet()) {
                int numVotes = counts.get(candidate);
                totalAmount += numVotes;
                if (numVotes > winAmount) {
                    winners = new ArrayList<Integer>();
                    winners.add(candidate);
                    winAmount = numVotes;
                } else if (numVotes == winAmount) {
                    winners.add(candidate);
                }

                if (numVotes < loseAmount) {
                    loser = candidate;
                    loseAmount = numVotes;
                } else if (numVotes == loseAmount && candidate < loser) {
                    loser = candidate;
                }

                counts.replace(candidate, 0);
            }

            if (winAmount > totalAmount / 2) {
                System.out.println(winners.get(0));
                break;
            } else {
                counts.remove(loser);
            }
        }

    }
}

class FastReader {
    private BufferedReader in;
    private String[] line = new String[0];
    private int pos = 0;

    public FastReader() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
    }

    public void close() throws IOException {
        in.close();
    }

    public String[] nextLine() throws IOException {
        line = in.readLine().split(" ");
        pos = 0;
        return line;
    }

    public String next() throws IOException {
        while (pos == line.length) {
            nextLine();
        }

        return line[pos++];
    }

    public int nextInt() throws IOException {
        String val = next();
        return Integer.parseInt(val);
    }
}