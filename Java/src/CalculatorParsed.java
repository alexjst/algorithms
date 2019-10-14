/**
 * This is from Microsoft onsite. It's not really a complicated problem but somehow I started with complex anticipation and screwed it up!
 */

public class CalculatorParsed {
    public static void main(String[] args) {
        CalculatorParsed inst = new CalculatorParsed();
        // following should be 360
        System.out.println(inst.calc("5 + 2 * 3 - 4 * 7 + 5 * 8 * 9".split(" ")));
    }

    int calc(String[] in) {
        int result = 0;
        int part = 0;
        for (int i = 0; i<in.length; i++) {
            if (i==0 || in[i-1].equals("+")) {
                result += part;
                part = Integer.parseInt(in[i]);
            } else if (in[i-1].equals("-")) {
                result += part;
                part = - Integer.parseInt(in[i]);
            } else if (in[i-1].equals("*")) {
                part *= Integer.parseInt(in[i]);
            }
        }
        result = part;
        return result;
    }
}