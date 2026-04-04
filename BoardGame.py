# Homework 3 - Board Game System
# Name: Riley Mayfield
# Date: 4/3/26
#Purpose: Organization and problem solving

import random


def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)


def turn(data):
    key, value = data[0].split(":")
    return value.strip() 


def splitBoard(data):
    board = {}
    for line in data:
        if ":" not in line:
            continue

        pos, item = line.split(":")

        if pos.strip().isdigit():
            board[int(pos.strip())] = item.strip()

    return board



def diceroll():
    roll=3
    #roll = random.randint(1,6)
    return roll


def movePlayer(data):
    roll = diceroll()
    print(f"\nYou rolled a {roll}\n")

    currentPlayer = turn(data)
    board = splitBoard(data)

    currentPos = None
    for pos, item in board.items():
        if item == currentPlayer:
            currentPos = pos
            break

    if currentPos is None:
        print(f"ERROR: {currentPlayer} not found on board.")
        return

    newPos = currentPos + roll

    # Trap check
    if newPos in board and board[newPos] == "Trap":
        print("\nLanded on a trap!")
        trap = drawTrap()
        print(f"Trap effect: {trap[1]}")

    # Update board
    del board[currentPos]
    board[newPos] = currentPlayer

    return board


    

def updateTurn(data):
    player = turn(data)
    if player == "Player1":
        data[0] = "Turn: Player2"


def drawCard():
    card = random.randint(1,3)
    if card == 1:
        description = "Roll 2 dice on a roll"
    elif card == 2:
        description = "Swap places with another player"
    else:
        description = "Prevent next trap space"

    return card, description


def drawTrap():
    card = random.randint(1,3)
    if card == 1:
        description = "Lose a life"
    elif card == 2:
        description = "Go back 20 spaces"
    else:
        description = "Lose next turn"

    return card, description



def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    displayGame(gameData)
    

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        board = movePlayer(gameData)
        for pos in sorted(board.keys()):
            print(f"{pos}:{board[pos]}")
        updateTurn(gameData)
    elif choice.lower() == "n":
        print(f"\nDrew a card\n")
        card = drawCard()
        print(card[1])
        

        


if __name__ == "__main__":
    main()
