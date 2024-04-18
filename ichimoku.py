

# برسي سهام دربورس ايران باپايتون3 فقط باتايپ نام سهم به فارسي
# وبازدن اينتر محاسبات راانجام داده وبه شمانشان ميدهد
# محاسبات RSI - ichimoku - EMA - Volume - Profit and loss - Charts - Canal - Moving 103 - Candel

import time
import math
import numpy as np
import pandas as pd
import finpy_tse as tse
import mplfinance as mplf
import scipy.stats as stt
import matplotlib.pyplot as plt
import pandas_ta as ta
import yfinance as yf
import pandas_datareader.data as web
from datetime import date
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

print ("="*15,"برسي سهام دربورس ايران باايچيموکو","="*15)
print ()

nam = input ("Hello,Please write the name of the stock you want : \n لطفا نام سهام موردنظرتان رابنويسسد :")


DF = tse.Get_Price_History(stock=nam,
                            start_date='1401-01-01',
                            end_date='1403-01-20',
                            ignore_date=True,
                            adjust_price=True,
                            show_weekday=True,
                            double_date=True)


DropList = ['Open', 'High', 'Low', 'Close', 'Final']

DF.drop(columns=DropList, axis=1, inplace=True)

RenameDict = {'Adj Open': 'Open',
               'Adj High': 'High',
               'Adj Low': 'Low',
               'Adj Close': 'Close',
               'Adj Final': 'Final',
               'Adj Max ' : 'Max '}

DF.rename(columns=RenameDict, inplace=True)

#=====================================================
# Get today's price قيمتهاي روزانه
print ()
today_price_max = DF['High'].iloc[-1] # بالاترين قيمت امروز
today_price_min = DF['Low'].iloc[-1]  # پايين ترين قيمت امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
today_price = DF['Close'].iloc[-1] # قيمت بسته شدن امروز
today_Final_price = DF['Final'].iloc[-1] # قيمت آخرين معامله امروز

today_price_max4 = DF['High'].iloc[-4]    #بالاترين قيمت 4روزپيش
today_price_min4 = DF['Low'].iloc[-4]      #پايين ترين قيمت 4روزپيش
today_two_price_min6 = DF['Low'].iloc[-6]  # پايين ترين قيمت 6روزقبل
today_price_max8 = DF['High'].iloc[-8]     #ب8#
today_price_min8 = DF['Low'].iloc[-8]       #پ8#
today_price_max12 = DF['High'].iloc[-12]    #ب12#
today_price_min12 = DF['Low'].iloc[-12]     #پ12#

yesterday_price_max = DF['High'].iloc[-2] # بالاترين قيمت ديروز
yesterday_price_min = DF['Low'].iloc[-2]  # پايين ترين قيمت ديروز
yesterday_Open_price = DF['Open'].iloc[-2] # قيمت بازشدن ديروز
yesterday_price = DF['Close'].iloc[-2] # قيمت بسته شده ديروز
yesterday_Final_price = DF['Final'].iloc[-2] #قيمت آخرين معامله ديروز

today_two_price_max = DF['High'].iloc[-3] # بالاترين قيمت پريروز
today_two_price_min = DF['Low'].iloc[-3]  # پايين ترين قيمت پريروز
today_two_Open_price = DF['Open'].iloc[-3] # بازشدن قيمت پريروز
today_two_price = DF['Close'].iloc[-3] # بسته شدن قيمت پريروز
today_two_Final_price = DF['Final'].iloc[-3] # قيمت آخرين معامله پريروز

print(f"today_Open_price: {today_Open_price} , yesterday_Open_price: {yesterday_Open_price} , today_two_Open_price: {today_two_Open_price}")
print(f"today_price: {today_price}      , yesterday_price : {yesterday_price}        , today_two_price: {today_two_price}")
print(f"today_price_max: {today_price_max}   , yesterday_price_max: {yesterday_price_max}   , today_two_price_max: {today_two_price_max}")
print(f"today_price_min: {today_price_min}   , yesterday_price_min: {yesterday_price_min}   , today_two_price_min: {today_two_price_min}")
print(f"today_Final_price: {today_Final_price} , yesterday_Final_price: {yesterday_Final_price} , today_two_Final_price: {today_two_Final_price}")

print ()

#================================================     
if today_price > yesterday_price:
     print (' قيمت امروزبالاترازديروزه ')
else :
     if today_price < yesterday_price:
          print (' قيمت امروزپايين ترازديروزه ')

#بدست آوردن درصدنوسان قيمتي امروز
nv1=today_price_max-today_price_min
nv2=(today_price_max+today_price_min)/2
jnv=nv1/nv2
jnv1=jnv*100
#بدست آوردن تفاوت درصدي قيمت ديروزبه امروز
n1=today_price-yesterday_price
n2=(today_price+yesterday_price)/2
j1=n1/n2
j2=j1*100
print (math.ceil(j2) ,': درصدتفاوت قيمت ديروزبه امروز')
print (n1 ,' : تفاوت قيمت ديروزبه امروزبه ريا ل')
print (math.ceil(jnv1) ,': درصدنوسان قيمتي امروز')
print()          
#===========================================================

max_price = DF['High'].iloc[-9:] # بالاترين قيمت هاي 9روز ten_max
min_price = DF['Low'].iloc[-9:]  # پايين ترين قيمت هاي 9روز ten_min

