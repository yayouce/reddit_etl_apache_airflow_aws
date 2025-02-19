from etls.reddit_etl import connect_reddit, extract_post, load_data_to_csv, transform_data
from utils.constants import CLIENT_ID, OUTPUT_PATH,SECRET
import pandas as pd


def reddit_pipeline(file_name:str,subreddit:str,time_filter="@daily",limit=None):
    # connexion à l'instance reddit
    instance =connect_reddit(CLIENT_ID,SECRET,'airscholar agent')
    #extraction
    posts= extract_post(instance,subreddit,time_filter,limit)
    post_df=pd.DataFrame(posts)
    #transformation
    post_df = transform_data(post_df)
    #loading to csv
    file_path=f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df,file_path)
    return file_path
