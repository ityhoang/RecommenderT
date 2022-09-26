from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from types import SimpleNamespace
import pandas as pd
import pickle
import sklearn
import array as arr
from sklearn.decomposition import TruncatedSVD
import numpy as np

cred = credentials.Certificate("D://Nam4//Ki2//doanchuyennganh2//flaskproject//testdemo.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

response = ''

def main():
    df1 = pd.DataFrame(columns=["ProductID", "rating", 'UserID'])
    titles = ["veges", "snack", "food", "drink", "dessert"]
    emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[0])
    docs = emp_ref0.get()
    for doc in docs:
        emp_ref0s = emp_ref0.document(doc.id).collection('rating')
        docs1 = emp_ref0s.get()
        for doc1 in docs1:
            data_list = list([[doc.id, doc1.to_dict()['rating'], doc1.id]])
            df = pd.DataFrame(data_list, columns=["ProductID", "rating", "UserID"])
            df1 = pd.concat([df1, df], ignore_index=True)

    emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[1])
    docs = emp_ref0.get()
    for doc in docs:
        emp_ref0s = emp_ref0.document(doc.id).collection('rating')
        docs1 = emp_ref0s.get()
        for doc1 in docs1:
            data_list = list([[doc.id, doc1.to_dict()['rating'], doc1.id]])
            df = pd.DataFrame(data_list, columns=["ProductID", "rating", "UserID"])
            df1 = pd.concat([df1, df], ignore_index=True)

    emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[2])
    docs = emp_ref0.get()
    for doc in docs:
        emp_ref0s = emp_ref0.document(doc.id).collection('rating')
        docs1 = emp_ref0s.get()
        for doc1 in docs1:
            data_list = list([[doc.id, doc1.to_dict()['rating'], doc1.id]])
            df = pd.DataFrame(data_list, columns=["ProductID", "rating", "UserID"])
            df1 = pd.concat([df1, df], ignore_index=True)

    emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[3])
    docs = emp_ref0.get()
    for doc in docs:
        emp_ref0s = emp_ref0.document(doc.id).collection('rating')
        docs1 = emp_ref0s.get()
        for doc1 in docs1:
            data_list = list([[doc.id, doc1.to_dict()['rating'], doc1.id]])
            df = pd.DataFrame(data_list, columns=["ProductID", "rating", "UserID"])
            df1 = pd.concat([df1, df], ignore_index=True)

    emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[4])
    docs = emp_ref0.get()
    for doc in docs:
        emp_ref0s = emp_ref0.document(doc.id).collection('rating')
        docs1 = emp_ref0s.get()
        for doc1 in docs1:
            data_list = list([[doc.id, doc1.to_dict()['rating'], doc1.id]])
            df = pd.DataFrame(data_list, columns=["ProductID", "rating", "UserID"])
            df1 = pd.concat([df1, df], ignore_index=True)

    print(df1)
    print(type(df1))
    df1 = df1.dropna()
    df1.head()
    ratings_utility_matrix = df1.pivot_table(values='rating', index='UserID', columns='ProductID', fill_value=0)
    X = ratings_utility_matrix.T
    pickle.dump(X, open("X.pkl", "wb"))
    SVD = TruncatedSVD()
    decomposed_matrix = SVD.fit_transform(X)

    correlation_matrix = np.corrcoef(decomposed_matrix)

    pickle.dump(correlation_matrix, open("correlation_matrix.pkl","wb"))
    i = "u3PP6kQcotPNuQ1hkz4w"
    product_names = list(X.index)
    pickle.dump(product_names, open("product_names.pkl", "wb"))
    product_ID = product_names.index(i)
    print(product_ID)

    correlation_product_ID = correlation_matrix[product_ID]
    Recommend = list(X.index[correlation_product_ID > 0.90])
    print(Recommend)



if __name__ == '__main__':
    main()