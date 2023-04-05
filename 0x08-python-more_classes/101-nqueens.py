#!/usr/bin/python3
import sys

def is_valid(board, row, col, N):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, N):
    if row == N:
        print(' '.join(str(x+1) for x in board))
    else:
        for i in range(N):
            if is_valid(board, row, i, N):
                board[row] = i
                solve_n_queens(board, row+1, N)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [-1] * N
    solve_n_queens(board, 0, N)
