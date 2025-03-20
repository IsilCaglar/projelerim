from game import Game
from mcts import Node
print("hello")
def human_move(game):
    game.print_board()
    print("x oyuncusu ")
    while True:
        row_input = (input("Satir giriniz: [0,1,2]: "))
        col_input = (input("Sutun giriniz: [0,1,2]: "))
        if not row_input or not col_input:
            print("deger girilmedi")
            continue
        try:
            row= int(row_input)
            col = int(col_input)
            action = (row, col)
            if action in game.bos_hucre_tespiti():
                return action
            else:
                print("bu hucre dolu")
        except ValueError:
            print("gecersiz deger")
        
def mcts_move(game, simulations=500):
    root = Node(game)
    for _ in range(simulations):
        node = root
        # 1.selecction
        while not node.game.is_terminal() and node.tamamen_expanded():
            node = node.best_child()
        
        # 2.expansion
        if not node.game.is_terminal():
            node = node.expand()

        # 3.simulation
        result = node.rollout()

        # 4.backpropagation
        node.backpropagate(result)
    return root.best_child(c_param=0).game
    #en iyi cocugu seçip oyunu döndürür

def main(): 
    game = Game(player='X')
    while not game.is_terminal():
        if game.player =='X' :
            move = human_move(game)
            game = game.hamle(move)
        else :
            game =mcts_move(game, simulations=250)
            #daha hızlı oynaması için 250 yaptım
    game.print_board()
    kazanan = game.winner()
    if kazanan == 'X':
        print("Kazandiniz")
    elif kazanan == 'O':
        print("Kaybettiniz.") #yapa zeka kazandı
    else:
        print("Oyun berabere.")
if __name__ == "__main__":
    main()