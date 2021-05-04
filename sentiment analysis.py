import pandas as pd
import textblob as TextBlob

def sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

if __name__ == '__main__':
    df = pd.read_csv("sample.csv")
    tweets = df['tweet']
    tweets = tweets.astype(str)
    df['sentiment'] = tweets.apply(sentiment)
    df.to_csv('sample.csv')