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

            ship_row = random.randint(0, 4)
            ship_column = random.randint(0, 4)
            ship = [ship_row, ship_column]
            self.ships.append(ship)

    def generate_board(self):
        """ 
        Generates an empty player board
        """

        column = [".",".",".","."]
        
        for index in range(4):
            self.board.append(column)
    




player_board = PlayerBoard("player")
player_board.generate_ships()
player_board.generate_board()
print(player_board.ships)
print(player_board.board)


