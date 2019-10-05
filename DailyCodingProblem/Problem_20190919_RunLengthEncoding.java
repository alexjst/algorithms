/**
 * This problem was asked by Amazon.
 * 
 * Run-length encoding is a fast and simple method of encoding strings. The
 * basic idea is to represent repeated successive characters as a single count
 * and character. For example, the string "AAAABBBCCDAA" would be encoded as
 * "4A3B2C1D2A".
 * 
 * Implement run-length encoding and decoding. You can assume the string to be
 * encoded have no digits and consists solely of alphabetic characters. You can
 * assume the string to be decoded is valid.
 */

class RunLengthCoder {
    public static void main(String[] args) {
        System.out.println(RunLengthCoder.encode("AAAABBBCCDAA"));
        System.out.println(RunLengthCoder.decode("4A3B2C1D2A"));
    }

    private static String encode(String in) {
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        Character cur = null;
        for (int i=0; i<in.length(); i++) {
            if (i==0 || in.charAt(i)!=in.charAt(i-1)) {
                cnt = 1;
                cur = in.charAt(i);
            } else {
                cnt++;
            }
            if (i==(in.length()-1) || in.charAt(i+1)!=in.charAt(i)) {
                sb.append(cnt); sb.append(cur);
            }
        }
        return sb.toString();
    }

    private static String decode(String in) {
        StringBuilder sb = new StringBuilder();
        StringBuilder sbDigits = new StringBuilder();
        Character cur = ' ';
        for (int i=0; i<in.length(); i++) {
            if (Character.isDigit(in.charAt(i))) {
                if (i==0 || !Character.isDigit(in.charAt(i-1))) {
                    sbDigits = new StringBuilder();
                    sbDigits.append(in.charAt(i));
                } else {
                    sbDigits.append(in.charAt(i));
                }
            } else {
                cur = in.charAt(i);
                int cnt = Integer.parseInt(sbDigits.toString());
                for (int j=0; j<cnt; j++) {
                    sb.append(cur);
                }
            }
        }
        return sb.toString();
    }

}