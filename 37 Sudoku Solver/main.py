import copy
from typing import List

class Solution:
    ready_board = []
    boxes = List[List[str]]
    LOC_BOX = {
        "(0, 0)": 0,
        "(0, 1)": 0,
        "(0, 2)": 0,
        "(1, 0)": 0,
        "(1, 1)": 0,
        "(1, 2)": 0,
        "(2, 0)": 0,
        "(2, 1)": 0,
        "(2, 2)": 0,
        "(0, 3)": 1,
        "(0, 4)": 1,
        "(0, 5)": 1,
        "(1, 3)": 1,
        "(1, 4)": 1,
        "(1, 5)": 1,
        "(2, 3)": 1,
        "(2, 4)": 1,
        "(2, 5)": 1,
        "(0, 6)": 2,
        "(0, 7)": 2,
        "(0, 8)": 2,
        "(1, 6)": 2,
        "(1, 7)": 2,
        "(1, 8)": 2,
        "(2, 6)": 2,
        "(2, 7)": 2,
        "(2, 8)": 2,
        "(3, 0)": 3,
        "(3, 1)": 3,
        "(3, 2)": 3,
        "(4, 0)": 3,
        "(4, 1)": 3,
        "(4, 2)": 3,
        "(5, 0)": 3,
        "(5, 1)": 3,
        "(5, 2)": 3,
        "(3, 3)": 4,
        "(3, 4)": 4,
        "(3, 5)": 4,
        "(4, 3)": 4,
        "(4, 4)": 4,
        "(4, 5)": 4,
        "(5, 3)": 4,
        "(5, 4)": 4,
        "(5, 5)": 4,
        "(3, 6)": 5,
        "(3, 7)": 5,
        "(3, 8)": 5,
        "(4, 6)": 5,
        "(4, 7)": 5,
        "(4, 8)": 5,
        "(5, 6)": 5,
        "(5, 7)": 5,
        "(5, 8)": 5,
        "(6, 0)": 6,
        "(6, 1)": 6,
        "(6, 2)": 6,
        "(7, 0)": 6,
        "(7, 1)": 6,
        "(7, 2)": 6,
        "(8, 0)": 6,
        "(8, 1)": 6,
        "(8, 2)": 6,
        "(6, 3)": 7,
        "(6, 4)": 7,
        "(6, 5)": 7,
        "(7, 3)": 7,
        "(7, 4)": 7,
        "(7, 5)": 7,
        "(8, 3)": 7,
        "(8, 4)": 7,
        "(8, 5)": 7,
        "(6, 6)": 8,
        "(6, 7)": 8,
        "(6, 8)": 8,
        "(7, 6)": 8,
        "(7, 7)": 8,
        "(7, 8)": 8,
        "(8, 6)": 8,
        "(8, 7)": 8,
        "(8, 8)": 8,
    }

    def dot_detector(self, board: List[List[str]]) -> list:
        dot_list = list()
        for col in range(9):
            for row in range(9):
                if board[col][row] == ".":
                    dot_list.append((col, row))
        return dot_list

    def box_devider(self, board: List[List[str]]) -> list:
        box_list = []
        box = []
        box_row = []
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                for j in range(3):
                    for k in range(3):
                        box_row.append(board[j + row][k + col])
                    box.append(box_row)
                    box_row = list()

                box_list.append(box)
                box = list()
        return box_list

    def number_filler(self,loc : list,board: List[List[str]]):
        for items in loc:
            board[items[0]][items[1]] = ['1','2','3','4','5','6','7','8','9']
        return board

    def column_checker(self, numbers : list, column : int, board : List[List[str]]):
        number_list = numbers.copy()
        for number in number_list:
            for i in range(9):
                if number == board[i][column] :
                            if number in number_list:
                                number_list.remove(number)
        return number_list

    def row_checher(self, numbers : list, row : list):
        number_list = numbers.copy()
        for number in number_list:
            for i in range(9):
                if number == row[i] and (number in number_list):
                    number_list.remove(number)
        return number_list

    def box_checker(self, numbers : list, box : int, boxes : List[List[str]]):
        number_list = numbers.copy()
        for number in number_list:
            if (number in boxes[box][0]) or (number in boxes[box][1]) or (number in boxes[box][2]):
                del number_list[number_list.index(number)]

        return number_list

    def dot_changer(self, numbers : list):
        return f'/{numbers[0]}'

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        condition = True
        self.ready_board = list(map(list, board))

        print(*self.ready_board, sep='\n')
        print('ID RD : ', id(self.ready_board))
        print("ID Board : ",id(board))
        print('ID RD[1]', id(self.ready_board[0]))
        print('ID B[1]', id(board[0]))


        self.boxes = self.box_devider(self.ready_board)
        print('Boxes', *self.boxes, sep='\n')
        dot_list = list(self.dot_detector(self.ready_board))
        self.ready_board = self.number_filler(dot_list, self.ready_board)
        i = 0
        print(*self.ready_board, sep='\n')

        while condition:
            if len(dot_list) == 0:
                condition = False
            for numbers in dot_list:
                self.ready_board[numbers[0]][numbers[1]] = self.box_checker(self.ready_board[numbers[0]][numbers[1]],
                                                                self.LOC_BOX[f"{numbers}"], self.boxes)
                if len(self.ready_board[numbers[0]][numbers[1]]) == 1:
                    board[numbers[0]][numbers[1]] = self.dot_changer(self.ready_board[numbers[0]][numbers[1]])
                    del dot_list[dot_list.index(numbers)]
                    self.boxes = self.box_devider(board)
                    continue
                self.ready_board[numbers[0]][numbers[1]] = self.column_checker(self.ready_board[numbers[0]][numbers[1]], numbers[0],
                                                                    board)
                if len(self.ready_board[numbers[0]][numbers[1]]) == 1:
                    board[numbers[0]][numbers[1]] = self.dot_changer(self.ready_board[numbers[0]][numbers[1]])
                    del dot_list[dot_list.index(numbers)]
                    self.boxes = self.box_devider(board)
                    continue
                self.ready_board[numbers[0]][numbers[1]] = self.row_checher(self.ready_board[numbers[0]][numbers[1]], board[numbers[1]])
                if len(self.ready_board[numbers[0]][numbers[1]]) == 1:
                    board[numbers[0]][numbers[1]] = self.dot_changer(self.ready_board[numbers[0]][numbers[1]])
                    del dot_list[dot_list.index(numbers)]
                    self.boxes = self.box_devider(board)
                    continue

            print('Length of DOT_LIST : ', len(dot_list))
            if i == 10:
                condition = False
            print("New iteration ", i)
            print(*board, sep='\n')
            i += 1

        print("Ready list ")
        print(*self.ready_board, sep='\n')



if __name__ == "__main__":
    Solution.solveSudoku(self=Solution(), board=[["5","3",".",".","7",".",".",".","."],
                                                 ["6",".",".","1","9","5",".",".","."],
                                                 [".","9","8",".",".",".",".","6","."],
                                                 ["8",".",".",".","6",".",".",".","3"],
                                                 ["4",".",".","8",".","3",".",".","1"],
                                                 ["7",".",".",".","2",".",".",".","6"],
                                                 [".","6",".",".",".",".","2","8","."],
                                                 [".",".",".","4","1","9",".",".","5"],
                                                 [".",".",".",".","8",".",".","7","9"]])



"""

"""