/**
 * Created by ayang on 2017/2/26.
 *
 * Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

 Example 1:
 Input: [0,1]
 Output: 2
 Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
 Example 2:
 Input: [0,1,0]
 Output: 2
 Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 Note: The length of the given binary array will not exceed 50,000.
 */
public class ContiguousArray {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.findMaxLength(new int[]{0,1,0}));
    }
    public static class Solution {
        public int findMaxLength(int[] nums) {
            return 0;
        }
    }
}
