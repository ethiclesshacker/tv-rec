import pandas as pd

import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import CountVectorizer

pd.options.mode.chained_assignment = None
df = pd.read_table("tvs-data.tsv",usecols=['primaryTitle','genres'])

df = df[df["genres"]!="\\N"]
df['genres'] = df['genres'].map(lambda x : x.lower().split(','))
df['genres'] = df['genres'].map(lambda x : x.lower().replace(','," "))
df = df.iloc[0:40000, :]
df.set_index('primaryTitle',inplace = True)

df.head()
df['genre list'] = ''

columns = df.columns

for index, row in df.iterrows():

    words = ''

    for col in columns:

        words = words + ' '.join(row[col])+ ' '

    row['genre list'] = words
df.drop(columns = [col for col in df.columns if col!= 'genre list'], inplace = True)
df.reset_index()
count = CountVectorizer()

count_matrix = count.fit_transform(df['genres'])
count_matrix
cosine_sim = cosine_similarity(count_matrix, count_matrix)
cosine_sim
cosine_sim.shape
data = cosine_sim
df2 = pd.DataFrame(data)
df2.head()
indices = pd.Series(df.index)
def recommendations(title, cosine_sim = cosine_sim):

    

    recomended_webseries = []

    

    idx = indices[indices == title].index[0]

    

    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    

    top_10_indexes = list(score_series.iloc[1:11].index)

    

    for i in top_10_indexes:

        recomended_webseries.append(list(df.index)[i])

        

    return recomended_webseries
recommendations('Aquí está Pancho Villa')