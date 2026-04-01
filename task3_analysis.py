import pandas as pd
import numpy as np # loading required libraries

#loading and explore part
df = pd.read_csv('data/trends_clean.csv')
print(f"Loaded data: {df.shape}") # returns data shape

print("first 5 rows, ",df.head()) # gives first 5 rows

#average values
avg_score = df['score'].mean()
avg_comments = df['num_comments'].mean()
print(f"\nAverage score: {int(avg_score)}")
print(f"Average comments: {int(avg_comments)}")

# 2.numpy analysis
scores = df['score'].values # storing in scores cause it required for ops using numpy
comments = df['num_comments'].values # similarly for comments too
print("\n--- NumPy Stats ---")
print(f"Mean score   : {int(np.mean(scores))}")
print(f"Median score : {int(np.median(scores))}")
print(f"Std deviation: {int(np.std(scores))}")
print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")

sub_counts = df['subreddit'].value_counts()
top_sub = sub_counts.idxmax()
top_count = sub_counts.max() # high sub with high posts
print(f"\nMost posts from: {top_sub} ({top_count} posts)")

max_comments_idx = np.argmax(comments) # selects the max comments of post
top_post_title = df.iloc[max_comments_idx]['title']
top_post_comments = df.iloc[max_comments_idx]['num_comments']

print(f"\nMost commented post: \"{top_post_title}\" — {top_post_comments} comments")
#add new columns
df['engagement'] = df['num_comments'] / (df['score']+1)
df['popular'] = df['score'] > avg_score
#save the result
output_path = "data/trends_analysed.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")