max_price2 = DF['High'].iloc[-26:] # بالاترين قيمت هاي 26 روزگذشته kij_max
min_price2 = DF['Low'].iloc[-26:]  # پايين ترين قيمت هاي 26 روزگذشته kij_min


# Get the closing prices for the last 10and26 days
closing_prices7 = DF['Close'].iloc[-3:]       # قيمت بسته شدن 3روزگذشته
closing_prices = DF['Close'].iloc[-10:]      # قيمت بسته شدن 10روز گذشته
closing_prices8 = DF['Close'].iloc[-20:]      # قيمت بسته شدن 20روزگذشته
closing_prices2 = DF['Close'].iloc[-26:]     # قيمت بسته شدن 26 روزگذشته
closing_prices3 = DF['Close'].iloc[-50:]     # قيمت بسته شدن 50روزگذشته
closing_prices4 = DF['Close'].iloc[-103:]    # قيمت بسته شدن 103روزگذشته
closing_prices5 = DF['Close'].iloc[-150:]    # قيمت بسته شدن 150روزگذشته
closing_prices6 = DF['Close'].iloc[-5:]      # قيمت بسته شدن 5 روزگذشته
closing_prices9 = DF['Close'].iloc[-4:]       # قيمت بسته شدن 4 روزگذشته
closing_prices10 = DF['Close'].iloc[-11:]      # قيمت بسته شدن 11 روزگذشته
closing_prices99 = DF['Close'].iloc[-99:]    # قيمت بسته شدن 99 روز
closing_prices94 = DF['Close'].iloc[-94:]    # 94
closing_prices89 = DF['Close'].iloc[-89:]    # 89
closing_prices84 = DF['Close'].iloc[-84:]    # 84
closing_prices79 = DF['Close'].iloc[-79:]    # 79

Volume_week = DF['Volume'].iloc[-5] # حجم هفتگي
Volume_Month = DF['Volume'].iloc[-26] # حجم ماهيانهBase volume
today_Volume = DF['Volume'].iloc[-1] # حجم امروز
today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز
today_Volume_yesterday2 = DF['Volume'].iloc[-3] # حجم سه روزقبل

# Calculate the average price محاسبه ميانگين هاي 10 و 26
average_price = closing_prices.mean()   #محاسبه ميانگين قيمت بسته شدن 10 روز
average_prices2 = closing_prices2.mean() # محاسبه ميانگين قيمت بسته شدن26روز
average_prices3 = closing_prices3.mean() #محاسبه ميانگين قيمت بسته شدن 50روز
average_prices4 = closing_prices4.mean() #محاسبه ميانگين قيمت بسته شدن 103روز
average_prices5 = closing_prices5.mean() #محاسبه ميانگين قيمت بسته شدن 150روز
average_prices6 = closing_prices6.mean() # محاسبات ميانگين قيمت بسته شدن 5روز
average_prices7 = closing_prices7.mean() #محاسبه ميانگين 3روزه
average_prices8 = closing_prices8.mean() #محاسبه ميانگين 20روزه
average_prices9 = closing_prices9.mean() #محاسبه ميانگين 4 روزه
average_price10 = closing_prices10.mean() #محاسبه ميانگين 11 روزه
average_prices99 = closing_prices99.mean() #ميانگين قيمت 99
average_prices94 = closing_prices94.mean() #94
average_prices89 = closing_prices89.mean() #89
average_prices84 = closing_prices84.mean() #84
average_prices79 = closing_prices79.mean() #79


average_max_price = max_price.mean() # ميانگين بالاترين قيمت 9روز ten_max_m9
average_min_price = min_price.mean() # ميانگين پايين ترين قيمت 9روز ten_min_m9

average_max_price2 = max_price2.mean() # ميانگين بالاترين قيمت 26روز kij_max_m26
average_min_price2 = min_price2.mean() #ميانگين پايين ترين قيمت 26روز kij_min_m26

average_Volume_week = Volume_week.mean() # محاسبه ميانگين حجم هفتگي
average_Volume_Month = Volume_Month.mean() # محاسبه ميانگين حجم ماهيان
#=====================================================
print ('='*20 ,"Calculations done RSI  ")

rsi = ta.momentum.rsi(DF['Close'], length=14)

rsi_diff = rsi
print(rsi.tail(3))

print ()
Month_price = DF['Final'].iloc[-26] # آخرين قيمت 30روزقبل
Month_price1 = DF['Final'].iloc[-25] # آخرين قيمت 29روزقبل
Month_price2 = DF['Final'].iloc[-24] # آخرين قيمت 28روزقبل
rsi_Month26 = rsi_diff.iloc[-26]  # يک ماه قبل rsi
rsi_Month25 = rsi_diff.iloc[-25]  #rsi 29روزقبل
rsi_Month24 = rsi_diff.iloc[-24]  # rsi 28روزقبل
rsi_Month = rsi_diff.iloc[-1]  # rsi امروز
rsi_Month1 = rsi_diff.iloc[-2]  #rsi ديروز
rsi_Month2 = rsi_diff.iloc[-3]  # rsi پري روز

