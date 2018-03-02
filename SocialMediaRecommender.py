# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:36:26 2018

@author: NAVEEN
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import pandas as pd
le=preprocessing.LabelEncoder()
data = pd.read_csv(r"C:\Users\NAVEEN\Desktop\Facebook.csv",delimiter=";",header=0)
cols=list(data.columns)
le.fit(data["Type"])
data["Type"]=le.transform(data["Type"])
cols.remove('Lifetime Post Total Reach')
cols.remove('Lifetime Post Total Impressions')
cols.remove('Lifetime Engaged Users')
cols.remove('Lifetime Post Consumers')
cols.remove('Lifetime Post Consumptions')
cols.remove('Lifetime Post Impressions by people who have liked your Page')
cols.remove('Lifetime People who have liked your Page and engaged with your post')
cols.remove('comment')
cols.remove('Total Interactions')
data3=data[cols]
data3=data3[data3['Page total likes'].notnull()]
data3=data3[data3['Type'].notnull()]
data3=data3[data3['Category'].notnull()]
data3=data3[data3['Post Month'].notnull()]
data3=data3[data3['Post Hour'].notnull()]
data3=data3[data3['Paid'].notnull()]
data3=data3[data3['Post Weekday'].notnull()]
data3=data3[data3['Lifetime Post reach by people who like your Page'].notnull()]
data3=data3[data3['like'].notnull()]
data3=data3[data3['share'].notnull()]
output=data3['Post Weekday']
data5=data3
cols.remove('Post Weekday')
data5=data5[cols]
data4=data3['Post Hour']
cols.remove('Post Hour')
data3=data3[cols]
model =  RandomForestClassifier(n_estimators=16,oob_score = 'TRUE', random_state = 1)
model.fit(data3,output)
predicted= model.predict([[134879,0,1,9,0,15744,345,121]])
print (predicted)
output=data4
model.fit(data5,output)
predicted= model.predict([[134879,0,1,predicted,9,0,15744,345,121]])
print (predicted)