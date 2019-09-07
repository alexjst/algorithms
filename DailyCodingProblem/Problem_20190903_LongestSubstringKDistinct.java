/**
 * This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
 */

class Problem_20190903_LongestSubstringKDistinct {
    public static int longestDistinct(String input, int k) {
        if (input == null || input.isEmpty() || k<=0) return 0;
        int len = input.length();
        if (k>=len) return len;

        int i=0, j=0;
        while (true) {
           while (j<len && (j-i+1) )
        }

    }
}