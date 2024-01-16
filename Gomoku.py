# ライブラリの読み込み
import numpy as np
import random
import os
import platform
import datetime

# 定数
TARGET = 4
BOARD_SIZE = TARGET * 4 - 5
PLAYER = "ME"
COMPUTER = "PC"
EMPTY = "  "
F_AROUND = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
S_AROUND = [[-2, -2], [-2, 0], [-2, 2], [0, 2], [2, 2], [2, 0], [2, -2], [0, -2]]
OS = platform.system()
if OS == "Windows":
  CLEAR = "cls"
else:
  CLEAR = "clear"

# 変数
board = []
logs = [["", ""], ["", ""], ["", ""]]

# ログ追加関数
def add_log(message):
  global logs
  now = datetime.datetime.now()
  logs.append(["[" + now.strftime("%H:%M:%S.%f") + "]", message])

def show_log():
  global logs
  print("==================== Logs ====================")
  for log in range(-3, 0):
    print(logs[log][0] + " " + logs[log][1])
  print("==============================================")
  print()

# 初期化関数
def init():
  global board
  add_log("プログラムを開始しました。")
  for _ in range(BOARD_SIZE):
    box = []
    for _ in range(BOARD_SIZE):
      box.append(EMPTY)
    board.append(box)
  show()

# 表示関数
def show():
  global board
  os.system(CLEAR)
  show_log()
  print("    ", end="")
  for i in range(BOARD_SIZE):
    print("{:>2} ".format(i + 1), end="")
  print()
  for row in range(BOARD_SIZE):
    print("{:>2}".format(row + 1) + " |", end="")
    for column in range(BOARD_SIZE):
      print(board[row][column] + "|", end="")
    print()

# 重複削除
def unique(lists):
  unique_list = []
  return [x for x in lists if x not in unique_list and not unique_list.append(x)]

# COMPUTERの選択関数
def computer_select():
  global board
  board_rotate = board.copy()
  place = []
  for i in range(2):
    for row in range(len(board_rotate)):
      for column in range(len(board_rotate[row]) - TARGET + 1):
        box = []
        for l in range(TARGET):
          if column + l < BOARD_SIZE:
            box.append(board_rotate[row][column + l])
        if box.count(PLAYER) >= 2 and box.count(EMPTY) >= 1 and box.count(COMPUTER) == 0:
          for l in range(len(box)):
            if box[l] == EMPTY:
              if i == 0:
                place.append([row, column + l])
              else:
                place.append([column + l, row])
    board_rotate = np.array(board).T.tolist()
  for i in range(2):
    for row in range(len(board_rotate) - TARGET + 1):
      for column in range(len(board_rotate) - TARGET + 1):
        box = []
        for l in range(TARGET):
          if column + l < BOARD_SIZE and row + l < BOARD_SIZE:
            box.append(board_rotate[row + l][column + l])
        if box.count(PLAYER) >= 2 and box.count(EMPTY) >= 1 and box.count(COMPUTER) == 0:
          for l in range(len(box)):
            if box[l] == EMPTY:
              if i == 0:
                place.append([row + l, column + l])
              else:
                place.append([column + l, row + l])
    board_swap = []
    for row in range(len(board)):
      board_swap.append(board[-1-row])
    board_rotate = np.array(board_swap).T.tolist()
  place_list = unique(place)
  for list in place_list:
    if board[list[0]][list[1]] != EMPTY:
      place_list.remove(list)
  if len(place_list) == 0:
    count = 0
    com_place = []
    for b_row in range(len(board)):
      for b_column in range(len(board[b_row])):
        if board[b_row][b_column] == COMPUTER:
          count += 1
          com_place.append([b_row, b_column])
    if count != 0:
      for i in com_place:
        now_check = i
        for l in range(len(F_AROUND)):
          if board[now_check[0] + F_AROUND[l][0]][now_check[1] + F_AROUND[l][1]] == EMPTY:
            row = now_check[0] + F_AROUND[l][0]
            column = now_check[1] + F_AROUND[l][1]
            add_log(COMPUTER + "が" + str(row + 1) + "行" + str(column + 1) + "列に置きました。")
            return add(row, column, COMPUTER)
    while 1:
      row = random.randint(2, BOARD_SIZE - 3)
      column = random.randint(2, BOARD_SIZE - 3)
      if board[row][column] == EMPTY:
        break
  else:
      row = place_list[0][0]
      column = place_list[0][1]
  add_log(COMPUTER + "が" + str(row + 1) + "行" + str(column + 1) + "列に置きました。")
  return add(row, column, COMPUTER)

# プレーヤーの選択関数
def player_select():
  while 1:
    print()
    key_input = input("行・列の順に数値を空白区切りで入力してください。\n")
    if key_input == "exit":
      exit()
    key_input = key_input.split(' ')
    if len(key_input) == 2 and key_input[0].isdigit() and key_input[1].isdigit():
      row = int(key_input[0]) - 1
      column = int(key_input[1]) - 1
      if row >= 0 and row < BOARD_SIZE and \
        column >= 0 and column < BOARD_SIZE and \
        board[row][column] == EMPTY:
        break
    else:
      print("入力内容が正しくありません。入力をやり直してください。")
  add_log(PLAYER + "が" + str(row + 1) + "行" + str(column + 1) + "列に置きました。")
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
    board_rotate = np.array(board).T.tolist()
  for i in range(2):
    for row in range(len(board_rotate) - TARGET + 1):
      for column in range(len(board_rotate) - TARGET + 1):
        box = []
        for i in range(TARGET):
          box.append(board_rotate[row + i][column + i])
        if box.count(PLAYER) == TARGET:
          return PLAYER
        elif box.count(COMPUTER) == TARGET:
          return COMPUTER
    board_swap = []
    for row in range(len(board)):
      board_swap.append(board[-1-row])
    board_rotate = np.array(board_swap).T.tolist()
  return None

# メイン関数
def main():
  global board
  init()
  while judge(board) == None:
    player_select()
    show()
    computer_select()
    show()
  add_log(judge(board) + "が勝利しました。")
  add_log("プログラムを終了します。")
  show()

main()