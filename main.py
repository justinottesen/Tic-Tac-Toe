import random
import time

DEPTH = 9
minimax_dict = dict()

def print_board(board: list[str]) -> None:
  print("   |   |   ")
  print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")
  print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")
  print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
  print("   |   |   ")

def check_board_full(board: list[str]) -> bool:
  return (" " not in board)

def set_of_threes(board: list[str]) -> set[tuple[str]]:
  threes = set()
  for i in range(1, 8, 3):
    threes.add(tuple(board[i:i+3]))
  for i in range(1, 4):
    threes.add(tuple(board[i:i+7:3]))
  threes.add(tuple(board[1::4]))
  threes.add(tuple(board[3:8:2]))
  return threes

def check_state(board: list[str]) -> str:
  """
  Return Values:
  " " - Game still going
  "X" - X wins
  "O" - O wins
  "Tie" - Tie
  """
  threes = set_of_threes(board)
  if ("X","X","X") in threes:
    return "X"
  if ("O","O","O") in threes:
    return "O"
  if check_board_full(board):
    return "Tie"
  return " "

def next_turn(x: str) -> str:
  if (x == "X"):
    return "O"
  return "X"

def get_open(board: list[str]) -> list[int]:
  return [i for (i, x) in enumerate(board) if x == " "]

def minimax(board: list[str], depth: int) -> tuple[int, int]:
  # Returns in format (choice, score)
  #   Score Format: 1 - X, 0 - Tie, -1 - O
  state = check_state(board)
  if (state == "X"):
    return (0, 1)
  if (state == "O"):
    return (0, -1)
  if (state == "Tie"):
    return (0, 0)

  if "".join(board) in minimax_dict:
    return minimax_dict["".join(board)]
  
  best_res = (0, 0)
  for i in get_open(board):
    if depth == 0:
      return (i ,0)
    board[i] = board[0]
    board[0] = next_turn(board[0])
    res = minimax(board, depth-1)
    board[0] = next_turn(board[0])
    board[i] = " "
    if best_res[0] == 0 or \
       board[0] == "X" and res[1] > best_res[1] or \
       board[0] == "O" and res[1] < best_res[1]:
      best_res = (i, res[1])
      if board[0] == "X" and best_res[1] == 1 or \
         board[0] == "O" and best_res[1] == -1:
        break
  
  minimax_dict["".join(board)] = best_res
  return best_res

def simulate(rounds: int) -> None:
  # 0 - mmax wins, 1 - ties, 2 - random wins
  results = [0, 0, 0]
  pct = 10
  tmp = rounds/10
  start = time.time()
  for game in range(1,rounds+1):
    board = [" " for _ in range(10)]
    board[0] = "X"

    if game % 2 == 1:
      mmax = "X"
      rand = "O"
    else:
      mmax = "O"
      rand = "X"

    state = " "
    while state == " ":
      if (board[0] == mmax):
        choice = minimax(board, DEPTH)[0]
      else:
        choice = random.choice(get_open(board))
      
      board[choice] = board[0]
      state = check_state(board)
      board[0] = next_turn(board[0])
    
    if state == mmax:
      results[0] += 1
    elif state == rand:
      results[2] += 1
    else:
      results[1] += 1
    
    if (game >= tmp):
      print(f"Game: {str(game).rjust(len(str(rounds)))} | {pct:3}% done | {time.time()-start:10.3f} seconds")
      pct += 10
      tmp += rounds/10
  
  end = time.time()
  print(f"Minimax Wins: {results[0]} ({100*results[0]/rounds:.3f}%) | Ties: {results[1]} ({100*results[1]/rounds:.3f}%) | Random Wins: {results[2]} ({100*results[2]/rounds:.3f}%)")
  print(f"Total Time: {end - start:.3f} ({1000000*(end-start)/rounds:.3f}us per game)")

def play_against() -> None:

  print("Use the number keys to choose where to go:")
  print("   |   |   ")
  print(" 1 | 2 | 3 ")
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")
  print(" 4 | 5 | 6 ")
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")
  print(" 7 | 8 | 9 ")
  print("   |   |   ")

  # Board uses 1-based indexing for easier I/O
  # Zero index represents the current turn
  board = [" " for _ in range(10)]
  board[0] = "X"

  player = input("Will you be X or O? (X goes first) ").strip()

  state = " "
  while (state == " "):
    if (board[0] == player):
      print_board(board)

      choice = int(input().strip())
      while choice not in get_open(board):
        print("Invalid Choice")
        print_board(board)
        choice = int(input().strip())      
    else:
      choice = minimax(board, DEPTH)[0]
  
    board[choice] = board[0]
    state = check_state(board)
    board[0] = next_turn(board[0])
  
  print_board(board)
  print(state)

if __name__ == "__main__":
  while True:
    print("==============================================")
    print("Choose a gamemode:")
    print("P: Play Against Bot")
    print("S: Simulate (Minimax vs Random Choice)")
    print("Q: Quit")
    gamemode = input().strip().upper()
    if (gamemode == "Q"):
      break
    elif (gamemode == "P"):
      play_against()
    elif (gamemode == "S"):
      while True:
        rounds = input("How many rounds to simulate? ").strip()
        if rounds.isnumeric():
          break
        else:
          print("Not a valid number")
      rounds = int(rounds)
      simulate(rounds)
    if (input("Press Y to play again: ").upper().strip() != "Y"):
      break