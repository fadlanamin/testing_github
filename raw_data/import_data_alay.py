import pandas as pd
import sqlite3

#Ini input data dari csv nya, pastiin di terminal location foldernya udah bener
data_alay = pd.read_csv('new_kamusalay.csv')

# Ini Data Clean up (Removing white spaces kalo ada)
data_alay.columns = data_alay.columns.str.strip()

# Connect/Create to sqlite database

#Ini import database dari csv jadi db
connection = sqlite3.connect('abusive.db')

#ini Load data file to sqlite
data_alay.to_sql('data_abusive', connection, if_exists='replace')