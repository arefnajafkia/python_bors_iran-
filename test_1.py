
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
                            end_date='1403-04-09',
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
#===================================================
print ()
print(25*"=","Check available stocks",25*"=")
import pytse_client as tse
#درج تاريخ ميلادي
import jdatetime
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S %d
dt_string = now.strftime("%Y/%m/%d - %A   %H:%M:%S:%p")
print("date and time =", dt_string)
print ('-'*30,)

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

print(f"today_Open_price:{today_Open_price}  , yesterday_Open_price:{yesterday_Open_price}  , today_two_Open_price:{today_two_Open_price}")
print(f"today_price: {today_price}      , yesterday_price : {yesterday_price}      , today_two_price: {today_two_price}")
print(f"today_price_max: {today_price_max}   , yesterday_price_max: {yesterday_price_max}   , today_two_price_max:{today_two_price_max}")
print(f"today_price_min: {today_price_min}   , yesterday_price_min: {yesterday_price_min}   , today_two_price_min:{today_two_price_min}")
print(f"today_Final: {today_Final_price}      , yesterday_Final: {yesterday_Final_price}      , today_two_Final: {today_two_Final_price}")

print ()

#================================================     
if today_price > yesterday_price:
     print (' قيمت امروزبالاترازديروزه ')
else :
     if today_price < yesterday_price:
          print (' قيمت امروزپايين ترازديروزه ')


print()          
#================================================

max_price = DF['High'].iloc[-9:] # بالاترين قيمت هاي 9روز ten_max
min_price = DF['Low'].iloc[-9:]  # پايين ترين قيمت هاي 9روز ten_min

max_price2 = DF['High'].iloc[-26:] # بالاترين قيمت هاي 26 روزگذشته kij_max
min_price2 = DF['Low'].iloc[-26:]  # پايين ترين قيمت هاي 26 روزگذشته kij_min


# Get the closing prices for the last 10and26 days
closing_prices7 = DF['Close'].iloc[-3:]       # قيمت بسته شدن 3روزگذشته
closing_prices8 = DF['Close'].iloc[-20:]      # قيمت بسته شدن 20روزگذشته
closing_prices2 = DF['Close'].iloc[-26:]     # قيمت بسته شدن 26 روزگذشته
closing_prices3 = DF['Close'].iloc[-50:]     # قيمت بسته شدن 50روزگذشته
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
average_prices2 = closing_prices2.mean() # محاسبه ميانگين قيمت بسته شدن26روز
average_prices3 = closing_prices3.mean() #محاسبه ميانگين قيمت بسته شدن 50روز
#محاسبه دقيق ميانگين 3روزه 
window_size = 3
past_3_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_3_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
mov3 = (past_3_days_high + past_3_days_low)/2
moving_3=(math.ceil(mov3))
#محاسبه دقيق ميانگين10روزه
window_size = 10
past_10_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_10_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
mov10 = (past_10_days_high + past_10_days_low)/2
moving_10=(math.ceil(mov10))
#محاسبه دقيق ميانگين 103روزه 
window_size = 103
past_103_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_103_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
mov103 = (past_103_days_high + past_103_days_low)/2
moving_103=(math.ceil(mov103))
#محاسبه دقيق ميانگين 240روزه 
window_size = 240
past_240_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_240_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
mov240 = (past_240_days_high + past_240_days_low)/2
moving_240=(math.ceil(mov240))
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
tenken10 = (math.ceil(ten10))

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
kijon28 = (math.ceil(kij28))

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

print(f"ten9  : {tenken9}     ,    kij27 :  {kijon27}")
print(f"ten10 : {tenken10}     ,    kij28 :  {kijon28}")
print ()

# محاسبات ابرکومو52 روزه به قبل
# Calculate the highest and lowest price over the past 26 days
window_size = 52
past_52_days_high = DF['High'].rolling(window_size).max().iloc[-1]
past_52_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
komu52_max = (math.ceil(past_52_days_high))
komu52_min = (math.ceil(past_52_days_low))

print(f"moving_103 : {moving_103}")
print(f"komu52_max : {komu52_max}   ,  komu52_min : {komu52_min} ")
#print(f"komu52_min: {komu52_min}")
print ()

#تعيين روندنزولي ياصعودي باتنکانسن وکيجونسن
window_size = 14
past_14_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
window_size = 28
past_28_days_low = DF['Low'].rolling(window_size).min().iloc[-14]


