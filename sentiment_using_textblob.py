import pandas as pd
from textblob import TextBlob
# import matplotlib.pyplot as pit
# pit.style.use('fivethirtyeight')

def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def get_sentiment(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

def start_text_blob():
    data = pd.read_csv("data.csv",encoding='cp1252')

    for news_heading in range(data.shape[0]):
        title = data.iloc[news_heading,0]
        polarity = get_polarity(title)
        data['Polarity'] = polarity

    data['Sentiment'] = data['Polarity'].apply(get_sentiment)

    print(data.head(10))
