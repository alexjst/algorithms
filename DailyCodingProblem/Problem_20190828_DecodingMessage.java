/**
 * This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
 */

class Problem_20190828_DecodingMessage {
    public static void main(String[] args) {
        System.out.println(decodingCount("111"));
    }

    public static int decodingCount(String encoded) {
        if (encoded==null) return 0;
        int len = encoded.length();
        if (len==0) return 0;

        // dp[i] is the number of possible decodings till the ith position
        int[] dp = new int[len];
        for (int i=0; i<len; i++) {
            boolean isOneValid = isInRange(encoded.charAt(i));
            boolean isTwoValid = (i>0) ? isInRange(encoded.charAt(i-1), encoded.charAt(i)) : false;
            dp[i] = (isOneValid ? ( i>0? dp[i-1]: 1) : 0) + (isTwoValid ? ( i>1 ? dp[i-2] : 1) : 0);
        }
        return dp[len-1];
    }

    private static boolean isInRange(char first, char second) {
        int num = (first-'0') * 10 + second - '0';
        if (num >= 10 && num <=26) return true;
        else return false;
    }

    private static boolean isInRange(char c) {
        int num = c -'0';
        if (num >= 1 && num <= 9) return true;
        else return false;
    }

}