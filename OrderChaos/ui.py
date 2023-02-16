from random import *

from OrderChaos.game import Board, Game


class UI:
    def __init__(self):
        #self.board = Board()
        self.game = Game()
        self.game_over = False

    def start_game(self):
        # print("1. Start new game!")
        # print("0. Exit")
        # option = int(input("Enter option: "))
        # if option == '1':
        self.new_game()
        print("Choose your move: ")
        row = input("Row: ")
        column = input("Column: ")
        symbol = input("Symbol: ")
        if self.check_if_valid_inputs(row, column, symbol) is not True:
            print(self.check_if_valid_inputs(row, column, symbol))
            self.start_game()
        if self.game_over is False:
            row = int(row)
            column = int(column)
            self.player_move(row, column, symbol)
            self.start_game()
        else:
            self.new_game()
        # row = int(row)
        # column = int(column)
        # self.player_move(row, column, symbol)
        # self.start_game()

    def check_if_valid_inputs(self, row, column, symbol):
        try:
            row = int(row)
            column = int(column)
        except ValueError:
            return "The inputs must be of int type!"
        if row not in range(6):
            return ValueError("The rows number must be between 0-5")
        if column not in range(6):
            return ValueError("The rows number must be between 0-5")
        if symbol not in ["X", "O"]:
            return ValueError("The symbol must be X or O")
        return True

    def new_game(self):
        print(self.game.player.create_board())

    def player_move(self, row, column, symbol):
        self.game.player.place_symbol(row, column, symbol)
        print(self.game.player.create_board())
        if self.game.check_victory(row, column, symbol):
            print("You won! :)")
            self.game_over = True
            return
        elif self.game.check_if_full_board():
            print("You lost! :(")
            self.game_over = True
        else:
            row, column, symbol = self.game.check_if_win()
            if row is not None:
                self.game.player.place_symbol(row, column, symbol)
                print(self.game.player.create_board())
            else:
                while self.game.not_empty(row, column, symbol):
                    row = choice([0, 1, 2, 3, 4, 5])
                    column = choice([0, 1, 2, 3, 4, 5])
                    symbol = choice(["X", "O"])
                self.game.player.place_symbol(row, column, symbol)
                print(self.game.player.create_board())
                if self.game.check_victory(row, column, symbol):
                    print("You won! :)")
                    self.game_over = True
                    return
                elif self.game.check_if_full_board():
                    print("You lost! :(")
                    self.game_over = True
                    return


ui = UI()
ui.start_game()



