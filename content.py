from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')

df = df[df['soup'].notna()]

count = CountVectorizer(stop_words = 'english')

countMatrix = count.fit_transform(df['title'])

cosineSimilarity = cosine_similarity(countMatrix, countMatrix)

df = df.reset_index()

indices = pd.Series(df.index, index = df['title'])

def getRecommendations(title, cosine_Similarity):
  id = indices[title]

  scores = list(enumerate(cosine_Similarity[id]))

  scores = sorted(scores, key = lambda x: x[1], reverse = True)
  scores = scores[1:11]

  movieIndices = [i[0] for i in scores]

  return df['title'].iloc[movieIndices]