if past_14_days_low < past_28_days_low :
     print ('روند نزوليه')
else:
     if past_14_days_low > past_28_days_low :
          print ('روند صعوديه')
#----------------------------------


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
    if kij30>=kij29>=kij28>=kij27>=kij26 >today_price>yesterday_price> ten8<=ten9<=ten10<=ten11<=ten12 :
         print ('قيمت بالاي تنکانسن ميباشد وروبه بالا بطرف کيجونسن ميرود')


if kij30>=kij29>=kij28>=kij27>=kij26>ten8<=ten9<=ten10<=ten11<=ten12 <today_price>yesterday_price :
     print ('قيمت بالاي تنکانسن وکيجونسن است وروبه بالادرحرکت ميباشد درضمن  تنکانسن زيرکيجونسن است ')



if kij30<=kij29<=kij28<=kij27<=kij26 <today_price<yesterday_price< ten8<=ten9<=ten10<=ten11<=ten12 :
     print ('قيمت زيرتنکانسن ميباشد وروبه پايين بطرف کيجونسن ميرود')
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

#----------------------------------
#تعين فاصله تنکانسن باکيجونسن
ten8_kij26 = kijon26 - tenken8

print (ten8_kij26 , ' : فاصله تنکانسن باکيجونسن')
#----------------------------------
print ()
# تقاطع تنکانسن وکيجونسن با ميانگين 103روزه که سيگنال خريد يافروش ميدهد

if tenken9>moving_103<kij27 and today_two_price<=yesterday_price<today_price>moving_103:
     print ('خيلي مهم Signal buy : کيجونسن وتنکانسن وقيمت ميانگين 103راروبه بالاقطع کردن')
else:
     if tenken10<=tenken9>moving_103 and today_two_price<=yesterday_price<today_price>moving_103:
          print ('خيلي مهم Signal buy : تنکانسن وقيمت ميانگين 103راروبه بالا قطع کردن')


          
if tenken9<moving_103>kij27 and today_two_price>=yesterday_price>today_price<moving_103:
     print ('خيلي مهم Signal sell : کيجونسن وتنکانسن وقيمت ميانگين 103راروبه پايين قطع کردن')
else:
     if tenken10>=tenken9<moving_103 and today_two_price>=yesterday_price>today_price<moving_103:
          print ('خيلي مهم Signal sell : تنکانسن وقيمت ميانگين 103راروبه پايين قطع کردن')
        

if today_price>moving_10:
     print ('قيمت بالاي ميانگين 10 روزه ميباشد')
else:
     if today_price<moving_10:
          print ('قيمت پايين ميانگين 10روزه ميباشد')


if today_price<moving_103<moving_240>ten8:
     print('تنکانسن وقيمت پايين ميانگين 103و240روزه ميباشد')
else:
     if today_price<moving_103<moving_240:
          print ('قيمت پايين ميانگين 103و240روزه ميباشد')


if today_price>moving_103>moving_240<ten8:
     print('تنکانسن وقيمت بالاي ميانگين 103و240روزه ميباشد')
else:
     if today_price>moving_103>moving_240:
          print ('قيمت بالاي ميانگين 103و240روزه ميباشد')


#===============================================
#تعيين اولين مقاومت وحمايت سرراه با محاسبات انجام شده باايچيموکو         
past_8 = past_8_days_high - past_8_days_low
past_8h = past_8  + past_8_days_high
past_8L = past_8_days_low - past_8
h8 = (math.ceil(past_8h))
L8 = (math.ceil(past_8L))

if yesterday_price < today_price >= tenken8 == kijon26 :
     print (past_8h, ' : اولين مقاومت سرراه')


if yesterday_price > today_price <= tenken8 == kijon26 :
     print (past_8L, ' : اولين حمايت سرراه')


print (20*'-')
if yesterday_price < today_price:
     print (h8, ' : اولين مقاومت سرراه')
else:
     if yesterday_price > today_price:
          print (L8, ' : اولين حمايت سرراه')


#===============================================
#تعيين دومين مقاومت وحمايت سرراه با محاسبات انجام شده ايچيموکو         
past_26 = past_26_days_high - past_26_days_low
past_26h = past_26  + past_26_days_high
past_26L = past_26_days_low - past_26
h26 = (math.ceil(past_26h))
L26 = (math.ceil(past_26L))

if yesterday_price < today_price >= tenken8 == kijon26 :
     print (past_26h, ' : دومين مقاومت سرراه')


