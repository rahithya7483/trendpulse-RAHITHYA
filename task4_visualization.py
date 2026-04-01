import pandas as pd
import matplotlib.pyplot as plt
import os
#setting up
df = pd.read_csv('data/trends_analysed.csv')

# Create outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

#charts 1 - horizontal bar of top 10 score posts
top_posts = df.sort_values(by="score", ascending=False).head(10)

# Shorten titles to 50 chars
top_posts['short_title'] = top_posts['title'].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

plt.figure()
plt.barh(top_posts['short_title'], top_posts['score'])
plt.xlabel("Score")
plt.ylabel("Post Title")
plt.title("Top 10 Posts by Score")

plt.gca().invert_yaxis()  # highest score on top

plt.savefig("outputs/chart1_top_posts.png")
plt.show()

# 3. CHART 2 of bar — POSTS PER SUBREDDIT

sub_counts = df['subreddit'].value_counts()

plt.figure()
plt.bar(sub_counts.index, sub_counts.values)
plt.xlabel("Subreddit")
plt.ylabel("Number of Posts")
plt.title("Posts per Subreddit")

plt.savefig("outputs/chart2_subreddits.png")
plt.show()

# 4. CHART 3 — SCATTER PLOT

plt.figure()

popular = df[df['is_popular'] == True]
not_popular = df[df['is_popular'] == False]

plt.scatter(popular['score'], popular['num_comments'], label="Popular")
plt.scatter(not_popular['score'], not_popular['num_comments'], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.show()

# BONUS — DASHBOARD - combining all to one plot
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1
axes[0].barh(top_posts['short_title'], top_posts['score'])
axes[0].set_title("Top Posts")
axes[0].invert_yaxis()

# Chart 2
axes[1].bar(sub_counts.index, sub_counts.values)
axes[1].set_title("Posts per Subreddit")

# Chart 3
axes[2].scatter(popular['score'], popular['num_comments'], label="Popular")
axes[2].scatter(not_popular['score'], not_popular['num_comments'], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

# Overall title
plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.show()
