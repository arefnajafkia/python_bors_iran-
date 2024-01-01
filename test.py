

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

#===================================================
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
#-------------------------------------------
# برسي سهام فقط بازدن شماره کنارسهم قابل برسي است
namad =["چکارن","تلیسه","غمینو","وسپه", "غکورش","شپاکسا",
        "پاکشو","تاپیکو","دسبحان","کگل","فصبا","حتوکا",
        "خگستر","فولاد","شپنا","فملی","حتاید","پی پاد",
        "خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور",
        "فپنتا","شبندر","فارس","غفارس","وبصادر","کچاد"]

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
print(ticker.last_price,' : آخرین معامله ')  
print(ticker.adj_close,' : قیمت پایانی ')  
print(ticker.yesterday_price,' : قیمت دیروز ')
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
#=====================================================
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
     print ((math.floor(Percent_last )),'% : رنج قيمتي فردامثبت است')
else:
     if (ticker.last_price) < (ticker.adj_close):
          print ((math.floor(Percent_last)),'% : رنج قيمتي فردا منفي است')

print(40*"=",sahame,"Process")     
if ticker.yesterday_price > ticker.adj_close < ticker.max_week  :
     print (' روند قيمتي هفتگي نزولي شد')
     print (ticker.max_week," : هفتگي ")
     print (ticker.yesterday_price," : قيمت ديروز")
     print (ticker.adj_close, ": قيمت امروز")


if ticker.yesterday_price < ticker.adj_close > ticker.max_week  :
     print (' روند قيمتي هفتگي صعودي شد')
     print (ticker.max_week," : هفتگي ")
     print (ticker.yesterday_price," : قيمت ديروز")
     print (ticker.adj_close, ": قيمت امروز")
     
#====================================================
price = ticker.adj_close
darsad_up4 = (math.ceil((price * 0.04 + price)*100)/100)      #قميت بسته شدن 4درصدبالاتر
darsad_down4 = (math.ceil((price * 0.04 - price)*100)/100)    #قيمت بسته شدن 4درصدپايين تر

darsad_up6 = (math.ceil((price * 0.06 + price)*100)/100)      #قيمت بسته شدن6درصدبالاتر
darsad_down6 = (math.ceil((price * 0.06 - price)*100)/100)    #قيمت بسته شدن 6درصدپايين تر

print ()
if ticker.adj_close > ticker.yesterday_price :
    print (darsad_up4 , ": قيمت فرداتا4درصدمثبت")
    print (darsad_up6 , ": قيمت فردا تا6درصدمثبت")

if ticker.adj_close < ticker.yesterday_price :
    print (darsad_down4 , ": قيمت فرداتا4درصدمنفي")
    print (darsad_down6 , ": قيمت فرداتا6درصدمنفي")
    
#=====================================================
print(20*"-")
ravand =(ticker.max_year + ticker.min_year)/2
ravand_2 =(ticker.max_week + ticker.min_week)/2


if ticker.adj_close > ravand and ticker.yesterday_price > ticker.adj_close :
    print (" قيمت بالاي نيمه ساليانه است وبه سمت پايين ميره")


if ticker.adj_close > ravand and ticker.yesterday_price < ticker.adj_close :
    print (" قيمت بالاي نيمه ساليانه است وبه سمت بالاميره")
    

if ticker.adj_close < ravand and ticker.yesterday_price < ticker.adj_close :
    print (" قيمت پايين نيمه ساليانه است وبه سمت بالاميره")


if ticker.adj_close < ravand and ticker.yesterday_price > ticker.adj_close :
    print (" قيمت پايين نيمه ساليانه است وبه سمت پايين ميره")
    

if ravand < ticker.adj_close :
     print ('** توجه داشته باشيد روند قيمتي ساليانه صعوديه **')
     print ()
else :
     if ravand > ticker.adj_close :
          print ('** توجه داشته باشيد روند قيمتي ساليانه نزوليه **')
          print ()


if ticker.adj_close > ravand_2 and ticker.yesterday_price > ticker.adj_close :
    print (" قيمت بالاي نيمه هفتگي است ولي به سمت پايين ميره")
    

if ticker.adj_close > ravand_2 and ticker.yesterday_price < ticker.adj_close :
    print (" قيمت بالاي نيمه هفتگي است وبه سمت بالاميره")


if ticker.adj_close < ravand_2 and ticker.yesterday_price < ticker.adj_close :
    print (" قيمت پايين نيمه هفتگي است ولي به سمت بالاميره")

    
if ticker.adj_close < ravand_2 and ticker.yesterday_price > ticker.adj_close :
    print (" قيمت پايين نيمه هفتگي است وبه سمت پايين ميره")
          

if ticker.max_year > ticker.adj_close > ticker.min_year :
    print (" قيمت درمحدوده رنج ساليانه حرکت ميکنه  بالا  و پايين  ميره")


if ticker.yesterday_price < ticker.max_year < ticker.adj_close > ticker.min_year :
    print ('بالاترين قيمت ساليانه راروبه بالا شکستيم ')

if ticker.max_year == ticker.adj_close :
    print (" خيلي مهم به سقف قيمت ساليانه رسيديم")

if ticker.max_year > ticker.adj_close < ticker.min_year < ticker.yesterday_price :
    print (" پايين ترين قيمت ساليانه را روبه پايين شکستيم")


if ticker.adj_close == ticker.min_year :
    print (" خيلي مهم به کف قيمت ساليانه رسيديم")

#=========================================================     
print(20*"-",sahame,"Tik Top or Down")

