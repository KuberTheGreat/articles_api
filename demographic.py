import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')

view = df.copy().loc[df['eventType'] == 'VIEW']
print("view", len(view)) #61086

like = df.copy().loc[df['eventType'] == 'LIKE']
print("like", len(like)) #5745

bookmark = df.copy().loc[df['eventType'] == 'BOOKMARK']
print("bookmark", len(bookmark)) #2463

follow = df.copy().loc[df['eventType'] == 'FOLLOW']
print("follow", len(follow)) # 1407

comment = df.copy().loc[df['eventType'] == 'COMMENT CREATED']
print("comment created", len(comment)) # 1611


print("Sum of all events ", len(view) + len(like) + len(bookmark) + len(follow) + len(comment))

def something(x):
  return view + like + bookmark + follow + comment