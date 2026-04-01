import pandas as pd
df = pd.read_json('data/trends_20260401.json') #loading using pandas
print(f"Loaded {len(df)} posts from data/trends_20260401.json")#total length of data
before = len(df) #intial total
#dropping duplicates row of post_id
df = df.drop_duplicates(subset='post_id')
after = len(df)
print(f"after removing duplicates: {after}") # after deleting, finding length

df.dropna(inplace = True) # dropping nulls
print(f"after removing missings: {len(df)}")

df['score'] = df['score'].astype(int) # chaging dtype to integer of score column
df['num_comments'] = df['num_comments'].astype(int) # changing to integer of num_comments columns

df = df[df['score'] >= 5] # removing low quality shows and updating
print(f"after removing low quality ones, length is {len(df)}")

df['title'] = df['title'].astype(str).str.strip() # removing unnecessary spaces
#saving to a csv file
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index = False)
print(f"\nSaved {len(df)} rows to {output_path}")
#summary after preprocessing
print("\nPosts per subreddit:")
print(df['subreddit'].value_counts())
