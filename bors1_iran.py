

# برسی روند سهام باتایپ نام سهم
# محاسبات max - min - year - month - week and mean price
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


nam = input ("Hello,Please write the name of the stock you want : \n لطفا نام سهام موردنظرتان رابنويسسد :")

DF = tse.Get_Price_History(stock=nam,
                             start_date='1401-05-01',
                             end_date='1402-05-08',
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
print ()
#-------------------------------------------

# Get today's price قيمتهاي امروز
today_price = DF['Close'].iloc[-1] # قيمت بسته شدن امروز
today_Final_price = DF['Final'].iloc[-1] # قيمت آخرين معامله امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
yesterday_price = DF['Close'].iloc[-2]  # قيمت بسته شدن ديروز
yesterday_Final_price = DF['Final'].iloc[-2] # قيمت آخرين معامله ديروز
yesterday_Open_price = DF['Open'].iloc[-2] # قيمت بازشدن ديروز
today_two_price = DF['Close'].iloc[-3]   # قيمت بسته شدن دوروزقبل
today_price_max = DF['High'].iloc[-1] # بالاترين قيمت امروز
today_price_min = DF['Low'].iloc[-1]  # پايين ترين قيمت امروز
# حجم هفتگي وروزانه وماهيانه Volume
Volume_week = DF['Volume'].iloc[-5] # حجم هفتگي
Volume_Month = DF['Volume'].iloc[-26] # حجم ماهيانهBase volume
today_Volume = DF['Volume'].iloc[-1] # حجم امروز
today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز
average_Volume_week = Volume_week.mean() # محاسبه ميانگين حجم هفتگي
average_Volume_Month = Volume_Month.mean() # محاسبه ميانگين حجم ماهيانه

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
print ( today_price_max,'price_max_day','******' ,today_price_min,'price_min_day' , "روزانه")
print ('-'*20)
print ( max_price_b1,'max7 -',min_price_b2,'min7','******' ,max_price_b3,'max14 -',min_price_b4,'min14' , "هفتگي")
print ('-'*20)
print ( max_price_b5,'max30 -',min_price_b6,'min30','******' ,max_price_b7,'max60 -',min_price_b8,'min60' , "ماهيانه")
print ('-'*20)
print ( max_price_b9,'max103 -',min_price_b10,'min103','******' ,max_price_b11,'max360 -',min_price_b12,'min360' , "ساليانه")
print ('-'*20)

print (math.ceil(average_max1),"max7 mean -- ",math.ceil(average_min1),"min7 mean" , "ميانگين هفتگي")
print (math.ceil(average_max2),"max14 mean -- ",math.ceil(average_min2),"min14 mean" , "ميانگين دوهفته")
print ()
print (math.ceil(average_max3),"max30 mean -- ",math.ceil(average_min3),"min30 mean" , "ميانگين ماه")
print (math.ceil(average_max4),"max60 mean -- ",math.ceil(average_min4),"min60 mean" , "ميانگين دوماه")
print ()
print (math.ceil(average_max5),"max103 mean -- ",math.ceil(average_min5),"min103 mean" , "ميانگين شش ماه")
print ()
print (math.ceil(average_max6),"max360 mean -- ",math.ceil(average_min6),"min360 mean" , "ميانگين ساليانه")
print(30*"-")
print ( 'today_price :',today_price)
print(40*"=")
#=======================================================

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
    print ('روند کمي حالت رنج پيداکرده دقت کن')
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
     
#==================================================
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
else :
     if today_price < yesterday_price:
          print (' دقت کنيد قيمت کاهشي است ')

#=======================================================
print(40*"=",nam,"bmi محاسبه")
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
    print("احتمالا پايين تربياد") 
elif bmi > adj_close:
    print("احتمالا بالاتربره")
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
     print ('اگرتوسودي آماده فروش باش')
     print ('omc > today_Open_price')
     
if today_Final_price == today_price_max:
     print('صف خريدشده')
if today_Final_price == today_price_min:
     print ('صف فروش شده')

#------------------------------------------------
print ('-'*20)

ma3 = (math.ceil(average_prices7))
ma10 = (math.ceil(average_price))
ma4 = (math.ceil(average_prices9))
ma11 = (math.ceil(average_price10))
ma20 = (math.ceil(average_prices8))

#for signal Buy or Sell (ma10 , ma3):
if ma3 > ma10 and ma4 <= ma10 or ma4 > ma10:
    print (" signal Buy نگهدارصعودي شده")
    print (" buy  اگه نداري بخر")
    print (' ma3 > ma10 and ma4 <= ma10 or ma4 > ma10 ')
    print ('-'*20)
      
    
if ma3 < ma10 and ma4 >= ma10 or ma4 < ma10:
    print (" signal Sell  نگه ندارنزولي شده")
    print (' ma3 < ma10 and ma4 >= ma10 or ma4 < ma10')
    print ('-'*20)
    
    
if ma3 > ma10 and ma10 > ma20 :
    print (' ascending Hold نگهدارصعوديه')
    print (" buy  اگه نداري بخر")
    print (' ma3 > ma10 & ma10 > ma20')
    print ('-'*20)
    
    
if ma3 >= ma10 and ma10 >= ma20 or ma10 <= ma20:
    print (" no signal wait کمي رنج شده بااحتياط بخريابفروش")
    print (' ma3 >= ma10 and ma10 >= ma20 or ma10 <= ma20')
    print ('-'*20)
    

print (ma3,'=ma3  ' ,ma10,'=ma10  ' ,ma4 ,'=ma4  ',ma11 ,'=ma11  ',ma20,'=ma20')
if today_price < ma10 :
    print ('قيمت زير ميانگين 10روزميباشد')
else:
    print ('قيمت بالاي ميانگين 10 روزه ميباشد')


if ma3 < today_Final_price:
    print ('ma3<price : قيمت بالاترميره')

if ma3 > today_Final_price:
    print ('ma3>price : قيمت پايين ترميره')

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
            
print (20*'-')
if today_price1 > today_price6 :
    print ('قيمت بسته شدن امروزاز6روزقبل هم بالاتررفت')

if today_price1 > today_price9 :
    print ('قيمت بسته شدن امروزاز9 روزقبل هم بالاتررفت')

if today_price1 < today_price6 :
    print ('قيمت بسته شدن امروز کمترازقيمت 6روزقبل شده')

if today_price1 < today_price9 :
    print ('قيمت بسته شدن امروزکمترازقيمت 9روزقبل شده')

            
#محاسبه 5درصد زيرقيمت امروز
zarar = (math.ceil((today_price*-5)/100)+today_price)
sood = (math.ceil((today_price*5)/100)+today_price)

if today_price_max2>today_price_max1 and today_price_min2>today_price_min1 and today_price2>today_price1:
    print (" به احتمال قوي فرداقيمت ميريزه")
    print (  zarar,'تا5درصد ضررميشه')

if today_price_max2<today_price_max1 and today_price_min2<today_price_min1 and today_price2<today_price1:
    print (" به احتمال قوي فردا قيمت ميره بالاتر")
    print (  sood , 'تا5درصدسودميشه')
    
    
print (40*'=')
#--------------------------------------------

