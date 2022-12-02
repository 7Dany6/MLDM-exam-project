import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

cat_features = ['B_30', 'B_38', 'D_114', 'D_116', 'D_117', 'D_120', 'D_126', 'D_63', 'D_64', 'D_66', 'D_68']
df_1_pkl = pd.read_pickle(r"C:\Users\danys\Downloads\train_new\data_split_1.pkl")
num_features = [col for col in df_1_pkl if col not in cat_features + ['S_2', 'customer_ID', 'B_31', 'D_87']]
aggregated_num = df_1_pkl.groupby('customer_ID')[num_features].agg(['mean', 'median', 'max', 'min', 'std'])
aggregated_cat = df_1_pkl.groupby('customer_ID')[cat_features].agg(['count', 'nunique'])
df_features = pd.concat([aggregated_cat, aggregated_num], axis=1)
df_features.reset_index(inplace=True)
df_features_sharp = df_features.drop('customer_ID', axis=1)
print(df_features_sharp.shape)

