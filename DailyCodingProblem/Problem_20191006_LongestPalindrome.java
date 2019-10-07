/**
 * This problem was asked by Amazon.
 * 
 * Given a string, find the longest palindromic contiguous substring. If there
 * are more than one with the maximum length, return any one.
 * 
 * For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The
 * longest palindromic substring of "bananas" is "anana".
 */

/**
 * Idea: I worked on this before, a simple and straight-forward-thinking is to
 * "expand from middle" where the middle can be any character or between any
 * two characters within the string.
 */

 class LongestPalindrome {
     public static void main(String[] args) {
         System.out.println(LongestPalindromeString(""));
         System.out.println(LongestPalindromeString("a"));
         System.out.println(LongestPalindromeString("ab"));
         System.out.println(LongestPalindromeString("aa"));
         System.out.println(LongestPalindromeString("aabcdcb"));
         System.out.println(LongestPalindromeString("bananas"));
     }
     public static String LongestPalindromeString(String in) {
         if (in.length() < 2) return in;
         int result = 1;
         String resultStr = in.substring(0,1);
         // expand from every char
         for (int k=0; k<in.length(); k++) {
             int i=k-1, j=k+1;
             while (i>=0 && j<in.length() && in.charAt(i)==in.charAt(j)) {
                 if (((j-k) * 2 + 1) > result) {
                    result = (j - k) * 2 + 1;
                    resultStr = in.substring(i, j+1);
                 }
                i--;
                j++;
             }
         }
         // expand from between every pair of neighbors (after every pos)
         for (int k=0; k<in.length()-1; k++) {
             int i=k, j=k+1;
             while (i>=0 && j<in.length() && in.charAt(i)==in.charAt(j)) {
                if ((j - k) * 2 > result) {
                    result = (j - k) * 2;
                    resultStr = in.substring(i, j + 1);
                }
                i--;
                j++;
             }
         }
         return resultStr;
     }
 }