if yesterday_price > today_price <= tenken8 == kijon26 :
     print (past_26L, ' : دومين حمايت سرراه')


print (20*'-')
if yesterday_price < today_price:
     print (h26, ' : دومين مقاومت سرراه')
else:
     if yesterday_price > today_price:
          print (L26, ' : دومين حمايت سرراه')


     
print ("="*40)
#====================================================
# برسي سهام فقط بازدن شماره کنارسهم قابل برسي است
namad =["چکارن","تلیسه","غمینو","وسپه","غکورش","شپاکسا","ثبهساز","تاپیکو",
        "دسبحان","ومعادن","فصبا","حتوکا","خگستر","فولاد","شپنا","فملی","شستا",
        "فسبزوار","خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور","فپنتا",
        "شبندر","فارس","غفارس","وبصادر","کچاد","کگل","داتام","نخريس","پاکشو",
        "درازک","كپارس","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
        "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
        "تاصيكو","نخريس","قهكمت"]


# Divide the list into three rows
rows = [namad[i:i+5] for i in range(0, len(namad), 5)]

# Print the rows next to each other with numbers
for i, row in enumerate(rows):
    for j, stock in enumerate(row):
        stock_number = i*5 + j + 1
        print(f"{stock_number}. {stock}", end="\t")
    print()


# Ask the user to enter a valid index
index = int(input("Please write the name of the stock you want : \n write in namad :"))
# Run Python for the selected stock    
stock = namad[index-1]

choice = index
sahame = namad[choice-1]
# Do some analysis or visualization here
tse.download(symbols=sahame,
             write_to_csv=True,
             adjust=True)
ticker = tse.Ticker(sahame)
  
print(ticker.last_date,'Date and time of the last transaction')
print ('-'*20)
print(ticker.title)
print(ticker.state,ticker.flow,ticker.group_name)     
print(ticker.fiscal_year,' : Fiscal year')  
print(ticker.eps ,'  :  EPS  ')  
print(ticker.p_e_ratio ,' :   P/E') 
print(ticker.float_shares,' : floating shares')   
print(ticker.base_volume,' :  Base volume ')
print()  
print(ticker.last_price,' :  Last price ')  
print(ticker.adj_close,' :  adj cloos ')  
print(ticker.yesterday_price,' : yesterday price ')
print(ticker.open_price,' : open price')   
print()
print(ticker.high_price,' :  high price')  
print(ticker.low_price,' :  Low price')
print(ticker.sta_max,' :  ste max ')  
print(ticker.sta_min,' :  sta min')
print()
print(ticker.volume,' :  volume ')
print(ticker.month_average_volume,' :  month average volume')
print()

print('-*'*20)
if ticker.adj_close > ticker.max_year :
     print ('  break ticker max year')


if (ticker.min_week)>(ticker.adj_close):
     print(' ticker min week > ticker adj close ')
else:
     if (ticker.min_week)<(ticker.adj_close):
          print(' ticker min week < ticker adj close ')


if (ticker.max_week)<(ticker.adj_close):
     print(' ticker max week < ticker adj close')
     
print('-*'*20) 

# محاسبه بدست آوردن فاصله بين حداکثروحداقل قيمت به درصد
Percent =((((ticker.high_price)-(ticker.low_price))/(ticker.high_price))*100)
Percent_last =((((ticker.last_price)-(ticker.adj_close))/(ticker.last_price))*100)                                                                         
tik_close_low = ((((ticker.adj_close)-(ticker.low_price))/(ticker.adj_close))*100)
tik_open_low = ((((ticker.open_price)-(ticker.low_price))/(ticker.open_price))*100)
tik_ascending = ((math.ceil(tik_close_low))-(math.ceil(tik_open_low)))
tik_close_high = ((((ticker.high_price)-(ticker.adj_close))/(ticker.high_price))*100)
tik_open_high = ((((ticker.high_price)-(ticker.open_price))/(ticker.high_price))*100)
tik_Descending =((math.ceil(tik_close_high))-(math.ceil(tik_open_high)))
                              
if (ticker.last_price) > (ticker.adj_close):
     print ((math.floor(Percent )),'% : فاصله بالاترين وپايين ترين قيمت امروزبه درصد')
else:
     if (ticker.last_price) < (ticker.adj_close):
          print (-(math.floor(Percent )),'% : فاصله بالاترين وپايين ترين قيمت امروزبه درصد')


