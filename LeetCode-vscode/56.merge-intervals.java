import java.awt.List;
import java.util.Map;

/*
 * @lc app=leetcode id=56 lang=java
 *
 * [56] Merge Intervals
 *
 * https://leetcode.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (37.79%)
 * Likes:    3209
 * Dislikes: 247
 * Total Accepted:    494.6K
 * Total Submissions: 1.3M
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * Given a collection of intervals, merge all overlapping intervals.
 * 
 * Example 1:
 * 
 * 
 * Input: [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
 * [1,6].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [[1,4],[4,5]]
 * Output: [[1,5]]
 * Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 * 
 * NOTE: input types have been changed on April 15, 2019. Please reset to
 * default code definition to get new method signature.
 * 
 */

// @lc code=start
class Solution {
    public int[][] merge(int[][] intervals) {
        List<Integer> resStarts = new ArrayList<>();
        List<Integer> resEnds = new ArrayList<>();

        Map<Integer,Integer> startCounts = new HashMap<>();
        Map <Integer,Integer> endCounts = new HashMap<>();
        int len = intervals.length;
        Set<Integer> points = new TreeSet<>();
        for (int i=0; i<len; i++) {
            startCounts.put(intervals[i][0], startCounts.getOrDefault(intervals[i][0], 0) + 1);
            endCounts.put(intervals[i][1], endCounts.getOrDefault(intervals[i][1], 0) + 1);
            points.add(intervals[i][0]);
            points.add(intervals[i][1]);
        }
        int cnt = 0;
        for (int point : points) {
            if (cnt==0) {
                resStarts.add(point);
            }
            cnt += startCounts.getOrDefault(point, 0);
            cnt -= endCounts.getOrDefault(point, 0);
            if (cnt==0) {
                resEnds.add(point);
            }
        }
        int sz = resStarts.size();
        int[][] res = new int[sz][2];
        for (int i=0; i<sz; i++) {
            res[i][0] = resStarts.get(i);
            res[i][1] = resEnds.get(i);
        }
        return res;
    }
}
// @lc code=end

