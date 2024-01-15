# ライブラリの読み込み
import shutil
import datetime
import numpy as np

# 定数
TARGET = 4
BOARD_SIZE = TARGET * 4 - 5
PLAYER = "YO"
COMPUTER = "CP"

# 変数
board = []
logs = []

# 初期化関数
def init():
  global board
  terminal_size = shutil.get_terminal_size()
  log("Game Start")
  box = []
  for _ in range(BOARD_SIZE):
    box.append("  ")
  for _ in range(BOARD_SIZE):
    board.append(box)

def log(message):
  global logs
  now = datetime.datetime.now()
  logs.append("[" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "] " + message)

def show():
  global board
  print("    ", end="")
  for i in range(BOARD_SIZE):
    print("{:>2} ".format(i + 1), end="")
  print()
  for row in range(BOARD_SIZE):
    print("{:>2}".format(row + 1) + " |", end="")
    for column in range(BOARD_SIZE):
      print(board[row][column] + "|", end="")
    print()

def player_select():
  while 1:
    key = input("行・列の順に数値を空白区切りで入力してください。\n").split(" ")
    input = {"row": int(key[0]), "column": int(key[1])}
    if input["row"] > 0 and input["row"] <= BOARD_SIZE and \
      input["column"] > 0 and input["column"] <= BOARD_SIZE and \
      board[input["row"]][input["column"]] == "  ":
      break
    else:
      print("入力内容が正しくありません。入力をやり直してください。")
  add(input["row"], input["column"], PLAYER)
  result = judge()
  return result

def add(row, column, player):
  global board
  board[row][column] = player

def judge():
  global board
  board_rotate = board
  for i in range(2):
    for row in board_rotate:
      for column in range(len(row) - TARGET + 1):
        box = []
        for i in range(TARGET):
          box.append(row[column + i])
        if box.count(PLAYER) == TARGET:
          return PLAYER
        elif box.count(COMPUTER) == TARGET:
          return COMPUTER
    for row in range(len(board_rotate) - TARGET + 1):
      for column in range(len(board_rotate) - TARGET + 1):
        box = []
        for i in range(TARGET):
          box.append(board_rotate[row + i][column + i])
        if box.count(PLAYER) == TARGET:
          return PLAYER
        elif box.count(COMPUTER) == TARGET:
          return COMPUTER
    board_rotate = np.array(board).T.tolist()
  return None

def main():
  init()
  result = judge()
  while result == None:
    player_select()
    show

main()