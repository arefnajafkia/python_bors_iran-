
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

# Get today's price قيمتهاي روزانه 
today_price_max = DF['High'].iloc[-1] # بالاترين قيمت امروز
today_price_min = DF['Low'].iloc[-1]  # پايين ترين قيمت امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
today_price = DF['Close'].iloc[-1] # قيمت بسته شدن امروز
today_Final_price = DF['Final'].iloc[-1] # قيمت آخرين معامله امروز

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

# حجم هفتگي وروزانه وماهيانه Volume
Volume_week = DF['Volume'].iloc[-5] # حجم هفتگي
Volume_Month = DF['Volume'].iloc[-26] # حجم ماهيانهBase volume
today_Volume = DF['Volume'].iloc[-1] # حجم امروز
today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز
average_Volume_week = Volume_week.mean() # محاسبه ميانگين حجم هفتگي
average_Volume_Month = Volume_Month.mean() # محاسبه ميانگين حجم ماهيانه

print(25*"=",nam,"How the share trend and now Stock information")
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
print ( 'today_price :',today_price)
print(20*"-")
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


if today_price > week7_mean:
    print ('سهم',nam,' اگه داري فعلا براي ميان مدت نگهدار')
    print (" چون ازميانگين هفتگي بالاتره")
    print ('-'*20)

if today_price < week7_mean:
    print ('سهم',nam,' اگه داري براي ميان مدت هم نگه ندار')
    print (" چون ازميانگين هفتگي پايين تره")
    print ('-'*20) 

if week7 > Month30 or week7 < Month30 :
    print (nam,' بين اين کف وسقف ها نوسان داره ميزنه')
    print ('سقف وکف روندرنج  :' ,  max_price_b7 ,'<==>', min_price_b8 )
    print ('احتمال برگشت قيمت از  :' ,  max_price_b3 ,'<==>', min_price_b4 )
    print ('-'*20)

if today_price_max > max_price_b1 >= yesterday_price:
     print (" سقف کانال هفتگي روبه بالازده شد ======>", max_price_b1)
     print ('احتمال صعود تا : ',max_price_b3,)
     print('-'*20)

if today_price_max < max_price_b1 <= yesterday_price:
     print (" سقف کانال هفتگي روبه پايين زده شد======>", max_price_b1)
     print('-'*20)

if today_price_min > min_price_b2 >= yesterday_price:
     print ("کف کانال هفتگي روبه بالازده شد =====>", min_price_b2)
     print('-'*20)

if today_price_min < min_price_b2 <= yesterday_price:
     print ("کف کانال هفتگي روبه پايين زده شد =====>", min_price_b2)
     print ('احتمال ريزش تا : ',min_price_b4,)
     print('-'*20)

if today_price_max > max_price_b3 >= yesterday_price:
     print ("سقف کانال دوهفتگي روبه بالازده شد =====>", max_price_b3)
     print('-'*20)

if today_price_max < max_price_b3 <= yesterday_price:
     print ("سقف کانال دوهفتگي روبه پايين زده شد =====>", max_price_b3)
     print('-'*20)

if today_price_min > min_price_b4 >= yesterday_price:
     print ("کف کانال دوهفتگي روبه بالازده شد =====>", min_price_b4)
     print('-'*20)

if today_price_min < min_price_b4 <= yesterday_price:
     print ("کف کانال دوهفتگي روبه پايين زده شد =====>", min_price_b4)
     print('-'*20)

if today_price_max > max_price_b5 >= yesterday_price:
     print ("سقف کانال ماهيان روبه بالازده شد =====>", max_price_b5)
     print('-'*20)

if today_price_max < max_price_b5 <= yesterday_price:
     print ("سقف کانال ماهيانه روبه پايين زده شد =====>", max_price_b5)
     print('-'*20)

if today_price_min > min_price_b6 >= yesterday_price:
     print ("کف کانال ماهيانه روبه بالازده شد =====>", min_price_b6)
     print('-'*20)

if today_price_min < min_price_b6 <= yesterday_price:
     print ("کف کانال ماهيانه روبه پايين زده شد =====>", min_price_b6)
     print('-'*20)

if today_price_max > Month103_mean < yesterday_price:
    print ('قيمت بالاي ميانگين    103')
    print ('-'*20)

