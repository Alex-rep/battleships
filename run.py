import random


class PlayerBoard:
    """
    Contains the board and relative data for each player
    """

    player_name = ""
    score = 0
    board = []
    ships = []

    def __init__(self, name, ship_list, board, score):
        """
        Constructs the object and inserts the board owner's name
        """

        self.player_name = name
        self.ships = ship_list
        self.board = board
        self.score = score

    def add_ships(self):
        """
        Adds the symbols for ships to the player board
        """
        for index in range(4):
            row = self.ships[index][0]
            column = self.ships[index][1]
            self.board[row][column] = "@"


def generate_board():
    """
    Generates an empty player board
    """

    column = [".", ".", ".", "."]
    board = []

    for index in range(4):
        new_col = column.copy()
        board.append(new_col)

    return board


def generate_ships():
    """
    Generates four couples of integers between 0 and 4 that
    represent the coordinates for the player's ships
    """
    ship_list = []

    for index in range(4):

        ship_row = index
        ship_column = random.randint(0, 3)
        ship = [ship_row, ship_column]
        ship_list.append(ship)

    return ship_list


def roll_guess():
    """
    Generates a couple of integers, guesses
    a position on the board
    """

    row = random.randint(0, 3)
    column = random.randint(0, 3)
    result = [row, column]
    return result


def get_guess():
    """
    Retrieves a guess from the player
    """
    print("Guess a row: \n")
    row = input()
    print("Guess a column: \n")
    column = input()

    result = [int(row) - 1, int(column) - 1]
    return result


def print_board(player_board):
    """
    Prints the board for the specified player
    """
    for index in range(4):
        print(player_board.board[index])
        print("\n")


def evaluate_guess(board, guess):
    """
    Takes a board, a guess, and evaluates if the guess
    hits a ship contained in the provided board
    """
    for index in range(4):

        if board.board[guess[0]][guess[1]] == "*":

            break

        if guess[0] == board.ships[index][0] and guess[1] == board.ships[index][1]:

            board.board[guess[0]][guess[1]] = "*"
            board.score += 1
            break

        else:

            board.board[guess[0]][guess[1]] = "X"


def main_game_loop(player_board, cpu_board):
    """
    Main Game Loop. The game keeps looping, asking for guesses to the player 
    and taking guesses from the CPU. The game ends when the player or the CPU
    achieve a score of 4.
    """

    while True:

        print(f"\nThe score is {cpu_board.score} for you and {player_board.score} for the CPU.\n")
        print("Player's Board: \n")
        print_board(player_board)

        print("CPU's Board: \n")
        print_board(cpu_board)

        guess = get_guess()

        evaluate_guess(cpu_board, guess)

        cpu_guess = roll_guess()

        evaluate_guess(player_board, cpu_guess)

        if player_board.score == 4 or cpu_board.score == 4:

            if player_board.score == 4:
                print("\nCPU wins!\n")
                break

            elif cpu_board.score == 4:
                print("\nYou win!\n")
                break


def main():
    """
    The main program function. generates boards and ships for 
    all players and the starts the main game loop.
    """

    player_board = PlayerBoard("player", generate_ships(), generate_board(), 0)

    cpu_board = PlayerBoard("CPU", generate_ships(), generate_board(), 0)

    player_board.add_ships()

    main_game_loop(player_board, cpu_board)


main()