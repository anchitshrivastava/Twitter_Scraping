import tweepy
from credentials import consumer_key , consumer_secret , access_token , access_token_secret
import pandas as pd

def from_a_user(username,count):
    try:
        tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list, columns=['datetime','id','tweet'])
        return tweets_df
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)




if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweets_from_a_user = from_a_user('elonmusk', 100)
    print("Latest tweets from Elon Musk is")
    print(tweets_from_a_user)
    tweets_from_a_user.to_csv("sample raw.csv")