if (ticker.last_price) > (ticker.adj_close):
     print ((math.floor(Percent_last )),'% : price Tomorrow ( - )')
     print ("قیمت امروزکمترازقیمت دیروزشد")
else:
     if (ticker.last_price) < (ticker.adj_close):
          print ((math.floor(Percent_last)),'% : price Tomorrow ( + )')
          print("قیمت امروزبشترازقیمت دیروزشد")


#===============================================================
print(40*"=",sahame,"Process")     
if ticker.adj_close >= ticker.max_week :
     print ('ticker adj close >= ticker max week')
     print (ticker.max_week," : max week")
     print (ticker.adj_close," : adj close")
else :
     if ticker.adj_close <= ticker.min_week  :
          print ('ticker adj close <= ticker max week')
          print (ticker.min_week," : max week")
          print (ticker.adj_close," : adj close")


#==================================================================
print(20*"-",sahame," Up or Down Tick")

if ticker.open_price>ticker.low_price < ticker.adj_close:
     if (math.ceil(tik_close_low))>(math.ceil(tik_open_low)):     
          if ticker.adj_close > ticker.open_price :
               print (tik_ascending , ' : Up tick')
          else:
               if ticker.open_price<ticker.high_price > ticker.adj_close:
                    if (math.ceil(tik_close_high))>(math.ceil(tik_open_high)):
                         if ticker.adj_close < ticker.open_price :
                              print (tik_Descending , ' :  Down tick')
               


if ticker.open_price > ticker.yesterday_price and ticker.low_price < ticker.yesterday_price:
     if ticker.adj_close > ticker.open_price:
          print (" Today Up tick")
     else:
          if ticker.open_price < ticker.yesterday_price and ticker.high_price > ticker.yesterday_price:           
               if ticker.adj_close < ticker.open_price:
                     print (" Today Down tick")


#=================================================

print(30*"=",sahame," True and False مقادير sma3-10")          

history = ticker.history

def sma(series, periods: int, ):
    return series.rolling(window=periods, min_periods=periods).mean()

sma_3 = sma(history.close, 3)
sma_10 = sma(history.close, 10)
buy_signals = (
        (sma_3 > sma_10) &
        (sma_10.shift(1) > sma_3.shift(1))
)
print(buy_signals.tail(3))
#-------------------------------------------
print(30*"=",sahame," True and False مقادير sma3-20")          

history = ticker.history

def sma(series, periods: int, ):
    return series.rolling(window=periods, min_periods=periods).mean()

sma_3 = sma(history.close, 3)
sma_20 = sma(history.close, 20)
buy_signals = (
        (sma_3 > sma_20) &
        (sma_20.shift(1) > sma_3.shift(1))
)
print(buy_signals.tail(3))         
#==========================================================
#print(45*"=",nam,"hm_Fib and mo_Fib")
#if (ticker.max_year)>(ticker.adj_close) and (ticker.adj_close)<(ticker.yesterday_price):
hm1= (((((ticker.max_year)*23.60)/100)-(ticker.max_year)),' : hm_Fib_23.60')#: max_Fib_23.60
hm2= (((((ticker.max_year)*38.20)/100)-(ticker.max_year)),' : hm_Fib_38.20')#: max_Fib_38.20'
hm3= (((((ticker.max_year)*50)/100)-(ticker.max_year)),' : hm_Fib_50')      #: max_Fib_50
hm4= (((((ticker.max_year)*61.80)/100)-(ticker.max_year)),' : hm_Fib_61.80')#: max_Fib_61.80
hm5= (ticker.min_year,' : hm_Fib_78.60')                                          #: Fib_0
hm6= (((((ticker.min_year)*23.60)/100)-(ticker.min_year)),' : hm_Fib_161.80')#: min_Fib_23.60
#print ('حمايت 1',hm1,'\nحمايت 2', hm2,'\nحمايت 3', hm3,'\nحمايت 4', hm4,'\nحمايت 5',hm5,'\nحمايت 6',hm6,'\nحمايت 7',hm7,'\nحمايت 8',hm8,'\nحمايت 9',hm9)
     
