# Import  Required LIbraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


# Function which performs SVC with kernel as linear
def lin_SVM(Xtr, ytr, Xte, yte):
    lin_cls = SVC(kernel='linear', random_state=10)  # setting Kernel to linear
    lin_cls.fit(Xtr, ytr)  # fitting the model
    y_pred = lin_cls.predict(Xte)  # predict the value using test data
    print('\nAccuracy when kernel is Linear: ', accuracy_score(yte, y_pred))  # print the Accuracy Score
    print('\nClassification Report for Linear Kernel: ')
    print(classification_report(yte, y_pred))  # print the Classification report


# function which performs SVC with kernel as rbf
def rbf_SVM(rXtr, rytr, rXte, ryte):
    rbf_cls = SVC(kernel='rbf', random_state=10)  # setting Kernel to rbf
    rbf_cls.fit(rXtr, rytr)
    y_pred = rbf_cls.predict(rXte)  # predict the value using test data
    print('\nAccuracy when Kernel is RBF: ', accuracy_score(ryte, y_pred))  # print the Accuracy Score
    print('\nClassification Report for RBF: ')
    print(classification_report(ryte, y_pred))  # print the Classification report


#Load Iris Data
df = load_iris()
predictor = df.data
response = df.target

# Split the test and train data. Here 20% of the data is test data
pred_train, pred_test, resp_train, resp_test = train_test_split(predictor, response, test_size = 0.20, random_state = 10)

# Feature Scaling for scaling the values
scale = StandardScaler()
pred_train = scale.fit_transform(pred_train)
pred_test = scale.transform(pred_test)

# Calling Functions
lin_SVM(pred_train, resp_train, pred_test, resp_test)
rbf_SVM(pred_train, resp_train, pred_test, resp_test)
