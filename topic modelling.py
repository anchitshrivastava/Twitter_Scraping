# Refer to this link for topic modelling = "https://towardsdatascience.com/twitter-topic-modeling-e0e3315b12e2"
import pandas as pd
from wordcloud import STOPWORDS
import spacy
from spacy.tokenizer import Tokenizer
import re
from gensim.corpora import Dictionary
from gensim.test.utils import common_corpus, common_dictionary
nlp = spacy.load('en_core_web_lg')
stopwords = set(STOPWORDS)
import gensim

def tokenizing_text(text):
    tokenizer = Tokenizer(nlp.vocab)
    custom_stopwords = ['hi', '\n', '\n\n', '&amp;', ' ', '.', '-', 'got', "it's", 'it’s', "i'm", 'i’m', 'im', 'want',
                        'like', '$', '@']
    STOP_WORDS = nlp.Defaults.stop_words.union(custom_stopwords)
    ALL_STOP_WORDS = STOP_WORDS.union(stopwords)

    tokens = []

    for doc in tokenizer.pipe(text):
        doc_tokens = []
        for token in doc:
            if token.text.lower() not in STOP_WORDS:
                doc_tokens.append(token.text.lower())
        tokens.append(doc_tokens)

    # Makes tokens column
    return tokens

def lemmatization(text):
    lemmas = []

    doc = nlp(text)

    # Something goes here :P
    for token in doc:
        if ((token.is_stop == False) and (token.is_punct == False)) and (token.pos_ != 'PRON'):
            lemmas.append(token.lemma_)

    return lemmas


def tokenize(text):
    pattern = r"http\S+"

    # tokens = re.sub(pattern, "", text)
    # tokens = re.sub('[^a-zA-Z 0-9]', '', text)
    # # tokens = re.sub('[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    # tokens = re.sub('\w*\d\w*', '', text)  # Remove words containing numbers
    # tokens = re.sub('@*!*\$*', '', text)  # Remove @ ! $
    # tokens = tokens.strip(',')  # TESTING THIS LINE
    # tokens = tokens.strip('?')  # TESTING THIS LINE
    # tokens = tokens.strip('!')  # TESTING THIS LINE
    # tokens = tokens.strip("'")  # TESTING THIS LINE
    # tokens = tokens.strip(".")  # TESTING THIS LINE

    tokens = tokens.split()  # Make text lowercase and split it

    return tokens


if __name__ == '__main__':
    df = pd.read_csv("sample with usernames, emoji and hyperlink as separate columns.csv")
    # print(df)
    df['tweet'] = df['tweet'].astype(str)
    tweets = df['tweet']
    df['tokens'] = tokenizing_text(tweets)
    df['tokens_back_to_text'] = [' '.join(map(str, l)) for l in df['tokens']]
    df['lemmas'] = df['tokens_back_to_text'].apply(lemmatization)
    df['lemmas_back_to_text'] = [' '.join(map(str, l)) for l in df['lemmas']]
    df['lemma_tokens'] = df['lemmas_back_to_text'].apply(tokenize)
    # print(df['lemma_tokens'])
    # print(df['lemmas'])
    # Create a id2word dictionary
    id2word = Dictionary(df['lemma_tokens'])
    # print(len(id2word))
    # Filtering Extremes
    id2word.filter_extremes(no_below=2, no_above=.99)
    # print(len(id2word))
    # Creating a corpus object
    corpus = [id2word.doc2bow(d) for d in df['lemma_tokens']]
    # Instantiating a Base LDA model
    base_model = gensim.models.ldamulticore.LdaMulticore(corpus=corpus, num_topics=5, id2word=id2word, workers=12, passes=5)
    # Filtering for words
    words = [re.findall(r'"([^"]*)"', t[1]) for t in base_model.print_topics()]
    # Create Topics
    topics = [' '.join(t[0:10]) for t in words]
    # Getting the topics
    for id, t in enumerate(topics):
        print(f"------ Topic {id} ------")
        print(t, end="\n\n")