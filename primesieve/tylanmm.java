import java.util.BitSet;
import java.io.*;

public class primesieve {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int q = Integer.parseInt(line[1]);

        BitSet sieve = new BitSet(n+1);
        sieve.set(0); sieve.set(1);
        int numPrimes = 0;

        for (int i = 2; i <= n; i++) {
            if (sieve.get(i)) continue;
            numPrimes++;
            for (int j = i*i; j <= n && j/i >= i; j += i) sieve.set(j);
        }

        System.out.println(numPrimes);
        for (int i = 0; i < q; i++) System.out.println(sieve.get(Integer.parseInt(br.readLine())) ? 0 : 1);

        br.close();
    }
}