print(ticker.max_year,' : حداکثر قیمت بازه سال')
print(ticker.min_year,' : حداقل قیمت بازه سال')


if ticker.adj_close > ticker.open_price > ticker.yesterday_price > ticker.low_price:
    print (tik_ascending , ' : تيک صعودي')

    
if ticker.adj_close < ticker.open_price < ticker.yesterday_price < ticker.high_price:
    print (tik_Descending , ' : تيک نزولي')

               

if ticker.adj_close > ticker.open_price > ticker.yesterday_price > ticker.low_price:
    print (" امروزتيک صعودي داريم")

     
if ticker.adj_close < ticker.open_price < ticker.yesterday_price < ticker.high_price:           
    print (" امروزتيک نزولي داريم")


#===============================================
print (40*'=',sahame,'volume')
print (ticker.volume ,'حجم امروز')
#print (today_Volume_yesterday , 'حجم ديروز')
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
if ticker.open_price < bmi > ticker.adj_close:
    print("قيمت پايين ترمياد")
elif ticker.open_price > bmi < ticker.last_price:
    print("قيمت بالاتر ميره")
elif bmi == adj_close:
    print("قيمت درجاميزنه گيجه")
elif ticker.adj_close <= bmi < ticker.yesterday_price:
    print ("احتمال ريزش شديدخارج شو")
else:
    print("معامله نکن")

#-------------------------------------
print(40*"=",sahame,"omc محاسبه")
# تعريف يک تابع براي محاسبه او ام سي (حدس زدن قيمت بسته شدن)
def bmi(open_price, price_min):

     omc = (((ticker.high_price *2 )+ price_min)/3)-(ticker.adj_close - yesterday_price)
     
    # برگرداندن او ام سي براي خروجي تابع
     return omc

# دريافت قيمت بازشدن با پايين ترين قيمت امروز
open_price = ticker.open_price
price_min = ticker.low_price
price_max = ticker.high_price
yesterday_price = ticker.yesterday_price # قيمت ديروز
#فراخاني تابع او ام سي باقيمت بازشدن وپايين ترين قيمت روز
omc = bmi(open_price, price_min)
# نمايش اوام سي به کاربر
print(f" او ام سي شما {omc:.2f} است ")
print ('-'*15)
# شروع شرط براي ادامه کار
if open_price > yesterday_price:
    print ('open_price > yesterday_price')
if open_price < yesterday_price:
    print ('open_price < yesterday_price')

if omc > ticker.adj_close :
    print ('قيمت بسته شدن فردابيشتراز بسته شدن امروزميشه')

if omc < ticker.adj_close :
    print ('قيمت بسنه شدن فردا کمترازبسته شدن امروزميشه')

if omc >= price_max :
    print ('صبرکن وآماده خريد باش')
    print ('omc >= price_max')
elif omc < price_min < yesterday_price :
     print (' شروع ريزش هفتگي ميتوني بفروشي')
     print ('omc < price_min')
elif omc > open_price > yesterday_price :     
     print ('ميتوني نگهداري اگرمنفي زدبفروشي')
     print ('omc > Open_price')

if ticker.last_price == price_max:
     print('صف خريدشده')
     
if ticker.last_price == price_min:
     print ('صف فروش شده')     

if omc > ticker.adj_close > yesterday_price <= ticker.min_week:
    print (ticker.max_week,": تا قيمت پايين تريامساوي کمترين قيمت هفتگيه وشروع کرده بره بالا")
if omc < ticker.adj_close < yesterday_price <= ticker.max_week:
    print(ticker.min_week,": قيمت ازبالاتري قيمت هفتگي پايين ترآمد امکان ريزش تا ")    


print ((math.ceil(omc)),": omc قيمت")
print (ticker.adj_close,": قيمت امروز")
print (yesterday_price,": قيمت ديروز")
print ((math.ceil(ticker.max_week),": بالاترين قيمت هفتگي "))
print ((math.ceil(ticker.min_week),": پايين ترين قيمت هفتگي"))
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

#------------------------------------------------
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

          
#----------------------------------
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
     p=4283
     s=0
     v=77000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')

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
     p=4398
     s=0
     v=1000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
    
# غکورش
if index == 5:
     p=9126
     s=0
     v=29000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')

# شپاکسا
if index == 6:
     p=3029
     s=0
     v=83000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')

# پاکشو
if index == 7:
     p=0
     s=6750
     v=1000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')

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

# فصبا
if index == 11:
     p=6640
     s=0
     v=15000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')

# حتوکا
if index == 12:
     p=0
     s=3705
     v=5000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
       


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
              print (sz ,": اگرامروزبفروشيد مقدارزيان شماميشود")
          if pk < today_price :
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
          print (' : تعيين حدسودوزيان بااحتساب قيمت خريد شمااز ',sahame)
          print (hs1,'حدسود20درصد')
          print (hs2,'حدسود10درصد')
          print (hs3,'حدسود5درصد') 
          print (hz,'حدضرر 3درصد')
          print (hs4,'قيمت سربه سربراي فروش')
          print(ticker.adj_close,' : قيمت بسته شدن امروز')
          print ('-'*20)

          
     if pk == pf :
          print (" اگرعلان بفروشيد سربه سرميشيد :" ,today_price )
          print ('-------')


#=====================================================
print ('='*30,sahame,'fibonacci')
#کد برنامه نویسی در پایتون برای سری فیبوناچی

def fibonacci(n):
    fib_series = [ticker.adj_close, ticker.yesterday_price]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
num_terms = 7
#num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
print(fibonacci(num_terms))

print ('-'*20)          
#====================================================
      
print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')         



