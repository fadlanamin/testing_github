#ini import pandas, seaborn sama sqlite
import pandas as pd
import seaborn as sns
import sqlite3


#Ini input data dari csv nya, pastiin di terminal location foldernya udah bener
data_abusive = pd.read_csv('abusive.csv')

#Ini import database dari csv jadi db
sqlite3.connect('abusive.db')