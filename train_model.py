import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("dataset/marks.csv")
X = df[['Hours']]
y = df['Marks']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))