if Month103_mean < today_price < yesterday_price < today_two_price:
    print ('قيمت روبه پايين وبه سمت ميانگين   103 روزه ميرود')
    print ('-'*20)

if Month103_mean < today_price > yesterday_price > today_two_price:
    print ('قيمت بالاي ميانگين 103 روزه است وداره بالاترميره')
    print ('-'*20)

if today_price_min < Month103_mean > yesterday_price:
    print ('قيمت پايين ميانگين   103')
    print ('-'*20)

if Month103_mean > today_price > yesterday_price > today_two_price:
    print ('قيمت روبه بالا وبه سمت ميانگين   103 روزه ميرود')
    print ('-'*20)

if Month103_mean > today_price < yesterday_price < today_two_price:
    print ('قيمت پايين ميانگين 103روزه است وداره پايين ترميره')
    print ('-'*20)

if today_price_max > Month30 >= yesterday_price:
    print ('Month60 شروع روند افزايشي بااحتياط خريدکن')
    print ('-'*20)

if today_price_min < Month30 <= yesterday_price:
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
     print (' قيمت امروزبالاترازديروزه ')
else :
     if today_price < yesterday_price:
          print (' قيمت امروزپايين ترازديروزه ')

print(25*"-")
if today_price > 4*(average_Volume_week):
    print (" حجم امروز 4برابر حجم هفتگي ميباشد")

#=======================================================

print(40*"=",nam,"omc محاسبه")
# تعريف يک تابع براي محاسبه او ام سي (حدس زدن قيمت بسته شدن)
def cmo(today_Open_price, today_price_min):

     omc = (((today_price_max *2 )+ today_price_min)/3)-(today_price - yesterday_price)
     
    # برگرداندن او ام سي براي خروجي تابع
     return omc
# دريافت قيمت بازشدن با پايين ترين قيمت امروز
today_Open_price = DF['Open'].iloc[-1]
today_price_min = DF['Low'].iloc[-1]
today_price_max = DF['High'].iloc[-1]
yesterday_price = DF['Close'].iloc[-2] # قيمت ديروز
#فراخاني تابع او ام سي باقيمت بازشدن وپايين ترين قيمت روز
omc = cmo(today_Open_price, today_price_min)
# نمايش اوام سي به کاربر
print(f" او ام سي شما {omc:.2f} است ")

# شروع شربراي ادامه کار
if today_Open_price > yesterday_price:
     print ('today_Open_price > yesterday_price ')
if today_Open_price < yesterday_price:
     print ('today_Open_price < yesterday_price ')

if omc > today_price :
    print ('قيمت بسته شدن فردا بيشترازبسته شدن امروزميشه')

if omc < today_price :
    print ('قيمت بسته شدن فرداکمترازبسته شدن امروزميشه')
     
if omc >= today_price_max:
     print (' صبرکن وآماده خريدباش')
     print ('omc >= today_price_max')
elif omc < today_price_min < yesterday_price :
     print (' شروع ريزش هفتگي ميتوني بفروشي')
     print ('omc < today_price_min')
elif omc > today_Open_price > yesterday_price:
     print ('ميتوني نگهداري اگرمنفي زدبفروشي')
     print ('omc > today_Open_price')
     
if today_Final_price == today_price_max:
     print('صف خريدشده')
     
if today_Final_price == today_price_min:
     print ('صف فروش شده')

if omc > today_price > yesterday_price <= min_price_b2:
    print (max_price_b1,": تا قيمت پايين تريامساوي کمترين قيمت هفتگيه وشروع کرده بره بالا")
if omc < today_price < yesterday_price <= max_price_b1:
    print(min_price_b2,": قيمت ازبالاتري قيمت هفتگي پايين ترآمد امکان ريزش تا ")
     

print((math.ceil(omc)),": omc قيمت")
print(today_price,": قيمت امروز")
print(yesterday_price,": قيمت ديروز")
print(max_price_b1,": بالاترين قيمت هفتگي ")
print(min_price_b2,": پايين ترين قيمت هفتگي")
#------------------------------------------------
print(40*"=",nam,"signal buy and sell")

ma3 = (math.ceil(average_prices7))
ma10 = (math.ceil(average_price))
ma4 = (math.ceil(average_prices9))
ma11 = (math.ceil(average_price10))
ma20 = (math.ceil(average_prices8))

