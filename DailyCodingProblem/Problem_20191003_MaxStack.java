/**
 * This problem was asked by Amazon.
 * 
 * Implement a stack that has the following methods:
 * 
 * push(val), which pushes an element onto the stack pop(), which pops off and
 * returns the topmost element of the stack. If there are no elements in the
 * stack, then it should throw an error or return null. max(), which returns the
 * maximum value in the stack currently. If there are no elements in the stack,
 * then it should throw an error or return null. Each method should run in
 * constant time.
 */

 /**
  * Idea: 1. use a linkedList for basic stack function itself
  *       2. use a second linkedList that always keeps max item on top
  */
import java.util.*;

class MaxStack {
    private LinkedList<Integer> s = new LinkedList<>();
    private LinkedList<Integer> ms = new LinkedList<>();

    public static void main(String[] args) {
        MaxStack inst = new MaxStack();
        inst.push(15);
        System.out.println(inst.max());
        inst.push(20);
        System.out.println(inst.max());
        inst.push(2);
        System.out.println(inst.max());
        inst.push(12);
        System.out.println(inst.max());
        inst.push(52);
        System.out.println(inst.max());

        System.out.println("Now starting poping:");
        System.out.println(inst.pop());
        System.out.println(inst.max());

        System.out.println(inst.pop());
        System.out.println(inst.max());

        System.out.println(inst.pop());
        System.out.println(inst.max());

        System.out.println(inst.pop());
        System.out.println(inst.max());

        System.out.println(inst.pop());
        System.out.println(inst.max());

        System.out.println(inst.pop());
        System.out.println(inst.max());

        System.out.println(inst.pop());
        System.out.println(inst.max());
    }

    public void push(Integer val) {
        s.add(val);
        if (ms.isEmpty() || ms.getLast()<=val) {
            ms.add(val);
        }
    }

    public Integer pop() {
        if (s.isEmpty()) return null;
        Integer val = s.getLast();
        s.removeLast();
        if (!ms.isEmpty() && ms.getLast() == val) {
            ms.removeLast();
        }
        return val;
    }

    public Integer max() {
        if (ms.isEmpty()) return null;
        else return ms.getLast();
    }
}