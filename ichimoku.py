

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
                            end_date='1403-02-07',
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

#----------------------------------------
print ()
print("          "," Time information")
import pytse_client as tse
#درج تاريخ ميلادي
import jdatetime
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S %d
dt_string = now.strftime("%Y/%m/%d - %A   %H:%M:%S:%p")
print("date and time =", dt_string)

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

print(f"today_Open_price:{today_Open_price}, yesterday_Open_price:{yesterday_Open_price}, today_two_Open_price:{today_two_Open_price}")
print(f"today_price: {today_price} , yesterday_price : {yesterday_price} , today_two_price: {today_two_price}")
print(f"today_price_max: {today_price_max}, yesterday_price_max: {yesterday_price_max}, today_two_price_max:{today_two_price_max}")
print(f"today_price_min: {today_price_min}, yesterday_price_min: {yesterday_price_min}, today_two_price_min:{today_two_price_min}")
print(f"today_Final: {today_Final_price}   ,  yesterday_Final: {yesterday_Final_price}   ,  today_two_Final: {today_two_Final_price}")

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
print (math.ceil(j2),'% : درصدتفاوت قيمت ديروزبه امروز')
print (n1 ,' : تفاوت قيمت ديروزبه امروزبه ريا ل')
print (math.ceil(jnv1),'% : درصدنوسان قيمتي امروز')
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

if DOje2 >= DOje1>=DOje3 and DOje2 >= today_price>=DOje3:
    print (' کندل دوجي شکل گرفته')


if today_Final_price == DOje1 :
    print (' کندل دوجي قوي شکل گرفته')
     


if today_price_max > today_Final_price >= DOje2:
    print (' کندل دوجي سبزشکل گرفته')
else:
    if today_price_min < today_Final_price <= DOje3:
        print (' کندل دوجي قرمزشکل گرفته')



if today_Open_price < today_price > DOje1:
    print (' candle Green')
else:
    if today_Open_price > today_price < DOje1:
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
#فاصله قيمت با مقاومت سه ماهه
fgh_3=highest_price_90 - today_price
#فاصله قيمت با حمايت سه ماهه
fgm_3=today_price - lowest_price_90

#درصد تفاوت قيمت امروزبا مقاومت سه ماهه
nv1=((highest_price_90)-(today_price))
nv2=((highest_price_90)+(today_price))/2
jnv=nv1/nv2
jnv1=(math.ceil(jnv*100)) 

if today_price > yesterday_price > today_two_price:
    print (today_price,' قيمت سه روزه افزايشي ميباشد')
    print (f"%فاصله قيمت بامقاومت سه ماه به ريا ل ميشود : { fgh_3 } , تفاوت به درصد : { jnv1 }")
else:
    if today_price < yesterday_price < today_two_price:
        print (today_price,' قيمت سه روزه کاهشي ميباشد')
        print (fgm_3 ,': فاصله قيمت باحمايت سه ماهه')
               

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
m_7=(highest_price_7)-50
m_30=(highest_price_60)-50
m_360=(highest_price_360)-50
h_7=(lowest_price_7)+50
h_30=(lowest_price_60)+50
h_360=(lowest_price_360)+50
#بدست آوردن درصدتفاوت قيمت امروزبه مقاومت هفتگي
nv1=((highest_price_7)-(today_price))
nv2=((highest_price_7)+(today_price))/2
jnv=nv1/nv2
jnv1=(math.ceil(jnv*100)) 


if m_7 <= today_price <= highest_price_7 :
     print ('قيمت نزديک مقاومت هفتگي ميباشد')
     print (jnv1,'% : درصدتفاوت قيمت امروزبامقاومت هفتگي')
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

window_size = 14
past_14_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
window_size = 28
past_28_days_low = DF['Low'].rolling(window_size).min().iloc[-14]


if past_14_days_low < past_28_days_low :
     print ('روند نزوليه')
else:
     if past_14_days_low > past_28_days_low :
          print ('روند صعوديه')



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
         


if kij30>=kij29>=kij28>ten12>=ten11>=ten10<kij27>=kij26>yesterday_price <=ten9<ten8<= today_price :
     print ('--- Signal buy :خيلي خيلي مهم: قيمت تنکانسن وکيجونسن روروبه بالاقطع کرد ---')
else:
     if kij30<=kij29<=kij28<ten12<=ten11<=ten10>kij27<=kij26<yesterday_price >=ten9>ten8>= today_price :
          print ('--- Signal sell :خيلي خيلي مهم : قيمت تنکانسن وکيجونسن روروبه پايين قطع کرد ---')



if kij30>=kij29>=kij28>=kij27>=kij26>yesterday_price and kij26 < today_price :
     print ('--- Signal buy :خيلي مهم : قيمت کيجونسن رو روبه بالاقطع کرد ---')
