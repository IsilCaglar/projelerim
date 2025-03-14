import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',500)

data = pd.read_csv('data.csv')

data.head()
print(data.dtypes)
#kullandığım verisetindeki id ve unnamed: NaN columnları sileceğim.
data = data.drop(['id', 'Unnamed: 32'], axis = 1)
print(data)

######################################################
#sayısal columnları sececegim
num_data = data.select_dtypes(include = ['int64','float64'])
print(num_data)

######################################################
corr = num_data.corr()
print(corr)
# 0'a yaklasmak ve korelasyon ters orantilidir.
# 1 ve -1'e yaklastıkca korelasyon yüksektir.
# birbiriyle yüksek korelasyonda olan degiskenlerin bulunmamasını isteriz
# cunku birbirleriyle aynı seyleri ifade ederler.

######################################################
#ısı haritası
plt.figure(figsize=(12, 12))
sns.heatmap(corr, cmap="RdBu")
plt.show()


######################################################
######################################################
cor_matrix = num_data.corr().abs() #1 ve -1 önemsiz. mutlak değerinialdık
#korelasyon matrisinin simetrik olusundan dolayı aynı bilgiyi 2 kez tutuyor.
#bu yuzden ust ucgen ya da alt ucgeni almamız yeterli
#np.ones numpyla ile yeni bir boş 1 lerdn olusan matris yapacagız.
#np.triu(.. k=1) = k nın 1 olması üst ücgeni al ama kosegeni alma demek. zaten kosegen kendisi.
#astype(bool): burada 1 leri true, 0 ları false yapıcak
#cor_matrix.where()=true olan üst ucgeni tutar, kalan false yerleri NaN yapıyor
upper_triangle = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(bool))
print(upper_triangle)


######################################################
######################################################
#yüksek korelasyonlu degiskenlerin silinmesi yani yoğun maviler
silinecek = [col for col in upper_triangle.columns if any(upper_triangle[col]>0.9)]
silinmis_data = num_data.drop(columns = silinecek)

######################################################
print(f"silenen sutunlar:{silinecek}")
print(f"kalan sutunlar: {silinmis_data}")

######################################################
#ısı haritası
plt.figure(figsize=(12, 12))
sns.heatmap(silinmis_data, cmap="RdBu")
plt.show()