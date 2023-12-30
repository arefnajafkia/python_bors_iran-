
# ichikumo و RSI  محاسبات وسيگنالهاي 
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


nam = input("Please write the name of the stock you want : \n write in nam :")

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

rsi = ta.momentum.rsi(DF['Close'], length=14)
#rsi_diff = rsi.diff()
rsi_diff = rsi
print(rsi.tail(3))
    
today_price = DF['Close'].iloc[-1] # قيمت بسته شدن امروز
today_Final_price = DF['Final'].iloc[-1] # قيمت آخرين معامله امروز
today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
yesterday_price = DF['Close'].iloc[-2]  # قيمت بسته شدن ديروز
today_price_max = DF['High'].iloc[-1] # بالاترين قيمت امروز
today_price_min = DF['Low'].iloc[-1]  # پايين ترين قيمت امروز

Volume_week = DF['Volume'].iloc[-5] # حجم هفتگي
Volume_Month = DF['Volume'].iloc[-26] # حجم ماهيانهBase volume
today_Volume = DF['Volume'].iloc[-1] # حجم امروز
today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز

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

print (20*"-",nam,": نمايش قيمت")
print (today_Open_price," : قيمت بازشدن امروز")
print (today_price," : قيمت بسته شدن امروز")
print (today_Final_price," : قيمت آخرين معامله امروز")
print (yesterday_price," : قيمت بسته شدن ديروز")
print (today_price_max," : بالاترين قيمت امروز")
print (today_price_min," : پايين ترين قيمت امروز")
print()
#=============================================
print (30*"=",nam,": نمايش ميانگين")
print(closing_prices7.mean()," : ميانگين3روزه")
print(closing_prices.mean()," : ميانگين 10روزه")
print(closing_prices8.mean()," : ميانگين 20روزه")
if closing_prices7.mean() < closing_prices.mean():
     print (" EM_3 < EM_10")
else:
     if closing_prices7.mean() > closing_prices.mean():
          print (" EM_3 > EM_10")

if closing_prices7.mean() < closing_prices8.mean():
     print (" EM_3 < EM_20")
else:
     if closing_prices7.mean() > closing_prices8.mean():
          print (" EM_3 > EM_20")
print()
#------------------------------------------------
print ('-'*20)

ma3 = (math.ceil(average_prices7))
ma10 = (math.ceil(average_price))
ma4 = (math.ceil(average_prices7))
ma11 = (math.ceil(average_price))

#for signal Buy or Sell (ma10 , ma3):
if ma3 > ma10 and ma4 <= ma11:
    print (" signal Buy")
if ma3 > ma10 and ma4 > ma11:
    print (" No signal and ascending Hold")
if ma3 < ma10 and ma4 >= ma11:
    print (" signal Sell")
if ma3 < ma10 and ma4 < ma11:
    print (" No signal and Descending not Hold")
else:
    print (" no signal wait")
    
    
print ('-'*20)
#==================================================
print(30*"=",nam,"Volume")
print(today_Volume," : حجم امروز")
print(today_Volume_yesterday," : حجم ديروز")
print(Volume_week," : حجم هفتگي")
print(Volume_Month," : حجم ماهيانه")
if today_Volume > today_Volume_yesterday:
     print (" حجم امروز بيشترازحجم ديروزشده")
else:
    if today_Volume < today_Volume_yesterday:
         print (" حجم امروزکمترازحجم ديروزشده")


if Volume_Month > today_Volume :
     print (" حجم امروزکمترازحجم ماهيانه ميباشد")
else:
     if Volume_Month < today_Volume :
          print (" حجم امروزبيشترازحجم ماهيانه ميباشد")
print()     
#====================================================
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
print()
#-------------------------------------
print(20*"-",nam,"omc محاسبه")
# تعريف يک تابع براي محاسبه او ام سي (حدس زدن قيمت بسته شدن)
def bmi(today_Open_price, today_price_min):

     omc = (((today_Open_price *4 )+ today_price_min)/5)-(today_Open_price - today_price_min)
     
    # برگرداندن او ام سي براي خروجي تابع
     return omc

