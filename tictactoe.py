##
##


def main():
    won = False
    # initial values for blank board
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # create list of players
    players = get_player_info()
    # verify ready, maybe explain rules
    input("{}, you are {}.\n{}, you are {}.\nPress ENTER to begin playing."
          .format(players[0].name, players[0].x_or_o, players[1].name, players[1].x_or_o))
    # loop to play game until it is won
    while not won:
        # iterate through the player object list, giving each player 1 turn per round
        for player in players:
            print_board(board)
            selection = get_selection(board, player)
            board = place_marker(board, player.x_or_o, (selection-1))
            won = check_for_win(board)
            clear_screen()
            # check to see if that was a winning move
            if won:
                print_board(board)
                print("{} WINS!".format(player.name))
                break
            # if nobody won, check to see if the board is full
            elif board_is_full(board):
                print("TIE GAME!")
                break


# get position selection from player. will not allow selection if position is used or not a valid selection
def get_selection(board, player):
    selection = 0
    print(board)
    while selection not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or spot_taken(board, selection) is True:
            selection = int(input("{}, what is your move?".format(player.name)))

    return selection


# if all positions on the board contain an x or and o, this will return true
def board_is_full(board):
    markers_found = 0
    # iterate through all 9 positions
    for x in board:
        # check to see if value is a number
        if x == "x" or x == "o":
            # x or o is found, increment markers found by 1
            markers_found += 1
    # return true if count reaches 9
    return markers_found >= 9


def spot_taken(board, selection):
    value_at_selection = board[selection - 1]
    print("That spot already has an {} in it.".format(value_at_selection))
    return value_at_selection == "x" or value_at_selection == "o"


# places marker on board at specified location. returns new board
def place_marker(board, marker, placement):
    # enforce all markers as lowercase
    board[placement] = marker
    return board


def print_board(board):
    print("   |   |   ")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("   |   |   ")


# get player info for both players and return player objects to player list
def get_player_info():
    # create empty player object list
    players = ["", ""]
    x_or_o = ""
    for index, user in enumerate(players):
        player_number = int(index) + 1
        name = input("Player {}, what is your name?".format(player_number))
        # only player 1 will get to choose their marker
        if index == 0:
            # loop until input is either x or o
            while x_or_o != "x" and x_or_o != "o":
                x_or_o = input("Player {}, you like to be X or O?".format(player_number))
                x_or_o = x_or_o.lower()
        else:
            # default player 2 to opposite marker of player 1
            if players[0].x_or_o.lower() == "x":
                x_or_o = "o"
            else:
                x_or_o = "x"
            print("Player {}, {} is using {}, so you will be {}"
                  .format(name, players[0].name, players[0].x_or_o, x_or_o))
        print("saved name {} to index location {} for player {}".format(name, index, player_number))
        players[index] = Player(name, x_or_o)
    return players


def clear_screen():
    print("\n" * 100)


# checks board list for win after each turn is played
def check_for_win(board):
    # horizontal checks
    if board[0] == board[1] == board[2]:
        found_winner = True
    elif board[3] == board[4] == board[5]:
        found_winner = True
    elif board[6] == board[7] == board[8]:
        found_winner = True
    # vertical checks
    elif board[0] == board[3] == board[6]:
        found_winner = True
    elif board[1] == board[4] == board[7]:
        found_winner = True
    elif board[2] == board[5] == board[8]:
        found_winner = True
    # diagonal checks
    elif board[0] == board[4] == board[8]:
        found_winner = True
    elif board[2] == board[4] == board[6]:
        found_winner = True
    else:
        found_winner = False
    # return the result
    return found_winner


# common base class for all players
class Player:
    # initial values for default player object
    def __init__(self, name, x_or_o):
        self.name = name
        self.x_or_o = x_or_o


main()

exit()
