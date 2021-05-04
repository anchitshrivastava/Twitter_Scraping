import tweepy
from credentials import consumer_key , consumer_secret , access_token , access_token_secret
import pandas as pd


def from_a_user(username,count):
    #username = 'anchit2000'
    #count = 150
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)

        # Pulling information from tweets iterable object
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list)
        return tweets_df
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


def text_search_query(text_query,count):
    #text_query = '2020 US Election'
    #count = 150
    try:
        tweets = tweepy.Cursor(api.search, q=text_query).items(count)
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list)
        return tweets_df
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweets_from_a_user = from_a_user('SrBachchan', 1)
    tweets_related_to_a_phrase = text_search_query('Amitabh Bachchan', 1)

    print("Example of tweets from a user is")
    print(tweets_from_a_user)
    print("**********************************")
    print("Example of tweets on a topic is")
    print(tweets_related_to_a_phrase[2][0])


