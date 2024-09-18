from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model():
    X_train, X_test, y_train, y_test = load_data()
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
