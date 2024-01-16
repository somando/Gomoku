# ライブラリの読み込み
import numpy as np
import os
import random
import platform
import datetime

# 定数
TARGET = 4
BOARD_SIZE = TARGET * 4 - 5
PLAYER1 = "ME"
PLAYER2 = "YO"
NO_ZONE = "XX"
EMPTY = "  "
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

# ログ表示関数
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

# プレーヤーの選択関数
def player_select(player):
  while 1:
    print()
    key_input = input(player + "のターンです。行・列の順に数値を空白区切りで入力してください。\n")
    if key_input == "exit":
      print()
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
  add_log(player + "が" + str(row + 1) + "行" + str(column + 1) + "列に置きました。")
  return add(row, column, player)

# 置けない場所の選定関数
def no_zone():
  global board
  while 1:
    row = random.randint(2, BOARD_SIZE - 3)
    column = random.randint(2, BOARD_SIZE - 3)
    if board[row][column] == EMPTY:
      break
  add_log(str(row + 1) + "行" + str(column + 1) + "列が妨害されました。")
  add(row, column, NO_ZONE)

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
        if box.count(PLAYER1) == TARGET:
          return PLAYER1
        elif box.count(PLAYER2) == TARGET:
          return PLAYER2
    board_rotate = np.array(board).T.tolist()
  for i in range(2):
    for row in range(len(board_rotate) - TARGET + 1):
      for column in range(len(board_rotate) - TARGET + 1):
        box = []
        for i in range(TARGET):
          box.append(board_rotate[row + i][column + i])
        if box.count(PLAYER1) == TARGET:
          return PLAYER1
        elif box.count(PLAYER2) == TARGET:
          return PLAYER2
    board_swap = []
    for row in range(len(board)):
      board_swap.append(board[-1-row])
    board_rotate = np.array(board_swap).T.tolist()
  return None

# メイン関数
def main():
  global board
  init()
  while 1:
    player_select(PLAYER1)
    show()
    if judge(board) != None:
      break
    player_select(PLAYER2)
    show()
    if judge(board) != None:
      break
    no_zone()
    show()
  add_log(judge(board) + "が勝利しました。")
  add_log("プログラムを終了します。")
  show()

if __name__ == "__main__":
  main()