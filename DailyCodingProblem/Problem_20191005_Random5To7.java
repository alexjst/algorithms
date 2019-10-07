import java.util.Random;

/**
 * This problem was asked by Two Sigma.
 * 
 * Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
 * uniform probability, implement a function rand7() that returns an integer
 * from 1 to 7 (inclusive).
 * 
 */

 /**
 * Wrong Idea: Target is 1~7 which means 0~6. What I have is 0~4 that allows me
 * to generate uniform distribution from 0 to (xx...4) where each digit is
 * base-5. if this number is also 7n+6 I'll just use modular 7 to get to 0~6.
 * ...... sorry I cannot continue this thoughts process to find a answer. So
 * problem is that: there is actually no deterministic way to do it! Reason:
 * say, call rand5 for X number of times to get 5^X possible values for
 * distribution that cannot be evenly distributed among 7 buckets!
 *
 */
import java.util.*;

 class Random5To7 {
     public static void main(String[] args) {
        Map<Integer,Integer> numCount = new HashMap<>();
        for (int i = 0; i < 7000; i++) {
            int r = Random5To7.rand7();
            numCount.put(r, numCount.getOrDefault(r,0) + 1);
        }
        for (Map.Entry<Integer,Integer> entry : numCount.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
     }
     private static int rand5() {
         return (int)(Math.random() * 5) + 1;
     }

     private static int rand25() {
         return (rand5()-1) * 5 + rand5() - 1;
     }

     // discard those out of range from 0 to 6
     private static int rand7() {
         int x = rand25();
         while (x>6) {
             x = rand25();
         }
         return x + 1;
     }
 }