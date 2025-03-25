# Korelasyon Analizi- Sklearn Decision Tree Diagnosis Tahmini Projesi
- Korelasyon iki değişken arasındaki doğrusal ilişkiyi ölçen doğrusal bir değerdir.
- Yüksek korelasyona sahip değişkenler tekrarlı bilgi içerir. bu durum : modeli karmaşıklaştırır ve aşırı öğrenmeye sebep olabilir. Bu nedenle yüksek korelasyonlu değişkenlerden bazılarını çıkarmak gerekebilir.



### Açıklama
#### `main.py  `
- `corr = num_data.corr()` : korelasyon sonuçlarını hesaplar. elde edilen sonuç kare matristir.
- `heatmap` : ısı haaritasında kırmızı negatif korelasyon, mavi pozitif korelasyon, beyaz-gri korelasyon az ya da yok anlamına gelir.
- `cor_matrix = num_data.corr().abs()` : işaret önemli değil yani pozitif ya da negatif korelasyon olduğu önemli değil. güçlü ilişki oluğ olmadığına bakıyoruz.
- `upper_triangle=cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(bool))` : `np.triu` matrisin sadece üst üçgenini alıyor. çünkü matris simetr,k olduğu için tekrar bilgiye gerek yok. `where()`alt üçgeni ve köşegeni NaN yapıyor.
- `silinecek=[col for col in upper_triangle.columns if any(upper_triangle[col]>0.9)]` : `if any(upper_triangle[col]>0.9)]` burada korelasyonu 0.9 dan büyük olan değişkenleri tespit eder ve `silinecek` listesine ekler.
- `silinmis_data=num_data.drop(columns = silinecek)` : yüksek korelasyonlu sütünlar veri setinden çıkarılıyor.
#### `model.py  `
- `x` : bağımsız değişkenler(features)
- `y` : hedef değişken (diagnosis)



## Gereksinimler
- Python 3.x
- Pandas, Matplotlib, Seaborn gibi kütüphaneler

### Örnek VeriSeti
https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data