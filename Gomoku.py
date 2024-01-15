# ライブラリの読み込み
import numpy as np
import random

# 定数
TARGET = 4
BOARD_SIZE = TARGET * 4 - 5
PLAYER = "ME"
COMPUTER = "PC"

# 変数
board = []

# 初期化関数
def init():
  global board
  for _ in range(BOARD_SIZE):
    box = []
    for _ in range(BOARD_SIZE):
      box.append("  ")
    board.append(box)
  show()

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

def computer_select():
  global board
  board_rotate = board.copy()
  flag = True
  for i in range(2):
    if flag == True:
      for row in range(len(board_rotate)):
        for column in range(len(board_rotate[row]) - TARGET + 1):
          box = []
          for l in range(TARGET):
            box.append(board_rotate[row][column + l])
          if box.count(PLAYER) >= TARGET - 2 and box.count(COMPUTER) == 0 or \
            box.count(PLAYER) == 0 and box.count(COMPUTER) >= TARGET - 2:
            print("Hi")
            for k in range(TARGET):
              if board_rotate[row][column + k] == "  ":
                s_row = row
                s_column = column + k
                flag = False
                break
    if flag == True:
      for row in range(len(board_rotate) - TARGET + 1):
        for column in range(len(board_rotate) - TARGET + 1):
          box = []
          for l in range(TARGET):
            box.append(board_rotate[row + l][column + l])
          if box.count(PLAYER) >= TARGET - 2 and box.count(COMPUTER) == 0 or \
            box.count(PLAYER) == 0 and box.count(COMPUTER) >= TARGET - 2:
            for k in range(TARGET):
              if board_rotate[row + k][column + k] == "  ":
                s_row = row + k
                s_column = column + k
                flag = False
                break
    board_rotate = np.array(board).T.tolist()
    if i == 1:
      i = 2
  print(i)
  if i == 0:
    return add(s_row, s_column, COMPUTER)
  elif i == 1:
    return add(s_column, s_row, COMPUTER)
  else:
    while 1:
      s_row = random.randint(0, BOARD_SIZE - 1)
      s_column = random.randint(0, BOARD_SIZE - 1)
      if board[s_row][s_column] == "  ":
        break
    return add(s_row, s_column, COMPUTER)

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
  return add(row, column, PLAYER)

def add(row, column, who):
  global board
  if board[row][column] == "  ":
    board[row][column] = who
  return judge(board)

def judge(board_rotate):
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
  global board
  init()
  while judge(board) == None:
    player_select()
    computer_select()
    show()
  print(judge(board) + "の勝利！")

main()