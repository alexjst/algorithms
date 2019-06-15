package alexyang.algorithms.Java.src;

import com.sun.org.apache.bcel.internal.generic.SWAP;

/**
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
*/

class RotateArray{
    public static void main(String[] args) {
        Integer[] arr = {1,2,3,4,5,6,7};
        int k = 3;
        for (int i=0; i<arr.length; i++) {
            System.out.print(arr[i]);
        }
        System.out.println();
        rotateArray(arr, k);
        for (Integer a : arr) {
            System.out.print(a);
        }
        System.out.println();
    }

    static void rotateArray(Integer[] arr, int k) {
        if (arr == null || arr.length < 2) {
            return;
        }
        int step = k % arr.length;
        reverseRange(arr, 0, arr.length);
        reverseRange(arr, 0, step);
        reverseRange(arr, step, arr.length);
    }

    static void reverseRange(Integer[] arr, int start, int end) {
        if (arr == null || arr.length < 2 || start >= end || end > arr.length || start < 0) {
            return;
        }
        for (int i = start, j = end - 1; i < j; i++, j--) {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
}

/**
 * this is very neat algorithm that is almost a trick. you turn array rotation into 3 reverals!
 * 
 * another thing I learnt is that in Java functions, everything is passed by value, things are copied
 * in argument list if it is a primitive, or reference is copied if it is an object.
 */