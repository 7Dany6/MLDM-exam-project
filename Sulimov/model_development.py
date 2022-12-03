from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from data_engineering import df_features_sharp
import pandas as pd
import numpy as np


train_labels = pd.read_csv(r"C:\Users\danys\Downloads\train_new\train_labels.csv")
train_labels_sharp = train_labels.iloc[:8294]  # since we are using only the first chunk with 8294 rows
X = df_features_sharp
y = train_labels_sharp.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .30, random_state=42)
X_train, X_test = X_train.reset_index(), X_test.reset_index()  # that's done for the sake of starting from 0
X_train, X_test = X_train.drop('index', axis=1), X_test.drop('index', axis=1)
model = RandomForestClassifier(class_weight='balanced')
# for the first attempt let's consider the most straightforward way of tackling missing values
for col in X_train.columns:
    if np.isnan(X_train[col]).sum().sum():
        X_train[col] = X_train[col].fillna(0)
for col in X_test.columns:
    if np.isnan(X_test[col]).sum().sum():
        X_test[col] = X_test[col].fillna(0)
model.fit(X_train, y_train)
predictions = model.predict(X_test)