else:
     if kij30<=kij29<=kij28<=kij27<=kij26<yesterday_price and kij26> today_price :
          print ('--- Signal sell :خيلي مهم : قيمت کيجونسن رو روبه پايين قطع کرد ---')



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


kij=kij26+60
if ten10<=ten9<=ten8>kij28<=kij27<=kij26 and kij<=ten8<today_price:
     print ('تنکانسن بافاصله بالاي کيجونسن ميباشدوقيمت هم بالاي تنکانسن است')
else:
     if ten9<=ten8>today_price>kij27<=kij26 and kij<=ten8<yesterday_price:
          print ('تنکانسن بافاصله بالاي کيجونسن ميباشد وقيمت تنکانسن راروبه پايين قطع کرد')


ten=ten8+60
if ten9>=ten8<kij27>=kij26 and today_price<=ten<kij26:
     print ('تنکانسن بافاصله پايين کيجونسن ميباشد وقيمت هم پايين تنکانسن است')
else:
     if ten9>=ten8<today_price<kij27>=kij26 and yesterday_price<=ten<kij26:
          print ('تنکانسن بافاصله پايين کيجونسن ميباشد وقيمت تنکانسن راروبه بالاقطع کرد')
          

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
elif today_price>movind103>yesterday_price>today_two_price:
     print ('قيمت امروزرفت بالاي ميانگين 103')
else:
     if today_price > movind10:
          print ('قيمت هنوزبالاي ميانگين ده روزه است')
     elif today_price > movind103:
           print ('قيمت هنوزبالاي ميانگين 103')       


     
if today_price<movind10<yesterday_price<today_two_price:
     print ('قيمت امروزرفت پايين ميانگين ده روزه')
elif today_price<movind103<yesterday_price<today_two_price:
     print ('قيمت امروزرفت پايين ميانگين 103')
else:
    if today_price < movind10:
        print ('قيمت هنوزپايين ميانگين ده روزه است')
    elif today_price < movind103:
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

print ('-'*20)
#=======================================================

#=======================================================
print ()
print("          "," Time information")
import pytse_client as tse
#درج تاريخ ميلادي
import jdatetime
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S %d
dt_string = now.strftime("%Y/%m/%d - %A   %H:%M:%S:%p")
print("date and time =", dt_string)
print ('-'*20)

# برسي سهام فقط بازدن شماره کنارسهم قابل برسي است
namad =["چکارن","تلیسه","غمینو","وسپه","غکورش","شپاکسا","ثبهساز","تاپیکو",
        "دسبحان","ومعادن","فصبا","حتوکا","خگستر","فولاد","شپنا","فملی","حتاید",
        "فسبزوار","خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور","فپنتا",
        "شبندر","فارس","غفارس","وبصادر","کچاد","کگل","داتام","نخريس","پاکشو",
        "درازک","كپارس","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
        "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
        "تاصيكو","نخريس","قهكمت"]

# Print the list of stocks and their indices
#for i, n in enumerate(namad):
     #print(f"{i+1}. {n}")

# Divide the list into three rows
rows = [namad[i:i+5] for i in range(0, len(namad), 5)]

# Print the rows next to each other with numbers
for i, row in enumerate(rows):
    for j, stock in enumerate(row):
        stock_number = i*5 + j + 1
        print(f"{stock_number}. {stock}", end="\t")
    print()


# Ask the user to enter a valid index
index = int(input("Please write down the selected share number \n لطفا فقط شماره مقابل سهم انتخابي رابنويسيد  : "))
# Run Python for the selected stock    
stock = namad[index-1]

choice = index
sahame = namad[choice-1]
# Do some analysis or visualization here
tse.download(symbols=sahame,
             write_to_csv=True,
             adjust=True)
