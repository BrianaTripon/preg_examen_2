from texttable import *


class Board:
    def __init__(self):
        self.data = [[" "]*6 for i in range(6)]

    def create_board(self):
        board = Texttable()
        for index in range(6):
            board.add_row(self.data[index])
        return board.draw()

    def place_symbol(self, row, column, symbol):
        """
        the function puts the given symbol into the correspondig position
        given by row and column
        :param row:
        :param column:
        :param symbol:
        """
        self.data[row][column] = symbol

    def set_value(self, i, j, val):
        if val == "-":
            self.data[i][j] = " "
        elif val == "X":
            self.data[i][j] = "X"
        elif val == "O":
            self.data[i][j] = "O"


def test_create_board():
    board = Board()
    print(board.create_board())
#test_create_board()


class Game:
    def __init__(self):
        self.player = Board()
        self.computer = Board()

    def human_move(self, row, column, symbol):
        self.player.place_symbol(row, column, symbol)

    def check_victory(self, row, column, symbol):
        """
        checks if the player has won or not; counts how many identical symbols are on the same
        row, column or diagonal with the las symbol added
        :param row:
        :param column:
        :param symbol:
        :return:
        """
        left_right = 0
        up_down = 0
        left_up_right_down = 0
        left_down_right_up = 0

        left_right += self.left_right(row, column, symbol)
        up_down += self.up_down(row, column, symbol)
        left_up_right_down += self.left_up_right_down(row, column, symbol)
        left_down_right_up += self.left_down_right_up(row, column, symbol)
        # if left_right >= 4:
        #     return True
        # if up_down >= 4:
        #     return True
        # if left_up_right_down >= 4:
        #     return True
        # if left_down_right_up >= 4:
        #     return True
        if left_right >= 5:
            return True
        if up_down >= 5:
            return True
        if left_up_right_down >= 5:
            return True
        if left_down_right_up >= 5:
            return True
        return False

    def check_if_full_board(self):
        """
        checks if the board is full, there no possible moves
        """
        for i in range(6):
            for j in range(6):
                if self.player.data[i][j] == " ":
                    return False
        return True

    def check_if_win(self):
        for i in range(6):
            for j in range(6):
                if self.player.data[i][j] == " ":
                    if self.check_victory(i, j, "X") is True:
                        return i, j, "O"
                    elif self.check_victory(i, j, "O") is True:
                        return i, j, "X"
        return None, None, None

    def not_empty(self, row, column, symbol):
        if row is None or column is None or symbol is None:
            return True
        if self.player.data[row][column] != " ":
            return True
        return False

    def left_right(self, row, column, symbol):
        """
        counts how many identical symbols are on the same row
        """
        count = 0
        #index = column - 1
        # while index >= 0 and self.player.data[row][index] == symbol:
        #     count += 1
        #     index -= 1
        # index = column + 1
        # while index <= 5 and self.player.data[row][index] == symbol:
        #     count += 1
        #     index += 1
        for index in range(6):
            if self.player.data[row][index] == symbol:
                count += 1
        return count

    def up_down(self, row, column, symbol):
        count = 0
        for index in range(6):
            if self.player.data[index][column] == symbol:
                count += 1
        return count

    def left_up_right_down(self, row, column, symbol):
        count = 1
        # index = 0
        # while index <= 5:
        #     if self.player.data[index][index] == symbol:
        #         count += 1
        #     index += 1
        index_row = row - 1
        index_column = column - 1
        while index_row >= 0 and index_column >= 0:
            if self.player.data[index_row][index_column] == symbol:
                count += 1
            index_row -= 1
            index_column -= 1

        index_row = row + 1
        index_column = column + 1
        while index_row <= 5 and index_column <= 5:
            if self.player.data[index_row][index_column] == symbol:
                count += 1
            index_row += 1
            index_column += 1
        return count

    def left_down_right_up(self, row, column, symbol):
        count = 1
        # index = 0
        # while index <= 5:
        #     if self.player.data[index][index] == symbol:
        #         count += 1
        #     index += 1
        index_row = row + 1
        index_column = column - 1
        while index_row <= 5 and index_column >= 0:
            if self.player.data[index_row][index_column] == symbol:
                count += 1
            index_row += 1
            index_column -= 1

        index_row = row - 1
        index_column = column + 1
        while index_row >= 0 and index_column <= 5:
            if self.player.data[index_row][index_column] == symbol:
                count += 1
            index_row -= 1
            index_column += 1
        return count




