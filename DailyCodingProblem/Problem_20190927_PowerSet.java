/* This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
*/

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class PowerSet {
    public List<List<Integer>> powerSet(List<Integer> input) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<Integer>());
        for (Integer i : input) {
            // make a deep copy of 'result' into moree
            List<List<Integer>> more = new ArrayList<>();
            for (List<Integer> lst : result) {
                List<Integer> copy = new ArrayList<>(lst);
                copy.add(i);
                more.add(copy);
            }
           result.addAll(more);
        }
        return result;
    }

    public static void main(String[] args) {
        PowerSet inst = new PowerSet();
        List<List<Integer>> res = inst.powerSet(Arrays.asList(1, 2, 3));
        for (List<Integer> ls : res) {
            for (Integer i : ls) {
                System.out.print(i);
                System.out.print("\t");
            }
            System.out.println();
        }
    }
}

/**
 * Important Learnings: In Java, when you copy an primitive or an wrapped primitive, you have a deep copy
 * so that when you operate on the copy, you don't touch the origin. However, with a composite type, copying
 * it involves copying its internal elements which are actually copies of references (shallow copies). Now
 * when you operate on the copy, you work on the inside references that may just changes the contents of
 * the original object, resulting in unexpected behaviors. So be careful with shallow and deep copying.
 */