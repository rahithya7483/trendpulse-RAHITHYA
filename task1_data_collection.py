import requests
import os
import time
import json
from datetime import datetime

#list of subreddits given in assignment question
subreddits = ['technology','worldnews','sports','science','entertainment']
#empty final list to store all lists in loop
all_posts =[]
#for authentication in making success api call
headers = {
    "User-Agent": "TrendPulse/1.0",
    "Accept" : "application/json"
}

#making api call in loop
for sr in subreddits:
  url = f"https://www.reddit.com/r/{sr}/hot.json?limit=25"
  try:
    response = requests.get(url,headers=headers,timeout =10)
    if response.status_code != 200: #avoinding crash
      print(f"Failed to fetch data from {sr}. Status Code: {response.status_code}")
      continue
    data = response.json()

    posts = data['data']['children']
    for post in posts:
      post_data = post['data'] #extracting in next step
      extracted ={
          "post_id":post_data.get('id'),
          "title":post_data.get('title'),
          'subreddit':post_data.get('subreddit'),
          'score':post_data.get('score'),
          'num_comments':post_data.get('num_comments'),
          'author':post_data.get('author'),
          'collected_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      }
      all_posts.append(extracted) #saving only post data to final list
  except Exception as e:
    print(f"Error fetching r/{sr}: {e}")
  time.sleep(2) #gap between each call
if not os.path.exists("data"): # creating new folder if there is not
    os.makedirs("data")
date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"
with open(file_path,"w", encoding = 'utf-8') as file:
    json.dump(all_posts, file,indent=4) # dumping into file
print(f"Collected {len(all_posts)} posts. Saved to {file_path}") # ensuring and identifying no.of posts in json file
