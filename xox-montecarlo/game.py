import numpy as np
import copy
class Game:
  def __init__(self, board = None, player = 'X'):
    #eğer board yoksa, 3x3 lük boş bir board oluşturucaz.
    if board is None :
      self.board = [[' ' for _ in range(3)]for _ in range(3)]
      # iç içe for lu comprehension
    else:
      self.board = board

    self.player = player

  def bos_hucre_tespiti(self):
    bos_hucre = []
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == ' ':
          bos_hucre.append((i,j))
    return bos_hucre

  def hamle(self, action):
    #hamle yaptıktan sonra oyuncu değişicek ve o oyuncuyu Game e göndercex.
    #tabloyu da güncellicez onu da Game classına gönderecez
    #ama terminal oldu mu - kazanan oldu mu
    i, j = action
    #action parametresi fonksiyonun çağırıldığı yerden geliyor.
    new_board = copy.deepcopy(self.board) #orijinal tahtayı kopyaladık
    #ama deeopcopy yaptıgımıziçin, yaptıgımız değişiklik sonrası orijinal thta aynı kalacak.
    new_board[i][j] = self.player # X ya da O hamlesi uygulanıyor.
    if self.player == 'X':
      next_player = 'O'
    else :
      next_player = 'X'
      
    
    return Game(new_board, next_player)

  #def is_terminal(self):
    #eger termianl olduysa kazanan var mı diye kontrole gidecek
    #def is_terminal(self):
        #return len(self.bos_hucre_tespiti()) == 0 or self.winner() is not None
  def is_terminal(self):
    win = self.winner()
    full = not any(' ' in row for row in self.board)
    #if win or full:
        #print("winner:", win, "Full:", full)
    return win is not None or full

    # bu fonksiyonu oynanış sırasında çağırcam:monte carlo ve playgame de

  def winner(self):
  # [[x x x]
  #  [o x o]
  #  [x o x]]
  #yatay, dikey, solcapraz ve sag caprazda aynı karakter kontrolü yapacagız.
    board = np.array(self.board)
    #for row in board :
      #ayni_mi = True
      #for item in row :
        #if item != row[0] or item == ' ' :
          #ayni_mi = False
          #break
      #if ayni_mi:
        #return row[0]

      # Yatay satır kontrolü
    for row in board:
        if row[0] != ' ' and all(item == row[0] for item in row):
            return row[0]
    for col in board.T:  # board.T ile transpoze
        if col[0] != ' ' and all(item == col[0] for item in col):
            return col[0]


        #sol üst capraz 00-11-22
    if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(3)):
      return board[0][0]

        #sag cpraz 02-11-20
    if board[0][2] != ' ' and all(board[i][2 - i] == board[0][2] for i in range(3)):
      return board[0][2]
    return None #eğer kazanan yoksa

  def print_board(self):
    for row in self.board:
      # | x| x|x
      # -----
      # |o |o |
      # -----
      # | | |
      # -----
      print('| '+'| '.join(row))
      print('-'*5)

