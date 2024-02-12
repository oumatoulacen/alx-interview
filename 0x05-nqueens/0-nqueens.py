#!/usr/bin/python3
''' solve the quench problem using backtracking'''
import sys


N = int(sys.argv[1])


class solution:
    def solveNquens(self, n: int):
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = 'Q'
                backtrack(row + 1)
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
                board[row][c] = '.'
        backtrack(0)
        return res


s = solution()
print(s.solveNquens(N))
