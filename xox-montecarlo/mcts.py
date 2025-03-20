from game import Game
import copy
import random
class Node:
  def __init__(self, game, parent = None):
    self.game = game #node un temsil ettiği oyundurumu
    self.parent = parent #bir üsteki oyun durumu : node un parentı
    self.children = [] #yapılmış hamleler sonucu oluan oyun durumları
    self.wins = 0 #bu node da kazanılan oyun - back propagation sonucu dolacak
    self.visits = 0 #bu dugum kac kez ziyaret edildi - simülasyon sayısı
    self.denenmemis_hamle = game.bos_hucre_tespiti()


  def expand(self):
  #henuz denenmemiş hamleyi alır ve buhamleyi uygular.
  #sonra agacta yeni bir child node oluşturur
    action = self.denenmemis_hamle.pop() #denenmemis hamlelerden bir hamle secer ve listeden cıkarıo

    next_game = self.game.hamle(action)
    #secilen hamleyi uygula ve yeni bir node üret ve yeni board ı günceller game den dolayı

    child_node = Node(next_game, parent = self)
    #burada recursive var
    self.children.append(child_node)
    #yeni oyun durumu için bir noe oluşturur ve bu node u childrena ekler

    return child_node
    #yeni node u döndürür

  def tamamen_expanded(self):
  #eger tüm hamleler denendiyse, o node tamamen genişletilmiştir
    return len(self.denenmemis_hamle) == 0
    #eger denenmemis hamle yoksa true donecek

  def best_child(self, c_param=1.4):
  # UCT upper confidence bound formulu ile en iyi cocuk secilir
    import math
    return max(
        self.children,
        key = lambda child :(child.wins / child.visits) +
        c_param * math.sqrt(math.log(self.visits)/child.visits)
    ) #uct formulu exploration(keşif) + exploitation(kullanım) dengesini kurar

  def backpropagate(self,result):
  #simülasyon kazandıgını ya da kaybettigini bu bilgiyi ust node lara yayar
    self.visits += 1
    self.wins += result #bu node için simülasyon sonucunu günceller

    if self.parent :
      self.parent.backpropagate(result)
      #eger parenti varsa ona da sonucu geri yayılım

  def rollout(self):
  # su anki oyun durumundan, restagele oynayarak sonuca kadar gitmek
    current_game = copy.deepcopy(self.game)

    # oyun sona erene kadar rastgele hamle yap
    while not current_game.is_terminal():
      actions = current_game.bos_hucre_tespiti()
      
      action = random.choice(actions)
      current_game = current_game.hamle(action)

    #sonucun kime ait oldugunu kontrol etme
    winner = current_game.winner()
    if winner == self.game.player :
      return 1
    elif winner is None :
      return 0.5
    else :
      return 0
    #buaradaki self.game.player oyun başında hamleyi yapan oyuncuyu temsil ediyor
  