#for signal Buy or Sell (ma10 , ma3):
if ma3 > ma10 >= ma4 :
    print (" signal Buy نگهدارصعودي شده")
    print (" buy  اگه نداري بخر")
    print (' ma3 > ma10 >= ma4 or ma4 > ma10 ')
    print ('-'*20)
      
    
if ma3 < ma10 <= ma4 :
    print (" signal Sell  نگه ندارنزولي شده")
    print (' ma3 < ma10 <= ma4 or ma4 < ma10')
    print ('-'*20)
    
    
if ma3 > ma10 > ma20 :
    print (' ascending Hold نگهدارصعوديه')
    print (" buy  اگه نداري بخر")
    print (' ma3 > ma10 > ma20')
    print ('-'*20)
    
    
if ma3 <= ma10 >= ma20 or ma10 <= ma20:
    print (" signal wait قيمت شايد بريزه کمي احتياط کن")
    print (' ma3 <= ma10 >= ma20 or ma10 <= ma20')
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

if today_price1 > today_price2 > today_price3 and today_price_min1 > today_price_min2:
    if today_price1 < today_price6 :
        print ('قيمت داره ميره بالا خريدکن')

if today_price1 < today_price2 < today_price3 and today_price_min1 < today_price_min2:
    if today_price1 > today_price6 :
        print ('قيمت داره ميره پايين بفروش')

if today_price_min9 < today_price_min1 > today_price_min6 :
    if today_price1 < today_price2 and today_price_min1 < today_price_min2 :
        print ('بانواسانات انجام شده احتمالا ريزشيه')
    
if today_price_min9 > today_price_min1 < today_price_min6:
    if today_price1 > today_price2 and today_price_min1 > today_price_min2 :
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

            
#محاسبه درصدسودوزيان امروزبراي فردا
zarar1 = (math.ceil((today_price*-3)/100)+today_price)    
zarar2 = (math.ceil((today_price*-5)/100)+today_price)
sood1 = (math.ceil((today_price*3)/100)+today_price)
sood2 = (math.ceil((today_price*5)/100)+today_price)

if today_price_max2>today_price_max1 and today_price_min2>today_price_min1 and today_price2>today_price1:
    print (" به احتمال قوي فرداقيمت ميريزه")
    print (  zarar1,'تا3درصد ضررميشه')
    print (  zarar2,'تا5درصد ضررميشه')

if today_price_max2<today_price_max1 and today_price_min2<today_price_min1 and today_price2<today_price1:
    print (" به احتمال قوي فردا قيمت ميره بالاتر")
    print (  sood1 , 'تا3درصدسودميشه')
    print (  sood2 , 'تا5درصدسودميشه')
    

#==================================================
print(40*"=",nam,"One year support and resistance")
# Engulfing Calculations  محاسبات اينگل فينگ
today_price = DF['Close'].iloc[-1]   # آخرین قیمت امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
yesterday_price = DF['Close'].iloc[-2] # آخرین قیمت دیروز
yesterday_Open_price = DF['Open'].iloc[-2] # قيمت بازشدن ديروز
# محاسبات مقاومت هفتگي تاساليانه 
highest_price_7 = max(DF['Close'][-7:])    #محاسبه مقاومت هفتگي
highest_price_8 = max(DF['Close'][-8:])
highest_price_30 = max(DF['Close'][-30:])
highest_price_31 = max(DF['Close'][-31:])
highest_price_90 = max(DF['Close'][-90:])
highest_price_180 = max(DF['Close'][-180:])
highest_price_280 = max(DF['Close'][-280:])
highest_price_360 = max(DF['Close'][-360:])    #محاسبه مقاومت ساليانه
#------------------------
# محاسبات حمايت هفتگي تاساليانه
lowest_price_7 = min(DF['Close'][-7:])         #محاسبه حمايت هفتگي
lowest_price_8 = min(DF['Close'][-8:])
lowest_price_30 = min(DF['Close'][-30:])
lowest_price_31 = min(DF['Close'][-31:])
lowest_price_90 = min(DF['Close'][-90:])
lowest_price_180 = min(DF['Close'][-180:])
lowest_price_280 = min(DF['Close'][-280:])                              
lowest_price_360 = min(DF['Close'][-360:])       #محاسبه حمايت ساليانه

