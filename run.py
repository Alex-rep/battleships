import random

class PlayerBoard: 

    player_name = ""
    score = 0
    board = []
    ships = []

    def __init__(self, name):
        """
        Constructs the object and inserts the board owner's name
        """

        self.player_name = name
    
    def generate_ships(self):
        """ 
        Generates four couples of integers between 0 and 4 that
        represent the coordinates for the player's ships
        """
        for index in range(4):

            ship_row = index
            ship_column = random.randint(0, 3)
            ship = [ship_row, ship_column]
            self.ships.append(ship)

    def generate_board(self):
        """ 
        Generates an empty player board
        """

        column = [".", ".", ".", "."]
        
        for index in range(4):
            new_col = column.copy()
            self.board.append(new_col)
    
    def add_ships(self):
        """ 
        Adds the symbols for ships to the player board
        """
        for index in range(4):  
            row = self.ships[index][0]
            column = self.ships[index][1]
            self.board[row][column] = "@"
           
def roll_guess(): 
    """ 
    Generates a couple of integers, guesses
    a position on the board
    """

    row = random.randint(0, 3)
    column = random.randint(0.3)
    result = [row, column]
    return result


player_board = PlayerBoard("player")
player_board.generate_ships()
player_board.generate_board()
player_board.add_ships()
print(player_board.ships)
for index in range(4):
    print(player_board.board[index])
    print("\n")


