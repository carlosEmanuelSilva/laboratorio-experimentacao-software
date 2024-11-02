import praw
import os
import json
import csv
from dotenv import load_dotenv, find_dotenv

reddit = praw.Reddit("request")
dict_data = []
# Função para monitorar menções, interações e criação de tópicos no Reddit
def get_hot_reddit(subreddit_name, ):
    for submission in reddit.subreddit(subreddit_name).hot(limit=None):
        data = { 
            "_id": submission.id,
            "title": submission.title,
            "tags": submission.link_flair_text or "",
            "num_comments": submission.num_comments,
            "description": submission.selftext,
            "upvotes": submission.score,
            "shares": submission.ups,
            "upvote_ratio": submission.upvote_ratio,
            "author": submission.author.name if submission.author else "N/A",
            "subreddit": subreddit_name,
        }

        dict_data.append(data)

    save_to_csv(data)

    

def save_to_csv(data):
    filename = "../data/test.csv"
    header = ['_id', 'title', 'tags', 'num_comments', 'description', 'upvotes', 'shares', 'upvote_ratio', 'author', 'subreddit']
   
    if(os.path.isfile(filename)):
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
            writer.writerows(dict_data)
    else:
        with open(filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
            writer.writerows(dict_data)
    dict_data.clear()

data = get_hot_reddit("learnprogramming")
save_to_csv(data)