# واگرايي منفي درفله ها
if (today_Final_price<yesterday_Final_price>today_two_Final_price) > (Month_price<Month_price1>Month_price2): 
    if (rsi_Month26 < rsi_Month25 > rsi_Month24) < 50<=(rsi_Month < rsi_Month1 > rsi_Month2)>=70:
        print ('sell down price : واگرايي منفي rsi')
    else:
        if (today_Final_price<yesterday_Final_price>today_two_Final_price) < (Month_price<Month_price1>Month_price2):
            if 50<=(rsi_Month26 < rsi_Month25 > rsi_Month24)>=70 > (rsi_Month < rsi_Month1 > rsi_Month2):
                print ('sell down price : واگرايي منفي rsi')
                

#واگرايي مثبت دردره ها
if (today_Final_price>yesterday_Final_price<today_two_Final_price) > (Month_price>Month_price1<Month_price2): 
    if (rsi_Month26 > rsi_Month25 < rsi_Month24) < 50>=(rsi_Month > rsi_Month1 < rsi_Month2)<=30:
        print ('Buy top price: واگراي مثبت شده rsi')
    else:
        if (today_Final_price>yesterday_Final_price<today_two_Final_price) < (Month_price>Month_price1<Month_price2):
            if 50>=(rsi_Month26 > rsi_Month25 < rsi_Month24)<=30 > (rsi_Month > rsi_Month1 < rsi_Month2):
                print ('Buy top price: واگراي مثبت شده rsi')
        

if rsi_diff.iloc[-2] < rsi_diff.iloc[-1] >= 50 :      
     print(" Rsi : ورود به بالاي 50 ")
else:
     if rsi_diff.iloc[-2] > rsi_diff.iloc[-1] <= 50 :      
          print(" Rsi : ريزش به زير50 ")
                

if rsi_diff.iloc[-2] > rsi_diff.iloc[-1] <= 30 :      
     print(" Rsi : ورود به منطقه اشباع فروش ")
else:
     if rsi_diff.iloc[-2] < rsi_diff.iloc[-1] >= 70:
          print(" Rsi : ورود به منطقه اشباع خريد")
                

if rsi_diff.iloc[-2] < rsi_diff.iloc[-1] >= 30 :      
     print(" Rsi : خروج ازمنطقه اشباع فروش ")
else:
     if rsi_diff.iloc[-2] > rsi_diff.iloc[-1] <= 70 :
          print(" Rsi : خروج ازمنطقه اشباع خريد")


if (rsi_diff.iloc[-3])<(rsi_diff.iloc[-2])<(rsi_diff.iloc[-1])>70:
     print (' RSI  >  70')
else:
    if (rsi_diff.iloc[-3])>(rsi_diff.iloc[-2])>(rsi_diff.iloc[-1])<70:
         print (' RSI  <  70')

         
if (rsi_diff.iloc[-3])<(rsi_diff.iloc[-2])<(rsi_diff.iloc[-1])>50:
     print (' RSI  >  50')
else:
    if (rsi_diff.iloc[-3])>(rsi_diff.iloc[-2])>(rsi_diff.iloc[-1])<50:
         print (' RSI  <  50')

         
if (rsi_diff.iloc[-3])<(rsi_diff.iloc[-2])<(rsi_diff.iloc[-1])>30:
     print (' RSI  >  30')
else:
    if (rsi_diff.iloc[-3])>(rsi_diff.iloc[-2])>(rsi_diff.iloc[-1])<30:
         print (' RSI  <  30')


#=====================================================
print ()         
print ('='*30,' candle DOje')
DOje1= (today_price_max+today_price_min)/2
DOje2= DOje1 + 20
DOje3= DOje1 - 20

if today_Final_price == DOje1 :
    print (' کندل دوجي شکل گرفته')



if today_price_max > today_Final_price >= DOje2:
    print (' کندل دوجي سبزشکل گرفته')
else:
    if today_price_min < today_Final_price <= DOje3:
        print (' کندل دوجي قرمزشکل گرفته')



if today_Open_price < today_Final_price > DOje1:
    print (' candle Green')
else:
    if today_Open_price > today_Final_price < DOje1:
        print (' candle Red')



if today_Open_price < today_Final_price == today_price_max > (today_price_min+150):
    print (' candle marabozo Green')
else:
    if today_Open_price > today_Final_price == today_price_min < (today_price_max-150):
        print (' candle marabozo Red')


#=====================================================
print()
print(40*"=",nam,"Volume")

print(f"today_Volume : {today_Volume}    ,    oday_Volume_yesterday : {today_Volume_yesterday}")
print (20*'-')

if today_Volume > (math.ceil(average_Volume_Month)):
     print ('حجم امروزبيشترازحجم ماهيانه شده')
else:
     if today_Volume < (math.ceil(average_Volume_Month)):
          print ('حجم امروزکمتر ازحجم ماهيانه شده')
          

if today_Volume < today_Volume_yesterday < Volume_week:
     print ('حجم درهفته گذشته کاهشي بود')
else:
     if today_Volume > today_Volume_yesterday > Volume_week:
         print ('حجم درهفته گذشته افزايشي بود')

          
if today_Volume > today_Volume_yesterday :
     print ('حجم امروزبيشترازحجم ديروزشده')
else:
    if today_Volume < today_Volume_yesterday :
        print ('حجم امروز کمترازحجم ديروزشده')

         
if today_Volume > (math.ceil(average_Volume_Month))*3 :
     print ('حجم امروز بيشترازدوبرابر حجم ماهيانه شده')
else:
    if today_price > 4*(average_Volume_week):
         print (" حجم امروز 4برابر حجم هفتگي ميباشد")


