# XOX : MCTS yapay zekasına karşı insan oyuncusu
Oyuncu X, yapay zeka O olarak belirlenmiştir

## Temel Bileşenler

### `Game.py`
- Game __init__(self, board, player) class : oyun kuralları, board yönetimi ve aktif oyuncuyu tanımlama.
- `bos_hucre_tespiti(self)` : boş hücreleri [(i,j)] formatında listeler.
- `hamle(action)` : mcts den gelen actionı oynayan oyuncunun hamlesini yaparve sıradaki oyuncuya geçer.
- `is_terminal(self)` : oyun bitmiş mi, boş hücre kalmış mı kontrolü yapar.
- `winner(self)` : kazanan oyuncu varsa döndürür. Yatay, dikey, sol üst çapraz, sağ üst çaprazlarda hepsi aynı karakterler var mı kontrolünü yapar.
- `print_board()` : tahtayı terminale yazdırır.

### `mcts.py`
- Node __init__(self, game, parent) class : her düğüm oyun durumunu ve üst düğümünü içerir. 
- `expand(self)`: henüz denenmemiş bir hamleyi genişletir. Yeni bir alt düğüm oluşturur.
- `tamamen_expanded()` : tüm hamleler denendiyse true döner.
- `best_child(c_param = 1.4)` : UCT formülü ile en iyi cocugu seçer.
- `backpropagte(result)` : simülasyon sonucunu yukarıya doğru aktarır.
- `rollout()` : terminal durumuna kadar rastgele oynar, sonuç dündürür.

### main.py
- Kullanıcının ve yapay zekanın play game dosyası.
- Oyun burada başlar ve hamle buradan alınır.
- mcts algoritması belirlediği en iyi hamle ile oynar.

#### Kaynaklar
https://int8-io.translate.goog/monte-carlo-tree-search-beginners-guide/?_x_tr_sl=en&_x_tr_tl=tr&_x_tr_hl=tr&_x_tr_pto=tc