/**
 * This problem was asked by Google.
 * 
 * We can determine how "out of order" an array A is by counting the number of
 * inversions it has. Two elements A[i] and A[j] form an inversion if A[i] >
 * A[j] but i < j. That is, a smaller element appears after a larger element.
 * 
 * Given an array, count the number of inversions it has. Do this faster than
 * O(N^2) time.
 * 
 * You may assume each element in the array is distinct.
 * 
 * For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has
 * three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has
 * ten inversions: every distinct pair forms an inversion.
 */

 /**
  * My idea: merge sort. during merge sort's merge phase, if I can calculate
  * inversions in linear time, because there's only log(n) number of merges,
  * the total time complexity should be nlog(n).
  */
class ArrayInversionsCount {
    public int[] aux;
    public static void main(String[] args) {
        ArrayInversionsCount s = new ArrayInversionsCount();
        System.out.println("Expect 0, 3, 10 below:");
        System.out.println(s.numInversions(new int[]{1,2,3,4,5}));
        System.out.println(s.numInversions(new int[]{2,4,1,3,5}));
        System.out.println(s.numInversions(new int[]{5,4,3,2,1}));
    }

    public int numInversions(int[] nums) {
        if (nums.length < 2) return 0;
        aux = new int[nums.length];
        return mergeSortAndCount(nums, 0, nums.length-1);
    }

    private int mergeSortAndCount(int[] nums, int lo, int hi) {
        if (lo==hi) return 0;
        if ((lo+1)==hi) {
            if (nums[lo]>nums[hi]) {
                swap(nums, lo, hi);
                return 1;
            } else {
                return 0;
            }
        }
        int mid = (lo + hi) / 2;
        int leftInversons = mergeSortAndCount(nums, lo, mid);
        int rightInversions = mergeSortAndCount(nums, mid+1, hi);
        int crossInversions = 0;
        // merge into aux
        for (int i=lo, j=mid+1, k=lo; k<=hi; k++) {
            if (j>hi || nums[i] < nums[j]) {
                aux[k] = nums[i];
                crossInversions += Math.abs(i-k);
                i++;
            } else if (i>mid || nums[i] > nums[j]) {
                aux[k] = nums[j];
                crossInversions += Math.abs(j-k);
                j++;
            }
        }
        // copy back
        for (int i=lo; i<=hi; i++) {
            nums[i] = aux[i];
        }
        crossInversions /= 2;
        return leftInversons + rightInversions + crossInversions;
    }

    private void swap(int[] nums, int lo, int hi) {
        if (lo==hi) return;
        nums[lo] ^= nums[hi];
        nums[hi] ^= nums[lo];
        nums[lo] ^= nums[hi];
    }
}