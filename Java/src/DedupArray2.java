package alexyang.algorithms.Java.src;

import java.util.List;

public class DedupArray2 {
    public static void main(String[] args) {
       Integer[] a = {0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7}; 
       dedup(a);
       for (int i= 0; i< a.length; i++)  {
           System.out.print(a[i]);
       }
       System.out.println("\n===END===");
    }

    // in-place without allocation non-constant-size memory
    protected static void dedup(Integer[] arr) {
        if (arr == null || arr.length == 1) {
            return;
        }

        int i = -1, j = -1;
        while (++j < arr.length) {
            if (j==0 || arr[j] != arr[i]) {
                arr[++i] = arr[j];
                printArray(arr);
                System.out.println(" ; i = " + i + "; j = " + j);
            }
        }
    }

    protected static void printArray(Integer[] arr) {
       for (int i= 0; i< arr.length; i++) {
           System.out.print(arr[i] + " ");
       }
    }
}

/**
 * Array is simpler than List. Array's size is 'length' but List size is 'size()''
 * For List, we use get(idx), and set(idx, element) to get and retrieve values.
 */
