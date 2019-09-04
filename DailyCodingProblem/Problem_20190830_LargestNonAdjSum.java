/**
 * This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

 */

 class Problem_20190830_LargestNonAdjSum {
    public static void main(String[] args) {
        System.out.println(getLargestSumNonAdjacent(new int[]{2,4,6,2,5}));
        System.out.println(getLargestSumNonAdjacent(new int[]{5,1,1,5}));
    }

    public static int getLargestSumNonAdjacent(int[] input) {
        int sz = input.length;
        if (sz==0) return Integer.MIN_VALUE;
        else if (sz==1) return input[0];
        else {
            int[] dp = new int[sz];
            dp[0] = input[0];
            dp[1] = Math.max(input[0], input[1]);
            for (int i=2; i<sz; i++) {
                dp[i] = Math.max(Math.max(dp[i-2], dp[i-2] + input[i]), dp[i-1]);
            }
            return dp[sz-1];
        }
    }
 }

 // follow up: O(N) is already implemented in the above code logic. For constant space, we only need the most recent 3 dp[] elements