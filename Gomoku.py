# ライブラリの読み込み
import numpy as np
import random

# 定数
TARGET = 4
BOARD_SIZE = TARGET * 4 - 5
PLAYER = "ME"
COMPUTER = "PC"
EMPTY = "  "

# 変数
board = []

# 初期化関数
def init():
  global board
  for _ in range(BOARD_SIZE):
    box = []
    for _ in range(BOARD_SIZE):
      box.append(EMPTY)
    board.append(box)
  show()

# 表示関数
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

# COMPUTERの選択関数
def computer_select():
  global board
  board_rotate = board.copy()
  place = []
  for i in range(2):
    for row in range(len(board_rotate)):
      for column in range(len(board_rotate[row]) - TARGET + 1):
        box = []
        for l in range(TARGET + 1):
          if column + l <= BOARD_SIZE:
            box.append(board_rotate[row][column + i])
        if box.count(PLAYER) >= 2 and box.count(EMPTY) >= 1:
          for l in range(len(box)):
            if box[l] == EMPTY:
              if i == 0:
                place.append([row, column + l])
              else:
                place.append([column + l, row])
    for row in range(len(board_rotate) - TARGET + 1):
      for column in range(len(board_rotate) - TARGET + 1):
        box = []
        for l in range(TARGET + 1):
          if column + l <= BOARD_SIZE and row + l <= BOARD_SIZE:
            box.append(board_rotate[row + i][column + i])
        if box.count(PLAYER) >= 2 and box.count(EMPTY) >= 1:
          for l in range(len(box)):
            if box[l] == EMPTY:
              if i == 0:
                place.append([row + l, column + l])
              else:
                place.append([column + l, row + l])
    board_rotate = np.array(board).T.tolist()
  print(place)

# プレーヤーの選択関数
def player_select():
  while 1:
    key_input = input("行・列の順に数値を空白区切りで入力してください。\n")
    key_input = key_input.split(' ')
    row = int(key_input[0]) - 1
    column = int(key_input[1]) - 1
    if row >= 0 and row < BOARD_SIZE and \
      column >= 0 and column < BOARD_SIZE and \
      board[row][column] == EMPTY:
      break
    else:
      print("入力内容が正しくありません。入力をやり直してください。")
  return add(row, column, PLAYER)

# 追加関数
def add(row, column, who):
  global board
  if board[row][column] == EMPTY:
    board[row][column] = who
  return judge(board)

# 勝敗判定
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

# メイン関数
def main():
  global board
  init()
  while judge(board) == None:
    player_select()
    computer_select()
    show()
  print(judge(board) + "の勝利！")

main()