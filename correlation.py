
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

df = pd.read_csv ("Foolad.csv",index_col=0,parse_dates=True)
tickers = ['Nafti','Khodro','Foolad','Felezi','Daroo']

df_list = []
for ticker in tickers:
    df = pd.read_csv(ticker+ ".csv", index_col=0,parse_dates=True)
    df_list.append(df['Adj'])

data = pd.concat(df_list,axis=1)
data.columns = tickers
data = np.log(data/data.shift())
data.corr().style.background_gradient(cmap='Blues')
