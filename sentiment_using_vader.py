import os.path
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as Sentiment

def delete_file():
    flag = os.path.exists('data.csv')

    if flag:
        open_file = open("data.csv",'a')
        open_file.seek(0)
        open_file.truncate()

def get_sentiment():
    data_set = pd.read_csv('data.csv',encoding='cp1252')

    sentiment = Sentiment()
    negative = []
    positive = []
    neutral = []
    compound = []

    for head_line in range(data_set.shape[0]):
        heading = data_set.iloc[head_line,0]
        polarity = sentiment.polarity_scores(heading)
        negative.append(polarity['neg'])
        positive.append(polarity['pos'])
        neutral.append(polarity['neu'])
        compound.append(polarity['compound'])


    data_set['Negative'] = negative
    data_set['Neutral'] = neutral
    data_set['Positive'] = positive
    data_set['compound'] = compound
    data_set['Lable'] = 0

    data_set.loc[data_set['compound'] > 0, 'Lable'] = 1
    data_set.loc[data_set['compound'] < 0,'Lable'] = -1

    data = data_set[['Heading ', 'Lable']]
    data.to_csv('data_with_labels.csv',mode='a',encoding='utf-8',index=False)