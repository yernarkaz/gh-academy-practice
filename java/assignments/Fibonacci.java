package assignments; // Ensure this matches your directory structure
import java.util.HashMap;

public class Fibonacci {

    static HashMap<Integer, Long>  cache = new HashMap<Integer, Long>();
    public static void main(String[] args) {
        int n = 1000;
        long result = fibonacci(n);
        System.out.println("Fibonacci number for " + n + " is: " + result);
    }

    static long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }

        /* look up the cache to see if we have already computed the fibonacci number for n */ 
        if (cache.containsKey(n)) {
            return cache.get(n);
        } else {
            /* compute the next fibonacci number for n and store it in the cache */
            long result = fibonacci(n - 1) + fibonacci(n - 2);
            cache.put(n, result);
            return result;
        }
    }
}