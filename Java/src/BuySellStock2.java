package alexyang.algorithms.Java.src;

/**
 * Input: [7,1,5,3,6,4]
 * Output: 7
 * Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
 *              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
 */
import java.lang.String;

 public class BuySellStock2 {
     public static void main(String[] args) {
         Integer[] prices = {7, 1, 5, 3, 6, 4};
         System.out.println(profit(prices));
     }

     // we basically take profit of each step
     public static int profit(Integer[] prices) {
         int profit = 0;
         if (prices == null || prices.length < 2) {
             return profit;
         }
        for (int i = 2; i< prices.length; i++) {
            if (prices[i]>prices[i-1]) {
                profit += prices[i] - prices[i-1];
            }
        }
        return profit;
     }
 }