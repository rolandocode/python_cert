#py -m pip install scipy
#py -m pip install scikit-learn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
print(iris.data)
print(iris.target)
print(iris.target_names)

k_values = {}
k = 1

while k <= 25:
    knn = KNeighborsClassifier(n_neighbors=k)
    X= iris.data
    Y= iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 0.4, random_state=42)
    knn.fit(X_train, y_train)

    predictions = knn.predict(X_test)
    performance = metrics.accuracy_score(y_test, predictions)
    k_values[k] = round(performance,4)
    k = k+1

print(k_values)

# plt.plot(k_values.keys(), k_values.values())
# plt.xlabel("Value of k")
# plt.ylabel("Performance ")

# plt.show()

from sklearn.linear_model import LogisticRegression
X= iris.data
Y= iris.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 0.4, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print("**************LINEAR MODEL**************")
print (logreg.predict_proba([[6.2,3.4,5.4,2.3]]))

predictions_logreg = logreg.predict(X_test)
performance_logreg =  metrics.accuracy_score(y_test, predictions_logreg)

print(performance_logreg)
