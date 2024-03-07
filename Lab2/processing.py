import nltk.corpus
import pandas as pd
import string
import re

data = pd.read_csv("McDonald_s_Reviews.csv", encoding="UTF-8", encoding_errors='ignore')
cols_to_remove = data.columns.delete(8)
data = data.drop(cols_to_remove, axis=1)

def remove_punctuation(text):
    raw_text = ""
    for c in text:
        if c not in string.punctuation:
            raw_text += c

    return raw_text

data["review"] = data["review"].apply(lambda text: remove_punctuation(str(text)))

def tokenize(text):
    pattern = r"\W+"
    splitted = re.split(pattern, text)

    return splitted

data["review"] = data["review"].apply(lambda text: tokenize(str(text).lower()))

# nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")

def remove_stopwords(text):
    return [word for word in text if word not in stopwords]

data["review"] = data["review"].apply(lambda text: remove_stopwords(text))

print(data.head(10))


