import pandas as pd
# import nltk
# import ssl  # if nltk is not able to download corpus or anything else use this commented code
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
#
# nltk.download('stopwords')
# nltk.download('punkt')

from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
import re
import demoji
# pip install 

def emoji(text):
    ls = set(demoji.findall_list(text))
    ls = list(ls)
    return ls

def extracting_username(text):
    text1 = text.split(" ")
    ls = []
    for i in text1:
        if '@' in i:
            ls.append(i)
            text.replace(i,'')
        else:
            pass
    return ls

def extracting_hyperlink(text):
    text1 = text.split(" ")
    for i in text1:
        if 'https://t.co/' in i:
            link = i
            text.replace(i,'')
            return link
        else:
            pass

def text_to_lower(text):  # done
    text = text.lower()
    return remove_hyperlink_and_username(text)

def remove_hyperlink_and_username(text):
    text1 = text.split(" ")
    for i in text1:
        if '@' in i:
            text = text.replace(i,'')
    for i in text1:
        if 'https://t.co/' in i:
            text = text.replace(i,'')
    return stop_words(text)

def stop_words(text):
    stop = stopwords.words('english')
    test = text.split(" ")
    filtered = [w for w in test if not w in stop]
    test = " ".join(filtered)
    return punctuation(test)
    #print(test)

def punctuation(text): # done
    res = re.sub(r'[^\w\s]', '', text)
    return spaces(res)
    # print(text)

# def numbers(text):  # I think we should not remove the numbers.
#     text = text.replace('\d+', '')
#     # print(text)
#     return spaces(text)

def spaces(text):
    text = text.replace('\n', "")
    text = text.strip()
    return text

if __name__ == '__main__':
    df = pd.read_csv("sample raw.csv")
    # print(df.head(5))
    tweets = df['tweet']
    tweets_emoji = tweets.apply(emoji)
    tweets_username = tweets.apply(extracting_username)
    tweets_hyperlink = tweets.apply(extracting_hyperlink)
    df['emoji mood'] = tweets_emoji
    df['usernames'] = tweets_username
    df['hyperlink'] = tweets_hyperlink
    # print(tweets_emoji[30])
    # df['tweet'] = df['tweet'].astype(str)
    tweets = tweets.apply(text_to_lower)
    # print(tweets[0])
    df['tweet'] = tweets
    # print(df['tweet'][33])
    df.to_csv('sample with usernames, emoji and hyperlink.csv')