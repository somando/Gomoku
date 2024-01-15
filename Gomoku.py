# ライブラリの読み込み
import numpy as np

# 定数
TARGET = 4
BOARD_SIZE = TARGET * 4 - 5
PLAYER = "YO"
COMPUTER = "CP"

# 変数
board = []

# 初期化関数
def init():
  global board
  box = []
  for _ in range(BOARD_SIZE):
    box.append("  ")
  for _ in range(BOARD_SIZE):
    board.append(box)

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
    key_input = input("行・列の順に数値を空白区切りで入力してください。\n")
    key_input = key_input.split(' ')
    row = int(key_input[0]) - 1
    column = int(key_input[1]) - 1
    if row >= 0 and row < BOARD_SIZE and \
      column >= 0 and column < BOARD_SIZE and \
      board[row][column] == "  ":
      break
    else:
      print("入力内容が正しくありません。入力をやり直してください。")
  add(row, column, PLAYER)
  result = judge()
  return result

def add(row, column, who):
  global board
  board[row][column] = who

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
    show()
    player_select()
  print(result + "の勝利！")

main()