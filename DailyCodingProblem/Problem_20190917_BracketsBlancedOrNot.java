/**
 * This problem was asked by Facebook.
 * 
 * Given a string of round, curly, and square open and closing brackets, return
 * whether the brackets are balanced (well-formed).
 * 
 * For example, given the string "([])[]({})", you should return true.
 * 
 * Given the string "([)]" or "((()", you should return false.
 */

 /**
  * I used to use stacks for such such problems, now I'd like to try counters:
  * I'll try to keep 3 counters, but how am I going to distinguish '([)..' (invalid already)
  * and '[()...' (still valid so far). So it appears simple counters cannot distinguish.
  *
  * Now getting back to stack solution.
  */

import java.util.*;

 class BracketsBalancedOrNot {
     public static void main(String[] args) {
         System.out.println(isValid("([])[]({})"));
         System.out.println(isValid("([)]"));
         System.out.println(isValid("((()"));
     }
     public static Boolean isValid(String in) {
         Map<Character,Character> mp = new HashMap<>();
         mp.put(')', '(');
         mp.put(']', '[');
         mp.put('}', '{');
         Stack<Character> s = new Stack<>();
         for (int i=0; i<in.length(); i++) {
             Character c = in.charAt(i);
             if (mp.containsKey(c)) {
                 if (s.isEmpty() || s.peek()!=mp.get(c)) return false;
                 else s.pop();
             } else s.push(c);
         }
         return s.isEmpty();
     }
 }
