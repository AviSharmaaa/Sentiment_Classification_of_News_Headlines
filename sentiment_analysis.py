import pickle
import time
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix

nb = MultinomialNB()

def train_model():
    dataset = pd.read_csv('data_with_labels.csv',encoding='cp1252')

    dataset = dataset[dataset['Lable'] != 0]

    x_data = dataset['Headline']
    y_data = dataset['Lable']

    x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.3)

    vect = CountVectorizer(max_features=2000,binary=True)

    x_train_vect = vect.fit_transform(x_train).toarray()

    sm = SMOTE()

    x_train_res,y_train_res = sm.fit_resample(x_train_vect,y_train)

    vect_file = 'vectorize.pickle'
    pickle.dump(vect,open(vect_file,'wb'))


    model = nb.fit(x_train_res,y_train_res)

    mod_file = 'classification.model'
    pickle.dump(model,open(mod_file,'wb'))


    x_test_vect = vect.transform(x_test).toarray()

    y_pred = nb.predict(x_test_vect)

    print("Model Trainig Complete!!!!\n")
    time.sleep(2)
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test,y_pred)*100))
    print("\nF1 Score: {:.2f}%".format(f1_score(y_test,y_pred)*100))
    print("\nConfusion Matrix: \n",confusion_matrix(y_test,y_pred))
