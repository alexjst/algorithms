package alexyang.algorithms.Java.src;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.sun.org.apache.xalan.internal.xsltc.compiler.Pattern;

public class Test {
    public static void main(String[] args) {
        String in = "soda moka 45+2 S someone else";
        String player;
        String time;
        String event;
        String player2;
        String pattern = "(\\D*)(\\d+[\\+]*[\\d]*)\\s+(S|Y|R|G)\\s+(.*)";
        Pattern p = Pattern.compile(pattern);
        Matcher m = p.matcher(in);
        if (m.find()) {
            //System.out.println(m.group(0));
            System.out.println(m.group(1));
            System.out.println(m.group(2));
            System.out.println(m.group(3));
            System.out.println(m.group(4));
        } else {
            System.out.println("no match");
        }
    }

}