# دريافت قيمت بازشدن با پايين ترين قيمت امروز
today_Open_price = DF['Open'].iloc[-1]
today_price_min = DF['Low'].iloc[-1]
yesterday_price = DF['Close'].iloc[-2] # قيمت ديروز
#فراخاني تابع او ام سي باقيمت بازشدن وپايين ترين قيمت روز
omc = bmi(today_Open_price, today_price_min)
# نمايش اوام سي به کاربر
print(f" او ام سي شما {omc:.2f} است ")
# شروع شرط براي ادامه کار
if today_Open_price <= yesterday_price:
     print ('خريدممنوع open < yesterday کاهشي ')
if omc == today_price_min:
     print ('صبرکن')
elif omc < today_price_min:
     print ('خريدنکن')
elif omc > today_Open_price:
     print ('آماده فروش باش')
     

if yesterday_price > today_Open_price:
     print(" قيمت بازشدن امروزکمترازبسته شدن ديروزاست")
else:
     if yesterday_price < today_Open_price:
          print(" قيمت بازشدن امروز بيشترازبسته شدن ديروزشده")

if today_Final_price == today_price_max:
     print('صف خريدشده')
else:
     if today_Final_price == today_price_min:
          print ('صف فروش شده')

#=====================================================
# EMA_3,10,20 نمايش نمودارقيمت و
DF.index = DF['Date']
mplf.plot(DF[-100:], type='candle', mav=(3, 10, 20))
plt.show()

# Calculate the average price for ten days
ten_day_average = DF['Close'].rolling(10).mean()
today_price_scalar = today_price.item()
#================================================ 
          
print(20*"-")
#--------------------------------------
txt = int(input(" آياميخواهيد سودوزيان شماراحساب کنم بله 1ونه 2 :"))

if txt == 1 :
     p = int(input(" قیمت خرید را وارد نمایید :"))
     v = int(input(" حجم خرید را وارد نمایید :"))
     c = today_price
     d = 1
     if p < c :
          s = ((c*-0.35% + c)*v) - ((p*-0.39% + p)*v)
          d = 'sell'
          print(d,'')
          print ((s*100)/100,'مقدارسودشما')
          
     if p > c :
          z = ((p*-0.39% + p)*v) - ((c*-0.35% + c)*v)
          d = 'buy'
          print(d,'')
          print (z,'مقدارضررشما')
           
     if p == p :
          hs1 = (( p * 0.2 + p )*100)/100 # حدسود20درصد
          hs2 = (( p * 0.1 + p )*100)/100 # حدسود10درصد
          hs3 = (( p * 0.05 + p )*100)/100 # حدسود5درصد
          hz = ((p * -0.03 + p)*100)/100# حدضرر3درصد
          d = ': تعيين حدسودوزيان بااحتساب قيمت خريد شمااز '
          print (d,'')
          print ()
          print (hs1,'حدسود20درصد')
          print ()
          print (hs2,'حدسود10درصد')
          print ()
          print (hs3,'حدسود5درصد')
          print () 
          print (hz,'حدضرر 3درصد')
          print ("="*15,"Next, choose your contribution","="*15)
          
else :
     if txt ==2 :
          print ("="*15,"Thank you for your time","="*15)
          print ()
          print ('-'*10,"If you want to continue, please select your share",'-'*10)
#==============================================================
import math
import yfinance as yf
#from operator import pos
from pandas.compat import numpy
import matplotlib.pyplot as plt
import pytse_client as tse

