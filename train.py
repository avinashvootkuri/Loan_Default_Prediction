import pickle

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.preprocessing import LabelEncoder

import warnings
def warn(*args, **kwargs):
    pass

warnings.warn = warn

# parameters
eta = 0.07
output_file = f'model_eta={eta}.bin'

data = pd.read_csv("data/Loan_default.csv")

data.columns = data.columns.str.lower()

print(data.columns)

def data_prep(df):
    catCols = [col for col in data.columns if df[col].dtype=="O"]
    catCols.remove("loanid")

    le = LabelEncoder()

    for col in catCols:
        df[col] = le.fit_transform(df[col])
        
    df = df.drop(['loanid'], axis=1)

    return df

data_clean = data_prep(df=data)

df_full_train, df_test = train_test_split(data_clean, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train['default'].values
y_test = df_test['default'].values

del df_full_train['default']
del df_test['default']

def train(df_full_train, y_train, xgb_params):
    dicts_full_train = df_full_train.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_full_train = dv.fit_transform(dicts_full_train)

    feature_names=dv.get_feature_names_out()

    dfulltrain = xgb.DMatrix(X_full_train, label=y_train)

    model = xgb.train(xgb_params, dfulltrain, num_boost_round=200)

    return dv, model

def predict(df, dv, model):
    dicts_test = df_test.to_dict(orient='records')
    X_test = dv.transform(dicts_test)

    dtest = xgb.DMatrix(X_test,label=y_test)

    y_pred = model.predict(dtest)

    return y_pred 


xgb_params = { 
 'eta': 0.07, 
 'max_depth': 4, 
 'min_child_weight': 20.0, 
 'n_estimators': 150.0, 
 
  'objective': 'binary:logistic',
  'eval_metric' : 'auc',
  'nthread': 8,
    
  'seed': 1,
  'verbosity': 1,
 }

dv, model = train(df_full_train, y_full_train, xgb_params=xgb_params)

y_pred = predict(df_test, dv, model)

score = accuracy_score(y_test, y_pred >= 0.5)

print(f"roc auc score={score}")

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')
print("Finished running Train.py")