if highest_price_280 < highest_price_90 and lowest_price_280 > lowest_price_90:
    print (" مقاومت روبه پايين وبه سمت حمايت يکساله ميرود")

if highest_price_7 > highest_price_30 > highest_price_90:
    print ("ومقاومت درسه ماه کلا افزايشي  است  7>30>90")

if highest_price_7 < highest_price_30 < highest_price_90:
    print ("ومقاومت درسه ماه کلاکاهشي شده 7<30<90")    


# فاصله مقاومت هفتگي باساليانه
resistance= highest_price_7 - highest_price_360
resistance_1= highest_price_8 - highest_price_360

if resistance < resistance_1 :
    print (resistance_1 ,": فاصله مقاومت هفتگي باساليانه داره کم ميشه")


if resistance > resistance_1 :
    print (resistance_1 ,": فاصله مقاومت هفتگي باساليانه داره زيادميشه")
 


if highest_price_30 < highest_price_31 :
    print ("مقاومت يکماه شروع کرده روبه بالابره")

if highest_price_30 > highest_price_31 :
    print ("مقاومت يکماهه شروع کرده روبه پايين بره")


if highest_price_7 < highest_price_8:
    print ("مقاومت هفتگي شروع کرده روبه بالابره")

if highest_price_7 > highest_price_8:
    print ("مقاومت هفتگي شروع کرده روبه پايين بره")   

    
if highest_price_30 == highest_price_7 :
    print (highest_price_7 , ": مقاومت هفتگي باماهيانه برابرشده")


if lowest_price_30 < lowest_price_31 :
    print ("حمايت يکماه شروع کرده روبه بالابره")

if lowest_price_30 > lowest_price_31 :
    print ("حمايت يکماه شروع کرده روبه  پايين بره")


if lowest_price_7 < lowest_price_8 :
    print ("حمايت هفتگي شروع کرده روبه بالابره")

if lowest_price_7 > lowest_price_8 :
    print ("حمايت هفتگي شروع کرده روبه پايين بره")


if lowest_price_30 == lowest_price_7:
    print (lowest_price_7,": حمايت هفتگي باماهيانه برابرشده")
   
# فاصله حمايت هفتگي باساليانه
support= lowest_price_7 -lowest_price_360
support_1= lowest_price_8 -lowest_price_360

if support < support_1:
    print (support_1 ,": فاصله حمايت هفتگي باساليانه داره زيادميشه")


if support > support_1:
    print (support_1 ,": فاصله حمايت هفتگي باساليانه داره کم ميشه")    



if highest_price_280 > highest_price_90 and lowest_price_280 < lowest_price_90:
    print ("حمايت روبه بالا وبه سمت مقاومت يکساله ميرود")

if lowest_price_7 > lowest_price_30 > lowest_price_90:
    print (" ودرکل حمايت سه ماه افزايشي است 7>30>90 ")

if lowest_price_7 < lowest_price_30 < lowest_price_90:
    print ("ودرکل حمايت سه ماه کاهشي است  7<30<90 ")      

    
if highest_price_90 <=  lowest_price_90 :
    print ("حمايت تبديل به مقاومت شد")
    
#==================================================
print(40*"=",nam,"Engulfing Calculations")
# Engulfing  ascending صعودي
# Bullish Engulfing Support level
h1 = today_price > today_Open_price
h2 = yesterday_Open_price > yesterday_price
h3 = yesterday_price > today_Open_price
h4 = today_price > yesterday_Open_price

h_ascending = h1 and h2 and h3 and h4
h5 =  (today_price - today_Open_price) > 5*(yesterday_Open_price - yesterday_price) 

# Engulfing  Descending نزولي
# Bullish Engulfing Resistance level 
h6 = today_price < today_Open_price
h7 = yesterday_Open_price < yesterday_price
h8 = yesterday_price < today_Open_price
h9 = today_price < yesterday_Open_price

h_Descending = h6 and h7 and h8 and h9
h10 = (today_price - today_Open_price) < 5*(yesterday_Open_price - yesterday_price)


if today_price > highest_price_90 :
     print (' مقاومت سه ماه شکسته شد')

if today_price < lowest_price_90 :
     print (' حمايت سه ماه ازدست رفت')
     

