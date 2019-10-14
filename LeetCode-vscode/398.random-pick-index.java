/*
 * @lc app=leetcode id=398 lang=java
 *
 * [398] Random Pick Index
 *
 * https://leetcode.com/problems/random-pick-index/description/
 *
 * algorithms
 * Medium (51.47%)
 * Likes:    294
 * Dislikes: 506
 * Total Accepted:    62.2K
 * Total Submissions: 120.8K
 * Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
 *
 * Given an array of integers with possible duplicates, randomly output the
 * index of a given target number. You can assume that the given target number
 * must exist in the array.
 * 
 * Note:
 * The array size can be very large. Solution that uses too much extra space
 * will not pass the judge.
 * 
 * Example:
 * 
 * 
 * int[] nums = new int[] {1,2,3,3,3};
 * Solution solution = new Solution(nums);
 * 
 * // pick(3) should return either index 2, 3, or 4 randomly. Each index should
 * have equal probability of returning.
 * solution.pick(3);
 * 
 * // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
 * solution.pick(1);
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Solution {
    private Map<Integer,List<Integer>> mp = null;
    private int[] numbers = null;
    public static void main(String[] args) {
        Solution obj = new Solution(new int[]{1});
        int param_1 = obj.pick(1);
        System.out.println(param_1);
    }

    public Solution(int[] nums) {
        this.numbers = nums;
        mp = new HashMap<>();
        int idx = 0;
        for (int num : nums) {
            if (mp.containsKey(num)) {
                mp.get(num).add(idx);
            } else {
                List<Integer> lst = new ArrayList<>();
                lst.add(idx);
                mp.put(num, lst);
            }
            idx++;
        }
    }
    
    public int pick(int target) {
       int sz = mp.get(target).size();
       int rnd = (int)(Math.random() * sz);
       System.out.println("rnd: " + rnd);
       System.out.println(numbers[mp.get(target).get(rnd)]);
       return numbers[mp.get(target).get(rnd)];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
// @lc code=end

