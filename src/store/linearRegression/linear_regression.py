import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def linearRegression():
    # Data Preprocessing
    dataset = pd.read_csv('src/studentscores.csv')
    

    X = dataset.iloc[:, :1].values
    Y = dataset.iloc[:, 1].values

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=1/4, random_state=0)

    # Fitting Simple Linear Regression Model to the training set

    regressor = LinearRegression()
    regressor = regressor.fit(X_train, Y_train)

    # Predecting the result

    Y_pred = regressor.predict(X_test)

    # Visualization

    plt.scatter(X_train, Y_train, color='red')
    plt.plot(X_train, regressor.predict(X_train), color='blue')

    plt.savefig("src/figures/train.png")

    plt.scatter(X_test, Y_test, color='red')
    plt.plot(X_test, regressor.predict(X_test), color='blue')

    plt.savefig("src/figures/predict.png")
