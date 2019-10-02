/**
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters
as possible anywhere in the word. If there is more than one palindrome of minimum length that can
be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters
to it (which is the smallest amount to make a palindrome). There are seven other palindromes that
can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
*/

/**
 * Method:
 * Go from outward bounds to internal mid position: if two outside chars are equal, go inward, otherwise choose the smaller char and go inward.
 */
class MakePalindrome {
    public static void main(String[] args) {
        System.out.println(makePalindrome("race"));
        System.out.println(makePalindrome("google"));
    }
    public static String makePalindrome(String input) {
        int len = input.length();
        if (len<2) return input;

        StringBuilder sb = new StringBuilder();
        for (int i=0, j=(input.length()-1); i<=j;) {
            if (i==j) {
                StringBuilder result = new StringBuilder(sb);
                String reverse = sb.reverse().toString();
                return result.append(input.charAt(i)).append(reverse).toString();
            } else {
                if (input.charAt(i) == input.charAt(j)) {
                    sb.append(input.charAt(i));
                    i++; j--;
                } else if (input.charAt(i) < input.charAt(j)) {
                    sb.append(input.charAt(i));
                    i++;
                } else {
                    sb.append(input.charAt(j));
                    j--;
                }
            }
        }
        StringBuilder result = new StringBuilder(sb);
        String reverse = sb.reverse().toString();
        return result.append(reverse).toString();
    }
}