ticker = tse.Ticker(sahame)
print ('-'*20)
print(ticker.last_date,': تاريخ وساعت آخرين اطلاعات قيمت پاياني ومعاملاتي')
print ('-'*20)
print(ticker.state,ticker.flow,ticker.group_name)     
print(f"نام شرکت : {ticker.title}    ,    سال مالي : {ticker.fiscal_year}")
print(f"EPS : {ticker.eps}  , P/E : {ticker.p_e_ratio}  ,  group P/E : {ticker.group_p_e_ratio}")
print(f"درصد سهام شناور : {ticker.float_shares}    ,    حجم مبنا : {ticker.base_volume}") 
print()  
print(ticker.open_price,' : قيمت بازشدن امروز')
print(f"قيمت پاياني امروز : {ticker.adj_close}    ,    قیمت دیروز : {ticker.yesterday_price}")
print(f"آخرین معامله : {ticker.last_price}    ,   آخرين تقاضاي خريد : {ticker.best_demand_price}")
print()
print(f"حداکثرقيمت امروز : {ticker.high_price}    ,    حداقل قيمت امروز : {ticker.low_price}")
print(f"حداکثر قیمت مجاز : {ticker.sta_max}    ,    حداقل قیمت مجاز : {ticker.sta_min}")
print()
print(f"تعداد معاملات : {ticker.count}    ,    ارزش معاملات : {ticker.value}")
print ('-'*20)
print(f"today_Volume : {ticker.volume}    ,    today_Volume_yesterday : {today_Volume_yesterday}")
print(ticker.month_average_volume,' : میانگین حجم ماه')
print ('-'*20)
#بدست آوردن درصدنوسان قيمتي امروز
nv1=ticker.high_price-ticker.low_price
nv2=(ticker.high_price+ticker.low_price)/2
jnv=nv1/nv2
jnv1=jnv*100
#بدست آوردن تفاوت درصدي قيمت ديروزبه امروز
n1=ticker.adj_close-ticker.yesterday_price
n2=(ticker.adj_close+ticker.yesterday_price)/2
j1=n1/n2
j2=j1*100
print (math.ceil(j2) ,': درصدتفاوت قيمت ديروزبه امروز')
print (n1 ,' : تفاوت قيمت ديروزبه امروزبه ريا ل')
print (math.ceil(jnv1) ,': درصدنوسان قيمتي امروز')
print()
#=======================================================

print ('='*30,' candel DOje')
DOje1= (ticker.high_price+ticker.low_price)/2
DOje2= DOje1 + 20
DOje3= DOje1 - 20

if ticker.last_price == DOje1 :
    print (' کندل دوجي شکل گرفته')


if ticker.high_price > ticker.last_price >= DOje2:
    print (' کندل دوجي سبزشکل گرفته')
else:
    if ticker.low_price < ticker.last_price <= DOje3:
        print (' کندل دوجي قرمزشکل گرفته')
        

if ticker.open_price < ticker.last_price > DOje1:
    print (' candle Green')
else:
    if ticker.open_price > ticker.last_price < DOje1:
        print (' candle Red')


if ticker.open_price < ticker.last_price == ticker.high_price > (ticker.low_price+150):
    print (' candle marabozo Green')
else:
    if ticker.open_price > ticker.last_price == ticker.low_price < (ticker.high_price-150):
        print (' candle marabozo Red')

#===============================================

today_price6 = DF['Close'].iloc[-6]
today_price9 = DF['Close'].iloc[-9]
Volume_week = DF['Volume'].iloc[-5] # حجم هفتگي
Volume_Month = DF['Volume'].iloc[-26] # حجم ماهيانهBase volume
today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز
average_Volume_week = Volume_week.mean() # محاسبه ميانگين حجم هفتگي
average_Volume_Month = Volume_Month.mean() # محاسبه ميانگين حجم ماهيان
        
print (35*'=',sahame,'volume')
print (ticker.volume ,'حجم امروز')
print (today_Volume_yesterday , 'حجم ديروز')
          
if ticker.volume > (math.ceil(average_Volume_Month)):
     print ('حجم امروزبيشترازحجم ماهيانه شده')
else:
     if ticker.volume < (math.ceil(average_Volume_Month)):
          print ('حجم امروزکمتر ازحجم ماهيانه شده')
          

if ticker.volume < today_Volume_yesterday < Volume_week:
     print ('حجم درهفته گذشته کاهشي بود')
else:
     if ticker.volume > today_Volume_yesterday > Volume_week:
         print ('حجم درهفته گذشته افزايشي بود')

          
if ticker.volume > today_Volume_yesterday :
     print ('حجم امروزبيشترازحجم ديروزشده')
else:
    if ticker.volume < today_Volume_yesterday :
        print ('حجم امروز کمترازحجم ديروزشده')

         
if ticker.volume > (math.ceil(average_Volume_Month))*3 :
     print ('حجم امروز بيشترازدوبرابر حجم ماهيانه شده')


if ticker.volume > 4*(average_Volume_week):
    print (" حجم امروز 4برابر حجم هفتگي ميباشد")


if ticker.yesterday_price > ticker.last_price > today_price6 and ticker.volume > today_Volume_yesterday:
    print ('حجم افزايشي وقيمت امروزاز 6 روزقبل هم بالاتره')
else:
    if ticker.yesterday_price< ticker.last_price < today_price6 and ticker.volume < today_Volume_yesterday:
        print ('حجم کاهشي وقيمت امروزاز 6 روزقبل هم کمترشده')

        
if ticker.last_price > today_price9 and ticker.volume > today_Volume_yesterday:
    print ('حجم افزايشي وقيمت امروزاز 9 روزقبل هم بالاتررفت')
