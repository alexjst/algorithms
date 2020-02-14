//package alexyang.algorithms.Java.Opendoor;

import java.io.*;
import java.util.*;

class Problem1 {

    Map<String, String> map = new HashMap<>();

    Map<String, Integer> valMap = new HashMap<>();

    // dependency graph
    Map<String,Set<String>> adj = new HashMap<>();

    public static void main(String[] args) {
        Problem1 p1 = new Problem1();
        p1.set_value("A1", "3");
        p1.set_value("B1", "5");
        p1.set_value("C2", "=A1+B1");
        System.out.println(p1.get_value("A1"));
        System.out.println(p1.get_value("B1"));
        System.out.println(p1.get_value("C2"));
        p1.set_value("A1", "10");
        System.out.println(p1.get_value("C2"));
    }

    /*
    void set_value(String cell, String val) {
        map.put(cell, val);
    }

    int get_value_eval(String cell) {
        String val = map.getOrDefault(cell, "0");
        if (val.startsWith("=")) {
            System.out.println("val=" + val);
            String[] segs = val.substring(1, val.length()).split("\\+");
            return get_value(segs[0]) + get_value(segs[1]);
        } else {
            return Integer.parseInt(val);
        }
    }
    */

    void set_value(String cell, String val) {
        invalidate(cell);
        if (val.startsWith("=")) {
            //System.out.println("val=" + val);
            String[] segs = val.substring(1, val.length()).split("\\+");
            Set<String> set0 = adj.get(segs[0]);
            if (set0 != null) {
                set0.add(cell);
            } else {
                set0 = new HashSet<>();
                set0.add(cell);
                adj.put(segs[0], set0);
            }
            Set<String> set1 = adj.get(segs[1]);
            if (set1 != null) {
                set1.add(cell);
            } else {
                set1 = new HashSet<>();
                set1.add(cell);
                adj.put(segs[0], set1);
            }
        } else {
            valMap.put(cell, Integer.parseInt(val));
        }
        map.put(cell, val);
    }

    int get_value(String cell) {
        if (valMap.containsKey(cell)) {
            return valMap.get(cell);
        }

        int res;

        String val = map.getOrDefault(cell, "0");
        if (val.startsWith("=")) {
            //System.out.println("val=" + val);
            String[] segs = val.substring(1, val.length()).split("\\+");
            res = get_value(segs[0]) + get_value(segs[1]);
        } else {
            res = Integer.parseInt(val);
        }

        return res;
    }

    void invalidate(String cell) {
        valMap.remove(cell);
        if (adj.containsKey(cell)) {
            Set<String> children = adj.get(cell);
            for (String s : children) {
                invalidate(s);
            }
        }
    }
}
