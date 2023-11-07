 
# برسي سهام فقط باتايپ نام سهم
# محاسبات RSI - ichimoku - EMA - Volume - Profit and loss - Charts
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

nam = input ("Please write the name of the stock you want : \n لطفا نام سهام موردنظرتان رابنويسسد :")

DF = tse.Get_Price_History(stock=nam,
                             start_date='1401-05-01',
                             end_date='1402-07-07',
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

#print(DF.head())

# Get today's price قيمت وحجم امروز
today_price = DF['Close'].iloc[-1] # قيمت بسته شدن امروز
today_Final_price = DF['Final'].iloc[-1] # قيمت آخرين معامله امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
yesterday_price = DF['Close'].iloc[-2]  # قيمت بسته شدن ديروز
yesterday_Final_price = DF['Final'].iloc[-2] # قيمت آخرين معامله ديروز
yesterday_Open_price = DF['Open'].iloc[-2] # قيمت بازشدن ديروز
today_two_price = DF['Close'].iloc[-3]   # قيمت بسته شدن دوروزقبل

today_price_max = DF['High'].iloc[-1] # بالاترين قيمت امروز
today_price_min = DF['Low'].iloc[-1]  # پايين ترين قيمت امروز


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

Volume_week = DF['Volume'].iloc[-5] # حجم هفتگي
Volume_Month = DF['Volume'].iloc[-26] # حجم ماهيانهBase volume
today_Volume = DF['Volume'].iloc[-1] # حجم امروز
today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز

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

average_max_price = max_price.mean() # ميانگين بالاترين قيمت 9روز ten_max_m9
average_min_price = min_price.mean() # ميانگين پايين ترين قيمت 9روز ten_min_m9

average_max_price2 = max_price2.mean() # ميانگين بالاترين قيمت 26روز kij_max_m26
average_min_price2 = min_price2.mean() #ميانگين پايين ترين قيمت 26روز kij_min_m26

average_Volume_week = Volume_week.mean() # محاسبه ميانگين حجم هفتگي
average_Volume_Month = Volume_Month.mean() # محاسبه ميانگين حجم ماهيانه
#print (" (220روزه)مقدارسودوزيان حاصل ازخريد اول وقت وفروش آخروقت")
#print (DF["Close"].head(220).sum())
#=====================================================
print(30*"-")
print(10*" ","rsi value")
rsi = ta.momentum.rsi(DF['Close'], length=14)
#rsi_diff = rsi.diff(3)
#print(rsi.diff())
rsi_diff = rsi
print(rsi.tail(3))

Month_price = DF['Close'].iloc[-26] # قيمت بسته شدن يک ماه قبل
rsi_Month = rsi_diff.iloc[-26]  # يک ماه قبل rsi

if today_price>yesterday_price > today_two_price :
    if yesterday_price<(Month_price):
        if (math.ceil(rsi_diff.iloc[-1]))>(math.ceil(rsi_diff.iloc[-2])) < (math.ceil(rsi_diff.iloc[-3])):
            if (math.ceil(rsi_diff.iloc[-2]))>(math.ceil(rsi_diff.iloc[-26]))and (math.ceil(rsi_diff.iloc[-2]))< 30 :
                print ('Buy down price : واگراي مثبت شده rsi')


if today_price>yesterday_price < today_two_price :
    if yesterday_price>(Month_price):
        if (math.ceil(rsi_diff.iloc[-1]))>(math.ceil(rsi_diff.iloc[-2])) < (math.ceil(rsi_diff.iloc[-3])):
            if (math.ceil(rsi_diff.iloc[-2]))<(math.ceil(rsi_diff.iloc[-26]))and (math.ceil(rsi_diff.iloc[-2]))< 30 :
                print ('Buy top price: واگراي مثبت شده rsi')   


if today_price<yesterday_price > today_two_price :
    if yesterday_price<(Month_price):
        if (math.ceil(rsi_diff.iloc[-1]))<(math.ceil(rsi_diff.iloc[-2])) > (math.ceil(rsi_diff.iloc[-3])):
            if (math.ceil(rsi_diff.iloc[-2]))>(math.ceil(rsi_diff.iloc[-26]))and (math.ceil(rsi_diff.iloc[-2]))>70 :
                print ('sell down price : واگرايي منفي rsi')
                

if today_price<yesterday_price > today_two_price :
    if yesterday_price>(Month_price):
        if (math.ceil(rsi_diff.iloc[-1]))<(math.ceil(rsi_diff.iloc[-2])) > (math.ceil(rsi_diff.iloc[-3])):
            if (math.ceil(rsi_diff.iloc[-2]))<(math.ceil(rsi_diff.iloc[-26]))and (math.ceil(rsi_diff.iloc[-2]))>70 :
                print ('sell top price : واگرايي منفي rsi')
        

if rsi_diff.iloc[-1] == 50 and rsi_diff.iloc[-2] < rsi_diff.iloc[-1] and today_price > yesterday_price:      
     print(" Rsi : ورود به بالاي 50 ")
else:
     if rsi_diff.iloc[-1] == 50 and rsi_diff.iloc[-2] > rsi_diff.iloc[-1] and today_price < yesterday_price:      
          print(" Rsi : ريزش به زير50 ")
                

if rsi_diff.iloc[-1] == 30 and rsi_diff.iloc[-2] > rsi_diff.iloc[-1] and today_price < yesterday_price:      
     print(" Rsi : ورود به منطقه اشباع فروش ")
else:
     if rsi_diff.iloc[-1] == 70 and rsi_diff.iloc[-2] < rsi_diff.iloc[-1] and today_price > yesterday_price:
          print(" Rsi : ورود به منطقه اشباع خريد")
                

if rsi_diff.iloc[-1] == 30 and rsi_diff.iloc[-2] < rsi_diff.iloc[-1] and today_price > yesterday_price:      
     print(" Rsi : خروج ازمنطقه اشباع فروش ")
else:
     if rsi_diff.iloc[-1] == 70 and rsi_diff.iloc[-2] > rsi_diff.iloc[-1] and today_price < yesterday_price:
          print(" Rsi : خروج ازمنطقه اشباع خريد")


if (rsi_diff.iloc[-1])>70 and (rsi_diff.iloc[-2])>(rsi_diff.iloc[-3]) and (rsi_diff.iloc[-2])>70:
     print (' RSI  >  70')
if (rsi_diff.iloc[-1])<70 and (rsi_diff.iloc[-2])<(rsi_diff.iloc[-3])and (rsi_diff.iloc[-2])<70:
     print (' RSI  <  70')
if (rsi_diff.iloc[-1])>50 and (rsi_diff.iloc[-2])>(rsi_diff.iloc[-3])and (rsi_diff.iloc[-2])>50:
     print (' RSI  >  50')
if (rsi_diff.iloc[-1])<50 and (rsi_diff.iloc[-2])<(rsi_diff.iloc[-3])and (rsi_diff.iloc[-2])<50:
     print (' RSI  <  50')
if (rsi_diff.iloc[-1])>30 and (rsi_diff.iloc[-2])>(rsi_diff.iloc[-3])and (rsi_diff.iloc[-2])>30:
     print (' RSI  >  30')
if (rsi_diff.iloc[-1])<30 and (rsi_diff.iloc[-2])<(rsi_diff.iloc[-3])and (rsi_diff.iloc[-2])<30:
     print (' RSI  <  30')

print(30*"-")
#================================================
# EMA_3,10,20 نمايش نمودارقيمت و
DF.index = DF['Date']
mplf.plot(DF[-100:], type='candle', mav=(3, 10, 20))
plt.show()

# Calculate the average price for ten days
ten_day_average = DF['Close'].rolling(10).mean()
today_price_scalar = today_price.item()
#================================================

# First row information اطلاعات کامل رديف اول سهم
nemone = DF.iloc[-1]
print (nemone)
#print(30*"-")
#print ('First:قيمت بازشدن - Value:ارزش کل معاملات امروز- OPENINT:بازده سودروز')
#print ()
 # نمايش واريانس وديسکرايو و...
#print (DF.describe())
#=================================================
print(40*"=",nam,"Volume")

print (' حجم ماهيانه : ' ,(math.ceil(average_Volume_Month)))
          
if today_Volume > (math.ceil(average_Volume_Month)):
     print ('حجم امروزبيشترازحجم ماهيانه شده')
else:
     if today_Volume < (math.ceil(average_Volume_Month)):
          print ('حجم امروزکمتر ازحجم ماهيانه شده')
     elif today_Volume > today_Volume_yesterday :
          print ('حجم امروزبيشترازحجم ديروزشده')
     else:
         if today_Volume < today_Volume_yesterday :
               print ('حجم امروز کمترازحجم ديروزشده')
               
if today_Volume < today_Volume_yesterday < Volume_week:
       print ('حجم درهفته گذشته کاهشي بود')
else:
     if today_Volume > today_Volume_yesterday > Volume_week:
         print ('حجم درهفته گذشته افزايشي بود')
     elif today_Volume < today_Volume_yesterday :
          print ('حجم امروز کمترازحجم ديروزشده')
     else:
          if today_Volume > (math.ceil(average_Volume_Month))*3 :
               print ('حجم امروز بيشترازدوبرابر حجم ماهيانه شده')

print ()               
print (today_Volume , 'حجم امروز')
print (today_Volume_yesterday , 'حجم ديروز')
#==================================================
print(40*"=",nam,"Moving Average")
ave7 = (' EM_3 :',(math.ceil(average_prices7)))
ave5 = (' EM_26 :',(math.ceil(average_prices2)))
print (ave7,'     ',ave5)
ave1 = (' EM_5 :',(math.ceil(average_prices6)))
ave2 = (' EM_50 :',(math.ceil(average_prices3)))
print (ave1,'     ',ave2)
ave3 = (' EM_10 :',(math.ceil(average_price)))
ave4 = (' EM_103 :',(math.ceil(average_prices4)))
print (ave3,'     ',ave4)
ave8 = (' EM_20 :',(math.ceil(average_prices8)))
ave6 = (' EM_150 :',(math.ceil(average_prices5)))
print  (ave8,'    ',ave6)
print(25*"-")

# Calculate the average price for ten days
ten_day_average = DF['Close'].rolling(10).mean()

# Calculate the average price for twenty-six days
twenty_six_day_average = DF['Close'].rolling(26).mean()

# Get today's 26-day average price
today_twenty_six_day_average = twenty_six_day_average.iloc[-1]
          
# Compare the average price to today's price
if today_price > average_prices7 > average_prices8 :
     print(' the news signal : price > EMA_3 > EmE_20')
else:
     if today_price < average_prices7 < average_prices8 :
          print(' Sell signal : price < EMA_3 < EmE_20')
          
if today_price > average_prices7 > average_price :
     print(' Buy signal Important : price > EMA_3 > EmE_10')
else:
     if today_price < average_prices7 < average_price : 
          print(' Sell signal Important: price < EMA_3 < EmE_10')         
          
if today_price > average_prices3 > average_prices4 :
     print (' signal Important ascending : price > EM_50 > EM_130 ')
else:
     if today_price < average_prices3 < average_prices4 :
          print (' signal Important Descending : price < EM_50 < EM_130 ')

if average_prices7 > average_price :
     print (' EM_3 > Em_10 ')
else:
     if average_prices7 < average_price :
         print (' EM_3 < Em_10 ')

if average_prices7 < average_prices8:
     print (" EM_3 < EM_20")
else:
     if average_prices7 > average_prices8:
          print (" EM_3 > EM_20")
               

print(25*"-")
if today_price > yesterday_price:
     print (' دقت کنيد قيمت افزايشي است ')
     print ("today_price > yesterday_price")
else :
     if today_price < yesterday_price:
          print (' دقت کنيد قيمت کاهشي است ')
          print ("today_price < yesterday_price")

#==================================================
print(45*"=",nam,"Engulfing Calculations")
# Engulfing Calculations  محاسبات اينگل فينگ
today_price = DF['Close'].iloc[-1]   # آخرین قیمت امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
yesterday_price = DF['Close'].iloc[-2] # آخرین قیمت دیروز
yesterday_Open_price = DF['Open'].iloc[-2] # قيمت بازشدن ديروز

highest_price_30 = max(DF['Close'][-30:])
highest_price_280 = max(DF['Close'][-280:])
highest_price_180 = max(DF['Close'][-180:])
highest_price_90 = max(DF['Close'][-90:])
lowest_price_30 = min(DF['Close'][-30:])
lowest_price_280 = min(DF['Close'][-280:])                              
lowest_price_180 = min(DF['Close'][-180:])
lowest_price_90 = min(DF['Close'][-90:])

print (today_price,': قيمت امروز')
print(highest_price_280,': مقاومت يک سال پيش')
print(highest_price_180,': مقاومت شش ماه پيش')
print(highest_price_90,': مقاومت سه ماه پيش')
print(lowest_price_280,': حمايت يک سال پيش')
print(lowest_price_180,': حمايت شش ماه پيش')
print(lowest_price_90,': حمايت سه ماه پيش')


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

print (h5,'ascending روند صعودي ')
print (h10 ,'Descending روند نزولي')

if today_price > highest_price_90 :
     print (' مقاومت سه ماه شکسته شد')

if today_price < lowest_price_90 :
     print (' حمايت سه ماه ازدست رفت')
     
print(20*"-")

if h_ascending and h5:
    c = "Engulfing :"
    print (c , "hemer ascending !  صعودي مناسب خريد" )
    
if h_Descending and h10:
    c = "Engulfing :"
    print (c , "hemer Descending !  نزولي وقت فروش" )
    
else:
    c = "hold :"
    print (c , "not Engulfing !")
    print ()
    print ("نمودارهاي قيمت هنوزاينگل فينگي تشکيل ندادند")
#===================================================
print(45*"=",nam,"hm_Fib and mo_Fib")
#if (ticker.max_year)>(ticker.adj_close) and (ticker.adj_close)<(ticker.yesterday_price):
hm1= (((((highest_price_90)*23.60)/100)-(highest_price_90)),' : hm_Fib_23.60')#: max_Fib_23.60
hm2= (((((highest_price_90)*38.20)/100)-(highest_price_90)),' : hm_Fib_38.20')#: max_Fib_38.20'
hm3= (((((highest_price_90)*50)/100)-(highest_price_90)),' : hm_Fib_50')      #: max_Fib_50
hm4= (((((highest_price_90)*61.80)/100)-(highest_price_90)),' : hm_Fib_61.80')#: max_Fib_61.80
hm5= (highest_price_90,' : hm_Fib_78.60')                                          #: Fib_0
hm6= (((((highest_price_90)*23.60)/100)-(highest_price_90)),' : hm_Fib_161.80')#: min_Fib_23.60
hm7= (((((highest_price_90)*38.20)/100)-(highest_price_90)),' : hm_Fib_261.80')#: min_Fib_38.20
hm8= (((((highest_price_90)*78.60)/100)-(highest_price_90)),' : hm_Fib_361.80')#: max_Fib_78.60
hm9= (((((highest_price_90)*50)/100)-(highest_price_90)),' : hm_Fib_423.60')      #: min_Fib_50
if (highest_price_90)>(today_price) and (today_price)<(yesterday_price):
     print (  hm1,'\n', hm2,'\n', hm3,'\n', hm4,'\n',hm5,'\n',hm6,'\n',hm7,'\n',hm8,'\n',hm9)
     
#if (ticker.min_year)<(ticker.adj_close) and (ticker.adj_close)>(ticker.yesterday_price):
mo1= (((((lowest_price_90)*23.60)/100)+(lowest_price_90)),' : mo_Fib_23.60') #: min_Fib_23.60
mo2= (((((lowest_price_90)*38.20)/100)+(lowest_price_90)),' : mo_Fib_38.20') #: min_Fib_38.20
mo3= (((((lowest_price_90)*50)/100)+(lowest_price_90)),' : mo_Fib_50')       #: min_Fib_50
mo4= (((((lowest_price_90)*61.80)/100)+(lowest_price_90)),' : mo_Fib_61.80') #: min_Fib_61.80
mo5= (((((lowest_price_90)*78.60)/100)+(lowest_price_90)),' : mo_Fib_78.60') #: min_Fib_78.60
mo6= (((((lowest_price_90)*100)/100)+(lowest_price_90)),' : mo_Fib_100')     #: min_Fib_100
mo7= (((((lowest_price_90)*161.80)/100)+(lowest_price_90)),' : mo_Fib_161.80')# : min_Fib_161.80
mo8= (((((lowest_price_90)*261.80)/100)+(lowest_price_90)),' : mo_Fib_261.80')#: min_Fib_261.80
mo9= (((((lowest_price_90)*361.80)/100)+(lowest_price_90)),' : mo_Fib_361.80')#: min_Fib_361.80
mo10=(((((lowest_price_90)*423.60)/100)+(lowest_price_90)),' : mo_Fib_423.60')#: min_Fib_423.60
if (lowest_price_90)<(today_price) and (today_price)>(yesterday_price):
     print (  mo1,'\n', mo2,'\n', mo3,'\n', mo4,'\n', mo5,'\n', mo6,'\n', mo7,'\n', mo8,'\n', mo9,'\n', mo10)
                   
    
#===================================================
print(45*"=",nam,"ichimoku")

today_price = DF['Close'].iloc[-1] # قيمت بسته شدن امروز
today_Volume = DF['Volume'].iloc[-1] # حجم امروز
today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز

highest_price_9 = max(DF['Close'][-9:]) #  ten_max_9
lowest_price_9 = min(DF['Close'][-9:])  #  ten_min_9
ten_list_max_9 = [highest_price_9]
ten_list_min_9 = [lowest_price_9]

highest_price_10 = max(DF['Close'][-10:]) #  ten_max_10
lowest_price_10 = min(DF['Close'][-10:])  #  ten_min_10
ten_list_max_10 = [highest_price_10]
ten_list_min_10 = [lowest_price_10]

highest_price_11 = max(DF['Close'][-11:]) #  ten_max_11
lowest_price_11 = min(DF['Close'][-11:])  #  ten_min_11
ten_list_max_11 = [highest_price_11]
ten_list_min_11 = [lowest_price_11]

highest_price_26 = max(DF['Close'][-26:]) #  kij_max_26
lowest_price_26 = min(DF['Close'][-26:])  #  kij_min_26
kij_list_max_26 = [highest_price_26]
kij_list_min_26 = [lowest_price_26]

highest_price_27 = max(DF['Close'][-27:]) #  kij_max_27
lowest_price_27 = min(DF['Close'][-27:])  #  kij_min_27
kij_list_max_27 = [highest_price_27]
kij_list_min_27 = [lowest_price_27]

highest_price_28 = max(DF['Close'][-28:]) #  kij_max_28
lowest_price_28 = min(DF['Close'][-28:])  #  kij_min_28
kij_list_max_28 = [highest_price_28]
kij_list_min_28 = [lowest_price_28]

# محاسبات تنکنسن ten_1
for ich_ten_1 in range (18):
    ich_ten_1 = (ten_list_max_9,ten_list_min_9)
    t1 = ((highest_price_9)+(lowest_price_9))
    ten_1 = (t1 / 2)

# محاسبات تنکنسن ten_2
for ich_ten_2 in range (20):
    ich_ten_2 = (ten_list_max_10,ten_list_min_10)
    t2 = ((highest_price_10)+(lowest_price_10))
    ten_2 = (t2 / 2)

# محاسبات تنکنسن ten_3
for ich_ten_3 in range (22):
    ich_ten_3 = (ten_list_max_11,ten_list_min_11)
    t3 = ((highest_price_11)+(lowest_price_11))
    ten_3 = (t3 / 2)

# محاسبات کيجونسن kij_1
for ich_kij_1 in range (52):
    ich_kij_1 = (kij_list_max_26,kij_list_min_26)
    kj1 = ((highest_price_26)+(lowest_price_26))
    kij_1 = (kj1 / 2)

# محاسبات کيجونسن kij_2
for ich_kij_2 in range (54):
    ich_kij_2 = (kij_list_max_27,kij_list_min_27)
    kj2 = ((highest_price_27)+(lowest_price_27))
    kij_2 = (kj2 / 2)

# محاسبات کيجونسن kij_3
for ich_kij_3 in range (56):
    ich_kij_3 = (kij_list_max_28,kij_list_min_28)
    kj3 = ((highest_price_28)+(lowest_price_28))
    kij_3 = (kj3 / 2)

if today_price > yesterday_price and ten_1>=kij_1:
     if ten_1>ten_2 and kij_1>kij_2:
          print (" buy : کراس تنکنس وکيجونسن روبه بالا ")


if today_price < yesterday_price and ten_1<=kij_1:
     if ten_1<ten_2 and kij_1<kij_2:
          print (" sell : کراس تنکنسن وکسجونسن رو به پايين ")


if  today_price > ten_1 >kij_1 and ten_2>ten_3 and kij_2>kij_3:
     if today_price > yesterday_price:
          c = (' price > ten > kij and ten_2 > ten_3 and kij_2 > kij_3:')
          print (c , ' \n ascending buy  !  صعودي ادامه دار')
          print()


if  today_price < ten_1 <kij_1 and ten_2<ten_3 and kij_2<kij_3:
     if today_price < yesterday_price:
          c1 = (' price < ten < kij and ten_2 < ten_3 and kij_2 < kij_3 :')
          print (c1 , ' \n Descending sell !  نزولي ادامه دار')
          print()


if  today_price > ten_1 >ten_2 and ten_1>kij_1 :
     if today_price > yesterday_price :
          c2 = (' price > ten > kij :')
          print (c2 , ' \n ascending !  صعودي شد') 


if  today_price < ten_1 <ten_2 and ten_1<kij_1 :
     if today_price < yesterday_price :
          c3 = (' price < ten < kij :')
          print (c3 , ' \n Descending !  نزولي شد')


if today_price > ten_1 >=ten_2 and ten_1<kij_1 and kij_1==kij_2 ==kij_3 :
     c4 = (' price > ten < kij_1=kij_2=kij_3 : ')
     print (c4 , ' \n Buy Equilibrium ')
     print ((int(kij_1))," : احتمال صعود تا")


if today_price < ten_1 <ten_2 and ten_1>kij_1 and kij_1==kij_2 ==kij_3  :
     c5 = (' price < ten > kij_1=kij_2 = kij_3: ')
     print (c5 , ' \n Sell Equilibrium ')
     print ((int(kij_1))," : احتمال ريزش تا")

senk_sa1 = (kij_1+ten_1)/2    # senkou aسنکو
senk_sa2 = (kij_2+ten_2)/2    # senkou aسنکو
senk_ab1 = (max(DF['Close'][-52:])+min(DF['Close'][-52:]))/2  #senkou  bسنکو
senk_ab2 = (max(DF['Close'][-54:])+min(DF['Close'][-54:]))/2  #senkou  bسنکو

if senk_sa1 <  senk_ab1  :
     print (" ابرکوموآينده قرمزه")
else:
     if senk_sa1 >  senk_ab1  :
          print (" ابرکومو آينده سبزه")

if senk_sa1 <  senk_ab1 < today_price :
     print (" قيمت داره ميره زيرابرقرمز ")
else:
     if senk_sa1 >  senk_ab1 > today_price :  
          print (" قيمت داره ميره بالاي ابرقرمز ")
print ()
#-------------------------------------------
print(20*"-",nam,"bmi محاسبه")
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

# شروع شرط براي محاسبه 
if bmi < adj_close:
    print("قيمت پايين ترمياد")
elif bmi > adj_close:
    print("قيمت بالاتر ميره")
elif bmi == adj_close:
    print("قيمت درجاميزنه گيجه")
elif bmi < ticker.yesterday_price:
    print ("احتمال ريزش شديدخارج شو")
else:
    print("معامله نکن")

#-------------------------------------
print(20*"-",nam,"omc محاسبه")
# تعريف يک تابع براي محاسبه او ام سي (حدس زدن قيمت بسته شدن)
def bmi(today_Open_price, today_price_min):

     omc = (((today_price_max *2 )+ today_price_min)/3)-(today_price - yesterday_price)
     
    # برگرداندن او ام سي براي خروجي تابع
     return omc
# دريافت قيمت بازشدن با پايين ترين قيمت امروز
today_Open_price = DF['Open'].iloc[-1]
today_price_min = DF['Low'].iloc[-1]
today_price_max = DF['High'].iloc[-1]
yesterday_price = DF['Close'].iloc[-2] # قيمت ديروز
#فراخاني تابع او ام سي باقيمت بازشدن وپايين ترين قيمت روز
omc = bmi(today_Open_price, today_price_min)
# نمايش اوام سي به کاربر
print(f" او ام سي شما {omc:.2f} است ")

# شروع شرط براي ادامه کار
if today_Open_price <= yesterday_price:
     print ('Open_price < yesterday_price ')
if omc == today_price_min:
     print (' صبرکن وآماده خريدباش')
     print ('omc == today_price_min')
elif omc < today_price_min:
     print (' مراقب باش نريزه پايين')
     print ('omc < today_price_min')
elif omc > today_Open_price:
     print ('آماده فروش باش')
     print ('omc > today_Open_price')
     
if today_Final_price == today_price_max:
     print('صف خريدشده')
if today_Final_price == today_price_min:
     print ('صف فروش شده')

#================================================================*****
print(20*"=",nam,"How the share trend and now Stock information")
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

# Calculate the average price محاسبه بالاترين وپايين ترينها تا360 روز
closing_price_b1 = DF['High'].iloc[-7:]  # max_price_day7
closing_price_b2 = DF['Low'].iloc[-7:]  # mix_price_day7
closing_price_b3 = DF['High'].iloc[-14:]  # max_price_day14
closing_price_b4 = DF['Low'].iloc[-14:]  # mix_price_day14

closing_price_b5 = DF['High'].iloc[-30:]  # max_price_day30
closing_price_b6 = DF['Low'].iloc[-30:]  # mix_price_day30
closing_price_b7 = DF['High'].iloc[-60:]  # max_price_day60
closing_price_b8 = DF['Low'].iloc[-60:]  # mix_price_day60

closing_price_b9 = DF['High'].iloc[-103:]  # max_price_day103
closing_price_b10 = DF['Low'].iloc[-103:]  # mix_price_day103

closing_price_b11 = DF['High'].iloc[-360:]  # max_price_day360
closing_price_b12 = DF['Low'].iloc[-360:]  # mix_price_day360

# محاسبه ميانگين بالاترين وپايين ترين هاتا360 روز

average_max1 = closing_price_b1.mean()   # average_max_price_day7                  
average_min1 = closing_price_b2.mean()   # average_mix_price_day7
average_max2 = closing_price_b3.mean()   # average_max_price_day14                  
average_min2 = closing_price_b4.mean()   # average_mix_price_day14

average_max3 = closing_price_b5.mean()   # average_max_price_day30                  
average_min3 = closing_price_b6.mean()   # average_mix_price_day30
average_max4 = closing_price_b7.mean()   # average_max_price_day60                  
average_min4 = closing_price_b8.mean()   # average_mix_price_day60

average_max5 = closing_price_b9.mean()   # average_max_price_day103                  
average_min5 = closing_price_b10.mean()   # average_mix_price_day103

average_max6 = closing_price_b11.mean()   # average_max_price_day360                 
average_min6 = closing_price_b12.mean()   # average_mix_price_day360


#=====================================================
print ()
print (today_price_max,'price_max_day','*****' ,today_price_min,'price_min_day')
print ('-'*20)
print ( max_price_b1,'max7 -',min_price_b2,'min7','*****' ,max_price_b3,'max14 -',min_price_b4,'min14')
print ('-'*20)
print ( max_price_b5,'max30 -',min_price_b6,'min30','*****' ,max_price_b7,'max60 -',min_price_b8,'min60')
print ('-'*20)
print ( max_price_b9,'max103 -',min_price_b10,'min103','*****' ,max_price_b11,'max360 -',min_price_b12,'min360')
print ('-'*20)

print (math.ceil(average_max1),"max7 mean -",math.ceil(average_min1),"min7 mean")
print (math.ceil(average_max2),"max14 mean -",math.ceil(average_min2),"min14 mean")
print ()
print (math.ceil(average_max3),"max30 mean -",math.ceil(average_min3),"min30 mean")
print (math.ceil(average_max4),"max60 mean -",math.ceil(average_min4),"min60 mean")
print ()
print (math.ceil(average_max5),"max103 mean -",math.ceil(average_min5),"min103 mean")
print ()
print (math.ceil(average_max6),"max360 mean -",math.ceil(average_min6),"min360 mean")
print(30*"-")
print ( 'today_price :',today_price)
print(20*"-")

# max year360 + min year360 /2
year = (max_price_b11 + min_price_b12)/2
# max year_mean + min year_mean /2
year_mean = (average_max6 + average_min6)/2

# (max 103 + min 103) /2
Month103 = (max_price_b9 + min_price_b10)/2
# (max 103_mean + min 103_mean) /2
Month103_mean = (average_max5 + average_min5)/2

# max Month60 + min Month60 /2
Month60 = (max_price_b7 + min_price_b8)/2
# max Month60_mean + min Month60_mean /2
Month60_mean = (average_max4 + average_min4)/2

# max Month30 + min Month30 /2
Month30 = (max_price_b5 + min_price_b6)/2
# max Month30_mean + min Month30_mean /2
Month30_mean = (average_max3 + average_min3)/2

# max week14 + min week14 /2
week14 = (max_price_b3 + min_price_b4)/2
# max week14_mean + min week14_mean /2
week14_mean = (average_max2 + average_min2)/2

# max week7 + min week7 /2
week7 = (max_price_b1 + min_price_b2)/2
# max week7_mean + min week7_mean /2
week7_mean = (average_max1 + average_min1)/2

if today_price > year_mean:
    print ('سهم',nam,'رونگهدارهنوزنفروش')
    print ('-'*20)

if today_price < year_mean:
    print ('سهم',nam,'روبفروش نگه ندار')
    print ('-'*20) 

if week7 > Month30 or week7 < Month30 :
    print ('روند حالت رنج داره دقت کنيد')
    print ('سقف وکف روندرنج  :' ,  max_price_b7 ,'<==>', min_price_b8 )
    print ('احتمال برگشت قيمت از  :' ,  max_price_b3 ,'<==>', min_price_b4 )
    print ('-'*20)

if today_price_max > max_price_b1 and yesterday_price <= max_price_b1:
     print (" سقف کانال هفتگي روبه بالازده شد ======>", max_price_b1)
     print ('احتمال صعود تا : ',max_price_b3,)
     print('-'*20)

if today_price_max < max_price_b1 and yesterday_price >= max_price_b1:
     print (" سقف کانال هفتگي روبه پايين زده شد======>", max_price_b1)
     print('-'*20)

if today_price_min > min_price_b2 and yesterday_price <= min_price_b2:
     print ("کف کانال هفتگي روبه بالازده شد =====>", min_price_b2)
     print('-'*20)

if today_price_min < min_price_b2 and yesterday_price >= min_price_b2:
     print ("کف کانال هفتگي روبه پايين زده شد =====>", min_price_b2)
     print ('احتمال ريزش تا : ',min_price_b4,)
     print('-'*20)

if today_price_max > max_price_b3 and yesterday_price <= max_price_b3:
     print ("سقف کانال دوهفتگي روبه بالازده شد =====>", max_price_b3)
     print('-'*20)

if today_price_max < max_price_b3 and yesterday_price >= max_price_b3:
     print ("سقف کانال دوهفتگي روبه پايين زده شد =====>", max_price_b3)
     print('-'*20)

if today_price_min > min_price_b4 and yesterday_price <= min_price_b4:
     print ("کف کانال دوهفتگي روبه بالازده شد =====>", min_price_b4)
     print('-'*20)

if today_price_min < min_price_b4 and yesterday_price >= min_price_b4:
     print ("کف کانال دوهفتگي روبه پايين زده شد =====>", min_price_b4)
     print('-'*20)

if today_price_max > max_price_b5 and yesterday_price <= max_price_b5:
     print ("سقف کانال ماهيان روبه بالازده شد =====>", max_price_b5)
     print('-'*20)

if today_price_max < max_price_b5 and yesterday_price >= max_price_b5:
     print ("سقف کانال ماهيانه روبه پايين زده شد =====>", max_price_b5)
     print('-'*20)

if today_price_min > min_price_b6 and yesterday_price <= min_price_b6:
     print ("کف کانال ماهيانه روبه بالازده شد =====>", min_price_b6)
     print('-'*20)

if today_price_min < min_price_b6 and yesterday_price >= min_price_b6:
     print ("کف کانال ماهيانه روبه پايين زده شد =====>", min_price_b6)
     print('-'*20)

if today_price_max > Month103_mean and yesterday_price > Month103_mean:
    print ('قيمت بالاي ميانگين    103')
    print ('-'*20)

if today_price > Month103_mean and today_price < yesterday_price < today_two_price:
    print ('قيمت روبه پايين وبه سمت ميانگين   103 روزه ميرود')
    print ('-'*20)

if today_price_min < Month103_mean and yesterday_price < Month103_mean:
    print ('قيمت پايين ميانگين   103')
    print ('-'*20)

if today_price < Month103_mean and today_price > yesterday_price > today_two_price:
    print ('قيمت روبه بالا وبه سمت ميانگين   103 روزه ميرود')
    print ('-'*20)

if today_price_max > Month60 and yesterday_price <= Month60:
    print ('Month60 شروع روند افزايشي بااحتياط خريدکن')
    print ('-'*20)

if today_price_min < Month60 and yesterday_price >= Month60:
    print ('Month60 شروع روند کاهشي مراقب باش ')
    print ('-'*20)


if max_price_b1 < max_price_b3 < max_price_b5 < max_price_b7 < max_price_b9 :
    if today_price < yesterday_price:
        print ("کانال وروند سه ماهه نزولي است")
        print ('-'*20)

if min_price_b2 > min_price_b4 > min_price_b6 > min_price_b8 > min_price_b10 :
    if today_price > yesterday_price:
        print ("کانال وروند سه ماهه صعودي است ")
        print ('-'*20)

if max_price_b1 > max_price_b3 > max_price_b5 and today_price_max > yesterday_price:
    print ("کانال وروند يک ماه همچنال افزايشي ميباشد")
    print ('-'*20)

if min_price_b2 < min_price_b4 < min_price_b6 and today_price_max < yesterday_price:
    print ("کانال وروند يک ماه همچنان نزولي ميباشد ")
    print ('-'*20)

if max_price_b1 < max_price_b3 > max_price_b5 and today_price_max < yesterday_price:
    print ("روند صعودي يکماه نزولي شد")
    print ('-'*20)

if min_price_b2 > min_price_b4 < min_price_b6 and today_price_max > yesterday_price:
    print ("روند نزولي يکماه صعودي شد")
    print ('-'*20)

#--------------------------------------------

ma3 = (math.ceil(average_prices7))
ma10 = (math.ceil(average_price))
ma4 = (math.ceil(average_prices9))
ma11 = (math.ceil(average_price10))
ma20 = (math.ceil(average_prices8))

#for signal Buy or Sell (ma10 , ma3):
if ma3 > ma10 and ma4 <= ma10:
    print (" signal Buy")
    print ('ma3 > ma10 & ma4 <= ma10')
    
    
if ma3 > ma10 and ma4 > ma10:
    print (" No signal and ascending Hold نگهدارصعوديه")
    print (' ma3 > ma10 and ma4 > ma10')
    
    
if ma3 < ma10 and ma4 >= ma10:
    print (" signal Sell")
    print ('ma3 < ma10 & ma4 >= ma10')
    
    
if ma3 < ma10 and ma4 < ma10:
    print (" No signal and Descending not Hold نگه ندارنزوليه")
    print (' ma3 < ma10 and ma4 < ma10')
    
    
if ma3 > ma10 and ma10 > ma20 :
    print ('ascending Hold نگهدارصعوديه')
    print ('ma3 > ma10 & ma10 > ma20')
    
    
if ma3 >= ma10 and ma10 >= ma20 or ma10 <= ma20:
    print (" no signal wait رنجه صبرکن")
    print ('ma3 >= ma10 and ma10 >= ma20 or ma10 <= ma20')
    

print ()
print (ma3,'=ma3  ' ,ma10,'=ma10  ' ,ma4 ,'=ma4  ',ma11 ,'=ma11  ',ma20,'=ma20')
if today_price < ma10 :
    print ('قيمت زير ميانگين 10روزميباشد')
else:
    print ('قيمت بالاي ميانگين 10 روزه ميباشد')


if ma3 < today_Final_price:
    print ('ma3<price : قيمت بالاترميره')

if ma3 > today_Final_price:
    print ('ma3>price : قيمت پايين ترميره')

print ()
#------------------------------------------------
print(20*"=",nam,"price_max,min,Close  6yers")
# محاسبه بالاترين وپايين ترين قيمت شش روزمتوالي
today_price_max1 = DF['High'].iloc[-1]
today_price_max2 = DF['High'].iloc[-2]
today_price_max3 = DF['High'].iloc[-3]
today_price_max4 = DF['High'].iloc[-4]
today_price_max5 = DF['High'].iloc[-5]
today_price_max6 = DF['High'].iloc[-6]
today_price_max9 = DF['High'].iloc[-9]

today_price_min1 = DF['Low'].iloc[-1]
today_price_min2 = DF['Low'].iloc[-2]
today_price_min3 = DF['Low'].iloc[-3]
today_price_min4 = DF['Low'].iloc[-4]
today_price_min5 = DF['Low'].iloc[-5]
today_price_min6 = DF['Low'].iloc[-6]
today_price_min9 = DF['Low'].iloc[-9]

today_price1 = DF['Close'].iloc[-1]
today_price2 = DF['Close'].iloc[-2]
today_price3 = DF['Close'].iloc[-3]
today_price4 = DF['Close'].iloc[-4]
today_price5 = DF['Close'].iloc[-5]
today_price6 = DF['Close'].iloc[-6]
today_price9 = DF['Close'].iloc[-9]

print ('max',today_price_max6,today_price_max5,today_price_max4,today_price_max3,today_price_max2,today_price_max1)
print ()
print ('min',today_price_min6,today_price_min5,today_price_min4,today_price_min3,today_price_min2,today_price_min1)
print ()
print ('Close',today_price6,today_price5,today_price4,today_price3,today_price2,today_price1)
print ()
if today_price1 > today_price2 and today_price_min1 > today_price_min2 :
    if today_price2 > today_price3 and today_price_min2 > today_price_min3 :
        if today_price1 < today_price9 :
            print ('قيمت داره ميره بالا خريدکن')

if today_price1 < today_price2 and today_price_min1 < today_price_min2 :
    if today_price2 < today_price3 and today_price_min2 < today_price_min3 :
        if today_price1 > today_price9 :
            print ('قيمت داره ميره پايين بفروش')

if today_price_min1 > today_price_min6 and  today_price_min1 > today_price_min9:
    if today_price1 < today_price2 and today_price_min1 < today_price_min2 :
        if today_price2 < today_price3 and today_price_min2 < today_price_min3 :
            print ('بانواسانات انجام شده احتمالا ريزشيه')
    
if today_price_min1 < today_price_min6 and  today_price_min1 < today_price_min9:
    if today_price1 > today_price2 and today_price_min1 > today_price_min2 :
        if today_price2 > today_price3 and today_price_min2 > today_price_min3 :
            print ('بانوسانات انجام شده احتمالا افزايشيه')

if today_price1 > today_price6 :
    print ('قيمت بسته شدن امروزاز6روزقبل هم بالاتررفت')

if today_price1 > today_price9 :
    print ('قيمت بسته شدن امروزاز9 روزقبل هم بالاتررفت')

if today_price1 < today_price6 :
    print ('قيمت بسته شدن امروز کمترازقيمت 6روزقبل شده')

if today_price1 < today_price9 :
    print ('قيمت بسته شدن امروزکمترازقيمت 9روزقبل شده')
    
print (20*'-')
#--------------------------------------------

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
namad =["چکارن","تلیسه","غمینو","وسپه",
        "غکورش","شپاکسا","پاکشو",
        "تاپیکو","دسبحان","کگل",
        "ومعادن","حتوکا","خگستر",
        "فولاد","شپنا","فملی",
        "حتاید","پی پاد","خودرو",
        "تیپیکو","خساپا","سرچشمه",
        "نیان","ختور","فپنتا",
        "شبندر","فارس","غفارس",
        "وبصادر","کچاد",]

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
index = int(input("Please write down the selected share number : "))
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
print(ticker.title,' : نام شرکت ')
print(ticker.state,ticker.flow,ticker.group_name)     
print(ticker.fiscal_year,' : سال مالی ')  
print(ticker.eps ,'  :  EPS  ')  
print(ticker.p_e_ratio ,' :   P/E')  
print(ticker.group_p_e_ratio, '  :  group P/E ')  
print(ticker.float_shares,' : درصد سهام شناور')   
print(ticker.base_volume,' : حجم مبنا ')
print()  
print(ticker.last_price,' : آخرین معامله') 
print(ticker.adj_close,' : قیمت پایانی ')  
print(ticker.yesterday_price,' : قیمت دیروز')  
print(ticker.open_price,' : قيمت بازشدن')   
print()
print(ticker.high_price,' : حداکثرقيمت امروز')  
print(ticker.low_price,' : حداقل قيمت امروز')
print(ticker.sta_max,' : حداکثر قیمت مجاز')  
print(ticker.sta_min,' : حداقل قیمت مجاز')
print()
print(ticker.min_week,' : حداقل قیمت هفته اخیر')  
print(ticker.max_week,' : حداکثر قیمت هفته اخیر')
print(ticker.min_year,' : حداقل قیمت بازه سال')  
print(ticker.max_year,' : حداکثر قیمت بازه سال')
print()
print(ticker.count,' : تعداد معاملات ')
print(ticker.value,' :  ارزش معاملات ')
print(ticker.volume,' : حجم معاملات امروز ')
print(ticker.month_average_volume,' : میانگین حجم ماه')
print()
print(30*"=",sahame,"RSI value")
DF.rename(columns=RenameDict, inplace=True)
rsi = ta.momentum.rsi(DF['Close'], length=14)
rsi_diff = rsi.diff()
print(rsi.tail(3))

#=====================================================
print('-'*30)
if ticker.adj_close > ticker.max_year :
     print (' مقاومت يک ساله شکسته شد')

if ticker.adj_close < average_price:
     print (' قيمت امروز پايين ترازميانگين 10 روزه است')
else:
    if ticker.adj_close > average_price:
          print (' قيمت امروزبالاترازميانگين 10روزه است') 

if (ticker.min_week)>(ticker.adj_close):
     print(' قيمت امروز پايين ترازحداقل قيمت هفتگي است')
else:
     if (ticker.min_week)<(ticker.adj_close):
          print(' قيمت امروز بالاترازحداقل قيمت هفتگي است')

if (ticker.max_week)<(ticker.adj_close):
     print(' قيمت امروزبالاترازحداکثرقيمت هفتگي است')
     
print('-'*30)   
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
     print ((math.floor(Percent_last )),'% : رنج قيمتي فردامثبت است')
else:
     if (ticker.last_price) < (ticker.adj_close):
          print ((math.floor(Percent_last)),'% : رنج قيمتي فردا منفي است')

print(35*"=",nam,"Process Stock trends")     
if ticker.adj_close > ticker.max_week  :
     print (' قيمت امروزازحداکثرقيمت هفتگي بالاتره')
     print (ticker.max_week," : هفتگي ")
     print (ticker.adj_close," : امروز")
else :
     if ticker.adj_close < ticker.min_week  :
          print (' قيمت امروزازحداقل قيمت هفتگي پايين تره')
          print (ticker.min_week," : هفتگي ")
          print (ticker.adj_close," : امروز")

print(20*"-")
ravand =(ticker.max_year + ticker.min_year)/2 

if ravand < ticker.high_price :
     print ('** توجه داشته باشيد روندقيمتي کلا صعودي **')
     print ()
else :
     if ravand > ticker.low_price :
          print ('** توجه داشته باشيد روندقيمتي کلا نزولي **')
          print ()
     

print(20*"-",nam,"Tik Top or Down")

if ticker.open_price>ticker.low_price < ticker.adj_close:
     if (math.ceil(tik_close_low))>(math.ceil(tik_open_low)):     
          if ticker.adj_close > ticker.open_price :
               print (tik_ascending , ' : تيک صعودي')
          else:
               if ticker.open_price<ticker.high_price > ticker.adj_close:
                    if (math.ceil(tik_close_high))>(math.ceil(tik_open_high)):
                         if ticker.adj_close < ticker.open_price :
                              print (tik_Descending , ' : تيک نزولي')
               

if ticker.open_price > ticker.yesterday_price and ticker.low_price < ticker.yesterday_price:
     if ticker.adj_close > ticker.open_price:
          print (" امروزتيک صعودي داريم")
     else:
          if ticker.open_price < ticker.yesterday_price and ticker.high_price > ticker.yesterday_price:           
               if ticker.adj_close < ticker.open_price:
                     print (" امروزتيک نزولي داريم")

#===============================================
print (40*'=',sahame,'volume')
print (ticker.volume ,'حجم امروز')
print (today_Volume , 'حجم يک روزقبل')
print (today_Volume_yesterday , 'حجم دوروزقبل')
#=================================================
print(40*"=",sahame,"bmi محاسبه")
# تعریف یک تابع برای محاسبه بی ام آی
def bmi(last_price, adj_close):

     bmi = (adj_close + (last_price*2))/3
     
    # برگرداندن بی ام آی به عنوان خروجی تابع
     return bmi

# دريافت قيمت پاياني  وآخرين قيمت
last_price = ticker.last_price
adj_close = ticker.adj_close
# فراخواني تابع بي ام آي با قيمت پاياني وآخرين قيمت
bmi = bmi(last_price, adj_close)
# نمایش بی ام آی کاربر
print(f" بی ام آی شما {bmi:.2f} است ")

# شروع شرط براي محاسبه 
if bmi < adj_close:
    print("قيمت پايين ترمياد")
elif bmi > adj_close:
    print("قيمت بالاتر ميره")
elif bmi == adj_close:
    print("قيمت درجاميزنه گيجه")
elif bmi < ticker.yesterday_price:
    print ("احتمال ريزش شديدخارج شو")
else:
    print("معامله نکن")

#-------------------------------------
print(40*"=",sahame,"omc محاسبه")
# تعريف يک تابع براي محاسبه او ام سي (حدس زدن قيمت بسته شدن)
def bmi(open_price, price_min):

     omc = (((open_price *4 )+ price_min)/5)-(open_price - price_min)
     
    # برگرداندن او ام سي براي خروجي تابع
     return omc

# دريافت قيمت بازشدن با پايين ترين قيمت امروز
open_price = ticker.open_price
price_min = ticker.low_price
yesterday_price = ticker.yesterday_price # قيمت ديروز
#فراخاني تابع او ام سي باقيمت بازشدن وپايين ترين قيمت روز
omc = bmi(open_price, price_min)
# نمايش اوام سي به کاربر
print(f" او ام سي شما {omc:.2f} است ")
print ('-'*15)
# شروع شرط براي ادامه کار
if open_price <= yesterday_price and open_price < price_min:
     print ('خريدممنوع open < yesterday کاهشي ')
if omc <= price_min and open_price >= price_min:
     print (' آماده خريد باش')
elif omc >= open_price and ticker.sta_max >= ticker.high_price:
     print (' آماده فروش باش')

if yesterday_price > open_price:
     print(" قيمت بازشدن امروزکمترازبسته شدن ديروزاست")
else:
     if yesterday_price < open_price:
          print(" قيمت بازشدن امروز بيشترازبسته شدن ديروزشده")

if ticker.sta_max == ticker.high_price:
     print(' صف خريدشده')
else:
     if ticker.sta_min == ticker.low_price:
          print (' صف فروش شده')
print ()
if ma3 < ticker.last_price :
    print ('ma3<price : قيمت بالاترميره')

if ma3 >  ticker.last_price :
    print ('ma3>price : قيمت پايين ترميره')
#======================================================
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
#---------------------------------------------------
print(30*"=",sahame," True and False مقادير sma10-20")          

history = ticker.history


def sma(series, periods: int, ):
    return series.rolling(window=periods, min_periods=periods).mean()


sma_10 = sma(history.close, 10)
sma_20 = sma(history.close, 20)
buy_signals = (
        (sma_10 > sma_20) &
        (sma_20.shift(1) > sma_10.shift(1))
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
hm7= (((((ticker.min_year)*38.20)/100)-(ticker.min_year)),' : hm_Fib_261.80')#: min_Fib_38.20
hm8= (((((ticker.max_year)*78.60)/100)-(ticker.max_year)),' : hm_Fib_361.80')#: max_Fib_78.60
hm9= (((((ticker.min_year)*50)/100)-(ticker.min_year)),' : hm_Fib_423.60')      #: min_Fib_50
#print ('حمايت 1',hm1,'\nحمايت 2', hm2,'\nحمايت 3', hm3,'\nحمايت 4', hm4,'\nحمايت 5',hm5,'\nحمايت 6',hm6,'\nحمايت 7',hm7,'\nحمايت 8',hm8,'\nحمايت 9',hm9)
     
#if (ticker.min_year)<(ticker.adj_close) and (ticker.adj_close)>(ticker.yesterday_price):
mo1= (((((ticker.min_year)*23.60)/100)+(ticker.min_year)),' : mo_Fib_23.60') #: min_Fib_23.60
mo2= (((((ticker.min_year)*38.20)/100)+(ticker.min_year)),' : mo_Fib_38.20') #: min_Fib_38.20
mo3= (((((ticker.min_year)*50)/100)+(ticker.min_year)),' : mo_Fib_50')       #: min_Fib_50
mo4= (((((ticker.min_year)*61.80)/100)+(ticker.min_year)),' : mo_Fib_61.80') #: min_Fib_61.80
mo5= (((((ticker.min_year)*78.60)/100)+(ticker.min_year)),' : mo_Fib_78.60') #: min_Fib_78.60
mo6= (((((ticker.min_year)*100)/100)+(ticker.min_year)),' : mo_Fib_100')     #: min_Fib_100
mo7= (((((ticker.min_year)*161.80)/100)+(ticker.min_year)),' : mo_Fib_161.80')# : min_Fib_161.80
mo8= (((((ticker.min_year)*261.80)/100)+(ticker.min_year)),' : mo_Fib_261.80')#: min_Fib_261.80
mo9= (((((ticker.min_year)*361.80)/100)+(ticker.min_year)),' : mo_Fib_361.80')#: min_Fib_361.80
mo10=(((((ticker.min_year)*423.60)/100)+(ticker.min_year)),' : mo_Fib_423.60')#: min_Fib_423.60
#print (' مقاومت1 ',mo1,'\n مقاومت2 ', mo2,'\n مقاومت3 ', mo3,'\n مقاومت4 ', mo4,'\n مقاومت5 ', mo5,'\n مقاومت6 ', mo6,'\n مقاومت7 ', mo7,'\n مقاومت8 ', mo8,'\n مقاومت9 ', mo9,'\n مقاومت10 ', mo10)
#-----------------------------------
Fib=print(45*"=",sahame,"hm_Fib and mo_Fib")
if (ticker.max_year)>(ticker.adj_close)<(ticker.yesterday_price):
     print (  hm1,'\n', hm2,'\n', hm3,'\n', hm4,'\n',hm5,'\n',hm6,'\n',hm7,'\n',hm8,'\n',hm9)
else:
    if (ticker.min_year)<(ticker.adj_close) >(ticker.yesterday_price):
         print (  mo1,'\n', mo2,'\n', mo3,'\n', mo4,'\n', mo5,'\n', mo6,'\n', mo7,'\n', mo8,'\n', mo9,'\n', mo10)
         
#----------------------------------
print(40*"=","محاسبات قيمت خريد شمااز ",sahame,)
# چکارن
if index == 1:
     p=0
     s=4250
     v=20000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib    
# تليسه
if index == 2:
     p=4357
     s=0
     v=65000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib
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
          Fib == Fib   
# وسپه
if index == 4:
     p=5017
     s=0
     v=6000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib     
# غکورش
if index == 5:
     p=9916
     s=0
     v=20333
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib
# شپاکسا
if index == 6:
     p=3310
     s=0
     v=51000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib
# پاکشو
if index == 7:
     p=0
     s=7100
     v=21000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib
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
          Fib == Fib
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
          Fib == Fib
# کگل
if index == 10:
     p=0
     s=7050
     v=4000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib
# ومعادن
if index == 11:
     p=0
     s=0
     v=0
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib
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
     print(20*"-" )
     
     if today_price > take_profit:
          profit = str ( pf - pk )
          profit_float = float(profit)
          profit_percentage =(profit_float / pk) * 100
          print (" جمع پرداختي شمابااحتساب قيمت خريدتان :" ,pk)
          print (" اگرباقيمت امروزبفروشيد ميشه :" , pf)
          print (" شماسود ميکنيد به مبلغ :" ,pp)
          print("Your profit percentage : درصدسودشماشده : {}% ".format(math.ceil(profit_percentage)))
          print(20*"-" )
 
     elif today_price < stop_loss:
          loss = str ( pk - pf )
          loss_float = float(loss)
          loss_percentage = (loss_float / pk) * 100
          print (" جمع پرداختي شمابااحتساب قيمت خريدتان :" ,pk)
          print (" اگرباقيمت امروزبفروشيد ميشه :" , pf)
          print (" شماضرر ميکنيد به مبلغ :" ,pp)
          print("The percentage of your loss : درصدضررشماشده : {}% ".format(math.ceil(loss_percentage)))
          print(20*"-" )
     else:
          if pk > today_price :
              print("Price to limit")
              print (" قيمت به حد سود20درصد نرسيده!  \n The price has not reached the profit of 20%")                             
              print(20*"-" )
          if pk < today_price :
              print("Price to limit")
              print (" قيمت به حد ضرر3درصد نرسيده !  \n The price has not reached the level of 3% loss") 
              print(20*"-" )

          
     if p == p :
          hs1 = (( p * 0.2 + p )*100)/100 # حدسود20درصد
          hs2 = (( p * 0.1 + p )*100)/100 # حدسود10درصد
          hs3 = (( p * 0.05 + p )*100)/100 # حدسود5درصد
          hs4 = (( p * 0.011 + p )*100)/100 # قيمت سربه سر
          hz = ((p * -0.03 + p)*100)/100# حدضرر3درصد
          print (' : تعيين حدسودوزيان بااحتساب قيمت خريد شمااز ',nam)
          print (hs1,'حدسود20درصد')
          print (hs2,'حدسود10درصد')
          print (hs3,'حدسود5درصد') 
          print (hz,'حدضرر 3درصد')
          print (hs4,'قيمت سربه سربراي فروش')
          print(ticker.last_price,' : آخرين معامله')
          print ('-'*20)
     if pk == pf :
          print (" اگرعلان بفروشيد سربه سرميشيد :" ,today_price )
          print ('-------')
          
#=====================================================
print ()          
print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')
#------------------------------------------------


