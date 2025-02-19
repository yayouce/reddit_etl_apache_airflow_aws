import sys
import pandas as pd
import numpy as np
from pandas import DataFrame
from praw import Reddit
from utils.constants import POST_FIELDS


def connect_reddit(client_id,client_secret,user_agent)->Reddit:
    try:
        reddit=Reddit(client_id=client_id,
                           client_secret=client_secret,
                           user_agent=user_agent)
        print("connected with success")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_post(reddit_instance:Reddit,subreddit:str,time_filter:str,limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter,limit=limit)

    posts_list=[]
    print(posts)
    for post in posts:
        post_dict=vars(post)  # En Python, la fonction vars() est utilisée pour retourner les attributs d'un objet sous forme de dictionnaire.
        
        post = {key:post_dict[key] for key in POST_FIELDS}
        post= posts_list.append(post)
    return posts_list

def transform_data(post_df:DataFrame):
    post_df["created_utc"] = pd.to_datetime(post_df["created_utc"],unit='s')
    post_df["over_18"] = np.where((post_df["over_18"]==True),True,False)
    post_df['author']=  post_df["author"].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df["edited"] = np.where(post_df["edited"].isin([True,False]),post_df["edited"],edited_mode).astype(bool)

    post_df['num_comments']=post_df['num_comments'].astype(int)
    post_df['score']=post_df['score'].astype(int)
    post_df['upvote_ratio']=post_df['upvote_ratio'].astype(int)
    post_df['selftext']=post_df['selftext'].astype(str)
    post_df['title']=post_df['title'].astype(str)


    return post_df


def load_data_to_csv(data:DataFrame,path):
    data.to_csv(path,index=False)



