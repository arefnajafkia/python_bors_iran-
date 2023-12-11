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
namad =["چکارن","تلیسه","غمینو","وسپه","غکورش","شپاکسا",
        "پاکشو","تاپیکو","دسبحان","کگل","ومعادن","حتوکا",
        "خگستر","فولاد","شپنا","فملی","حتاید","پی پاد",
        "خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور",
        "فپنتا","شبندر","فارس","غفارس","وبصادر","کچاد",]


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
if ticker.adj_close > ticker.max_week :
     print ('ticker adj close > ticker max week')
     print (ticker.max_week," : max week")
     print (ticker.adj_close," : adj close")
else :
     if ticker.adj_close < ticker.min_week  :
          print ('ticker adj close < ticker max week')
          print (ticker.min_week," : max week")
          print (ticker.adj_close," : adj close")


#==================================================================
print(20*"-",sahame,"Tik Top or Down")

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
print(40*"=",sahame,"bmi Computing")
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
print(40*"=",sahame,"omc Computing")
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
     print(" yesterday_price > open_price")
else:
     if yesterday_price < open_price:
          print(" yesterday_price < open_price")

if ticker.sta_max == ticker.high_price:
     print(' صف خريدشده')
else:
     if ticker.sta_min == ticker.low_price:
          print (' صف فروش شده')
print ()
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
     print ( hm1,'\n', hm2,'\n', hm3,'\n', hm4,'\n',hm5,'\n',hm6,'\n',hm7,'\n',hm8,'\n',hm9)     
  
     print('-'*20)

else:
    if (ticker.min_year)<(ticker.adj_close) >(ticker.yesterday_price):
         print (  mo1,'\n', mo2,'\n', mo3,'\n', mo4,'\n', mo5,'\n', mo6,'\n', mo7,'\n', mo8,'\n', mo9,'\n', mo10) 
  
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
     p=9916
     s=0
     v=20333
     if p > 0 :
          print (p , ': your buy price ',sahame )
          print (v ,': Your number of shares')
     if s > 0 :
          print (s , ': your sell price',sahame )
          print (v ,': Number of shares sold')
          Fib == Fib    
# شپاکسا
if index == 6:
     p=3310
     s=0
     v=51000
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
     
     if today_price > take_profit:
          profit = str ( pf - pk )
          profit_float = float(profit)
          profit_percentage =(profit_float / pk) * 100
          print (" جمع پرداختي شمابااحتساب قيمت خريدتان :" ,pk)
          print (" اگرباقيمت امروزبفروشيد ميشه :" , pf)
          print (" You make a profit in the amount :" ,pp)
          print("Your profit percentage : درصدسودشماشده : {}% ".format(math.ceil(profit_percentage)))
          print(20*"-" )
 
     elif today_price < stop_loss:
          loss = str ( pk - pf )
          loss_float = float(loss)
          loss_percentage = (loss_float / pk) * 100
          print (" جمع پرداختي شمابااحتساب قيمت خريدتان :" ,pk)
          print (" اگرباقيمت امروزبفروشيد ميشه :" , pf)
          print ("   You lose the amount  :" ,pp)
          print("The percentage of your loss : درصدضررشماشده : {}% ".format(math.ceil(loss_percentage)))
          print(20*"-" )
     else:
          print("Price to limit")
          print (" قيمت به حدزيان3وسود20درصدنرسيده است !  \n The price has not reached the limit of 5% loss and 20% profit")                             
          print(20*"-" )
          
          
     if p == p :
          hs1 = (( p * 0.2 + p )*100)/100 # حدسود20درصد
          hs2 = (( p * 0.1 + p )*100)/100 # حدسود10درصد
          hs3 = (( p * 0.05 + p )*100)/100 # حدسود5درصد
          hs4 = (( p * 0.011 + p )*100)/100 # قيمت سربه سر
          hz = ((p * -0.03 + p)*100)/100# حدضرر3درصد
          print (' : تعيين حدسودوزيان بااحتساب قيمت خريد شمااز ',sahame)
          print (hs1,'   20% profit')
          print (hs2,'   10% profit')
          print (hs3,'   5% profit') 
          print (hz,'    3% loss')
          print (hs4,'   Best selling price')
          print(ticker.last_price,' : last price ')
          print ('-'*20)
     if pk == pf :
          print ("  Best selling price :" ,today_price )
          print ('-------')

#=====================================================          
print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')         

