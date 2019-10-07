/**
 * This problem was asked by Facebook.
 * 
 * Given a array of numbers representing the stock prices of a company in
 * chronological order, write a function that calculates the maximum profit you
 * could have made from buying and selling that stock once. You must buy before
 * you can sell it.
 * 
 * For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
 * buy the stock at 5 dollars and sell it at 10 dollars.
 */

 class BuySellStockOnce {
     public static void main(String[] args) {
         System.out.println(getBestProfit(new int[]{9,11,8,5,7,10}));
     }

     public static int getBestProfit(int[] arr) {
         int result = 0;
         if (arr.length < 2) return result;

         int lowestSofar = arr[0];
         for (int i=1; i<arr.length; i++) {
             lowestSofar = Math.min(lowestSofar, arr[i]);
             result = Math.max(result, arr[i]-lowestSofar);
         }
         return result;
     }
 }