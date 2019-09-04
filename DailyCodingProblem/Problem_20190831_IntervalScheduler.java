/**
 * This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
 */

 import java.util.Timer;
 import java.util.TimerTask;

 class Problem_20190831_IntervalScheduler {
     public static void main(String[] args) {
        System.out.println("Starting...");
        new Timer().schedule(new TimerTask(){
            @Override
            public void run() {
                System.out.println("Hello world!");
            }
        }, 5000);
     }
 }