else:
    if ticker.last_price < today_price9 and ticker.volume < today_Volume_yesterday:
        print ('حجم کاهشي وقيمت امروزاز 9 روزقبل هم پايين تررفت')


#================================================
print(25*"-")     
if ticker.adj_close > ticker.yesterday_price:
     print (' قيمت امروزبالاترازديروزه ')
else :
     if ticker.adj_close < ticker.yesterday_price:
          print (' قيمت امروزپايين ترازديروزه ')


if ticker.volume > today_Volume_yesterday and ticker.last_price < ticker.yesterday_price :
    print ("sell : قيمت داره ميادپايين حجم ميره بالابفروش")
else:
    if ticker.volume < today_Volume_yesterday and ticker.last_price > ticker.yesterday_price :
        print ("sell : حجم داره ميادپايين قيمت ميره بالا بفروش")


if ticker.volume > today_Volume_yesterday and ticker.last_price > ticker.yesterday_price :
    print ("buy : حجم وقيمت هردوميره بالا يااول حمايت بخرياباشکست مقاومت بخر")
else:
    if ticker.volume < today_Volume_yesterday and ticker.last_price < ticker.yesterday_price :
        print ("buy : حجم وقيمت هردوداره ميادپايين نزديک حمايت بخر")
        

print()
#=======================================================

closing_prices7 = DF['Close'].iloc[-3:]       # قيمت بسته شدن 3روزگذشته
closing_prices = DF['Close'].iloc[-10:]      # قيمت بسته شدن 10روز گذشته
average_price = closing_prices.mean()   #محاسبه ميانگين قيمت بسته شدن 10 روز
average_prices7 = closing_prices7.mean() #محاسبه ميانگين 3روزه
# بدست آوردن ميانگين هاي 3و10و20 روزه
ma3 = (math.ceil(average_prices7))
ma10 = (math.ceil(average_price))

print (30*'=','  moving',sahame,)

if ticker.yesterday_price+400 > ticker.yesterday_price< ma10 < ticker.adj_close :
    print (' بعدازريزش 20درصدي که داشته price > ma10 : موقع خريده')
else:
    if ticker.yesterday_price-400 < ticker.yesterday_price> ma10 > ticker.adj_close :
        print ('بعدازسعود 20درصدي که داشته price < ma10 : موقع فروشه')
        


if ma3<ma10 >ticker.last_price <ticker.yesterday_price:
    print (' ميانگين ها وقيمت همه نزولي شدن')
else:
    if ma3>ma10 <ticker.last_price >ticker.yesterday_price:
        print (' ميانگين هاوقيمت همه صعودي شدن')
        


if ticker.yesterday_price+500 > ticker.yesterday_price < ticker.adj_close :
     print ('باريزشي که داشته 10% احتمال برگشت داره')
else:
    if ticker.yesterday_price-500 < ticker.yesterday_price > ticker.adj_close :
         print ('باصعودي که داشته 10% احتمال ريزش داره')
     

print ()
#=======================================================
        
# بالاترين وپايين ترين قيمتهاي 7و14و30و60و103و360 روز قبل max and min
max_price_b1 = max(DF['High'][-7:]) # max_price day7
min_price_b2 = min(DF['Low'][-7:])  # min_price day7
max_price_b3 = max(DF['High'][-14:]) # max_price day14
min_price_b4 = min(DF['Low'][-14:])  # min_price day14

max_price_b5 = max(DF['High'][-30:]) # max_price day30
min_price_b6 = min(DF['Low'][-30:])  # min_price day30
max_price_b7 = max(DF['High'][-60:]) # max_price day60
min_price_b8 = min(DF['Low'][-60:])  # min_price day60

max_price_b9 = max(DF['High'][-103:]) # max_price day103
min_price_b10 = min(DF['Low'][-103:])  # min_price day103

max_price_b11 = max(DF['High'][-360:]) # max_price day360
min_price_b12 = min(DF['Low'][-360:])  # min_price day360

closing_price_b9 = DF['High'].iloc[-103:]  # max_price_day103
closing_price_b10 = DF['Low'].iloc[-103:]  # mix_price_day103
average_max5 = closing_price_b9.mean()   # average_max_price_day103                  
average_min5 = closing_price_b10.mean()   # average_mix_price_day103
# (max 103_mean + min 103_mean) /2
Month103_mean = (average_max5 + average_min5)/2
# max Month30 + min Month30 /2
Month30 = (max_price_b5 + min_price_b6)/2
        
print (30*'=','kanal ',sahame,)

if ticker.adj_close > average_price :
     print (' price > Em_10 ')
else:
     if ticker.adj_close < average_price :
         print (' price < Em_10 ')


if ticker.adj_close > Month103_mean > ticker.yesterday_price:
    print ('قيمت امروز ميانگين 103رو روبه بالاقطع کرد')