if today_Volume > today_Volume_yesterday and today_price < yesterday_price :
    print ("sell : قيمت داره ميادپايين حجم ميره بالابفروش")
else:
    if today_Volume < today_Volume_yesterday and today_price > yesterday_price :
        print ("sell : حجم داره ميادپايين قيمت ميره بالا بفروش")


if today_Volume > today_Volume_yesterday and today_price > yesterday_price :
    print ("buy : حجم وقيمت هردوميره بالا يااول حمايت بخرياباشکست مقاومت بخر")
else:
    if today_Volume < today_Volume_yesterday and today_price < yesterday_price :
        print ("buy : حجم وقيمت هردوداره ميادپايين نزديک حمايت بخر")


if today_price>today_price_max4>today_price_max8>today_price_max12:
    print ("بعدازدوازده روزسقف جديدزديم")
else:
    if today_price<today_price_min4<today_price_min8<today_price_min12:
        print ("بعدازدوازده روز کف جديدزديم")


if today_Volume_yesterday2 < today_Volume_yesterday < today_Volume :
    print ('سه روزحجم داره ميره بالا')
else:
    if today_Volume_yesterday2 > today_Volume_yesterday > today_Volume :
        print ('سه روزحجم داره ميره پايين')


if today_price > yesterday_price > today_two_price :
    print ('سه روز قيمت داره ميره بالا')
else:
    if today_price < yesterday_price < today_two_price :
        print ('سه روز قيمت داره ميره پايين')


print ()

#==================================================       
print(40*"=",nam,"One year support and resistance")
# Engulfing Calculations  محاسبات اينگل فينگ
today_price = DF['Close'].iloc[-1]   # آخرین قیمت امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
yesterday_price = DF['Close'].iloc[-2] # آخرین قیمت دیروز
yesterday_Open_price = DF['Open'].iloc[-2] # قيمت بازشدن ديروز
# محاسبات مقاومت هفتگي تاساليانه 
highest_price_7 = max(DF['High'][-7:])    #محاسبه مقاومت هفتگي
highest_price_10 = max(DF['High'][-10:])
highest_price_30 = max(DF['High'][-30:])
highest_price_33 = max(DF['High'][-33:])
highest_price_60 = max(DF['High'][-60:])
highest_price_90 = max(DF['High'][-90:])
highest_price_180 = max(DF['High'][-180:])
highest_price_280 = max(DF['High'][-280:])
highest_price_360 = max(DF['High'][-360:])    #محاسبه مقاومت ساليانه
#------------------------
# محاسبات حمايت هفتگي تاساليانه
lowest_price_7 = min(DF['Low'][-7:])         #محاسبه حمايت هفتگي
lowest_price_10 = min(DF['Low'][-10:])
lowest_price_30 = min(DF['Low'][-30:])
lowest_price_33 = min(DF['Low'][-33:])
lowest_price_60 = min(DF['Low'][-60:])
lowest_price_90 = min(DF['Low'][-90:])
lowest_price_180 = min(DF['Low'][-180:])
lowest_price_280 = min(DF['Low'][-280:])                              
lowest_price_360 = min(DF['Low'][-360:])       #محاسبه حمايت ساليانه

# محاسبه قيمتي مابين حمايت ومقاومت يکساله
mohasebeh = (highest_price_360 + lowest_price_360)/2
# محاسبه قيمتي مابين نيمه حمايت ومقاومت بامقاومت يکساله
mohasebeh1= (mohasebeh + highest_price_360)/2
# محاسبه قيمتي مابين نيمه حمايت ومقاومت باحمايت يکساله
mohasebeh2= (mohasebeh + lowest_price_360)/2
# ازمقاومت سه ماهه 50تاکم کرديم براي محاسبات سقف کانال
kh_3=(highest_price_90)-50
# به حمايت سه ماهه 50تا اضافه کرديم براي محاسبات کف کانال
kL_3=(lowest_price_90)+50

if today_price > yesterday_price > today_two_price:
    print (today_price,' قيمت سه روزه افزايشي ميباشد')
else:
    if today_price < yesterday_price < today_two_price:
        print (today_price,' قيمت سه روزه کاهشي ميباشد')
        
        

#تشخيص روند
if highest_price_90>=highest_price_60>=highest_price_30>=today_price>=lowest_price_90<=lowest_price_60<=lowest_price_30:
    print (' کانال سه ماه رنج شده')
elif highest_price_60>=highest_price_30>=today_price>=lowest_price_60<=lowest_price_30:
     print (' کانال ماهيانه رنج شده')
else :
     if kh_3 <= today_price <= highest_price_90 :
          print ('قيمت به سقف کانال سه ماه رسيده')
     elif kL_3 >= today_price >= lowest_price_90 :
          print ('قيمت به کف کانال سه ماه رسيده')
          


#قرارگرفتن قيمت درنزديکي حمايت ومقاومت هاي هفتگي به بالا
if today_price < highest_price_7 < yesterday_price:
     print ('قيمت مقاومت هفتگي رو بطرف پايين شکست')
elif today_price > highest_price_7 > yesterday_price:
     print ('قيمت مقاومت هفتگي روبطرف بالاشکست')
else:
     if today_price < lowest_price_7 < yesterday_price:
         print ('قيمت حمايت هفتگي روبطرف پايين شکست')
     elif today_price > lowest_price_7 > yesterday_price:
          print ('قيمت حمايت هفتگي روبطرف بالاشکست')
          


