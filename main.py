import pickle
import time
from sentiment_using_vader import get_sentiment
from sentiment_analysis import train_model

def test_manually(str1):
    load_vectorizer = pickle.load(open('vectorize.pickle','rb'))
    load_model = pickle.load(open('classification.model','rb'))
    headline = str1.lower()
    headline = headline.replace(',','')
    headline = headline.replace(':',"")
    headline = headline.replace('%','')
    headline = headline.replace('?','')

    inp = []
    temp = ""
    for i in range(len(headline)):
        if headline[i]!=" ":
            temp+=headline[i]
        elif headline[i] == " ":
            inp.append(temp)
            temp = ""

    pred = load_model.predict((load_vectorizer.transform(inp)))

    count_pos = 0
    count_neg = 0
    print(pred)
    for i in range(len(pred)):
        if pred[i] == 1:
            count_pos+=1
        else:
            count_neg+=1

    if count_pos > count_neg:
        print("\nIt is positive news\n")
    else:
        print("\nIt is Negative news\n")

def start():
    print("\t\t\t\t\tSENTIMENT CLASSIFICATION OF NEWS HEADLINES\n")
    print("\nRunning Vader Sentiment on collected data")
    get_sentiment()
    print("\nSentiment Analysis using Vader Complete\n")
    print("\nNow Training the Model using Multinomial NB\n")
    train_model()
    time.sleep(1)

    flag = True
    while flag:
        print("1. Test the model against a manual input again\n")
        print("2. Exit\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            news_headline = input("Enter a news headline: ")
            test_manually(news_headline)
            print("\n")

        elif choice == '2':
            flag = False
        else:
            print("Wrong Choice\n")

start()
