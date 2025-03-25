import pandas as pd
import numpy as np
from main import get_cleaned_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score




data = pd.read_csv('data.csv')
diagnosis = data[['diagnosis']]

final_data = get_cleaned_data()
final_data = pd.concat([diagnosis, final_data], axis = 1)

# y = diagnosis
# x = features
y = final_data[['diagnosis']]
x = final_data.drop(['diagnosis'], axis = 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42) 
tree = DecisionTreeClassifier()
model = tree.fit(x_train, y_train)
skor = model.score(x_test, y_test)
print(skor)


