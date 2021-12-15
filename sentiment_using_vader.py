import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def start_vader():
    data = pd.read_csv("data.csv",encoding='cp1252')

    analyzer = SentimentIntensityAnalyzer()

    negative = []
    neutral = []
    positive = []

    for news_heading in range(data.shape[0]):
        tittle = data.iloc[news_heading,0]
        title_analyzed = analyzer.polarity_scores(tittle)
        negative.append(title_analyzed['neg'])
        neutral.append(title_analyzed['neu'])
        positive.append(title_analyzed['pos'])

    data['Negative'] = negative
    data['Neutral'] = neutral
    data['Positive'] = positive

    print(data.head(10))
