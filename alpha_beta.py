"""
Compute alpha and beta for SPX components
"""


from datetime import datetime, timedelta
import numpy as np
import pandas_datareader.data as reader
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Set up parameters.
n_tickers = 10
n_batch = 50
days_lookback = 365

#Load data from IEX.
data_source = 'iex'
Nasdaq = pd.read_csv("/Users/yajingleo/Documents/companylist.csv")
tickers = Nasdaq.loc[Nasdaq.Sector == "Technology", "Symbol"].values 

end = datetime.today()
start = end - timedelta(days = days_lookback)
SPX = reader.DataReader("SPXC", data_source, start, end)

Return_60d_SPX = ((SPX - SPX.shift(60))/SPX).ix[60:].fillna(0)


Ticker_to_Name = dict(zip(Nasdaq['Symbol'], Nasdaq.Name))

regr = LinearRegression()

#Computing alpha, beta
alpha = []
beta = []
stocks = []
for stock in tickers:
    try:
        stock_data = reader.DataReader(stock, data_source, start, end)
        Return_60d_Stock = ((stock_data - stock_data.shift(60))/stock_data).ix[60:].fillna(0)
        regr.fit(Return_60d_SPX.close.values.reshape(-1, 1), Return_60d_Stock.close.values)
        beta.append(regr.coef_)
        alpha.append(regr.intercept_)
        stocks.append(stock)
    except:
        print stock

Output = pd.DataFrame({"Stock": stocks, "Alpha" : alpha, "Beta": beta})

