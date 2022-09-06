import random

class PlayerBoard: 

    player_name = ""
    score = 0
    board = []
    ships = []

    def __init__(self, name, ship_list):
        """
        Constructs the object and inserts the board owner's name
        """

        self.player_name = name
        self.ships = ship_list
    

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
    column = random.randint(0.3)
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
    
    result = [int(row) - 1 , int(column) - 1]
    return result

def print_board(player_board):
    """ 
    Prints the board for the specified player
    """
    for index in range(4):
        print(player_board.board[index])
        print("\n")

player_board = PlayerBoard("player", generate_ships())
player_board.generate_board()

cpu_board = PlayerBoard("CPU", generate_ships())
cpu_board.generate_board()

player_board.add_ships()
cpu_board.add_ships()

print(player_board.ships)
print(cpu_board.ships)

#for index in range(4):

    #print("Player's board: \n")
    #print_board(player_board)
    #print("CPU's board: \n")
    #print_board(cpu_board)
    #print(cpu_board.ships)

    #guess = get_guess()

    #for index in range(4):
        
        #if guess[0] == cpu_board.ships[index][0] and guess[1] == cpu_board.ships[index][1]:
         #   print("It's a hit! \n")
          #  player_board.score += 1
           # break