if today_price < highest_price_60 < yesterday_price:
     print ('قيمت مقاومت ماهيانه روبطرف پايين شکست')
elif today_price > highest_price_60 > yesterday_price:
     print ('قيمت مقاومت ماهيانه روبطرف بالا شکست')
else:
     if today_price < lowest_price_60 < yesterday_price:
         print ('قيمت حمايت ماهيانه روبطرف پايين شکست')
     elif today_price > lowest_price_60 > yesterday_price:
          print ('قيمت حمايت ماهيانه روبطرف بالا شکست')
          


if today_price < highest_price_280 < yesterday_price:
     print ('قيمت مقاومت يکساله رابطرف پايين شکست')
elif today_price > highest_price_280 > yesterday_price:
     print ('قيمت مقاومت يکساله روبطرف بالاشکست')
else:
     if today_price < lowest_price_280 < yesterday_price:
         print ('قيمت حمايت يکساله روبطرف پايين شکست')
     elif today_price > lowest_price_280 > yesterday_price:
          print ('قيمت حمايت يکساله روبطرف بالاشکست')
        


if highest_price_180>highest_price_90>highest_price_30>=today_price_max>=lowest_price_30<lowest_price_90<lowest_price_180:
    print ("کانال کاهشي يکساله داريم")
else:
    if highest_price_180<highest_price_90<highest_price_30>=today_price_max>=lowest_price_30>lowest_price_90>lowest_price_180:
         print ("کانال افزايشي يکساله داريم")
         


if highest_price_90>highest_price_60>highest_price_30>=today_price_max>=lowest_price_30<lowest_price_60<lowest_price_90:
    print ("کانال کاهشي 90روزه داريم")
else:
    if highest_price_90<highest_price_60<highest_price_30>=today_price_max>=lowest_price_30>lowest_price_60>lowest_price_90:
         print ("کانال افزايشي 90روزه داريم")
         


if highest_price_60>highest_price_30>=today_price_max>=lowest_price_30<lowest_price_60  :
    print ("کانال کاهشي ماهيانه داريم")
else:
    if highest_price_60<highest_price_30>=today_price_max>=lowest_price_30>lowest_price_60 :
         print ("کانال افزايشي ماهيانه داريم")
         

    
if highest_price_90 <=  lowest_price_90 :
    print ("حمايت تبديل به مقاومت شد")

    
print ()
print ('-'*20,' حمايت ومقاومت هاي هفتگي وماهيانه')
print ()
print(f"Weekly support : {lowest_price_7}    ,    Weekly resistance : {highest_price_7}")
print(f"Monthly support : {lowest_price_60}  ,    Monthly resistance : {highest_price_60}")

# براي انجام محاسبات مقاومت وحمايتهامقدار20تا کم يازيادکرديم
m_7=(highest_price_7)-20
m_30=(highest_price_60)-20
m_360=(highest_price_360)-20
h_7=(lowest_price_7)+20
h_30=(lowest_price_60)+20
h_360=(lowest_price_360)+20


if m_7 <= today_price <= highest_price_7 :
     print ('قيمت نزديک مقاومت هفتگي ميباشد')
elif m_30 <= today_price <= highest_price_60 :
     print ('قيمت نزديک مقاومت ماهيانه ميباشد')
elif m_360 <= today_price <= highest_price_360 :
     print ('قيمت نزديک مقاومت ساليانه ميباشد')
else:
     if h_7 >= today_price >= lowest_price_7 :
          print ('قيمت نزديک حمايت هفتگي ميباشد')
     elif h_30 >= today_price >= lowest_price_60 :
          print ('قيمت نزديک حمايت ماهيانه ميباشد')
     elif h_360 >= today_price >= lowest_price_360 :
          print ('قيمت نزديک حمايت ساليانه ميباشد')
          
             
print ()
#=====================================================
print(30*"=",nam,"ichimoku Signals for buying and selling  ")
# Ensure the DataFrame is sorted by date
DF.sort_values('Date', inplace=True)

# محاسبات تنکانسن8 روزه به قبل
# Calculate the highest and lowest price over the past 26 day

window_size = 12
past_12_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_12_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
ten12 = (past_12_days_high + past_12_days_low)/2

window_size = 11
past_11_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_11_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
ten11 = (past_11_days_high + past_11_days_low)/2

window_size = 10
past_10_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_10_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
ten10 = (past_10_days_high + past_10_days_low)/2

window_size = 9
past_9_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_9_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
ten9 = (past_9_days_high + past_9_days_low)/2
tenken9 = (math.ceil(ten9))

window_size = 8
past_8_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_8_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
ten8 = (past_8_days_high + past_8_days_low)/2
tenken8 = (math.ceil(ten8))

#print ('ten9 :',(math.ceil(ten9)))
#print ('ten8 :',(math.ceil(ten8)))

# محاسبات کيجونسن26 روزه به قبل
# Calculate the highest and lowest price over the past 26 days

window_size = 26
past_26_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_26_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
kij26 = (past_26_days_high + past_26_days_low)/2
kijon26 = (math.ceil(kij26))

window_size = 27
past_27_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_27_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
kij27 = (past_27_days_high + past_27_days_low)/2
kijon27 = (math.ceil(kij27))

window_size = 28
past_28_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_28_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
kij28 = (past_28_days_high + past_28_days_low)/2