# برسي سهام فقط بازدن شماره کنارسهم قابل برسي است
namad =["چکارن","تلیسه","غمینو","وسپه",
        "غکورش","شپاکسا","پاکشو",
        "تاپیکو","دسبحان","کگل",
        "فصبا","حتوکا","خگستر",
        "فولاد","شپنا","فملی",
        "حتاید","پی پاد","خودرو",
        "تیپیکو","خساپا","سرچشمه",
        "نیان","ختور","فپنتا",
        "شبندر","شستان","غفارس",
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
print(30*"=",sahame," RSI value")
DF.rename(columns=RenameDict, inplace=True)
rsi = ta.momentum.rsi(DF['Close'], length=14)
rsi_diff = rsi.diff()
print(rsi.tail(3))

#===================================================
print(40*"=",sahame,"ichimoku")

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
     print (" ابرکومو آينده سبزه")

if senk_sa1 <  senk_ab1 < today_price :
     print (" قيمت داره ميره زيرابرقرمز ")
else:
     print (" قيمت داره ميره بالاي ابرقرمز ")
print('-'*20)
#==============================================  
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
          
#====================================================
print(35*"=",nam,"Process Stock trends")     
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
print(20*"-",nam,"Tik Top or Down")

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

#=========================================================     
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
    if ticker.adj_close > ticker.open_price :
        print (tik_ascending , ' : تيک صعودي')
    else:
        if ticker.open_price < ticker.yesterday_price and ticker.high_price > ticker.yesterday_price:
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
print (today_Volume_yesterday , 'حجم ديروز')
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
    
print()
#-------------------------------------
print(30*"=",sahame,"omc محاسبه")
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
# شروع شرط براي ادامه کار
if open_price <= yesterday_price:
     print ('خريدممنوع open < yesterday کاهشي ')
if omc == price_min:
     print (' آماده خريد باش')
elif omc < price_min:
     print (' مراقب باش نريزه پايين')
elif omc > open_price:
     print (' آماده فروش باش')

if yesterday_price > open_price:
     print(" قيمت بازشدن امروزکمترازبسته شدن ديروزاست")
else:
     if yesterday_price < open_price:
          print(" قيمت بازشدن امروز بيشترازبسته شدن ديروزشده")

if ticker.sta_max == ticker.high_price:
     print('صف خريدشده')
else:
     if ticker.sta_min == ticker.low_price:
          print ('صف فروش شده')

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

history1 = ticker.history


def sma(series, periods: int, ):
    return series.rolling(window=periods, min_periods=periods).mean()


sma_3 = sma(history.close, 3)
sma_20 = sma(history.close, 20)
buy_signals1 = (
        (sma_3 > sma_20) &
        (sma_20.shift(1) > sma_3.shift(1))
)
print (buy_signals.tail(3))
#-------------------------------------------------
print(30*"=",sahame," True and False مقادير sma10-20")          

history1 = ticker.history


def sma(series, periods: int, ):
    return series.rolling(window=periods, min_periods=periods).mean()


sma_10 = sma(history.close, 10)
sma_20 = sma(history.close, 20)
buy_signals1 = (
        (sma_10 > sma_20) &
        (sma_20.shift(1) > sma_10.shift(1))
)
print (buy_signals.tail(3))
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
Fib=print(40*"=",sahame,"hm_Fib and mo_Fib")
if (ticker.max_year)>(ticker.adj_close)<(ticker.yesterday_price):
     print ('حمايت 1',hm1,'\nحمايت 2', hm2,'\nحمايت 3', hm3,'\nحمايت 4', hm4,'\nحمايت 5',hm5,'\nحمايت 6',hm6,'\nحمايت 7',hm7,'\nحمايت 8',hm8,'\nحمايت 9',hm9)
else:
    if (ticker.min_year)<(ticker.adj_close) >(ticker.yesterday_price):
         print (' مقاومت1 ',mo1,'\n مقاومت2 ', mo2,'\n مقاومت3 ', mo3,'\n مقاومت4 ', mo4,'\n مقاومت5 ', mo5,'\n مقاومت6 ', mo6,'\n مقاومت7 ', mo7,'\n مقاومت8 ', mo8,'\n مقاومت9 ', mo9,'\n مقاومت10 ', mo10)
         
#==========================================================
print(30*"=","محاسبات خريد شمااز",sahame,)
          
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
          Fib == Fib    
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
     p=5384
     s=0
     v=8000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib     
# غکورش
if index == 5:
     p=9194
     s=0
     v=28000
     if p > 0 :
          print (p , ': قيمت خريد شمااز',sahame )
          print (v ,': تعداد سهام موجود')
     if s > 0 :
          print (s , ': قيمت فروش شمااز',sahame )
          print (v ,': تعدادسهام فروخته شده')
          Fib == Fib
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
          Fib == Fib
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
              print(20*"-" )
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
          print (' : تعيين حدسودوزيان بااحتساب قيمت خريد شمااز ',nam)
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
    print (20*'-')

if ticker.adj_close < ticker.yesterday_price :
    print (darsad_down4 , ": قيمت فرداتا4درصدمنفي")
    print (darsad_down6 , ": قيمت فرداتا6درصدمنفي")
    print (20*'-')
    
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
#=====================================================       
         
print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')

#===================================================== 
print (30*'-')
print (" Good luck "," موفق باشيد                    "," پايان محاسبات ",nam)
print () 

