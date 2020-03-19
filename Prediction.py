# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\phishing\niave.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from DBConnection import DBConnection
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import BernoulliNB

import numpy as np
import pandas as pd
import sys
import time
from sklearn import metrics


class Prediction:
    def predict_nv():
        try:
            
            trainset = []
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute(
                "select * from dataset")
            row = cursor.fetchall()
            y_train = []
            trainset.clear()
            y_train.clear()
            train = len(row)
            for r in row:
                x_train = []
                x_train.clear()

                x_train.append(float(r[0]))
                x_train.append(float(r[1]))
                x_train.append(float(r[2]))

                y_train.append(r[3])
                trainset.append(x_train)
            print("y=", y_train)
            # print("trd=", trainset)
            trainset = np.array(trainset)
            print("trd=", trainset)

            # Train the model

            y_train = np.array(y_train)

            print("sssss", pd.read_csv("test.csv"))
            tf = pd.read_csv("test.csv")
            print(tf, "<----------")

            testdata = np.array(tf)
            print("td=", testdata)
            testdata = testdata.reshape(len(testdata), -1)

            ann = BernoulliNB()

            ann.fit(trainset, y_train)
            s = time.clock()
            result = ann.predict(testdata)  # Predicting
            e = time.clock()
            t = round(e - s, 5)
            print("elm:", t, "s")
            print("pre=", result[0])
            return result[0]


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

if __name__ == '__main__':
    Prediction.predict_nv()

