import configparser
import os
parser = configparser.ConfigParser()#parser est une instance de ConfigParser, une classe de Python qui sert à lire les fichiers de configuration au format INI.

parser.read(os.path.join(os.path.dirname(__file__),'../config/config.conf'))  

SECRET = parser.get('api_key','reddit_secret_key')
CLIENT_ID= parser.get('api_key','reddit_client_id')


DATABASE_HOST=parser.get('database','database_host')
DATABASE_NAME=parser.get('database','database_name')
DATABASE_PORT=parser.get('database','database_port')
DATABASE_USERNAME=parser.get('database','database_username')
DATABASE_PASSWORD=parser.get('database','database_password')


INPUT_PATH = parser.get('file_path','input_path')
OUTPUT_PATH = parser.get('file_path','output_path')



POST_FIELDS=(
    'id',
    'title',
    'selftext',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'upvote_ratio',
    'over_18',
    'edited',
    'spoiler',
    'stickied'

)



