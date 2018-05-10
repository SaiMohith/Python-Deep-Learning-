from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df = load_iris()
predictor = df.data
response = df.target
pred_train, pred_test, resp_train, resp_test = train_test_split(predictor, response)

acc_scores = []

for k in range(1, 51):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(pred_train, resp_train)
    resp_pred=knn.predict(pred_test)
    a = metrics.accuracy_score(resp_test, resp_pred)
    acc_scores.append(a)
    print("Accuracy when k = ", k, ": ", a)


plt.plot(k_values, acc_scores)
plt.xlabel("k")
plt.ylabel("accuracy")
plt.show()