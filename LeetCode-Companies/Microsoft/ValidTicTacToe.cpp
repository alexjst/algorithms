/*
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        int rows = board.size();
        if (rows!=3) return false;
        int cols = board[0].size();
        if (cols!=3) return false;

        // let 'X' be 1 and 'O' be -1, let's calculate the sums of each rows and cols
        vector<int> rowSum(3);
        vector<int> colSum(3);
        fill(rowSum.begin(), rowSum.end(), 0);
        fill(colSum.begin(), colSum.end(), 0);
        int turns = 0;
        int diag = 0, antidiag = 0;

        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (board[i][j] == 'X') {
                    rowSum[i]++;
                    colSum[j]++;
                    turns++;
                    if (i==j) diag++;
                    if ((i+j)==2) antidiag++;
                } else if (board[i][j] == 'O') {
                    rowSum[i]--;
                    colSum[j]--;
                    turns--;
                    if (i==j) diag--;
                    if ((i+j)==2) antidiag--;
                }
            }
        }

        if (turns<0 || turns>1) return false;

        bool xwin = rowSum[0]==3 || rowSum[1]==3 || rowSum[2]==3 || colSum[0]==3
         || colSum[2]==3 || colSum[3]==3 || diag==3 || antidiag==3;
        bool owin = rowSum[0]==-3 || rowSum[1]==-3 || rowSum[2]==-3 || colSum[0]==-3
         || colSum[2]==-3 || colSum[3]==-3 || diag==-3 || antidiag==-3;

         if (xwin && owin) return false;
         return (xwin && turns == 1) || (owin && turns == 0) || (!xwin && !owin);
    }
};

int main() {
    Solution s;
    vector<string> input = {"XOX","O O","XOX"};
    cout << s.validTicTacToe(input) << endl;
    return 0;
}