import random

class TicTacToe():
    def __init__(self):
        self.board = list(' ' * 10)  #ignore the 0th cell
        self.player = random.choice(['X', 'O'])

    def show_board(self):
        """Method for displaying the current game board
        """
        print(f'| {self.board[1]} | {self.board[2]} | {self.board[3]} |')
        print('-' * 13)
        print(f'| {self.board[4]} | {self.board[5]} | {self.board[6]} |')
        print('-' * 13)
        print(f'| {self.board[7]} | {self.board[8]} | {self.board[9]} |\n\n')

    def fill_cell(self, cell : int, player : str) -> None:
        """Method for fixing the spot which user choosed

        :param cell: Number of the cell between 1 and 9
        :param player: Which player is filling the spot
        """
        self.board[cell] = player

    def determine_winner(self, player : str) -> bool:
        """Method for deciding if a player won

        :param player: Which player is being checked
        :return: True if the player won. False if not
        """
        win_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9), #rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9), #columns
            (1, 5, 9), (3, 5, 7) #diogonals
        ]

        for combination in win_combinations:
            # if all([self.board[cell] == player for cell in combination]):
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == player:
                return True
        return False

    def players_turn(self) -> None:
        """Method for swapping the turn
        """
        self.player = 'X' if self.player == 'O' else 'O'

    def is_board_filled(self) -> bool:
        """Method for checking if the game board is filled completely 

        :return: True if the board is filled. False if not
        """
        return ' ' not in self.board[1:10]

    def start_game(self) -> None:
        """Manin method for starting the game
        """
        while True:
            self.show_board()
            try:
                cell = int(input(f"It's Player {self.player}'s turn. Enter a cell number: "))

                if cell in range(1,10) and self.board[cell] == ' ':
                    self.fill_cell(cell, self.player)

                    if self.determine_winner(self.player):
                        self.show_board()
                        print(f"Player {self.player} won!")
                        break

                    if self.is_board_filled():
                        self.show_board()
                        print("It's a draw!")
                        break
                    
                    self.players_turn()

                else:
                    print("Invalid input. Please try again: ")

            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")


    
if __name__ == "__main__":
    tic = TicTacToe()
    tic.start_game()