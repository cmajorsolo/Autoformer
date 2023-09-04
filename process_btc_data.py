# The data ./dataset/btc/btc_usd_2012-01-01_to_2021-03-31.csv is downloaded from
# https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data?resource=download

import pandas as pd

# read txt file with assigned header
btc_data = pd.read_csv('./dataset/btc/BTC_full_30min.txt')
# Assign the column names
btc_data.columns = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume_(BTC)']
# Get the first 2000 rows
btc_data = btc_data.iloc[:2000, :]
# save the data to csv file
btc_data.to_csv('./dataset/btc/btc_short.csv', index=False)