window_size = 29
past_29_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_29_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
kij29 = (past_29_days_high + past_29_days_low)/2

window_size = 30
past_30_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_30_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
kij30 = (past_30_days_high + past_30_days_low)/2

#print ('kij26 :',(math.ceil(kij26)))
#print ('kij27 :',(math.ceil(kij27)))

print(f"ten8: {tenken8}   ,    kij26 : {kijon26}")
print(f"ten9: {tenken9}   ,    kij27 : {kijon27}")
print ()

# محاسبات ابرکومو52 روزه به قبل
# Calculate the highest and lowest price over the past 26 days
window_size = 52
past_52_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_52_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
komu52_max = (math.ceil(past_52_days_high))
komu52_min = (math.ceil(past_52_days_low))

print(f"komu52_max: {komu52_max}  ,  komu52_min: {komu52_min} ")
#print(f"komu52_min: {komu52_min}")
print ()


if ten12<ten11<ten10<=ten9>=ten8 < today_two_price<yesterday_price>today_price > kij26==kij27==kij28>=kij29>=kij30 :
     print ('به احتمال زياد سقف روند صعوديه مواظب ريزش باش')
else:
     if ten12>ten11>ten10>=ten9>=ten8 > today_two_price>yesterday_price<today_price < kij26==kij27==kij28<=kij29<=kij30 :
          print ('به احتمال زياد کف روند نزوليه مراقب صعودي شدن روند باش')



if kij28<=kij27<=kij26< ten8 >ten9>ten10 <today_price> yesterday_price and today_Volume> today_Volume_yesterday:
    print ('Signal buy : تنکانسن بالاي کيجونسن رفت')
else :
    if kij28>=kij27>=kij26> ten8 <ten9<ten10 >today_price< yesterday_price and today_Volume> today_Volume_yesterday:
        print ('Signal sell : تنکانسن پايين کيجونسن رفت')



if kij27<kij26 <ten8 >ten9<today_price> yesterday_price >komu52_min:
    print ('قيمت بالاي ابرسبزميباشد وروندصعودي شده')
else :
    if kij27>kij26 >ten8 <ten9>today_price< yesterday_price <komu52_min:
        print ('قيمت پايين ابرقرمزه وروندنزولي شده')



if komu52_max > kij30>=kij29>=kij28>=kij27>=kij26 <ten8>ten9< today_price>yesterday_price>=today_two_price :
    print ('قيمت زيرابرقرمزوفلت کيجونسن رو روبه بالاقطع کرد')
    print ('--- Signal buy : قوي ---')
else:
    if komu52_min < kij30<=kij29<=kij28<=kij27<=kij26 >ten8<ten9> today_price<yesterday_price<=today_two_price :
        print ('قيمت بالاي ابرسبز وفلت کيجونسن رو روبه پايين قطع کرد')
        print ('--- Signal sell : قوي ---')

        

if komu52_min<kij30<=kij29<=kij28<=kij27<=kij26<ten8>=ten9>=ten10>=ten11>=ten12 >today_price<yesterday_price :
    print ('فلت کيجونسن بالاي ابر،وقيمت تنکانسن رو روبه پايين قطع کرده')
    print ('--- Signal sell : بسيارقوي ---')
else:
    if komu52_min>kij30>=kij29>=kij28>=kij27>=kij26>ten8<=ten9<=ten10>=ten11>=ten12 <today_price>yesterday_price :
        print ('فلت کيجونسن زيرابر،وقيمت تنکانسن رو روبه بالاقطع کرده')
        print ('--- Signal buy : بسيارقوي ---')



if yesterday_price <today_price>komu52_max <ten8>ten9 >=kij27<kij26 :
    print ('تنکانسن وکيجونسن وقيمت ابر رو روبه بالاقطع کردند')
    print ('/// Signal buy : خريدکن ////')
else:
    if yesterday_price >today_price<komu52_max >ten8<ten9 <=kij27>kij26 :
        print ('تنکانسن وکيجونسن وقيمت ابر رو روبه پايين قطع کردند')
        print ('/// Signal sell : بفروش ////')



if komu52_max>kij30>=kij29>=kij28>=kij27>=kij26<ten8>ten9<=today_price>yesterday_price:
    print ('زيرابرکوموهو قيمت وتنکانسن هردوفلت کيجونسن رو روبه بالاقطع کردن')
    print ('/// Signal buy : بااحتياط خريدکن ////')
else:
    if komu52_min<kij30<=kij29<=kij28<=kij27<=kij26>ten8<ten9>=today_price<yesterday_price:
        print ('بالاي ابرکوموهو قيمت وتنکانسن هردو فلت کيجونسن رو روبه پايين قطع کردن')
        print ('/// Signal sell : بااحتياط بفروش ////')



if today_price>yesterday_price > ten8>ten9 > kij26>kij27:
    print ('روند صعودي است چون قيمت بالاي تنکانسن وکيجونسن است')
else:
    if today_price<yesterday_price < ten8<ten9 < kij26<kij27:
        print ('روند نزولي است چون قيمت پايين تنکانسن وکيجونسن است')



if kij30<=kij29<=kij28<=kij27<=kij26 >today_price>yesterday_price< ten8<=ten9<=ten10<=ten11<=ten12 :
     print ('قيمت زيرتنکانسن ميباشد وروبه بالابطرف کيجونسن ميرود')
