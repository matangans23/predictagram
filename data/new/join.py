#!/usr/bin/python3
import csv
import pandas as pd
import sqlite3
import json

"""
# connect to sqlite db
conn = sqlite3.connect('./data.db')
c = conn.cursor()

# create table command base
CREATE_TABLE_BASE = "CREATE TABLE IF NOT EXISTS"
"""

# ====================== post data ====================== #

# loading post_data.json into pandas
post_df = pd.read_json('post_data.json', typ='frame')
post_df = post_df[['ownerUsername', 'timestamp', 'firstComment', 'imageUrl', 'url', 'likesCount']]

# filter by timestamp, taking only posts from the last year
post_df = post_df[post_df['timestamp'] > '2019-04-13']

"""
# form create table command
post_df_name = 'post_data'
post_df_cols = (
ownerUsername TEXT PRIMARY KEY,
timeStamp TEXT NOT NULL,
firstComment TEXT,
imageURL TEXT UNIQUE,
url TEXT UNIQUE,
likesCount INTEGER
)
CREATE_POST_TABLE = " ".join([CREATE_TABLE_BASE, post_df_name, post_df_cols])

# execute create table command
c.execute(CREATE_POST_TABLE)
conn.commit()

# convert the data
post_df.to_sql('post_data', conn, if_exists='replace', index = False)
"""

# ====================== page (user) data ====================== #

# load page_data.json into pandas
user_df = pd.read_json('./user_data.json', typ='frame')
user_df = user_df[['username', 'followersCount', 'followsCount', 'isBusinessAccount', 'verified', 'postsCount']]

"""
# form create table command
page_df_name = 'page_data'
page_df_cols = (
username TEXT PRIMARY KEY,
followersCount INTEGER NOT NULL,
followsCount INTEGER NOT NULL,
isBusinessAccount INTEGER NOT NULL,
verified INTEGER NOT NULL,
postsCount INTEGER NOT NULL
)
CREATE_PAGE_TABLE = " ".join([CREATE_TABLE_BASE, page_df_name, page_df_cols])

# execute create table command
c.execute(CREATE_PAGE_TABLE)
conn.commit()

# convert the data
page_df.to_sql('page_data', conn, if_exists='replace', index = False)
"""

# ====================== join dataframes ====================== #

# rename username col of post_df to prepare for join
post_df = post_df.rename(columns={ "ownerUsername" : "username" })

# join the dataframes into a new dataframe called final_df
final_df = post_df.join(user_df.set_index('username'), on='username')

# drop duplicates in the final dataframe
final_df = final_df.drop_duplicates(subset="url")

"""
# generate sample of final_data in final_data_samp.csv
final_df_samp = final_df.sample(30)
"""

# output .csv & .json files
final_df.to_json('data.json', orient='records')
"""
final_df_samp.to_json('final_data_samp.json', orient='records')
final_df.to_csv('final_data.csv')
final_df_samp.to_csv('final_data_samp.csv')
"""
