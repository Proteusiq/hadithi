from numpy.typing import NDArray
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from knn import KNN


def get_iris(
    train_size: float = 0.8, random_state: int = 42
) -> tuple[NDArray, NDArray, NDArray, NDArray]:
    iris = load_iris()
    X, y = iris.data, iris.target

    return train_test_split(
        X, y, train_size=train_size, stratify=y, random_state=random_state
    )


if __name__ == "__main__":
    # get data
    X_train, X_test, y_train, y_test = get_iris(train_size=0.8)

    # get number of classes
    k = len(set(y_train))

    # create a kNN predictor and train
    predictor = KNN(k)
    predictor.fit(X_train, y_train)

    # predict on test set
    y_pred = predictor.predict(X_test)

    # evaluate performance
    print(classification_report(y_true=y_test, y_pred=y_pred))
