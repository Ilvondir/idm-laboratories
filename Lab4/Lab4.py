# Michal Komsa
# Lab3

from math import log
import pandas as pd
import string
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 34)
pd.set_option('display.max_rows', 50)

data = pd.read_csv("SMSSpamCollection.csv", encoding_errors="ignore", header=None, sep="\t")
data.columns = ["label", "message"]


data["length"] = data["message"].apply(lambda text: len(text) - text.count(" "))

def set_percents(text):
    punc_num = 0
    for c in string.punctuation:
        punc_num += text.count(c)

    return round((punc_num / (len(text)-text.count(" ")))*100, 2)

data["percent_of_punctuations"] = data["message"].apply(lambda text: set_percents(text))

px.histogram(x=data["length"]).show()
px.histogram(x=data["percent_of_punctuations"]).show()

def box_cox(x, lambd):
    if lambd == 0:
        return  log(x)
    return ((x**lambd)-1)/lambd


log_box = data["length"].apply(lambda x: box_cox(x, 0))
sqrt_box = data["length"].apply(lambda x: box_cox(x, 0.5))
box_minus2 = data["length"].apply(lambda x: box_cox(x, -2))
box_minus1 = data["length"].apply(lambda x: box_cox(x, -1))

fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Histogram(x=log_box, name='lambda = 0'), row=1, col=1)
fig.add_trace(go.Histogram(x=sqrt_box, name='lambda = 0.5'), row=1, col=2)
fig.add_trace(go.Histogram(x=box_minus1, name='lambda = -2'), row=2, col=1)
fig.add_trace(go.Histogram(x=box_minus2, name='lambda = -1'), row=2, col=2)
fig.show()



b1 = data["percent_of_punctuations"].apply(lambda x: box_cox(x, 0.1))
b2 = data["percent_of_punctuations"].apply(lambda x: box_cox(x, .2))
b3 = data["percent_of_punctuations"].apply(lambda x: box_cox(x, .3))
b4 = data["percent_of_punctuations"].apply(lambda x: box_cox(x, .5))

fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Histogram(x=b1, name='lambda = 0.1'), row=1, col=1)
fig.add_trace(go.Histogram(x=b2, name='lambda = 0.2'), row=1, col=2)
fig.add_trace(go.Histogram(x=b3, name='lambda = 0.3'), row=2, col=1)
fig.add_trace(go.Histogram(x=b4, name='lambda = 0.5'), row=2, col=2)
fig.show()
