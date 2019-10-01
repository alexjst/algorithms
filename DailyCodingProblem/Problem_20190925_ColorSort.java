/**
 * This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
 */

 class ColorSort {
     public static void main(String[] args) {
        char[] colors = {'G', 'B', 'R', 'R', 'B', 'R', 'G'};
        rgbSort(colors);
        for (char c : colors) {
            System.out.print(c + "\t");
        }
     }

     public static char[] rgbSort(char[] input) {
        int len = input.length;
        if (len < 2) return input;

        int lo = 0, hi = len-1, cur = 0;;
        while (lo<hi && cur<=hi) {
            if (input[cur]=='R') {
                swap(input, lo++, cur);
            } else if (input[cur] == 'B') {
                swap(input, cur, hi--);
            } else {
                cur++;
            }
        }
        return input;
     }

     public static void swap(char[] input, int lo, int hi) {
         char tmp = input[lo];
         input[lo] = input[hi];
         input[hi] = tmp;
     }
 }