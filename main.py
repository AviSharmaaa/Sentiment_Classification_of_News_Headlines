import pickle
from google_news import delete_file,get_news
from sentiment_using_vader import get_sentiment
from sentiment_analysis import train_model

def test_manually(str1):
    load_vectorizer = pickle.load(open('vectorize.pickle','rb'))
    load_model = pickle.load(open('classification.model','rb'))
    headline = str1.lower()
    headline = headline.replace(',','')
    headline = headline.replace(':',"")
    headline = headline.replace('%','')
    headline = headline.replace(' ...','')
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
    for i in range(len(pred)):
        if pred[i] == '1':
            count_pos+=1
        else:
            count_neg+=1
    if count_pos > count_neg:
        print("It is positive news\n")
    else:
        print("It is Negative news\n")

def start():
    print("\t\t\t\t\tSENTIMENT CLASSIFICATION OF NEWS HEADLINES\n")
    link = input("Enter google news link: ")
    print("\t\t\t\t\tThe google_news.py file is scrapping the website, Wait for a few sec....\n")
    delete_file()
    get_news(link)
    print("\t\t\t\t\tWeb Scraping Complete\n")
    print("\t\t\t\t\tRunning Vader Sentiment on collected data")
    get_sentiment()
    print("\t\t\t\t\tSentiment Analysis using Vader Complete\n")
    print("\t\t\t\t\tNow Training the Model using Multinomial NB\n")
    train_model()

    flag = True
    while flag:
        print("\n1. Test the model against a manual input again\n")
        print("2. Exit\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            news_headline = input("Enter a news headline: ")
            test_manually(news_headline)
            print("\n")
                     
        elif choice == '2':
            flag = False
        else:
            print("\t\t\t\t\tWrong Choice\n")


start()
