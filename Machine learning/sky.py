import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

music_data = pd.read_csv("baseData.csv")
# print(music_data)

x = music_data.drop(columns=['genre'])
y = music_data['genre']

x_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
print(X_test)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

prediction = model.predict(X_test)

# predition_value = model.predict([[21,1]])

# so this saves our model in the file music-reccomender
joblib.dump(model,"music-reccomender.joblib")

model = joblib.load("music-reccomender.joblib")
predition_value = model.predict([[21,1]])
print(predition_value)
#
# score = accuracy_score(y_test,prediction)
#
#
# print(score)