else:
    if ticker.adj_close < Month103_mean < ticker.yesterday_price:
        print ('قيمت امروزميانگين 103 رو روبه پايين قطع کرد')
        


if Month103_mean < ticker.adj_close < ticker.yesterday_price < today_two_price:
    print ('قيمت روبه پايين وبه سمت ميانگين   103 روزه ميرود')
else:
    if Month103_mean > ticker.adj_close > ticker.yesterday_price > today_two_price:
        print ('قيمت روبه بالا وبه سمت ميانگين   103 روزه ميرود')
        


if Month103_mean < ticker.adj_close > ticker.yesterday_price > today_two_price:
    print ('قيمت بالاي ميانگين 103 روزه است وداره بالاترميره')
else:
    if Month103_mean > ticker.adj_close < ticker.yesterday_price < today_two_price:
        print ('قيمت پايين ميانگين 103روزه است وداره پايين ترميره')
        


if ticker.low_price > yesterday_price_min > today_two_price_min6 :
    print (' کف امروزبالاترازکف 6روزپيش شده ')
else:
    if ticker.low_price < yesterday_price_min < today_two_price_min6 :
        print (' کف امروز پايين ترازکف 6 روزپيش شده')
        


if ticker.high_price > Month30 >= ticker.yesterday_price:
    print ('Month30 شروع روند افزايشي بااحتياط خريدکن')
else:
    if ticker.low_price < Month30 <= ticker.yesterday_price:
        print ('Month30 شروع روند کاهشي مراقب باش ')


        
if ticker.adj_close<min_price_b4<min_price_b8<min_price_b10<min_price_b12:
     print ("کانال وروند سه ماهه کاملا نزولي ميباشد ")
else:
    if ticker.adj_close<min_price_b4<min_price_b8<min_price_b10:
         print ("کانال وروند يک ماه همچنان نزولي ميباشد ")
                


if ticker.adj_close>min_price_b4>min_price_b8>min_price_b10>min_price_b12:
     print ("کانال وروند سه ماهه کاملاصعودي ميباشد")
else:
    if ticker.adj_close>min_price_b4>min_price_b8>min_price_b10:
         print ("کانال وروند يک ماه همچنال افزايشي ميباشد")



#========================================================        
print(40*"=","محاسبات قيمت خريد شمااز ",sahame,)
# چکارن
if index == 1:
     p=0
     s=4591
     v=20000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          
          
# تليسه
if index == 2:
     p=4313
     s=4251
     v=5000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
     if 2370>ticker.adj_close>1334:
         print ("مابين حمايت 1334ومقاومت 2370هستيم ودرميانه 1878روداريم")
     if 3421>ticker.adj_close>2370:
         print ("مابين حمايت 2370ومقاومت 3421هستيم درميانه 2920روداريم")
     if 4516>ticker.adj_close>3421:
         print ("مابين حمايت 3421 ومقاومت 4516 هستيم درميانه 3956 روداريم ")
     if 5597>ticker.adj_close>4516:
         print ("مابين حمايت 4516 ومقاومت 5597 هستيم درميانه 5025 روداريم")
     if 6663>ticker.adj_close>5597:
         print ("مابين حمايت 5597 ومقاومت 6663 هستيم درميانه 6094 روداريم")
     if 7758>ticker.adj_close>6663:
         print ("مابين حمايت 6663 ومقاومت 7758 هستيم درميانه 7208 روداريم")
     if 8839>ticker.adj_close>7758:
         print ("مابين حمايت 7758 ومقاومت 8839 هستيم درميانه 8262روداريم")
     if 9918>ticker.adj_close>8839:
         print ("مابين حمايت 8839 ومقاومت 9918 هستيم درميانه 9361 روداريم")
         
          
# غمينو
if index == 3:
     p=11181
     s=10020
     v=4000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          
          
# وسپه
if index == 4:
     p=4255
     s=4545
     v=2000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
     if 1330>ticker.adj_close>618:
         print ("مابين حمايت 618 ومقاومت 1330 هستيم درميانه 974 روداريم")
     if 2022>ticker.adj_close>1330:
         print ("مابين حمايت 1330 ومقاومت2022 هستيم درميانه 1666 روداريم")
     if 2714>ticker.adj_close>2022:
         print ("مابين حمايت 2022 ومقاومت 2714 هستيم درميانه 2358 روداريم ")
     if 3397>ticker.adj_close>2714:
         print ("مابين حمايت 2714 ومقاومت 3397 هستيم درميانه 3041 روداريم")
     if 4079>ticker.adj_close>3397:
         print ("مابين حمايت 3397 ومقاومت 4079 هستيم درميانه 3733 روداريم")
     if 4782>ticker.adj_close>4079:
         print ("مابين حمايت 4079 ومقاومت 4782 هستيم درميانه 4435 روداريم")
     if 5465>ticker.adj_close>4782:
         print ("مابين حمايت 4782 ومقاومت 5465 هستيم درميانه 5127 روداريم")
     if 6146>ticker.adj_close>5465:
         print ("مابين حمايت 5465 ومقاومت 6146 هستيم درميانه 5807 روداريم")
     if 6810>ticker.adj_close>6146:
         print ("مابين حمايت 6146 ومقاومت 6810 هستيم درميانه 6461 روداريم")
     if 7473>ticker.adj_close>6810:
         print ("مابين حمايت 6810 ومقاومت 7473 هستيم درميانه 7149 روداريم")  
         
         
