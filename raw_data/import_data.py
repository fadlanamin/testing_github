#ini import pandas, seaborn sama sqlite
import pandas as pd
import sqlite3

#Ini input data dari csv nya, pastiin di terminal location foldernya udah bener
data_abusive = pd.read_csv('abusive.csv')
data_alay = pd.read_csv('new_kamusalay.csv')
data_raw_text = pd.read_csv('data.csv')

# Ini Data Clean up (Removing white spaces kalo ada)
data_abusive.columns = data_abusive.columns.str.strip()
data_alay.columns = data_alay.columns.str.strip()
data_raw_text.columns = data_raw_text.columns.str.strip()

# Connect/Create to sqlite database

#Ini import database dari csv jadi db
connection_abusive = sqlite3.connect('abusive.db')
connection_alay = sqlite3.connect('kamus_alay.db')
connection_raw_text = sqlite3.connect('data_raw.db')

#ini Load data file to sqlite
data_abusive.to_sql('data_abusive', connection_abusive, if_exists='replace')
data_alay.to_sql('data_alay', connection_alay, if_exists='replace')
data_raw_text.to_sql('data_raw_text', connection_raw_text, if_exists='replace')

#ini close the connection
