# Michal Komsa
# Lab3

import re
import nltk.corpus
import pandas as pd
import string
from nltk import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

pd.set_option('display.max_columns', None)

data = pd.read_csv("SMSSpamCollection.csv", sep="\t", encoding_errors="ignore", header=None)
data.columns = ("label", "message")

ps = PorterStemmer()
stopwords = nltk.corpus.stopwords.words("english")
def clean_text(text):
    text = "".join([c for c in text if c not in string.punctuation])
    text = re.split(r"\W+", text)
    return "".join([ps.stem(word) + " " for word in text if word not in stopwords])

data["message"] = data["message"].apply(lambda text: clean_text(text))


cv = CountVectorizer()
new_data = cv.fit_transform(data["message"])
print("CountVectorizer:")

# n_gram = CountVectorizer(ngram_range=(2,2))
# new_data = n_gram.fit_transform(data["message"])
# print("N-Gram (only bigrams):")

# tfidf = TfidfVectorizer()
# new_data = tfidf.fit_transform(data["message"])
# print("TF-IDF:")

rfc = RandomForestClassifier()
param = {
    'n_estimators': [10, 90, 150],
    'max_depth': [10, 30, 75, None]
}

gs = GridSearchCV(rfc, param, cv=5, n_jobs=-1)

gs_fit = gs.fit(new_data, data['label'])
res = pd.DataFrame(gs_fit.cv_results_).sort_values("mean_test_score", ascending=False)[0:7]

print(res[["mean_fit_time", "mean_test_score", "params"]])
