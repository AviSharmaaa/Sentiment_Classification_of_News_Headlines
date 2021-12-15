import os.path
from pandas import read_csv as rd
from sentiment_using_vader import start_vader
from sentiment_using_textblob import start_text_blob
from google_news import delete_file, get_news

def start():

    flag = True
    print("\n\t\t\t\tNews Headlines Sentiment Analysis\n")

    link = input("Enter google News link: ")
    delete_file()
    get_news(link)
    while flag:
        print("\n1. Sentiment Analysis using Vader Sentiment Library\n")
        print("2. Sentiment Analysis using TextBlob Library\n")
        print("3. Read File Data")
        print("4. Exit")

        choice  = input("Enter your choice: ")

        if choice == '1':
            start_vader()
        elif choice == '2':
            start_text_blob()
        elif choice == '3':
            file_exists = os.path.exists('data.csv')
            if file_exists:
                print("\t\t\t\t\tFile Found!!!\n\n")
                read_file = rd("data.csv")
                print(read_file.head(10))
            else:
                print("\t\t\t\t\tERROR: File does not exist in this system")
        elif choice == '4':
            flag = False
        else:
            print("Wrong Choice")


start()
