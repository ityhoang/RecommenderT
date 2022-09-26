from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from types import SimpleNamespace
import pandas as pd
import array as arr
import sklearn
from sklearn.decomposition import TruncatedSVD
import numpy as np

cred = credentials.Certificate("D://projectpython/tyhoang/testdemo.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

response = ''
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
@app.route('/name',methods = ['GET','POST'])
def nameRoute():
    global response
    # db = firestore.client()
    if(request.method == 'POST'):
        idproduct = request.args.get('idproduct')
        response = jsonify("Recommend[0:3]")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        df1 = pd.DataFrame(columns=["ProductID","rating",'UserID'])
        titles = ["veges", "snack", "food", "drink", "dessert"]
        emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[0])
        docs = emp_ref0.get()
        for doc in docs:
            emp_ref0s = emp_ref0.document(doc.id).collection('rating')
            docs1 = emp_ref0s.get()
            for doc1 in docs1:
                data_list = list([[doc.id,doc1.to_dict()['rating'],doc1.id]])
                df = pd.DataFrame(data_list, columns = ["ProductID","rating","UserID"])
                df1=pd.concat([df1,df], ignore_index=True)

        emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[1])
        docs = emp_ref0.get()
        for doc in docs:
            emp_ref0s = emp_ref0.document(doc.id).collection('rating')
            docs1 = emp_ref0s.get()
            for doc1 in docs1:
                data_list = list([[doc.id,doc1.to_dict()['rating'],doc1.id]])
                df = pd.DataFrame(data_list, columns = ["ProductID","rating","UserID"])
                df1=pd.concat([df1,df], ignore_index=True)

        emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[2])
        docs = emp_ref0.get()
        for doc in docs:
            emp_ref0s = emp_ref0.document(doc.id).collection('rating')
            docs1 = emp_ref0s.get()
            for doc1 in docs1:
                data_list = list([[doc.id,doc1.to_dict()['rating'],doc1.id]])
                df = pd.DataFrame(data_list, columns = ["ProductID","rating","UserID"])
                df1=pd.concat([df1,df], ignore_index=True)
        
        emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[3])
        docs = emp_ref0.get()
        for doc in docs:
            emp_ref0s = emp_ref0.document(doc.id).collection('rating')
            docs1 = emp_ref0s.get()
            for doc1 in docs1:
                data_list = list([[doc.id,doc1.to_dict()['rating'],doc1.id]])
                df = pd.DataFrame(data_list, columns = ["ProductID","rating","UserID"])
                df1=pd.concat([df1,df], ignore_index=True)

        emp_ref0 = db.collection('categoryicon').document('A8JoMU51G5b0O2bdLqTf').collection(titles[4])
        docs = emp_ref0.get()
        for doc in docs:
            emp_ref0s = emp_ref0.document(doc.id).collection('rating')
            docs1 = emp_ref0s.get()
            for doc1 in docs1:
                data_list = list([[doc.id,doc1.to_dict()['rating'],doc1.id]])
                df = pd.DataFrame(data_list, columns = ["ProductID","rating","UserID"])
                df1=pd.concat([df1,df], ignore_index=True)
        
        print(df1)
        df1 = df1.dropna()
        response = jsonify("Recommend[0:3]")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
if __name__ == '__main__':
     app.run(host='127.0.0.1', debug = True)