else:
    if kij30>=kij29>=kij28>=kij27>=kij26 <today_price<yesterday_price> ten8<=ten9<=ten10<=ten11<=ten12 :
         print ('قيمت بالاي تنکانسن ميباشد وروبه پايين بطرف کيجونسن ميرود')



if kij30>=kij29>=kij28>=kij27>=kij26>yesterday_price and kij26 < today_price :
     print ('--- Signal buy :خيلي خيلي مهم : قيمت کيجونسن رو روبه بالا قطع کرد ---')
else:
     if kij30<=kij29<=kij28<=kij27<=kij26<yesterday_price and kij26> today_price :
          print ('--- Signal sell :خيلي خيلي مهم : قيمت کيجونسن رو روبه پايين قطع کرد ---')



if kij30>=kij29>=kij28>=kij27>=kij26 > today_price>=yesterday_price>=today_two_price :
     print ('احتمال صعود: قيمت سه روزه روبه بالا وبه سمت کيجونسن درحرکت است')
else:
     if kij30<=kij29<=kij28<=kij27<=kij26 < today_price<=yesterday_price<=today_two_price :
          print ('احتمال ريزش شديد: قيمت سه روزه روبه پايين وبه سمت کيجونسن درحرکت است')

   

if today_price >= yesterday_price >= today_two_price > kij26 >= kij27 >= kij28 :
     print ('***همچنان قيمت بالاي کيجونسن ميباشدواحتمالاروندصعودي است***')
else:
     if today_price <= yesterday_price <= today_two_price < kij26 <= kij27 <= kij28 :
          print ('***همچنان قيمت پايين کيجونسن ميباشد واحتمالا روندنزولي است***')

          

print ()
#================================================
print(40*"=",nam,"Engulfing Calculations")
# Engulfing  ascending صعودي
h1 = today_price > today_Open_price
h2 = yesterday_Open_price > yesterday_price
h3 = yesterday_price > today_Open_price
h4 = today_price > yesterday_Open_price

h_ascending = h1 and h2 and h3 and h4
h5 = (today_price - today_Open_price) > 5*(yesterday_Open_price - yesterday_price) 

# Engulfing  Descending نزولي
h6 = today_price < today_Open_price
h7 = yesterday_Open_price < yesterday_price
h8 = yesterday_price < today_Open_price
h9 = today_price < yesterday_Open_price

h_Descending = h6 and h7 and h8 and h9
h10 = (today_price - today_Open_price) < 5*(yesterday_Open_price - yesterday_price)


     
if  h5:
    c = "Engulfing :"
    print (c , "hemer ascending !  صعودي مناسب خريد" )
elif  h10 :
    c = "Engulfing :"
    print (c , "hemer Descending !  نزولي وقت فروش" )
else:
    c = "hold :"
    print (c , "not Engulfing !")
    print ("نمودارهاي قيمت هنوزاينگل فينگي تشکيل ندادند")
    
print ('~'*10)
print ('بودن روند False يا True دقت کنيدبه')
print (h5,': ascending روند صعودي ')
print (h10 ,': Descending روند نزولي')

#=================================================
print ('='*40,' ميانگين قيمت')
#ميانگين قيمت 10 و20 روزسهم
# Calculate the 10-day moving average
avg_10_days = DF['Close'].rolling(window=10).mean().iloc[-1]
avg_20_days = DF['Close'].rolling(window=20).mean().iloc[-1]
avg_103_days = DF['Close'].rolling(window=103).mean().iloc[-1]
movind10 = (math.ceil(avg_10_days))
movind20 = (math.ceil(avg_20_days))
movind103 = (math.ceil(avg_103_days))

# Print the most recent price and the 10-day moving average
print(f"today_price : {DF['Close'].iloc[-1]}       ,   moving_price10_day : {movind10}")
print(f"yesterday_price : {DF['Close'].iloc[-2]}   ,   moving_price20_day : {movind20}")
print(f"today_two_price : {DF['Close'].iloc[-3]}   ,   moving_price103_day : {movind103}")
print ()


if today_price>movind10>yesterday_price>today_two_price:
    print ('قيمت امروزرفت بالاي ميانگين ده روزه')
else:
    if today_price > movind10:
        print ('قيمت هنوزبالاي ميانگين ده روزه است')
        

if today_price<movind10<yesterday_price<today_two_price:
    print ('قيمت امروزرفت پايين ميانگين ده روزه')
else:
    if today_price < movind10:
        print ('قيمت هنوزپايين ميانگين ده روزه است')


if today_price>movind103>yesterday_price>today_two_price:
    print ('قيمت امروزرفت بالاي ميانگين 103')
else:
    if today_price > movind103:
        print ('قيمت هنوزبالاي ميانگين 103')
        

if today_price<movind103<yesterday_price<today_two_price:
    print ('قيمت امروزرفت پايين ميانگين 103')
else:
    if today_price < movind103:
        print ('قيمت هنوز پايين ميانگين 103')


print ()
#================================================
print(40*"=",nam,"bmi and omc محاسبه")
# تعریف یک تابع برای محاسبه بی ام آی
def bmi(last_price, adj_close):

     bmi = (adj_close + (last_price*2))/3
     
     # برگرداندن بی ام آی به عنوان خروجی تابع
     return bmi