# غکورش
if index == 5:
     p=9352
     s=7260
     v=26000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
     if 5210>ticker.adj_close>4032:
         print ("مابين حمايت 4032 ومقاومت 5210 هستيم درميانه 4615 روداريم")
     if 6410>ticker.adj_close>5210:
         print ("مابين حمايت 5210 ومقاومت 6410 هستيم درميانه 5804 روداريم")
     if 7599>ticker.adj_close>6410:
         print ("مابين حمايت 6410 ومقاومت 7599 هستيم درميانه 7004 روداريم ")
     if 8788>ticker.adj_close>7599:
         print ("مابين حمايت 7599 ومقاومت 8788 هستيم درميانه 8204 روداريم")
     if 9977>ticker.adj_close>8788:
         print ("مابين حمايت 8788 ومقاومت 9977 هستيم درميانه 9383 روداريم")
     if 11160>ticker.adj_close>9977:
         print ("مابين حمايت 9977 ومقاومت 11160 هستيم درميانه 10550 روداريم") 
         
         
# شپاکسا
if index == 6:
     p=2150
     s=0
     v=200000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
     if 1769>ticker.adj_close>1382:
         print ("مابين حمايت 1382 ومقاومت 1769 هستيم درميانه1572 روداريم")
     if 2543>ticker.adj_close>1769:
         print ("مابين حمايت 1769 ومقاومت 2543 هستيم درميانه 2149 روداريم")
     if 3302>ticker.adj_close>2543:
         print ("مابين حمايت 2543 ومقاومت 3302 هستيم درميانه 2922 روداريم ")
     if 4061>ticker.adj_close>3302:
         print ("مابين حمايت 3302 ومقاومت 4061 هستيم درميانه 3688 روداريم")
     if 4834>ticker.adj_close>4061:
         print ("مابين حمايت 4061 ومقاومت 4834 هستيم درميانه 4452 روداريم")
     if 5591>ticker.adj_close>4834:
         print ("مابين حمايت 4834 ومقاومت 5591 هستيم درميانه 5211 روداريم")
         
          
# ثبهساز
if index == 7:
     p=3207
     s=3324
     v=30000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
     if 2381>ticker.adj_close>1891:
         print ("مابين حمايت 1891 ومقاومت 2381 هستيم درميانه 2133 روداريم")
     if 2865>ticker.adj_close>2381:
         print ("مابين حمايت 2381 ومقاومت 2865 هستيم درميانه 2569 روداريم")
     if 3355>ticker.adj_close>2865:
         print ("مابين حمايت 2865 ومقاومت 3355 هستيم درميانه 3118 روداريم")
     if 3835>ticker.adj_close>3355:
         print ("مابين حمايت 3355 ومقاومت 3835 هستيم درميانه 3588 روداريم")
     if 4320>ticker.adj_close>3835:
         print ("مابين حمايت 3835 ومقاومت 4320 هستيم درميانه 4067 روداريم")
     if 4807>ticker.adj_close>4320:
         print ("مابين حمايت 4320 ومقاومت 4807 هستيم درميانه 4565 روداريم")          
         
         
# تاپيکو
if index == 8:
     p=0
     s=17560
     v=2000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          
          
# دسبحان
if index == 9:
     p=0
     s=11650
     v=10000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          
          
# ومعادن
if index == 10:
     p=4874
     s=4844
     v=47000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
     if 4066>ticker.adj_close>2526:
          print ("مابين حمايت 2526 ومقاومت 4066 هستيم درميانه 3198 روداريم") 
     if 5610>ticker.adj_close>4066:
          print ("مابين حمايت  4066 ومقاومت 5610 هستيم درميانه  4763 روداريم")
     if 7184>ticker.adj_close>5610:
          print ("مابين حمايت 5610 ومقاومت 7184 هستيم درميانه  6343  روداريم")
          

# فصبا
if index == 11:
     p=4893
     s=4992
     v=3000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          
          
# حتوکا
if index == 12:
     p=0 
     s=3400
     v=5000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')


# خگستر
if index == 13:
     p=0 
     s=0
     v=0
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')


