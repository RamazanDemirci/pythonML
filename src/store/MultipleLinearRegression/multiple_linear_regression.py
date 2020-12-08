import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer


def multipleLinearRegression():
    #importing dataset
    dataset = pd.read_csv('src/MultipleLinearRegression/datasets/50_Startups.csv')
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, 4].values

    #encoding categorical data
    label_encoder = LabelEncoder()
    X[:, 3]= label_encoder.fit_transform(X[: , 3])

    ct = ColumnTransformer(
        [('State', OneHotEncoder(), [3])],    # The column numbers to be transformed
        remainder='passthrough'               # Leave the rest of the columns untouched
    )
    X = ct.fit_transform(X)

    #avoiding dummy variable trap
    X=X[:, 1:]

    #splitting the dataset into the Training Set and Test Set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=0)

    #fitting multiple linear regression to the training set
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)

    #predicting the test set results
    Y_pred = regressor.predict(X_test)

    
    # Visualization

    # todo



    

