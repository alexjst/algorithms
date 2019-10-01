/**
 * This problem was asked by Microsoft.
 * 
 * You have an N by N board. Write a function that, given N, returns the number
 * of possible arrangements of the board where N queens can be placed on the
 * board without threatening each other, i.e. no two queens share the same row,
 * column, or diagonal.
 * 
 */

 /*
 * Use DFS:
 *  1. each row is a node, keep path, result in the DFS recursion arg list
 *  2. use 4 array to quickly check attacking conditions
 *  3. When adding a path to the result, need to make an explicit copy of the path since otherwise it will be reference (single copy in memory)
 */ 

import java.util.List;
import java.util.ArrayList;

class NQueen {
    public static void main(String[] args) {
        List<Integer[][]> positionLists = getPositions(8);
        for (Integer[][] positions : positionLists) {
            for (Integer[] pos : positions) {
                System.out.print("(" + pos[0] + "," + pos[1] + ") ");
            }
            System.out.println();
        }
    }

    private static void markPosition(int N, int row, int col,
            boolean[] rowCheck,
            boolean[] colCheck,
            boolean[] diagCheck,
            boolean[] antidiagCheck, boolean flag) {
                rowCheck[row] = flag;
                colCheck[col] = flag;
                diagCheck[row-col + N -1] = flag;
                antidiagCheck[row + col] = flag;
    }

    private static boolean hasAttack(int N, int row, int col,
            boolean[] rowCheck,
            boolean[] colCheck,
            boolean[] diagCheck,
            boolean[] antidiagCheck) {
        if (row<0 || row>=N || col<0 || col >=N) return true;
        return (rowCheck[row] || colCheck[col]
                || diagCheck[row - col + N - 1] || antidiagCheck[row + col]);
    }

    public static List<Integer[][]> getPositions(int N) {
        List<Integer[][]> result = new ArrayList<>();
        boolean[] rowCheck = new boolean[N];
        boolean[] colCheck = new boolean[N];
        boolean[] diagCheck = new boolean[N*2-1];
        boolean[] antidiagCheck = new boolean[N*2-1];

        Integer[][] path = new Integer[N][2];
        dfs(N, 0, rowCheck, colCheck, diagCheck, antidiagCheck, path, result);
        return result;
    }

    private static void dfs(int N, int row, boolean[] rowCheck, boolean[] colCheck, boolean[] diagCheck,
            boolean[] antidiagCheck, Integer[][] path, List<Integer[][]> result) {
        if (row >= N) return;
        // find a good position from row
        for (int j = 0; j < N; j++) {
            if (!hasAttack(N, row, j, rowCheck, colCheck, diagCheck, antidiagCheck)) {
                path[row][0] = row;
                path[row][1] = j;
                 if (row == N-1) {
                     // make a copy of the path as the result
                     // otherwise it's reference and there' only a single copy that changes
                    Integer[][] goodPath = new Integer[N][2];
                    for (int r=0; r<N; r++)
                        for (int c=0; c<2; c++)
                            goodPath[r][c] = path[r][c];
                    result.add(goodPath);
                    return;
                } else {
                    markPosition(N, row, j, rowCheck, colCheck, diagCheck, antidiagCheck, true);
                    dfs(N, row + 1, rowCheck, colCheck, diagCheck, antidiagCheck, path, result);
                    markPosition(N, row, j, rowCheck, colCheck, diagCheck, antidiagCheck, false);
                }
            }
        }
    }
}