# فولاد
if index == 14:
     p=0 
     s=0
     v=0
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')


          
if ticker.yesterday_price < ticker.last_price :
    print (' بطرف مقاومت ميرويم')
else:
    if ticker.yesterday_price > ticker.last_price :
        print (' بطرف حمايت ميرويم')
          

if index >= 15 : 
     print (sahame ,'  :  شماازاين سهم خريد نداريد')

     
import sys

if index<=14 and p > 0:
     price=p
     price_s=s
     vol=v
     # قيمت امروزسهم Today's stock price
     today_price = (math.ceil(ticker.adj_close))     
     price_kharid= (-0.004 * price)  #کارمزد خريد
     price_forosh= (-0.006 * today_price) #کارمزد فروش محاسبه باقيمت امروز
     pk=((math.ceil(price_kharid)+price) * vol)#قيمت کل خريد باکارمزد
     pf=((math.ceil(price_forosh)+today_price) * vol)#قيمت کل فروش باکارمزد
     sl = 0.03 # حدضرر3درصد
     tp = 0.2 # حدسود20درصد
     # تعیین حد ضرر
     stop_loss = price * (1-sl)
     # تعیین حد سود
     take_profit = price * (1+tp)
     pp = (((math.ceil(price_forosh)+today_price)* vol)-(((math.ceil(price_kharid)+price)* vol)))
     sz= pf-pk 
     print(20*"-" )
     
     if today_price > take_profit:
          profit = str ( pf - pk )
          profit_float = float(profit)
          profit_percentage =(profit_float / pk) * 100
          print (" جمع پرداختي شمابااحتساب قيمت خريدتان :" ,pk)
          print (" اگرباقيمت امروزبفروشيد ميشه :" , pf)
          print (" شماسود ميکنيد به مبلغ :" ,pp)
          print("Your profit percentage :% درصدسودشماشده : {} ".format(math.ceil(profit_percentage)))
          print(20*"-" )
     elif today_price < stop_loss:
          loss = str ( pk - pf )
          loss_float = float(loss)
          loss_percentage = (loss_float / pk) * 100
          print (" جمع پرداختي شمابااحتساب قيمت خريدتان :" ,pk)
          print (" اگرباقيمت امروزبفروشيد ميشه :" , pf)
          print (" شماضرر ميکنيد به مبلغ :" ,pp)
          print("The percentage of your loss :% درصدضررشماشده : {} ".format(math.ceil(loss_percentage)))
          print(20*"-" )
     else:
          if pk > (ticker.adj_close * vol) :
              print("Price to limit")
              print (" قيمت به حد سود20درصد نرسيده!  \n The price has not reached the profit of 20%")                             
              print (sz ,": اگرامروزبفروشيد مقدارزيان شماميشود")
              print(20*"-" )
          if pk < (today_price * vol) :
              print("Price to limit")
              print (" قيمت به حد ضرر3درصد نرسيده !  \n The price has not reached the level of 3% loss") 
              print(sz,": اگرامروزبفروشيد مقدارسودشماميشود")
              print(20*"-" )

          
     if p == p :
          hs1 = (( p * 0.2 + p )*100)/100 # حدسود20درصد
          hs2 = (( p * 0.1 + p )*100)/100 # حدسود10درصد
          hs3 = (( p * 0.05 + p )*100)/100 # حدسود5درصد
          hs4 = (( p * 0.011 + p )*100)/100 # قيمت سربه سر
          hz = ((p * -0.03 + p)*100)/100# حدضرر3درصد
          print (' تعيين حدسودوزيان بااحتساب قيمت خريد شمااز  :' ,sahame)
          print(f"حدسود20درصد : {hs1}    ,    حدسود10درصد : {hs2}")
          print(f"حدسود5درصد : {hs3}    ,    حد ضرر سه درصد : {hz}")
          print (hs4,'قيمت سربه سربراي فروش')
          print (today_price,' : قيمت بسته شدن امروز')
          print (ticker.last_price,' : قيمت آخرين معامله امروز')
          print ('-'*20)

          
     if pk == pf :
          print (" اگرعلان بفروشيد سربه سرميشيد :" ,today_price )
          print ('-------')


#=====================================================      
# (ticker.open_price,' : قيمت بازشدن امروز')
# yesterday_Open_price: قيمت بازشدن ديروز
#قيمت پاياني امروز : {ticker.adj_close}
#قیمت دیروز : {ticker.yesterday_price}
#حداکثرقيمت امروز : {ticker.high_price}    ,    حداقل قيمت امروز : {ticker.low_price}
#yesterday_price_max: حداکثرقيمت ديروز   ,    yesterday_price_min:  حداقل قيمت ديروز
# lowest_price_7 : حمايت هفتگي   ,   highest_price_7  مقاومت هفتگي
# lowest_price_60 : حمايت ماهيانه  ,   highest_price_60   مقاومت ماهيانه  

