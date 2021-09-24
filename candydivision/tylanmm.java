import java.io.*;
import java.util.*;

public class candydivision {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(in.readLine());
        ArrayList<Long> factors = new ArrayList<Long>();

        for (long i = 1L; i * i <= n; i++) {
            if (n % i == 0) {
                factors.add(i-1);
                if (i*i != n) factors.add((n/i - 1));
            }
        }

        Collections.sort(factors);
        for (int i = 0; i < factors.size() - 1; i++) {
            System.out.print(factors.get(i) + " ");
        }
        System.out.print(factors.get(factors.size()-1));
    }
}