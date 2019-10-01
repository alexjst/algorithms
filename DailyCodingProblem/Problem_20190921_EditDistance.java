/**
 * This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
 */

 class EditDistance {
     public static int distance(String left, String right) {
         int llen = left.length();
         int rlen = right.length();
         if (llen==0) return rlen;
         if (rlen==0) return llen;
         int[][] dp = new int[llen+1][rlen+1];
         for (int i = 0; i <= llen; i++) dp[i][0] = i;
         for (int j = 1; j <= rlen; j++) dp[0][j] = j;
         for (int i=1; i<=llen; i++) {
             for (int j=1; j<=rlen; j++) {
                 if (left.charAt(i-1)==right.charAt(j-1)) {
                     dp[i][j] = dp[i-1][j-1];
                 } else {
                     dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]) + 1;
                 }
             }
         }
         return dp[llen][rlen];
     }
 }