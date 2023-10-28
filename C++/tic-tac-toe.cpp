#include <iostream>
using namespace std;

// Function to display the Tic-Tac-Toe board
void displayBoard(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << board[i][j];
            if (j < 2) {
                cout << " | ";
            }
        }
        cout << endl;
        if (i < 2) {
            cout << "---------\n";
        }
    }
}

// Function to check if the game is won
bool checkWin(char board[3][3], char player) {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
            return true;  // Horizontal win
        }
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) {
            return true;  // Vertical win
        }
    }
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) {
        return true;  // Diagonal win (top-left to bottom-right)
    }
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) {
        return true;  // Diagonal win (top-right to bottom-left)
    }
    return false;
}

int main() {
    char board[3][3] = { { ' ', ' ', ' ' }, { ' ', ' ', ' ' }, { ' ', ' ', ' ' } };
    char currentPlayer = 'X';

    cout << "Welcome to Tic-Tac-Toe!" << endl;

    for (int turn = 0; turn < 9; turn++) {
        displayBoard(board);
        int row, col;
        cout << "Player " << currentPlayer << ", enter your move (row and column): ";
        cin >> row >> col;

        if (row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] != ' ') {
            cout << "Invalid move. Try again." << endl;
            turn--;
        } else {
            board[row][col] = currentPlayer;

            if (checkWin(board, currentPlayer)) {
                displayBoard(board);
                cout << "Player " << currentPlayer << " wins!" << endl;
                break;
            }

            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }
    }

    if (!checkWin(board, 'X') && !checkWin(board, 'O')) {
        displayBoard(board);
        cout << "It's a draw!" << endl;
    }

    return 0;
}