#if (ticker.min_year)<(ticker.adj_close) and (ticker.adj_close)>(ticker.yesterday_price):
mo1= (((((ticker.min_year)*23.60)/100)+(ticker.min_year)),' : mo_Fib_23.60') #: min_Fib_23.60
mo2= (((((ticker.min_year)*38.20)/100)+(ticker.min_year)),' : mo_Fib_38.20') #: min_Fib_38.20
mo3= (((((ticker.min_year)*50)/100)+(ticker.min_year)),' : mo_Fib_50')       #: min_Fib_50
mo4= (((((ticker.min_year)*61.80)/100)+(ticker.min_year)),' : mo_Fib_61.80') #: min_Fib_61.80
mo5= (((((ticker.min_year)*78.60)/100)+(ticker.min_year)),' : mo_Fib_78.60') #: min_Fib_78.60
mo6= (((((ticker.min_year)*100)/100)+(ticker.min_year)),' : mo_Fib_100')     #: min_Fib_100
#print (' مقاومت1 ',mo1,'\n مقاومت2 ', mo2,'\n مقاومت3 ', mo3,'\n مقاومت4 ', mo4,'\n مقاومت5 ', mo5,'\n مقاومت6 ', mo6,'\n مقاومت7 ', mo7,'\n مقاومت8 ', mo8,'\n مقاومت9 ', mo9,'\n مقاومت10 ', mo10)
#-----------------------------------
Fib=print(45*"=",sahame,"year for hm_Fib and mo_Fib")
if (ticker.max_year)>(ticker.adj_close)<(ticker.yesterday_price):
     print ( hm1,'\n', hm2,'\n', hm3,'\n', hm4,'\n',hm5,'\n',hm6)     
  
     print('-'*20)

else:
    if (ticker.min_year)<(ticker.adj_close) >(ticker.yesterday_price):
         print (  mo1,'\n', mo2,'\n', mo3,'\n', mo4,'\n', mo5,'\n', mo6) 
  
         print('-'*20)          
#----------------------------------

#==========================================================
#print(45*"=",nam,"hm_Fib and mo_Fib")
#if (ticker.max_year)>(ticker.adj_close) and (ticker.adj_close)<(ticker.yesterday_price):
hm1= (((((komu52_max)*23.60)/100)-(komu52_max)),' : hm_Fib_23.60')#: max_Fib_23.60
hm2= (((((komu52_max)*38.20)/100)-(komu52_max)),' : hm_Fib_38.20')#: max_Fib_38.20'
hm3= (((((komu52_max)*50)/100)-(komu52_max)),' : hm_Fib_50')      #: max_Fib_50
hm4= (((((komu52_max)*61.80)/100)-(komu52_max)),' : hm_Fib_61.80')#: max_Fib_61.80
hm5= (komu52_max,' : hm_Fib_78.60')                                          #: Fib_0
hm6= (((((komu52_min)*23.60)/100)-(komu52_min)),' : hm_Fib_161.80')#: min_Fib_23.60
#print ('حمايت 1',hm1,'\nحمايت 2', hm2,'\nحمايت 3', hm3,'\nحمايت 4', hm4,'\nحمايت 5',hm5,'\nحمايت 6',hm6,'\nحمايت 7',hm7,'\nحمايت 8',hm8,'\nحمايت 9',hm9)
     
#if (ticker.min_year)<(ticker.adj_close) and (ticker.adj_close)>(ticker.yesterday_price):
mo1= (((((komu52_min)*23.60)/100)+(komu52_min)),' : mo_Fib_23.60') #: min_Fib_23.60
mo2= (((((komu52_min)*38.20)/100)+(komu52_min)),' : mo_Fib_38.20') #: min_Fib_38.20
mo3= (((((komu52_min)*50)/100)+(komu52_min)),' : mo_Fib_50')       #: min_Fib_50
mo4= (((((komu52_min)*61.80)/100)+(komu52_min)),' : mo_Fib_61.80') #: min_Fib_61.80
mo5= (((((komu52_min)*78.60)/100)+(komu52_min)),' : mo_Fib_78.60') #: min_Fib_78.60
mo6= (((((komu52_min)*100)/100)+(komu52_min)),' : mo_Fib_100')     #: min_Fib_100
#print (' مقاومت1 ',mo1,'\n مقاومت2 ', mo2,'\n مقاومت3 ', mo3,'\n مقاومت4 ', mo4,'\n مقاومت5 ', mo5,'\n مقاومت6 ', mo6,'\n مقاومت7 ', mo7,'\n مقاومت8 ', mo8,'\n مقاومت9 ', mo9,'\n مقاومت10 ', mo10)
#-----------------------------------
Fib=print(45*"=",sahame,"komu52 for hm_Fib and mo_Fib")
if (komu52_max)>(ticker.adj_close)<(ticker.yesterday_price):
     print ( hm1,'\n', hm2,'\n', hm3,'\n', hm4,'\n',hm5,'\n',hm6)     
  
     print('-'*20)

