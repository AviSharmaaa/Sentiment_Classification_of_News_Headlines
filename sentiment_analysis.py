import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix

nb = MultinomialNB()

def train_model():
    dataset = pd.read_csv('data_with_labels.csv',encoding='cp1252')

    dataset = dataset[dataset['Lable'] != 0]

    counts = dataset['Lable'].value_counts()
    print(counts)


    x_data = dataset['Heading ']
    y_data = dataset['Lable']

    x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.2)

    vect = CountVectorizer(max_features=2000,binary=True)

    x_train_vect = vect.fit_transform(x_train).toarray()

    vect_file = 'vectorize.pickle'
    pickle.dump(vect,open(vect_file,'wb'))


    model = nb.fit(x_train_vect,y_train)

    mod_file = 'classification.model'
    pickle.dump(model,open(mod_file,'wb'))


    x_test_vect = vect.transform(x_test).toarray()

    y_pred = nb.predict(x_test_vect)

    print("\t\t\t\t\tModel Trainig Complete!!!!\n")
    print("\t\t\t\t\tAccuracy: {:.2f}%".format(accuracy_score(y_test,y_pred)*100))
    print("\n\t\t\t\t\tF1 Score: {:.2f}%".format(f1_score(y_test,y_pred)*100))
    print("\n\t\t\t\t\tConfusion Matrix: \n",confusion_matrix(y_test,y_pred))
