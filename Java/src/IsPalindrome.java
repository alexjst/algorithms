
package alexyang.algorithms.Java.src;

class Solution {
    public static void main(String[] args) {
        System.out.println(isPalindrome(".,"));
    }
    public static boolean isPalindrome(String s) {
        int len = s.length();
        if (len==0) return true;
        
        int i = 0;
        int j = len-1;
        
        while (i<j && i<len && j>=0) {
            System.out.println("i: " + i + "; j: " + j);
            while (i < len && !Character.isLetterOrDigit(s.charAt(i))) i++;
            while (j >=0 && !Character.isLetterOrDigit(s.charAt(j))) j--;
            if (i>=len || j<0) return true;
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) return false;
            i++; j--;
        }
        
        return true;
    }
}