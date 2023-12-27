
# correlation  محاسبه کرولیشن یاهمان ضریب همبستگی دوسهم رامیگویند
#جدول کرولیشن دراینجا گفته شده دوبه دو محاسبه شود و
#هرچه مقدارضریب همبستگی به یک مثبت یا یک منفی نزدیکتر باشد,همبستگی مثبت یامنفی متغیرها قوی تراست
# ضریب همبستگی مثبت یعنی  افزایش یک متغیربا افزایش متغیردیگروهمچنین کاهش یک متغیرباکاهش 
#متغیردیگرهمراه است
# ضریب همبستگی منفی یعنی افزایش یک متغیرباکاهش متغیردیگروهمچنین کاهش آن متغییر
#باافزایش متغیردیگرهمراه است
# ضریب همبستگی صفریعنی افزایش وکاهش دومتغیرمستقل ازیکدیگربوده وهیچ ارتباطی ندارند
# هرچه مقدارضریب همبستگی به یک مثبت یا یک منفی نزدیکتر باشدهمبستگی مثبت یامنفی متغیرها قوی تراست
# Adj نام ستون قیمتی مییاشد دراینجا

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pyplot
%matplotlib notebook

#df = pd.read_csv ("Foolad.csv",index_col=0,parse_dates=True)
tickers = ['Nafti','Khodro','Foolad','Felezi','Daroo']

df_list = []
for ticker in tickers:
    df = pd.read_csv(ticker+ ".csv", index_col=0,parse_dates=True)
    df_list.append(df['Adj'])

data = pd.concat(df_list,axis=1)
data.columns = tickers
data = np.log(data/data.shift())
#data.corr().style.background_gradient(cmap='Blues')

def lin_regr (ticker_a,ticker_b):
    X = data[ticker_a].iloc[1:].values.reshape(-1, 1)
    Y = data[ticker_b].iloc[1:].values.reshape(-1, 1)

    lin_regressor = LinearRegression()
    lin_regressor.fit(X, Y)
    Y_pred = lin_regressor.predict(X)

    alpha = str(round(lin_regressor.intercept_[0], 5))
    beta = str(round(lin_regressor.coef_[0][0], 5))

    fig, ax = plt.subplots()
    ax.set_title("Alpha: " + alpha + ",Beta: " + beta)
    ax.scatter(X, Y, alpha=0.3)
    ax.plot(X, Y_pred, c='r')


def calc_beta(ticker_a, ticker_b)
    X = data[ticker_a].iloc[1:].values.reshape(-1, 1)
    Y = data[ticker_b].iloc[1:].values.reshape(-1, 1)

    lin_regressor = LinearRegression()
    lin_regressor.fit(X, Y)
    Y_pred = lin_regressor.predict(X)

    return lin_regressor.coef_[0][0]

import itertools

df = pd.DataFrame(None, index=tickers, columns=tickers)
for t1, t2 in itertools.combinations(tickers, 2):
    df.loc[t1][t2] = calc_beta(t1, t2)
    df.loc[t2][t1] = calc_beta(t2, t1)


for t in tickers:
    df .loc[t][t] = calc_beta(t, t)
