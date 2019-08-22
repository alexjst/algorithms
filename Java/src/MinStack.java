package alexyang.algorithms.Java.src;

import java.util.*;

/**
 * ["MinStack","push","push","push","push","pop","getMin","pop","getMin","pop","getMin"]
 * [[],[512],[-1024],[-1024],[512],[],[],[],[],[],[]]
 */
class MinStack {
    public static void main(String[] args) {
        int i1 = 1;
        Integer i2 = 1;
        Integer i3 = new Integer(1);
        Long l1 = 1L;
    
        System.out.println("i1 == i2"+(i1==i2));
        System.out.println("i2 == i1"+(i2==i1));
        System.out.println("i1 == i3"+(i1==i3));
        System.out.println("i2 == i3"+(i2==i3));

        MinStack ms = new MinStack();
        ms.push(512);
        ms.push(-1024);
        ms.push(-1024);
        ms.push(512);
        System.out.println(ms.getMin());
        ms.pop();
        System.out.println(ms.getMin());
        ms.pop();
        System.out.println(ms.getMin());
        ms.pop();
        System.out.println(ms.getMin());
    }

    /** initialize your data structure here. */
    public MinStack() {
        s = new Stack<Integer>();
        ms = new Stack<Integer>();
    }
    
    public void push(int x) {
        if (ms.empty() || x <= ms.peek()) ms.push(x);
        s.push(x);
    }
    
    public void pop() {
        if (s.empty()) return;
        Integer p = s.pop();
        if (p != null && p == ms.peek().intValue()) {
            ms.pop();
        } 
    }
    
    public int top() {
        if (s.empty()) return 0;
        else return s.peek();
    }
    
    public int getMin() {
        if (s.empty()) return 0;
        return ms.peek();
    }
    
    private Stack<Integer> s;
    private Stack<Integer> ms;
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */