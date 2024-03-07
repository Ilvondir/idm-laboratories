# Michal Komsa
# Lab3

import string
import re
import nltk.corpus
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("McDonald_s_Reviews.csv", encoding_errors="ignore")
data = data.drop(data.columns.delete(8), axis=1)

ps = nltk.PorterStemmer()
stopwords = nltk.corpus.stopwords.words("english")
def clean_text(text):
    if pd.isna(text):
        return ""
    text = "".join([c for c in text if c not in string.punctuation])
    tokens = re.split(r'\W+', text)
    text = "".join([ps.stem(word) + " " for word in tokens if word not in stopwords])
    return text

data["review"] = data["review"].apply(lambda text: clean_text(text))

# CountVectorizer
cv = CountVectorizer()
data_cv = cv.fit_transform(data["review"])

print(f"Vectorized data shape:{data_cv.shape}")
temp = data_cv.toarray()
cv_result = pd.DataFrame(temp, columns=cv.get_feature_names_out())
print(cv_result)


# N-Gram
ng = CountVectorizer(ngram_range=(2,2))
data_ng = ng.fit_transform(data["review"])

print(f"N-Gram shape:{data_ng.shape}")
temp = data_ng.toarray()
ng_result = pd.DataFrame(temp, columns=ng.get_feature_names_out())
print(ng_result)


# TF-IDF
tfidf = TfidfVectorizer()
data_tfidf = tfidf.fit_transform(data['review'])

print(f"TF-IDF shape:{data_tfidf.shape}")
temp = data_tfidf.toarray()
tfidf_result = pd.DataFrame(temp, columns=tfidf.get_feature_names_out())
print(tfidf_result)

# Wykonanie wszystkich wektoryzatorow na raz u mnie skutkuje bledem
# numpy.core._exceptions._ArrayMemoryError: Unable to allocate 37.7 GiB for an array with shape (33396, 151398) and data type int64
# Mam za malo pamieci w komputerze :(