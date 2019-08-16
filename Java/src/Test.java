package alexyang.algorithms.Java.src;

public class Test {
    public static long swapBits(long x, int i, int j) {
        // TODO - you fill in here.
        if ( ((x>>>i) & 1) != ((x>>>j) & 1) ) {
            long bitMask = (1L << i) | (1L << j);
            x ^= bitMask;
        }
        return x;
    }

    public static void main(String[] args) {
        swapBits(71, 1, 6);
    }
}