# دريافت قيمت پاياني  وآخرين قيمت
last_price = today_Final_price
adj_close = today_price
# فراخواني تابع بي ام آي با قيمت پاياني وآخرين قيمت
bmi = bmi(last_price, adj_close)
# نمایش بی ام آی کاربر
print(f" بی ام آی شما {bmi:.2f} است ")
#------------------------------------
print(20*"-")
# تعريف يک تابع براي محاسبه او ام سي (حدس زدن قيمت بسته شدن)
def cmo(open_price, price_min):

     omc = (((today_price_max *2 )+ price_min)/3)-(today_price - yesterday_price)
     
     # برگرداندن او ام سي براي خروجي تابع
     return omc

# دريافت قيمت بازشدن با پايين ترين قيمت امروز
open_price = today_Open_price
price_min = today_price_min
price_max = today_price_max
#فراخاني تابع او ام سي باقيمت بازشدن وپايين ترين قيمت روز
omc = cmo(open_price, price_min)
# نمايش اوام سي به کاربر
print(f" او ام سي شما {omc:.2f} است ")
print(20*"-")

if today_Final_price == price_max:
     print('صف خريدشده')
else:
     if today_Final_price == price_min:
          print ('صف فروش شده')


if omc < bmi :
     print ('omc < bmi : به احتمال زيادفردا قيمت بالاترازامروزه')
else:
    if omc > bmi :
         print ('omc > bmi : به احتمال زيادفردا قيمت پايين ترازامروزه')
         
        
#===============================================
print(40*"=",nam,"Charts EMA_3,10,20 ")
# EMA_3,10,20 نمايش نمودارقيمت و
DF.index = DF['Date']
mplf.plot(DF[-200:], type='candle', mav=(50, 10, 20))
plt.show()
# Calculate the average price for ten days
ten_day_average = DF['Close'].rolling(10).mean()
today_price_scalar = today_price.item()

print (' The graph of the averages was done .')
print ()
#=================================================
#رسم نمودارايچيموکو
print(40*"=",nam,"Charts ichimoku ")
# Convert the 'Date' column to a datetime object
DF['Date'] = pd.to_datetime(DF['Date'])

# Calculate the conversion line (Tenkan-sen)
DF['conversion_line'] = (DF['High'].rolling(9).mean() + DF['Low'].rolling(9).mean()) / 2

# Calculate the base line (Kijun-sen)
DF['base_line'] = (DF['High'].rolling(26).mean() + DF['Low'].rolling(26).mean()) / 2

# Calculate the leading span A (Senkou Span A)
DF['leading_span_a'] = ((DF['conversion_line'].rolling(9).mean()) + (DF['base_line'].rolling(9).mean())) / 2
DF['leading_span_a'] = DF['leading_span_a'].shift(9)

# Calculate the leading span B (Senkou Span B)
DF['leading_span_b'] = ((DF['conversion_line'].rolling(26).mean()) + (DF['base_line'].rolling(26).mean())) / 2
DF['leading_span_b'] = DF['leading_span_b'].shift(26)

# Calculate the lagging span (Chikou Span)
DF['lagging_span'] = DF['Close'].shift(-26)

# Plot the Ichimoku cloud
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(DF['Date'], DF['Close'], label='Close', color='blue', alpha=0.5)
ax.plot(DF['Date'], DF['leading_span_a'], label='Leading Span A', color='green', linestyle='--')
ax.plot(DF['Date'], DF['leading_span_b'], label='Leading Span B', color='red', linestyle='--')
ax.plot(DF['Date'], DF['conversion_line'], label='Conversion Line', color='orange', linestyle='-')
ax.plot(DF['Date'], DF['base_line'], label='Base Line', color='purple', linestyle='-')
ax.plot(DF['Date'], DF['lagging_span'], label='Lagging Span', color='black', linestyle=':')

ax.fill_between(DF['Date'], DF['leading_span_a'], DF['leading_span_b'], alpha=0.2, color='gray')

plt.title('Ichimoku Cloud for {}'.format(nam))
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

print (' The Ichimoku diagram was drawn .')
print ()
#==========================================================
print ('-'*20,' ميانگين حجم')
# ميانگين حجم 7 وچندروزه سهم
# Calculate the 7-day moving average of the volume
avg_1_days = DF['Volume'].rolling(window=1).mean().iloc[-1]
avg_2_days = DF['Volume'].rolling(window=2).mean().iloc[-1]
avg_5_days = DF['Volume'].rolling(window=5).mean().iloc[-1]
avg_26_days = DF['Volume'].rolling(window=26).mean().iloc[-1]
moving_volume1 = (math.ceil(avg_1_days))
moving_volume2 = (math.ceil(avg_2_days))
moving_volume5 = (math.ceil(avg_5_days))
moving_volume26 = (math.ceil(avg_26_days))

# Print the most recent volume and the 7-day moving average
print(f"moving_volume1_day : {moving_volume1}  ,   moving_volume2_day: {moving_volume2}")
print(f"moving_volume5_day : {moving_volume5}  ,   moving_volume26_day: {moving_volume26}")
print ()


if moving_volume1>moving_volume2:
    print ('ميانگين حجم روزانه افزايشي است')
else:
    if moving_volume1<moving_volume2:
        print ('ميانگين حجم روزانه کاهشي است')


if moving_volume5>moving_volume26:
    print ('ميانگين حجم هفتگي نسبت به ماهيانه افزايشي است')
else:
    if moving_volume5<moving_volume26:
        print ('ميانگين حجم هفتگي نسبت به ماهيانه کاهشي است')

#===========================================================


