#py -m pip install scipy
#py -m pip install scikit-learn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()
print(iris.data)
print(iris.target)
print(iris.target_names)

knn = KNeighborsClassifier(n_neighbors=1)
X= iris.data
Y= iris.target

print(knn.fit(X,Y))
print("*****************************************")
print("Prediction", knn.predict( [ [5.1, 3.5, 1.4, 0.2], [5.9, 3, 5.1,1.8] ] ))

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 0.4, random_state=42)

print(X_train.shape)
print(X_test.shape)

knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(predictions)

performance = metrics.accuracy_score(y_test, predictions)
print(performance)