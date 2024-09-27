package assignments;


public class Prime {
    public static void main(String[] args) {
        long n = 109;
        boolean result = isPrime(n);
        System.out.println("Check if " + n + " is a prime number or not: " + result);
    }

    static boolean isPrime(long n) {
        if (n <= 1) {
            return false;
        }
        
        /* speed up the process by checking only up to the square root of n */ 
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}