#هرموقع اينگلفينگ صورت بگيرد تذکرميدهد 
# Bullish Harami EngulFing support or Resistance level

if ticker.yesterday_price<yesterday_Open_price>ticker.open_price<ticker.adj_close:
     if yesterday_price_max<ticker.high_price and yesterday_price_min>ticker.low_price:
          if ticker.low_price<=lowest_price_7 or lowest_price_60<=ticker.high_price:
               print ("Bullish Harami EngulFing support")
               print ('---اينگل فينگ صعودي شده ميتوني خريدکني---')
               print ("-"*10)

               

if ticker.yesterday_price>yesterday_Open_price<ticker.open_price>ticker.adj_close:
     if yesterday_price_max<ticker.high_price and yesterday_price_min>ticker.low_price:
          if ticker.low_price<=highest_price_7 or highest_price_60<=ticker.high_price:
               print ("Bullish Harami EnngulFung Resistance level")
               print ('---اينگل فينگ نزولي شده ميتوني بفروشي---')
               print ("-"*10)
               


if today_two_price_max > yesterday_price_max and today_two_price_min < yesterday_price_min:
   if today_two_price < yesterday_price < ticker.adj_close:
       if ticker.min_week or lowest_price_30 or ticker.min_year <= today_two_price_min :
           print ("Bullish Harami EngulFing support")
           print ("-----اینگل فینگ صعودی شده خریدکن -----")
           print ("-"*10)



if today_two_price_max > yesterday_price_max and today_two_price_min < yesterday_price_min:
   if today_two_price > yesterday_price > ticker.adj_close:
      if ticker.max_week or highest_price_30 or ticker.max_year >=(today_two_price_max):
          print ("Bullish Harami EnngulFung Resistance level")
          print ("----- اینگل فینگ نزولی شده بفروش -----")
          print ("-"*10)

#=====================================================
# اين کد براي اينگل فينگ نوشته شده است ودرصورت اجراشدن پرينت انجام ميشود
# درغيراين صورت هيچ چيزي پرينت نميکند
# Bullish Harami EngulFing support or Resistance level

if today_two_price_max < yesterday_price_max < ticker.high_price:
    if today_two_price_min > yesterday_price_min < ticker.low_price:
        if today_two_price < yesterday_price < ticker.adj_close:
            if ticker.min_week or lowest_price_30 or ticker.min_year <= yesterday_price_min:
                print ("EngulFing support level")
                print ("----- اینگل فینگ صعودی رخ داده خریدکن-----")
                print ("-"*10)



if today_two_price_max < yesterday_price_max > ticker.high_price:
    if today_two_price_min > yesterday_price_min > ticker.low_price:
        if today_two_price > yesterday_price > ticker.adj_close:
            if ticker.max_week or highest_price_30 or ticker.max_year >= yesterday_price_min:
                print ("EngulFing Resistance level")
                print ("----- اينگل فينگ نزولي رخ داده بفروش -----")
                print ("-"*10)


#=================================================           
print(40*"=",nam,"Engulfing Calculations")
# Engulfing  ascending صعودي
# Bullish Engulfing Support level
h1 = ticker.adj_close > ticker.open_price
h2 = yesterday_Open_price > yesterday_price
h3 = yesterday_price > ticker.open_price
h4 = ticker.adj_close > yesterday_Open_price

h_ascending = h1 and h2 and h3 and h4
h5 =  (ticker.adj_close - ticker.open_price) > 5*(yesterday_Open_price - yesterday_price) 

# Engulfing  Descending نزولي
# Bullish Engulfing Resistance level 
h6 = ticker.adj_close < ticker.open_price
h7 = yesterday_Open_price < yesterday_price
h8 = yesterday_price < ticker.open_price
h9 = ticker.adj_close < yesterday_Open_price

h_Descending = h6 and h7 and h8 and h9
h10 = (ticker.adj_close - ticker.open_price) < 5*(yesterday_Open_price - yesterday_price)


if ticker.adj_close > highest_price_90 :
     print (' مقاومت سه ماه شکسته شد')

if ticker.adj_close < lowest_price_90 :
     print (' حمايت سه ماه ازدست رفت')
     

if h_ascending and h5:
    c = "Engulfing :"
    print (c , "hemer ascending !  صعودي مناسب خريد" )
    
if h_Descending and h10:
    c = "Engulfing :"
    print (c , "hemer Descending !  نزولي وقت فروش" )
    
print ('~'*10)
print ('روند False يا True دقت کنيدبه')
print (h5, ' :ascending   روند صعودي ')
print (h10 , ' :Descending   روند نزولي')
               
#=======================================================

print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')
#------------------------------------------------



