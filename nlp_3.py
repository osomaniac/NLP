## stop words are words that do not any value (a, the, am, is, etc)
## only have to do the download one time

import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path
import pandas as pd

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

stops = stopwords.words("english")
#print(stops)
'''
blob = TextBlob("Today is a beautiful day.")
print(blob.words)
new_blob = [word for word in blob.words if word not in stops]
print(new_blob)
'''
items = blob.word_counts.items()
#print(items)

items = [i for i in items if i[0] not in stops]
#print(items)

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
#print(sorted_items)

top20 = sorted_items[:20]
#print(top20)

df = pd.DataFrame(top20, columns=['word','count'])
print(df)

import matplotlib.pyplot as plt
axes = df.plot.bar(x='word', y='count', legend=False)
plt.gcf().tight_layout()
plt.show()