'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board2 = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                live = 0
                if i > 0:
                    # check top left
                    if j > 0:
                        live += board[i-1][j-1]
                    # check top
                    live += board[i-1][j]
                    # check top right
                    if j < len(board[i])-1:
                        live += board[i-1][j+1]
                # check left
                if j > 0:
                    live += board[i][j-1]
                # check right
                if j < len(board[i])-1:
                    live += board[i][j+1]
                if i < len(board)-1:
                     # check bottom left
                    if j > 0:
                        live += board[i+1][j-1]
                    # check bottom
                    live += board[i+1][j]
                    # check bottom right
                    if j < len(board[i])-1:
                        live += board[i+1][j+1]
                #print(live)
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board2[i][j] = 0
                else:
                    if live == 3:
                        board2[i][j] = 1
        for i in range(len(board)):
            board[i] = board2[i]
#        board = copy.deepcopy(board2)