if h_ascending and h5:
    c = "Engulfing :"
    print (c , "hemer ascending !  صعودي مناسب خريد" )
    
if h_Descending and h10:
    c = "Engulfing :"
    print (c , "hemer Descending !  نزولي وقت فروش" )
    
print ('~'*10)
print ('روند False يا True دقت کنيدبه')
print (h5,'ascending   روند صعودي ')
print (h10 ,'Descending   روند نزولي')
#===================================================
print ('='*10)
# کدهای برنامه نویسی پایتون برای بررسی اول بودن اعداد
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num = today_price
#num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#=====================================================
print ('='*30,nam,'fibonacci')
#کد برنامه نویسی در پایتون برای سری فیبوناچی

def fibonacci(n):
    fib_series = [today_price, yesterday_price]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
num_terms = 7
#num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
print(fibonacci(num_terms))
print ('-'*10)
#=====================================================
print()
#===================================================
#هرموقع باريش هارامي صعودي يانزولي صورت بگيرد پرينت ميکند درغيراين
#صورت چيزي نشان نميدهد 
# Bullish Harami EngulFing support or Resistance level

if (today_two_price_max)>(yesterday_price_max) and (today_two_price_min)<(yesterday_price_min):
   if (today_two_price)<(yesterday_price)<(today_price):
       if lowest_price_7 or lowest_price_30 or lowest_price_90 <=(today_two_price_min):
           print ("Bullish Harami EngulFing support")
           print ("-----اینگل فینگ صعودی شده خریدکن -----")
           print ("-"*10)


if (today_two_price_max)>(yesterday_price_max) and (today_two_price_min)<(yesterday_price_min):
   if (today_two_price)>(yesterday_price)>(today_price):
      if highest_price_7 or highest_price_30 or highest_price_90 >=(today_two_price_max):
          print ("Bullish Harami EnngulFung Resistance level")
          print ("----- اینگل فینگ نزولی شده بفروش -----")
          print ("-"*10)
#=====================================================
# اين کد براي اينگل فينگ نوشته شده است ودرصورت اجراشدن پرينت انجام ميشود
# درغيراين صورت هيچ چيزي پرينت نميکند
# Bullish Harami EngulFing support or Resistance level

if today_two_price_max < yesterday_price_max < today_price_max:
    if today_two_price_min > yesterday_price_min < today_price_min:
        if today_two_price < yesterday_price < today_price:
            if lowest_price_7 or lowest_price_30 or lowest_price_90 <= yesterday_price_min:
                print ("EngulFing support level")
                print ("----- اینگل فینگ صعودی رخ داده خریدکن-----")
                print ("-"*10)


if today_two_price_max < yesterday_price_max > today_price_max:
    if today_two_price_min > yesterday_price_min > today_price_min:
        if today_two_price > yesterday_price > today_price:
            if highest_price_7 or highest_price_30 or highest_price_90 >= yesterday_price_min:
                print ("EngulFing Resistance level")
                print ("----- اینگل فینگ نزولی زخ داده بفروش -----")
                print ("-"*10)        
#=======================================================
# سرانه خريد
import pandas as pd

def per_capita_purchase_filter(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Filters the given DataFrame based on the per capita purchase amount.

    Args:
        df (pd.DataFrame): The DataFrame to filter.
        threshold (float): The minimum per capita purchase amount.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    # Calculate the per capita purchase amount
    df['per_capita_purchase'] = df['purchase_amount'] / df['population']

    # Filter the DataFrame based on the threshold
    filtered_df = df[df['per_capita_purchase'] >= threshold]

    # Drop the per capita purchase column
    filtered_df.drop(columns=['per_capita_purchase'], inplace=True)

    return filtered_df
# سرانه فروش
import pandas as pd

def per_capita_sales_filter(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Filters the given DataFrame based on the per capita sales amount.

    Args:
        df (pd.DataFrame): The DataFrame to filter.
        threshold (float): The minimum per capita sales amount.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    # Calculate the per capita sales amount
    df['per_capita_sales'] = df['sales_amount'] / df['population']

    # Filter the DataFrame based on the threshold
    filtered_df = df[df['per_capita_sales'] >= threshold]

    # Drop the per capita sales column
    filtered_df.drop(columns=['per_capita_sales'], inplace=True)

    return filtered_df
