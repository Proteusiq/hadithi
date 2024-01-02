from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from knn import KNN


iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.8, stratify=y, random_state=42)

k = len(set(y_train))
predictor = KNN(k)

predictor.fit(X_train, y_train)
y_pred = predictor.predict(X_test)

print(classification_report(y_true=y_test, y_pred=y_pred))
