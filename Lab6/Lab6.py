# Michal Komsa
# Lab3

import re
import string
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud

pd.set_option('display.max_columns', None)



data = pd.read_csv("file.csv")
data = data.drop(data.columns.delete([3, 10]), axis=1)
data["date"] = pd.to_datetime(data["date"])

print(f"Data shape: {data.shape}")


stopwords = nltk.corpus.stopwords.words("english")
def clean_text(text):
    text = "".join(c for c in text if c not in string.punctuation)
    tokens = re.split(r"\W", text)
    text = "".join([word + " " for word in tokens if word not in stopwords and "http" not in word])
    return text

data["tweet"] = data["tweet"].apply(lambda t: clean_text(str(t)))


analyzer = SentimentIntensityAnalyzer()
def sentiment(text):
    res = analyzer.polarity_scores(text)
    if res["compound"] > 0:
        return "pos"
    else:
        return "neg"

data["sentiment"] = data["tweet"].apply(lambda text: sentiment(text))

print(f"Negative tweets: {data['sentiment'].str.contains('neg').sum()}")
print(f"Positive tweets: {data['sentiment'].str.contains('pos').sum()}")



tweets_text = ' '.join(data["tweet"])
wordcloud = WordCloud(width=700, height=350, background_color ='white').generate(tweets_text)

fig = px.imshow(wordcloud)
fig.update_layout(xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                  yaxis=dict(showgrid=False, showticklabels=False, zeroline=False))
fig.show()


data['year_month'] = data['date'].dt.to_period('M')

aggregated_data = pd.DataFrame(data.groupby(['year_month', 'sentiment']).size().unstack(fill_value=0))

fig = go.Figure()
fig.add_trace(go.Bar(x=[str(v) for v in aggregated_data.index], y=aggregated_data["neg"], name="Negative", marker=dict(color='red')))
fig.add_trace(go.Bar(x=[str(v) for v in aggregated_data.index], y=aggregated_data["pos"], name="Positive", marker=dict(color='green')))
fig.show()


normalized_data = aggregated_data.div(aggregated_data.sum(axis=1), axis=0)

fig = go.Figure()
fig.add_trace(go.Scatter(x=[str(v) for v in normalized_data.index], y=normalized_data["neg"], name="Negative", marker=dict(color='red')))
fig.add_trace(go.Scatter(x=[str(v) for v in normalized_data.index], y=normalized_data["pos"], name="Positive", marker=dict(color='green')))
fig.update_layout(yaxis=dict(range=[0, 1]))
fig.show()