else:
    if (komu52_min)<(ticker.adj_close) >(ticker.yesterday_price):
         print (  mo1,'\n', mo2,'\n', mo3,'\n', mo4,'\n', mo5,'\n', mo6) 
  
         print('-'*20)          
#----------------------------------

print(40*"="," Your stock purchase and sale calculations",sahame,)
# چکارن
if index == 1:
     p=0
     s=4250
     v=20000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib    
# تليسه
if index == 2:
     p=4285
     s=0
     v=75000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  
# غمينو
if index == 3:
     p=11181
     s=10110
     v=5000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib   
# وسپه
if index == 4:
     p=4548
     s=5062
     v=7538
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib   
# غکورش
if index == 5:
     p=9605
     s=0
     v=23000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib    
# شپاکسا
if index == 6:
     p=1625
     s=0
     v=5000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your buy price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  
# پاکشو
if index == 7:
     p=0
     s=7100
     v=21964
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  
# تاپيکو
if index == 8:
     p=0
     s=17560
     v=2000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  
# دسبحان
if index == 9:
     p=0
     s=11650
     v=10000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your buy price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  
# کگل
if index == 10:
     p=0
     s=7050
     v=4000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  
# ومعادن
if index == 11:
     p=0
     s=0
     v=0
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  
# حتوکا
if index == 12:
     p=3261
     s=3400
     v=5000
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib  

if index >= 13 :
     print (sahame ,'  :  شماازاين سهم خريد نداريد')
         
import sys

if index<=12 and p > 0:     
     price=p
     price_s=s
     vol=v
     # قيمت امروزسهم Today's stock price
     today_price = (math.ceil(ticker.adj_close))     
     price_kharid= (-0.004 * price)  #کارمزد خريد
     price_forosh= (-0.009 * today_price) #کارمزد فروش محاسبه باقيمت امروز
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
          print (" Your total payment is Buy  :" ,pk)
          print (" If you sell the rest today :" , pf)
          print (" You make a profit in the amount :" ,pp)
          print("Your profit percentage : درصدسودشماشده : {}% ".format(math.ceil(profit_percentage)))
          print(20*"-" )
     elif today_price < stop_loss:
          loss = str ( pk - pf )
          loss_float = float(loss)
          loss_percentage = (loss_float / pk) * 100
          print (" Your total payment is Buy :" ,pk)
          print (" if sell price :" , pf)
          print ("   You lose the amount  :" ,pp)
          print("The percentage of your loss : درصدضررشماشده : {}% ".format(math.ceil(loss_percentage)))
          print(20*"-" )
     else:
          if pk > pf :
              print("Price to limit")
              print (" price is not  +20% !  \n The price has not reached the profit of 20%")                             
              print (sz ,": If you sell today, your profit سود")
              print(20*"-" )
          if pk < pf :
              print("Price to limit")
              print (" price is not -3% !  \n The price has not reached the level of 3% loss") 
              print(sz,": If you sell today, you will lose زيان")
              print(20*"-" )
          
          
     if p == p :
          hs1 = (( p * 0.2 + p )*100)/100 # حدسود20درصد
          hs2 = (( p * 0.1 + p )*100)/100 # حدسود10درصد
          hs3 = (( p * 0.05 + p )*100)/100 # حدسود5درصد
          hs4 = (( p * 0.011 + p )*100)/100 # قيمت سربه سر
          hz = ((p * -0.03 + p)*100)/100# حدضرر3درصد
          print (' : تعيين حدسودوزيان بااحتساب قيمت خريد شمااز ',sahame)
          print ((math.ceil(hs1)),'   20% profit')
          print ((math.ceil(hs2)),'   10% profit')
          print ((math.ceil(hs3)),'   5% profit') 
          print ((math.ceil(hz)),'    3% loss')
          print ((math.ceil(hs4)),'   Best selling price ( = )')
          print (ticker.last_price,' : last price ')
          print ('-'*20)

          
     if pk == pf :
          print ("  Best selling price :" ,today_price )
          print ('-------')

#=====================================================          
print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')         

