/**
 * This problem was asked by Facebook.
 * 
 * You are given an array of non-negative integers that represents a
 * two-dimensional elevation map where each element is unit-width wall and the
 * integer is the height. Suppose it will rain and all spots between two walls
 * get filled up.
 * 
 * Compute how many units of water remain trapped on the map in O(N) time and
 * O(1) space.
 * 
 * For example, given the input [2, 1, 2], we can hold 1 unit of water in the
 * middle.
 * 
 * Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2
 * in the second, and 3 in the fourth index (we cannot hold 5 since it would run
 * off to the left), so we can trap 8 units of water.
 */

 /**
 * Method 1 (Three passes): find the highest bar, then scan from left to bar and
 * accumulate the diff between a bar that is being scanned and the highest bar
 * seen so far, do the same from right side to highest bar
 * 
 * Method 2 (One pass): scan from left and right toward the middle (till
 * collision) at the same time, the shorter one's diff to its side's highest bar
 * seen so far is the amount of water trapped. Then increment the shorter one's
 * index.
 */

 class TrapRainWater {
     public static void main(String[] args) {
         System.out.println(trapWater(new int[]{3,0,1,3,0,5}));
     }

     public static int trapWater(int[] walls) {
        return 0;
     }
 }