
# برسي سهام دربورس ايران باپايتون3 فقط باتايپ نام سهم به فارسي
# محاسبات ايچيمکو راانجام ميدهد ودرمرحله دوم
# فقط بازدن شماره کنارسهم محاسبات راانجام داده ونتيجه رااغلام مي کند
# RSI-ichimoku-EMA-Volume-Profit and loss-Charts-Canal-Moving 103-Candel

import time
import numpy as np
import pandas as pd
import finpy_tse as tse
from datetime import datetime
import warnings
import jdatetime  # اضافه کردن کتابخانه jdatetime

warnings.filterwarnings("ignore", category=FutureWarning)

def calculate_elliott_wave(prices):
    if len(prices) < 5:
        return "Insufficient data for wave analysis", None, None
    
    diffs = np.diff(prices)
    peaks = [i for i in range(1, len(diffs)-1) if diffs[i-1] < 0 < diffs[i]]
    troughs = [i for i in range(1, len(diffs)-1) if diffs[i-1] > 0 > diffs[i]]
    
    wave_count = len(peaks) + len(troughs)

    # Determine current wave type and position
    if len(peaks) > 0 and (len(troughs) == 0 or peaks[-1] > troughs[-1]):
        current_wave_type = "صعودی"  # Bullish
        current_wave_position = len(peaks)
    elif len(troughs) > 0 and (len(peaks) == 0 or troughs[-1] > peaks[-1]):
        current_wave_type = "نزولی"  # Bearish
        current_wave_position = len(troughs)
    else:
        current_wave_type = "نامشخص"  # Undefined
        current_wave_position = None

    return wave_count, current_wave_type, current_wave_position


def main_menu():
    print ()
    print(10*"-" , 'لطفا انتخاب کنيد',10*"-")

def open_testnew_py():
    # 1 .  test.py محاسبات سهام دربورس ايران بافايل
    pass

def for_exit_tsenew_py():
    # 2 . براي خارج شدن ازبرنامه
    pass


while True:
    main_menu()
    user_input = input("Enter 1 ؟ testnew.py برنامه راادامه ميدهيدبا \nEnter 2 ياازبرنامه خارج ميشويد؟ : ")
    print ('-'*30)
    print ()

    if user_input == "2":
        for_exit_tsenew_py()
        print ('شماازبرنامه خارج شديد')

        exit()
        

    elif user_input == "1":
          open_testnew_py()
          
          
          try:

              import math
              import mplfinance as mplf
              import scipy.stats as stt
              import matplotlib.pyplot as plt
              import pandas_ta as ta
              import yfinance as yf
              import pandas_datareader.data as web
              from datetime import date
              warnings.filterwarnings("ignore", category=FutureWarning)

              print ("="*15,"برسي سهام دربورس ايران باايچيموکو","="*15)
              print ()

              nam = input ("Hello,Please write the name of the stock you want : \n لطفا نام سهام موردنظرتان رابنويسسد :")


              DF = tse.Get_Price_History(stock=nam,
                                         start_date='1401-01-01',
                                         end_date='1403-09-01',
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

              print(f"today_Open_price:{today_Open_price}  , yesterday_Open_price:{yesterday_Open_price}  , today_two_Open_price:{today_two_Open_price}")
              print(f"today_price: {today_price}      , yesterday_price : {yesterday_price}      , today_two_price: {today_two_price}")
              print(f"today_price_max: {today_price_max}   , yesterday_price_max: {yesterday_price_max}   , today_two_price_max:{today_two_price_max}")
              print(f"today_price_min: {today_price_min}   , yesterday_price_min: {yesterday_price_min}   , today_two_price_min:{today_two_price_min}")
              print(f"today_Final: {today_Final_price}      , yesterday_Final: {yesterday_Final_price}      , today_two_Final: {today_two_Final_price}")

              print ()

               #================================================     
              if today_price > yesterday_price:
                  print (' قيمت امروزبالاترازديروزه ')
              else:
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

              print (today_Volume, ' : حجم امروز')
              print (today_Volume_yesterday, ' : حجم ديروز')
              print (today_Volume_yesterday2, ' : حجم سه روزقبل')
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
              tenken12 = (math.ceil(ten12))

              window_size = 11
              past_11_days_high = DF['High'].rolling(window_size).max().iloc[-1]
              past_11_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
              ten11 = (past_11_days_high + past_11_days_low)/2
              tenken11 = (math.ceil(ten11))

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

              print(f"ten8  : {tenken8}     ,    kij26 :  {kijon26}")
              print(f"ten9 : {tenken9}     ,    kij27 :  {kijon27}")
              print ()

               # محاسبات ابرکومو52 روزه به قبل
               # Calculate the highest and lowest price over the past 26 days
              window_size = 52
              past_52_days_high = DF['High'].rolling(window_size).max().iloc[-1]
              past_52_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
              kij52 = (past_52_days_high + past_52_days_low)/2
              komu52_max = (math.ceil(past_52_days_high))
              komu52_min = (math.ceil(past_52_days_low))

              print(f"moving_103 : {moving_103}")
              print(f"komu52_max : {komu52_max}   ,  komu52_min : {komu52_min} ")


              if kijon27 <= kijon26 == tenken8 >= tenken9 :
                   print ('kijon26 == tenken8 , تنکانسن وکيجونسن به حالت فلت برابرشدن')


              if kijon27 < kijon26 == tenken8 > tenken9 :
                   print ('kijon26 == tenken8 , تنکانسن وکيجونسن روبه بالا باهم برابرشدن')



              if kijon27 > kijon26 == tenken8 < tenken9 :
                   print ('kijon26 == tenken8 , تنکانسن وکيجونسن روبه پايين باهم برابرشدن')
                    

              print ()
               #--------------------------------
               # تعيين فاصله تنکانسن وکيجونسن به درصد
              num1 = tenken8
              num2 = kijon26

               # Calculate percentage
              percent_1 = ((num2-num1)/((num2 + num1)/2))*100
              percent_2 = ((num1-num2)/((num1 + num2)/2))*100
               #-------------------------------
               #تعيين مقدارفاصله تنکانسن باکيچونسن
              ten8_kij26 = tenken8 - kijon26
               #تعيين مقدارفاصله قيمت به تنکانسن
              price_ten8 = today_Final_price - ten8
               #--------------------------------
              print (30*'-' ,nam)

               #تعيين روند با تنکانسن وکيجونسن
              if kijon28 > tenken12 > today_Final_price :
                   print ('روند نزوليه')
                   print ('kijon26 > tenken8 > price')
                   print ("{:.0f}%".format(percent_1),':  درصد فاصله مانده تاتنکانسن به کيجونسن برسد')
                   print (ten8_kij26 , ' : مقدارفاصله مانده تاتنکانسن به کيجونسن برسد')
                   print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')
                   print (' : اگرفاصله تنکانسن باکيجونسن از4- بيشترباشد - احتمال برگشت روندميباشد')
                   print (percent_1)
              else:
                   if kijon28 < tenken12 < today_Final_price :
                        print ('روند صعوديه')
                        print ('kijon26 < tenken8 < price')
                        print ("{:.0f}%".format(percent_2),':  درصدفاصله مانده تاکيجونسن به تنکانسن برسد')
                        print (ten8_kij26 , ' : مقدارفاصله مانده تاکيجونسن به تنکانسن برسد')
                        print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')
                        print (' : اگرفاصله تنکانسن باکيجونسن از4+ بيشترباشد - احتمال برگشت روندميباشد')
                        print (percent_2)



              if kijon28 == tenken12 > today_Final_price :
                   print ('استراحت تونزول ')
                   print ('kijon26 = tenken8 > price')
                   print ("{:.0f}%".format(percent_1),':  درصد فاصله مانده تاتنکانسن به کيجونسن برسد')
                   print (ten8_kij26 , ' : مقدارفاصله مانده تاتنکانسن به کيجونسن برسد')
                   print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')
              else:
                   if kijon28 == tenken12 < today_Final_price :
                         print ('استراحت توصعود ')
                         print ('kijon26 = tenken8 < price')
                         print ("{:.0f}%".format(percent_2),':  درصد فاصله مانده تاتنکانسن به کيجونسن برسد')
                         print (ten8_kij26 , ' : مقدارفاصله مانده تاتنکانسن به کيجونسن برسد')
                         print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')



              print (20*'-')

              if percent_1 == percent_2 and kijon28 == tenken12 :
                   print ('اگرتنکانسن بالاي کيجونسن رفت بخر,وبلعکسش روبفروش')
                   print (percent_2)
                    
               #------------------------------


              if today_Final_price > moving_3 >=ten8>ten9 :
                   print ('قيمت بالاي ميانگين 3روزه وتنکانسن ميباشد وشروع روندصعودي بشرط حمايت تنکانسن')
              else:
                  if today_Final_price < moving_3 <=ten8<ten9 :
                       print ('قيمت زيرميانگين 3روزه وتنکانسن ميباشد وشروع ريزش بشرط حمايت تنکانسن')



              if today_Final_price > moving_3 >=ten8<ten9 > moving_10 > kij26 :
                   print ('قيمت بالاي ميانگين 3و10روزه وهمچنين تنکانسن وکيجونسن ميباشدوشروع روند صعودي ادامه داراست')
              else:
                  if today_Final_price < moving_3 <=ten8<ten9 < moving_10 < kij26 :
                       print ('قيمت زيرميانگين 3و10روزه وهمچنين تنکانسن وکيجونسن ميباشد وشروع ريزش ادامه داراست')
                         

              print (20*'-')          
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
                     print ()
                     print ('--- Signal buy :خيلي خيلي مهم: قيمت تنکانسن وکيجونسن روروبه بالاقطع کرد ---')
                     print ()
                     print ()
              else:
                   if kij30<=kij29<=kij28<ten12<=ten11<=ten10>kij27<=kij26<yesterday_price >=ten9>ten8>= today_price :
                         print ()
                         print ('--- Signal sell :خيلي خيلي مهم : قيمت تنکانسن وکيجونسن روروبه پايين قطع کرد ---')
                         print ()
                         print ()



              if kij30>=kij29>=kij28>=kij27>=kij26>yesterday_price and kij26 < today_price :
                     print ()
                     print ('--- Signal buy :خيلي مهم : قيمت کيجونسن رو روبه بالاقطع کرد ---')
                     print ()
              else:
                   if kij30<=kij29<=kij28<=kij27<=kij26<yesterday_price and kij26> today_price :
                         print ()
                         print ('--- Signal sell :خيلي مهم : قيمت کيجونسن رو روبه پايين قطع کرد ---')
                         print ()
                        


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
                   print (h8 , ' : اولين مقاومت سرراه')
              else:
                   if yesterday_price > today_price <= tenken8 == kijon26 :
                        print (L8 , ' : اولين حمايت سرراه')


              print (20*'-')

               #===============================================
               #تعيين دومين مقاومت وحمايت سرراه با محاسبات انجام شده ايچيموکو         
              past_26 = past_26_days_high - past_26_days_low
              past_26h = past_26  + past_26_days_high
              past_26L = past_26_days_low - past_26
              h26 = (math.ceil(past_26h))
              L26 = (math.ceil(past_26L))


              if yesterday_price < today_price >= tenken8 == kijon26 :
                    print (h26 , ' : دومين مقاومت سرراه')
              else:
                   if yesterday_price > today_price <= tenken8 == kijon26 :
                         print (L26 , ' : دومين حمايت سرراه')

               #=====================================================
              print ('='*30,' hammer candle and Doji ')


              if today_price_max > today_price > today_Open_price >= today_price_min :
                   print ('چکش سبز برگشتي درروند نزولي ')
                   print (' H > C > O >= L ')


              if today_price_max > today_Open_price > today_price >= today_price_min :
                   print ('چکش قرمزبرگشتي درروند صعودي ')
                   print (' H > O > C >= L ')


              if today_Open_price == today_price_max > today_price > today_price_min :
                   print ('دوجي قرمزشد نزولي است ياادامه دهنده نزول واگرسبزشد صعودي ياادامه دهنده صعود')
                   print (' O = H > C > L ')
                    

              if today_Open_price > today_price_max > today_price > today_price_min :
                   print ('مارابوزوي قرمز نزولي')
                   print (' O > H > C > L ')


              if today_Open_price < today_price_max == today_price > today_price_min :
                   print ('مارابوزوي سبز صعودي ')
                   print (' O < H = C > L ')
                    
                    
               #===================================================
              print ("-"*20,nam,'Signal candlestick patterns')
              piercing_1= (yesterday_Open_price + yesterday_price)/2
              

              if today_Open_price > yesterday_price < yesterday_Open_price > today_price > today_Open_price:
                  print ('_ مهم _ Harami patterns Bullish الگوي برگشتي صعودي (مادرباردار) ')


              if today_price > yesterday_Open_price < yesterday_price > today_Open_price > today_price:
                   print ('_ مهم _ Harami patterns Bearish الگوي برگشتي نزولي (مادرباردار) ')


              if today_Open_price < yesterday_price < yesterday_Open_price < today_price > today_Open_price:
                   print ('_ مهم _ Bullish Engulfing الگوي برگشتي صعودي معتبر')


              if today_price < yesterday_Open_price < yesterday_price <  today_Open_price > today_price:
                   print ('_ مهم _ Bearish Engulfing الگوي برگشتي نزولي معتبر')


              if today_price >= yesterday_price_max < today_price_max and today_Open_price >= yesterday_price_min > today_price_min and yesterday_Open_price > yesterday_price:
                    print ('Bullish Engulfing الگوي برگشتي صعودي معمولادرکف رخميده')


              if today_price <= yesterday_price_min > today_price_min and today_Open_price <= yesterday_price_max < today_price_max and yesterday_Open_price < yesterday_price:
                    print ('Bearish Engulfing الگوي برگشتي نزولي درکف رخميده')


              if yesterday_price_max > today_price_max > piercing_1 < today_price and yesterday_price_min > today_price_min < yesterday_price > today_Open_price <yesterday_Open_price :
                    print ('piercing patterns الگوي برگشتي صعودي پرسينگ (کندل دومي پايين ترازنيمه اولي)')


              if yesterday_price_max < today_price_max > piercing_1 > today_price and yesterday_price_min < today_price_min < yesterday_price < today_Open_price > yesterday_Open_price  :
                    print ('Dark Cloud patterns الگوي برگشتي نزولي دارک کلود (کندل دومي بالاترازنيمه اولي)')     


              if today_two_price_max <= today_price_max > yesterday_price_max > today_two_price_min < today_price_min > yesterday_Open_price == yesterday_price_min < yesterday_price and today_price_min > yesterday_price_max :
                    print ('Morning star الگوي سه کندلي برگشتي صعودي,کندل وسط دوجي سبز')


              if today_two_price_max > today_price_max < yesterday_price_max > today_two_price_min < today_price_min < yesterday_Open_price > yesterday_price > yesterday_price_min and today_price_min < today_two_price_max :
                    print ('Evening star الگوي سه کندلي برگشتي نزولي,کندل وسط دوجي قرمز')
                    

               #=====================================================
              print ('='*30,' signal canal Day26 and Day52 ')
              

              if past_26_days_low < yesterday_price < today_price > kij26 and today_price < past_26_days_high :
                  print ('قيمت بالاي نيمه کانال 26روزه است وروبه بالاميره')


              if past_26_days_low < yesterday_price > today_price > kij26 and today_price < past_26_days_high :
                    print ('قيمت بالاي نيمه کانال26روزه است وروبه پايين ميره')


              if past_26_days_low < yesterday_price < today_price < kij26 and today_price < past_26_days_high :
                    print ('قيمت پايين نيمه کانال26روزه است وروبه بالاميره')


              if past_26_days_low < yesterday_price > today_price < kij26 and today_price < past_26_days_high :
                    print ('قيمت پايين نيمه کانال26روزه است وروبه پايين ميره')
                  

              if past_26_days_high < yesterday_price > today_price < past_26_days_high:
                    print ('signal sell : ','قيمت بالاي کانال 26روزه روبه سمت پايين شکست')


              if past_26_days_high > yesterday_price < today_price > past_26_days_high :
                    print ('signal buy : ','قيمت بالاي کانال 26روزه روبه سمت بالا شکست')
                    

              if past_26_days_low < yesterday_price > today_price < past_26_days_low :
                    print ('قيمت پايين کانال26روزه روبه سمت پايين شکست')


              if past_26_days_low > yesterday_price < today_price > past_26_days_low :
                    print ('قيمت پايين کانال26روزه روبه سمت بالاشکست')


               #-------------------52
              if past_52_days_low < yesterday_price < today_price > kij52 and today_price < past_52_days_high :
                    print ('قيمت بالاي نيمه کانال52روزه است وروبه بالاميره')


              if past_52_days_low < yesterday_price > today_price > kij52 and today_price < past_52_days_high :
                    print ('قيمت بالاي نيمه کانال52روزه است وروبه پايين ميره')


              if past_52_days_low < yesterday_price < today_price < kij52 and today_price < past_52_days_high :
                    print ('قيمت پايين نيمه کانال52روزه است وروبه بالاميره')


              if past_52_days_low < yesterday_price > today_price < kij52 and today_price < past_52_days_high :
                    print ('قيمت پايين نيمه کانال52روزه است وروبه پايين ميره')
                    

              if past_52_days_high < yesterday_price > today_price < past_52_days_high:
                    print ('signal sell : ','قيمت بالاي کانال52روزه روبه سمت پايين شکست')


              if past_52_days_high > yesterday_price < today_price > past_52_days_high :
                    print ('signal buy : ','قيمت بالاي کانال52روزه روبه سمت بالاشکست')
                    

              if past_52_days_low < yesterday_price > today_price < past_52_days_low :
                    print ('قيمت پايين کانال52روزه روبه سمت پايين شکست')


              if past_52_days_low > yesterday_price < today_price > past_52_days_low :
                    print ('قيمت پايين کانال52روزه روبه سمت بالاشکست')                  


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
                       
   
              print ("="*40)
               #==========================================================
               #-----------------------------------------
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
              namad =["چکارن","تلیسه","غمینو","سيمانو","وسپه","شپاکسا","ومعادن","تاپیکو",
                       "دسبحان","کچاد","شستا","حتوکا","خگستر","فولاد","شپنا","فملی","فصبا",
                       "فسبزوار","خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور","فپنتا",
                       "شبندر","فارس","غفارس","وبصادر","کچاد","درازک","داتام","نخريس","پاکشو",
                       "کگل","ثبهساز","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
                       "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
                       "تاصيكو","حكشتي","قهكمت","تكشا","شاروم","مارون","آريا","اپال",
                       "واعتبار","اطلس","شپترو","سمگا","سبزوا","غکورش","استيل","ارفع"]

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
              print ()

              print ('-'*20)
              PE_ticker=(math.ceil(ticker.p_e_ratio))

              print(ticker.last_date,': تاريخ وساعت آخرين اطلاعات قيمت پاياني ومعاملاتي')
              print ('-'*20)

              print(ticker.title,' : نام شرکت ')
              print(ticker.state,ticker.flow,ticker.group_name)     
              print(ticker.fiscal_year,' : سال مالی ')  
              print(math.ceil(ticker.eps) ,'   :  EPS  ')  
              print(math.ceil(ticker.p_e_ratio) ,'   :   P/E')  
              print(ticker.group_p_e_ratio, '  :  group P/E ')  
              print(math.ceil(ticker.float_shares),'  : درصد سهام شناور')   
              print(math.ceil(ticker.base_volume),'  : حجم مبنا ')
              print()  
              print(ticker.last_price,'  : آخرین معامله ')  
              print(ticker.adj_close,'  : قیمت پایانی ')  
              print(ticker.yesterday_price,' : قیمت دیروز ')  
              print(ticker.open_price,'  : قيمت بازشدن')   
              print()
              print(ticker.high_price,' : حداکثرقيمت امروز')  
              print(ticker.low_price,'  : حداقل قيمت امروز')
              print(math.ceil(ticker.sta_max),' : حداکثر قیمت مجاز')  
              print(math.ceil(ticker.sta_min),' : حداقل قیمت مجاز')
              print()
              print(math.ceil(ticker.min_week),' : حداقل قیمت هفته اخیر')  
              print(math.ceil(ticker.max_week),' : حداکثر قیمت هفته اخیر')
              print(math.ceil(ticker.min_year),' : حداقل قیمت بازه سال')  
              print(math.ceil(ticker.max_year),' : حداکثر قیمت بازه سال')
              print()
              print(ticker.count,'  : تعداد معاملات ')
              print(ticker.value,'  :  ارزش معاملات ')
              print(ticker.volume,' : حجم معاملات امروز ')
              print(today_Volume_yesterday,"     : حجم ديروز")
              print(today_Volume_yesterday2,"    : حجم سه روزقبل")
              print(ticker.month_average_volume,': میانگین حجم ماه')

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
              print (math.ceil(j2) ,'   : درصدتفاوت قيمت ديروزبه امروز')
              print (n1 ,' : تفاوت قيمت ديروزبه امروزبه ريا ل')
              print (math.ceil(jnv1) ,' : درصدنوسان قيمتي امروز')
              print()
               #======================================================****
               # محاسبه بدست آوردن فاصله بين حداکثروحداقل قيمت به درصد                                                                         
              tik_close_low = ((((ticker.adj_close)-(ticker.low_price))/(ticker.adj_close))*100)
              tik_open_low = ((((ticker.open_price)-(ticker.low_price))/(ticker.open_price))*100)
              tik_ascending = ((math.ceil(tik_close_low))-(math.ceil(tik_open_low)))
              tik_close_high = ((((ticker.high_price)-(ticker.adj_close))/(ticker.high_price))*100)
              tik_open_high = ((((ticker.high_price)-(ticker.open_price))/(ticker.high_price))*100)
              tik_Descending =((math.ceil(tik_close_high))-(math.ceil(tik_open_high)))

              print(30*"=",sahame," Up or Down Tick")
              

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



              print(30*"=",sahame," Tik ascending or Descending")
              #------------------------------------------

              if ticker.adj_close > ticker.open_price > ticker.yesterday_price > ticker.low_price:
                   print (tik_ascending , ' : تيک صعودي')
              else :
                  if ticker.adj_close < ticker.open_price < ticker.yesterday_price < ticker.high_price:
                        print (tik_Descending , ' : تيک نزولي')
                    
                                    
               #======================================================****
              print ('='*20 ,"Calculations done RSI-MACD-ichimoku-Stochastic  ")

              
              rsi = ta.momentum.rsi(DF['Close'], length=14)

              rsi_diff = rsi
              #print(rsi.tail(3))
              #=====================================================

              # تاریخ و زمان جاری به فرمت شمسی
              now = datetime.now()
              dt_string = now.strftime("%Y/%m/%d - %A   %H:%M:%S:%p")
              persian_date = jdatetime.datetime.now().strftime("%Y/%m/%d - %A   %H:%M:%S:%p")

              print ()
              print("تاریخ و زمان میلادی =", dt_string)
              print("تاریخ و زمان شمسی =", persian_date)

              # محاسبه تنکانسن و کیجونسن
              high_9 = DF['High'].rolling(window=9).max()
              low_9 = DF['Low'].rolling(window=9).min()
              DF['Tenkan-sen'] = (high_9 + low_9) / 2

              high_26 = DF['High'].rolling(window=26).max()
              low_26 = DF['Low'].rolling(window=26).min()
              DF['Kijun-sen'] = (high_26 + low_26) / 2

              # بررسی و حذف مقادیر NA
              DF['Tenkan-sen'] = DF['Tenkan-sen'].fillna(0)  # جایگزینی NA با 0
              DF['Kijun-sen'] = DF['Kijun-sen'].fillna(0)  # جایگزینی NA با 0

              # گرد کردن مقادیر تنکانسن و کیجونسن به نزدیک‌ترین عدد صحیح و تبدیل به نوع integer
              DF['Tenkan-sen'] = DF['Tenkan-sen'].round(0).astype(int)
              DF['Kijun-sen'] = DF['Kijun-sen'].round(0).astype(int)

              # سیگنال خرید و فروش بر اساس تقاطع تنکانسن و کیجونسن
              DF['Signal'] = np.where(DF['Tenkan-sen'] > DF['Kijun-sen'], 1, 
                                    np.where(DF['Tenkan-sen'] < DF['Kijun-sen'], -1, 0))



              # محاسبه کیجونسن 103 روزه
              high_103 = DF['High'].rolling(window=103).max()
              low_103 = DF['Low'].rolling(window=103).min()
              DF['Kijun-sen_103'] = (high_103 + low_103) / 2

              # بررسی و حذف مقادیر NA برای کیجونسن 103 روزه
              DF['Kijun-sen_103'] = DF['Kijun-sen_103'].fillna(0)  # جایگزینی NA با 0
              DF['Kijun-sen_103'] = DF['Kijun-sen_103'].round(0).astype(int)  # گرد کردن به عدد صحیح

              # سیگنال خرید و فروش بر اساس تقاطع تنکانسن و کیجونسن 103 روزه
              DF['Signal_103'] = np.where(DF['Tenkan-sen'] > DF['Kijun-sen_103'], 1,
                                           np.where(DF['Tenkan-sen'] < DF['Kijun-sen_103'], -1, 0))


              # تابع برای بررسی و بازگشت آخرین واگرایی بین تنکانسن و قیمت بسته‌شده
              def get_last_divergence_with_close(DF):
                  last_divergence = None
                  for i in range(1, len(DF)):
                      # بررسی واگرایی مثبت
                      if (DF['Tenkan-sen'].iloc[i] < DF['Tenkan-sen'].iloc[i-1] and 
                          DF['Close'].iloc[i] > DF['Close'].iloc[i-1]):
                          last_divergence = f"آخرین واگرایی مثبت در تاریخ {DF.index[i]}: ten and close سيگنال خريد"
                      # بررسی واگرایی منفی
                      elif (DF['Tenkan-sen'].iloc[i] > DF['Tenkan-sen'].iloc[i-1] and 
                            DF['Close'].iloc[i] < DF['Close'].iloc[i-1]):
                          last_divergence = f"آخرین واگرایی منفی در تاریخ {DF.index[i]}: ten and close سيگنال فروش"
                    
                  return last_divergence


                # تابع برای بررسی و بازگشت آخرین واگرایی بین تنکانسن و کیجونسن
              def get_last_divergence(DF):
                  last_divergence = None
                  for i in range(1, len(DF)):
                      # بررسی واگرایی مثبت
                      if (DF['Tenkan-sen'].iloc[i] < DF['Tenkan-sen'].iloc[i-1] and 
                          DF['Kijun-sen'].iloc[i] > DF['Kijun-sen'].iloc[i-1]):
                          last_divergence = f"آخرین واگرایی مثبت در تاریخ {DF.index[i]}: ten and kij سيگنال خريد"
                # بررسی واگرایی منفی
                      elif (DF['Tenkan-sen'].iloc[i] > DF['Tenkan-sen'].iloc[i-1] and 
                              DF['Kijun-sen'].iloc[i] < DF['Kijun-sen'].iloc[i-1]):
                          last_divergence = f"آخرین واگرایی منفی در تاریخ {DF.index[i]}: ten and kij سيگنال فروش"
                    
                  return last_divergence               


               # Ichimoku  ترکيب سه کندل آخربا
              def analyze_last_three_candles_with_ichimoku(DF):
                  # دریافت سه روز آخر از DataFrame
                  last_three = DF.tail(3)
                
                  # استخراج قیمت‌های بسته‌شدن و خطوط ایچیموکو
                  closes = last_three['Close'].values
                  tenkan_sen = last_three['Tenkan-sen'].values
                  kijun_sen = last_three['Kijun-sen'].values

                  # تعیین وضعیت سه کندل آخر
                  if closes[2] < closes[1] < closes[0]:
                      trend = "صعودی"  # Bullish
                  elif closes[2] > closes[1] > closes[0]:
                      trend = "نزولی"  # Bearish
                  else:
                      trend = "خنثی"  # Neutral

                  # بررسی سیگنال‌های ایچیموکو
                  ichimoku_signal = ""
                  if tenkan_sen[-1] > kijun_sen[-1]:
                      ichimoku_signal = "سیگنال خرید (Tenkan بالای Kijun)"
                  elif tenkan_sen[-1] < kijun_sen[-1]:
                      ichimoku_signal = "سیگنال فروش (Tenkan زیر Kijun)"
                  else:
                      ichimoku_signal = "هیچ سیگنالی"

                  return trend, ichimoku_signal


               # Ichimoku  ترکيب سه کندل آخربراي واگرايي با
              def check_divergence_with_ichimoku(DF):
                  # دریافت سه روز آخر از DataFrame
                  last_three = DF.tail(3)

                  # استخراج قیمت‌های بسته‌شدن و خطوط ایچیموکو
                  closes = last_three['Close'].values
                  tenkan_sen = last_three['Tenkan-sen'].values
                  kijun_sen = last_three['Kijun-sen'].values

                  # بررسی واگرایی مثبت
                  if closes[2] < closes[1] < closes[0] and tenkan_sen[2] > tenkan_sen[1] > tenkan_sen[0]:
                      return f"واگرایی مثبت در تاریخ {last_three.index[0]} : Candl and ichimoku قيمت درحال افزايش ولي تنکانسن کاهشي."

                  # بررسی واگرایی منفی
                  elif closes[2] > closes[1] > closes[0] and tenkan_sen[2] < tenkan_sen[1] < tenkan_sen[0]:
                      return f"واگرایی منفی در تاریخ {last_three.index[0]} : Candl and ichimoku قيمت درحال کاهش ولي تنکانسن افزايشي."

                  return "Candl and ichimoku هيچ واگرايي مشاهده نشد براي."



              # Add this function to calculate Bollinger Bands سيگنال خريد وفروش با
              def calculate_bollinger_bands(DF, window=20, num_std_dev=2):
                  DF['MA'] = DF['Close'].rolling(window=window).mean()  # Moving Average
                  DF['STD'] = DF['Close'].rolling(window=window).std()  # Standard Deviation
                  DF['Upper Band'] = DF['MA'] + (DF['STD'] * num_std_dev)  # Upper Band
                  DF['Lower Band'] = DF['MA'] - (DF['STD'] * num_std_dev)  # Lower Band

                  # Generate Buy/Sell Signals based on Bollinger Bands
                  DF['Bollinger_Signal'] = np.where(DF['Close'] < DF['Lower Band'], 1, 
                                                   np.where(DF['Close'] > DF['Upper Band'], -1, 0))
                
                  return DF


              def analyze_last_three_candles_with_bollinger(DF):
                  last_three = DF.tail(3)
                  closes = last_three['Close'].values
                  upper_band = last_three['Upper Band'].values
                  lower_band = last_three['Lower Band'].values

                  # تعیین وضعیت سه کندل آخر
                  if closes[2] < closes[1] < closes[0]:
                      trend = "صعودی"  # Bullish
                      if closes[0] > upper_band[0]:  # قیمت بالای نوار بالایی
                          signal = "سیگنال خرید (قیمت بالای نوار بالایی)"
                      elif closes[0] < lower_band[0]:  # قیمت پایین نوار پایینی
                          signal = "سیگنال فروش (قیمت پایین نوار پایینی)"
                      else:
                          signal = "هیچ سیگنالی"
                  elif closes[2] > closes[1] > closes[0]:
                      trend = "نزولی"  # Bearish
                      if closes[0] < lower_band[0]:  # قیمت پایین نوار پایینی
                          signal = "سیگنال خرید (قیمت پایین نوار پایینی)"
                      elif closes[0] > upper_band[0]:  # قیمت بالای نوار بالایی
                          signal = "سیگنال فروش (قیمت بالای نوار بالایی)"
                      else:
                          signal = "هیچ سیگنالی"
                  else:
                      trend = "خنثی"  # Neutral
                      signal = "هیچ سیگنالی"

                  return trend, signal

              # Call this function after loading your DataFrame (DF)
              DF = calculate_bollinger_bands(DF)

              # محاسبه نوارهای بولینگر
              DF = calculate_bollinger_bands(DF)

              # تحلیل سه کندل آخر با نوارهای بولینگر
              trend_last_three, bollinger_signal = analyze_last_three_candles_with_bollinger(DF)



              # محاسبه RSI
              delta = DF['Close'].diff()
              gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
              loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
              RS = gain / loss
              DF['RSI'] = 100 - (100 / (1 + RS))

              # بررسی و حذف مقادیر NA
              DF['RSI'] = DF['RSI'].fillna(0)  # جایگزینی NA با 0

              # گرد کردن مقادیر RSI به نزدیک‌ترین عدد صحیح و تبدیل به نوع integer
              DF['RSI'] = DF['RSI'].round(0).astype(int)

              # سیگنال خرید و فروش بر اساس واگرایی RSI بدون هشدار
              DF['RSI_Signal'] = 0
              for i in range(1, len(DF)):
                  if (DF['RSI'].iloc[i] < 30 and DF['Close'].iloc[i] > DF['Close'].iloc[i-1]):
                      DF.at[DF.index[i], 'RSI_Signal'] = 1   # سیگنال خرید
                  elif (DF['RSI'].iloc[i] > 70 and DF['Close'].iloc[i] < DF['Close'].iloc[i-1]):
                      DF.at[DF.index[i], 'RSI_Signal'] = -1  # سیگنال فروش


              # RSI ترکيب سه کندل آخربا
              def analyze_last_three_candles_with_rsi(DF):
                  # دریافت سه روز آخر از DataFrame
                  last_three = DF.tail(3)
                
                  # استخراج قیمت‌های بسته‌شدن و RSI
                  closes = last_three['Close'].values
                  rsi_values = last_three['RSI'].values
                
                  # تعیین وضعیت سه کندل آخر
                  if closes[2] < closes[1] < closes[0]:
                      trend = "صعودی"  # Bullish
                  elif closes[2] > closes[1] > closes[0]:
                      trend = "نزولی"  # Bearish
                  else:
                      trend = "خنثی"  # Neutral

                  # بررسی سیگنال‌های RSI
                  rsi_signal = ""
                  if rsi_values[-1] < 30:
                      rsi_signal = "اشباع فروش (خرید)"
                  elif rsi_values[-1] > 70:
                      rsi_signal = "اشباع خرید (فروش)"
                  else:
                      rsi_signal = "عادی"

                  return trend, rsi_signal

             # محاسبه MACD
              exp1 = DF['Close'].ewm(span=12, adjust=False).mean()
              exp2 = DF['Close'].ewm(span=26, adjust=False).mean()
              DF['MACD'] = exp1 - exp2

              # محاسبه سیگنال MACD
              DF['Signal_MACD'] = DF['MACD'].ewm(span=9, adjust=False).mean()

              # بررسی و حذف مقادیر NA
              DF['MACD'] = DF['MACD'].fillna(0)  # جایگزینی NA با 0
              DF['Signal_MACD'] = DF['Signal_MACD'].fillna(0)  # جایگزینی NA با 0

              # سیگنال خرید و فروش بر اساس تقاطع MACD
              DF['MACD_Signal'] = np.where(DF['MACD'] > DF['Signal_MACD'], 1, 
                                          np.where(DF['MACD'] < DF['Signal_MACD'], -1, 0))

              # گرد کردن مقادیر MACD و سیگنال MACD به نزدیک‌ترین عدد صحیح و تبدیل به نوع integer
              DF['MACD'] = DF['MACD'].round(0).astype(int)
              DF['Signal_MACD'] = DF['Signal_MACD'].round(0).astype(int) 


              # MACD  ترکيب سه کندل آخر با
              def analyze_last_three_candles_with_macd(DF):
                  # دریافت سه روز آخر از DataFrame
                  last_three = DF.tail(3)
                
                  # استخراج قیمت‌های بسته‌شدن و مقادیر MACD
                  closes = last_three['Close'].values
                  macd_values = last_three['MACD'].values
                  signal_macd_values = last_three['Signal_MACD'].values
                
                  # تعیین وضعیت سه کندل آخر
                  if closes[2] < closes[1] < closes[0]:
                      trend = "صعودی"  # Bullish
                  elif closes[2] > closes[1] > closes[0]:
                      trend = "نزولی"  # Bearish
                  else:
                      trend = "خنثی"  # Neutral

                  # بررسی سیگنال‌های MACD
                  macd_signal = ""
                  if macd_values[-1] > signal_macd_values[-1]:
                      macd_signal = "سیگنال خرید (MACD بالای سیگنال)"
                  elif macd_values[-1] < signal_macd_values[-1]:
                      macd_signal = "سیگنال فروش (MACD زیر سیگنال)"
                  else:
                      macd_signal = "هیچ سیگنالی"

                  return trend, macd_signal  

              # محاسبه میانگین متحرک ساده (SMA) برای دوره‌های 3 و 9 روزه
              DF['SMA_3'] = DF['Close'].rolling(window=3).mean()
              DF['SMA_9'] = DF['Close'].rolling(window=9).mean()

              # بررسی و حذف مقادیر NA
              DF['SMA_3'] = DF['SMA_3'].fillna(0)  # جایگزینی NA با 0
              DF['SMA_9'] = DF['SMA_9'].fillna(0)  # جایگزینی NA با 0

              # گرد کردن مقادیر SMA به نزدیک‌ترین عدد صحیح و تبدیل به نوع integer
              DF['SMA_3'] = DF['SMA_3'].round(0).astype(int)
              DF['SMA_9'] = DF['SMA_9'].round(0).astype(int)

              # سیگنال خرید و فروش بر اساس تقاطع SMA ها
              DF['SMA_Signal'] = np.where(DF['SMA_3'] > DF['SMA_9'], 1, 
                                         np.where(DF['SMA_3'] < DF['SMA_9'], -1, 0)) 

              # محاسبه میانگین متحرک نمایی (EMA) برای دوره‌های 3 و 9 روزه
              DF['EMA_3'] = DF['Close'].ewm(span=3, adjust=False).mean()
              DF['EMA_9'] = DF['Close'].ewm(span=9, adjust=False).mean()

              # بررسی و حذف مقادیر NA
              DF['EMA_3'] = DF['EMA_3'].fillna(0)  # جایگزینی NA با 0
              DF['EMA_9'] = DF['EMA_9'].fillna(0)  # جایگزینی NA با 0

              # گرد کردن مقادیر EMA به نزدیک‌ترین عدد صحیح و تبدیل به نوع integer
              DF['EMA_3'] = DF['EMA_3'].round(0).astype(int)
              DF['EMA_9'] = DF['EMA_9'].round(0).astype(int)

              # سیگنال خرید و فروش بر اساس تقاطع EMA ها
              DF['EMA_Signal'] = np.where(DF['EMA_3'] > DF['EMA_9'], 1, np.where(DF['EMA_3'] < DF['EMA_9'], -1, 0))


              # محاسبه میانگین متحرک 20 روزه
              DF['MA_20'] = DF['Close'].rolling(window=20).mean()

              # بررسی وضعیت کانال
              if DF['Close'].iloc[-1] > DF['MA_20'].iloc[-1]:
                  trend_status = "صعودی"
              else:
                  trend_status = "نزولی"


              # محاسبه استوکاستیک
              high_stoch = DF['High'].rolling(window=14).max()
              low_stoch = DF['Low'].rolling(window=14).min()

              # %K و %D
              DF['%K'] = (DF['Close'] - low_stoch) / (high_stoch - low_stoch) * 100
              DF['%D'] = DF['%K'].rolling(window=3).mean()

              # بررسی و حذف مقادیر NA
              DF['%K'] = DF['%K'].fillna(0)  # جایگزینی NA با 0
              DF['%D'] = DF['%D'].fillna(0)  # جایگزینی NA با 0

              # گرد کردن مقادیر %K و %D به نزدیک‌ترین عدد صحیح و تبدیل به نوع integer
              DF['%K'] = DF['%K'].round(0).astype(int)
              DF['%D'] = DF['%D'].round(0).astype(int)

              # سیگنال خرید و فروش بر اساس واگرایی استوکستیک
              DF['Stochastic_Signal'] = np.where((DF['%K'] < 20) & (DF['%K'] > DF['%D']), 1,
                                                np.where((DF['%K'] > 80) & (DF['%K'] < DF['%D']), -1, 0))

              # Calculate Gator Oscillator
              DF['Jaw'] = DF['Close'].rolling(window=13).mean().shift(8)
              DF['Teeth'] = DF['Close'].rolling(window=8).mean().shift(5)
              DF['Lips'] = DF['Close'].rolling(window=5).mean().shift(3)

              # Generate Buy/Sell Signals based on Gator Oscillator
              DF['Gator_Signal'] = np.where((DF['Lips'] > DF['Teeth']) & (DF['Teeth'] > DF['Jaw']), 1,
                                            np.where((DF['Lips'] < DF['Teeth']) & (DF['Teeth'] < DF['Jaw']), -1, 0)) 
              
              # نمایش نتایج نهایی فقط برای آخرین سه روز
              last_three_days = DF.tail(3)
            
              print(30*'-')
              print(last_three_days[['Close', 'Upper Band', 'Lower Band', 'Bollinger_Signal']])
              print(last_three_days[['Jaw', 'Teeth', 'Lips', 'Gator_Signal']])
              print(last_three_days[['Tenkan-sen', 'Kijun-sen_103', 'Signal_103']])
              print(last_three_days[['Tenkan-sen', 'Kijun-sen', 'Signal']])
              print(last_three_days[['EMA_3', 'EMA_9', 'EMA_Signal']])
              print(last_three_days[['SMA_3', 'SMA_9', 'SMA_Signal']])
              print(last_three_days[['RSI', 'RSI_Signal']])
              print(last_three_days[['MACD', 'Signal_MACD', 'MACD_Signal']])
              print(last_three_days[['%K', '%D', 'Stochastic_Signal']])
              print(last_three_days[['Close', 'Volume']])
              print(20*'-')
              print(f"وضعیت کانال: {trend_status}")
              # در داخل تابع main_menu یا بعد از محاسبات ایچیموکو
              last_divergence_signal = get_last_divergence_with_close(DF)
              if last_divergence_signal:
                  print(last_divergence_signal)
              else:
                  print("ten and close هيچ واگرايي مشاهده نشد.")

              # در داخل تابع main_menu یا بعد از محاسبات ایچیموکو
              last_divergence_signal = get_last_divergence(DF)
              if last_divergence_signal:
                  print(last_divergence_signal)
              else:
                  print("ten and kij هيچ واگرايي مشاهده نشد.") 


              # Ichimoku  ترکيب سه کندل آخربراي واگرايي با
              # در داخل تابع main_menu یا بعد از محاسبات ایچیموکو، این تابع را فراخوانی کنید:
              divergence_signal = check_divergence_with_ichimoku(DF)
              print(divergence_signal)
              
              print(30*'-')

              # Ichimoku  ترکيب سه کندل آخربا
              # در داخل تابع main_menu یا بعد از محاسبات ایچیموکو، این تابع را فراخوانی کنید:
              trend_last_three, ichimoku_signal = analyze_last_three_candles_with_ichimoku(DF)
              print(f" وضعیت سه کندل آخر: {trend_last_three} \n سیگنال ایچیموکو: {ichimoku_signal}")            

              # RSI ترکيب سه کندل آخربا 
              # در داخل تابع main_menu یا بعد از محاسبات ایچیموکو، این تابع را فراخوانی کنید:
              trend_last_three, rsi_signal = analyze_last_three_candles_with_rsi(DF)
              print(f" سیگنال RSI: {rsi_signal}")

              # MACD  ترکيب سه کندل آخر با
              # در داخل تابع main_menu یا بعد از محاسبات ایچیموکو، این تابع را فراخوانی کنید:
              trend_last_three, macd_signal = analyze_last_three_candles_with_macd(DF)
              print(f" سیگنال MACD: {macd_signal}")

              #نوارهاي بولينگر چاپ نتایج
              print(f" سیگنال بولینگر: {bollinger_signal}")

              print(30*'-') 

              # چاپ پیام خرید و فروش فقط برای آخرین روز
              last_day = last_three_days.iloc[-1]

              if isinstance(last_day.name, str):
                  last_day_date = pd.to_datetime(last_day.name, errors='coerce')  
              else:
                  last_day_date = last_day.name

              if last_day.get('Signal') == 1:
                   print(f"در تاریخ {last_day_date.date()} : بخر (تنکانسن بالای کیجونسن)")
              elif last_day.get('Signal') == -1:
                   print(f"در تاریخ {last_day_date.date()} : بفروش (تنکانسن پایین کیجونسن)")

              if last_day.get('Signal_103') == 1:
                   print(f"در تاریخ {last_day_date.date()} : بخر (تنکانسن بالاي کيجونسن 103)")
              elif last_day.get('Signal_103') == -1:
                   print(f"در تاریخ {last_day_date.date()} : بفروش (تنکانسن پايين کيجونسن 103)")

              if last_day.get('Gator_Signal') == 1:
                   print(f"در تاریخ {last_day_date.date()} : ('Gator_Signal') بخر")
              elif last_day.get('Signal_103') == -1:
                   print(f"در تاریخ {last_day_date.date()} : ('Gator_Signal') بفروش")
                   
                   
              if last_day.get('Stochastic_Signal') == 1:
                   print(f"در تاریخ {last_day_date.date()} : ('Stochastic') بخر")
              elif last_day.get('Stochastic_Signal') == -1:
                   print(f"در تاریخ {last_day_date.date()} : ('Stochastic') بفروش")

              if last_day.get('SMA_Signal') == 1:
                   print(f"در تاریخ {last_day_date.date()} : ('SMA3 > SMA9') بخر")
              elif last_day.get('SMA_Signal') == -1:
                   print(f"در تاریخ {last_day_date.date()} : ('SMA3 < SMA9') بفروش")

              if last_day.get('EMA_Signal') == 1:
                   print(f"در تاریخ {last_day_date.date()} : ('EMA3 > EMA9') بخر")
              elif last_day.get('EMA_Signal') == -1:
                   print(f"در تاریخ {last_day_date.date()} : ('EMA3 < EMA9') بفروش")

              if last_day.get('SMA_9') < last_day.get('EMA_9'):
                   print(f"در تاریخ {last_day_date.date()} : ('SMA9 < EMA9') بخر")
              elif last_day.get('SMA_9') > last_day.get('EMA_9'):
                   print(f"در تاریخ {last_day_date.date()} : ('SMA9 > EMA9') بفروش")

              if last_day.get('SMA_3') < last_day.get('EMA_3'):
                   print(f"در تاریخ {last_day_date.date()} : ('SMA3 < EMA3') بخر")
              elif last_day.get('SMA_3') > last_day.get('EMA_3'):
                   print(f"در تاریخ {last_day_date.date()} : ('SMA3 > EMA3') بفروش")      

              if last_day.get('MACD_Signal') == 1:
                   print(f"در تاریخ {last_day_date.date()} : (MACD) بخر")
              elif last_day.get('MACD_Signal') == -1:
                   print(f"در تاریخ {last_day_date.date()} : (MACD) بفروش")

              if last_day.get('RSI_Signal') == 1:
                   print(f"در تاریخ {last_day_date.date()} : (RSI) بخر")
              elif last_day.get('RSI_Signal') == -1:
                   print(f"در تاریخ {last_day_date.date()} : (RSI) بفروش")


              date_format = '%Y-%m-%d'  # Example format; adjust based on your actual date format
                 
            
              # محاسبه حجم مبنا (میانگین حجم معاملات در دوره مشخص)
              volume_base_period_days = 30
              volume_base = DF["Volume"].tail(volume_base_period_days).mean() if len(DF["Volume"]) >= volume_base_period_days else None

              # نمایش نتایج نهایی فقط برای آخرین سه روز
              last_three_days = DF.tail(3)
              current_volume_today = last_three_days.iloc[-1]['Volume']
              previous_close_price_today = last_three_days.iloc[-1]['Close']
              previous_close_price_yesterday = last_three_days.iloc[-2]['Close']

              # بررسی شرایط برای سیگنال خرید جدید
              if previous_close_price_today < previous_close_price_yesterday and today_Volume_yesterday < today_Volume > (today_Volume_yesterday2)*3:
                  print (': سیگنال خرید به دلیل کاهش قیمت و افزایش حجم')
              if previous_close_price_today > previous_close_price_yesterday and today_Volume_yesterday < today_Volume > (today_Volume_yesterday2)*3:
                  print (': سيگنال فروش به دليل افزايش قيمت وافزايش حجم بالا')


              # تعریف داده‌ها
              data = {
                  'Open': [1, 2, 3],
                  'High': [2, 3, 4],
                  'Low': [0, 1, 2],
                  'Close': [1.5, 2.5, 3.5]
              }

              # ایجاد DataFrame
              df = pd.DataFrame(data)

              def is_hammer(candle):
                  body = candle['Close'] - candle['Open']
                  range_ = candle['High'] - candle['Low']
                  lower_shadow = candle['Open'] - candle['Low']
                  upper_shadow = candle['High'] - candle['Close']

                  if (lower_shadow > 2 * abs(body)) and (upper_shadow < abs(body)):
                      return 'green' if body > 0 else 'red'
                  return None

              for i in range(1, len(df)):
                  current_candle = df.iloc[i]
                  previous_candle = df.iloc[i - 1]

                  hammer_type = is_hammer(current_candle)

                  if hammer_type == 'green' and previous_candle['Close'] < previous_candle['Open']:
                     print("سیگنال خرید: چکش سبز برگشتی در روند نزولی")
                  elif hammer_type == 'red' and previous_candle['Close'] > previous_candle['Open']:
                      print("سیگنال فروش: چکش قرمز برگشتی در روند صعودی")
                    


              # Calculate the Elliott Wave based on closing prices
              current_wave_count, current_wave_type, current_wave_position = calculate_elliott_wave(DF['Close'].values)
              print ('-'*30)
              print(f"تعداد امواج الیوت فعلی: {current_wave_count}")
              print(f"نوع موج فعلی: {current_wave_type}")
              if current_wave_position is not None:
                  print(f"موج فعلی در موقعیت: {current_wave_position}")
                  print ('-'*30)

              #========================================================
              Month_price = DF['Final'].iloc[-26] # آخرين قيمت 30روزقبل
              Month_price1 = DF['Final'].iloc[-25] # آخرين قيمت 29روزقبل
              Month_price2 = DF['Final'].iloc[-24] # آخرين قيمت 28روزقبل
              rsi_Month26 = rsi_diff.iloc[-26]  # يک ماه قبل rsi
              rsi_Month25 = rsi_diff.iloc[-25]  #rsi 29روزقبل
              rsi_Month24 = rsi_diff.iloc[-24]  # rsi 28روزقبل
              rsi_Month = rsi_diff.iloc[-1]  # rsi امروز
              rsi_Month1 = rsi_diff.iloc[-2]  #rsi ديروز
              rsi_Month2 = rsi_diff.iloc[-3]  # rsi پري روزد

               #=====================================================
              print ('='*30,' hammer candle and Doji ')
              DOje1= (ticker.high_price+ticker.low_price)/2


              if ticker.last_price == DOje1 :
                   print (' کندل دوجي شکل گرفته')
              else:
                  if ticker.high_price >ticker.adj_close<= DOje1 >ticker.low_price:
                        print (' معتبرترین کندل دوجي شکل گرفته')
                        


              if ticker.open_price > ticker.adj_close < DOje1:
                   print (' candle Red')
              else:
                   if ticker.open_price < ticker.adj_close > DOje1:
                         print (' candle Green')



              if ticker.low_price <= ticker.last_price<=ticker.adj_close <= DOje1<=ticker.open_price:
                    print (' کندل دوجي قرمزشکل گرفته')
              else:
                   if ticker.high_price >= ticker.last_price>=ticker.adj_close >= DOje1>=ticker.open_price:
                        print (' کندل دوجي سبزشکل گرفته')



              if ticker.high_price > ticker.adj_close > ticker.open_price >= ticker.low_price :
                  print ('چکش سبز برگشتي درروند نزولي ')
                  print (' H > C > O >= L ')



              if ticker.high_price > ticker.open_price > ticker.adj_close >= ticker.low_price :
                   print ('چکش قرمزبرگشتي درروند صعودي ')
                   print (' H > O > C >= L ')



              if ticker.open_price == ticker.high_price > ticker.adj_close > ticker.low_price :
                    print ('دوجي قرمزشد نزولي است ياادامه دهنده نزول واگرسبزشد صعودي ياادامه دهنده صعود')
                    print (' O = H > C > L ')
                    


              if ticker.open_price > ticker.high_price > ticker.adj_close > ticker.low_price :
                    print ('مارابوزوي قرمز نزولي')
                    print (' O > H > C > L ')



              if ticker.open_price < ticker.high_price == ticker.adj_close > ticker.low_price :
                    print ('مارابوزوي سبز صعودي ')
                    print (' O < H = C > L ')

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
              print(today_Volume_yesterday,"حجم ديروز")
                         
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


              if ticker.yesterday_price > ticker.adj_close > today_price6 and ticker.volume > today_Volume_yesterday:
                   print ('حجم افزايشي وقيمت امروزاز 6 روزقبل هم بالاتره')
              else:
                   if ticker.yesterday_price< ticker.adj_close < today_price6 and ticker.volume < today_Volume_yesterday:
                       print ('حجم کاهشي وقيمت امروزاز 6 روزقبل هم کمترشده')

                       
              if ticker.adj_close > today_price9 and ticker.volume > today_Volume_yesterday:
                   print ('حجم افزايشي وقيمت امروزاز 9 روزقبل هم بالاتررفت')
              else:
                  if ticker.adj_close < today_price9 and ticker.volume < today_Volume_yesterday:
                       print ('حجم کاهشي وقيمت امروزاز 9 روزقبل هم پايين تررفت')


               #================================================
              print(25*"-")
              
              if ticker.adj_close > ticker.yesterday_price:
                    print (' قيمت امروزبالاترازديروزه ')
              else :
                    if ticker.adj_close < ticker.yesterday_price:
                         print (' قيمت امروزپايين ترازديروزه ')



              if (ticker.volume)*2 > today_Volume_yesterday and ticker.adj_close > ticker.yesterday_price and today_price>moving_10:
                   print ("sell  : سيگنال فروش به دليل افزايش قيمت وافزايش حجم بالاوقيمت بالاي ميانگين 10روزه")
              else:
                   if (ticker.volume)*2 > today_Volume_yesterday and ticker.adj_close < ticker.yesterday_price and today_price<moving_10:
                       print ("buy  : سیگنال خرید به دلیل کاهش قیمت و افزایش حجم وقيمت پايين ميانگين 10روزه")
                       

              print()
               #=====================================================
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

              print ()
               #=======================================================
              print(39*"=",nam,"One year support and resistance")
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
              highest_price_120 = max(DF['High'][-120:])
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
              lowest_price_120 = min(DF['Low'][-120:])
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
              kh_3=(highest_price_90)-100
               # به حمايت سه ماهه 50تا اضافه کرديم براي محاسبات کف کانال
              kL_3=(lowest_price_90)+100
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
                   print (today_price,' قيمت بسته شدن سه روزه افزايشي ميباشد')
                   print (f"%فاصله قيمت بامقاومت سه ماه به ريا ل ميشود : { fgh_3 } , تفاوت به درصد : { jnv1 }")
              else:
                   if today_price < yesterday_price < today_two_price:
                       print (today_price,' قيمت بسته شده سه روزه کاهشي ميباشد')
                       print (fgm_3 ,': فاصله قيمت باحمايت سه ماهه')
                              

               #تشخيص روند
              if highest_price_180>=highest_price_30>=today_price or lowest_price_180<=lowest_price_30<=today_price and highest_price_90>=highest_price_60 or lowest_price_90<=lowest_price_60 and highest_price_10>=today_price>=lowest_price_10:
                   print (' کانال رنج ميباشد')
              else:
                   if highest_price_60>=highest_price_30>=today_price>=lowest_price_60<=lowest_price_30:
                         print (' کانال ماهيانه رنج شده')

                         

              if highest_price_120>=highest_price_60>=highest_price_30 and lowest_price_120>today_price:
                    print ('کانال نزولي ميباشد')
              else:
                   if lowest_price_120<=lowest_price_60<=lowest_price_30 and highest_price_120<today_price:
                         print ('کانال صعودي ميباشد')
                         

                    
              if kh_3 <= today_price <= highest_price_90 :
                    print ('قيمت به سقف کانال سه ماه رسيده')
              else:
                   if kL_3 >= today_price >= lowest_price_90 :
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
               #بدست آوردن درصد تفاوت قيمت امروزبه حمايت هفتگي
              nv3=((lowest_price_7)-(today_price))
              nv4=((lowest_price_7)+(today_price))/2
              jnh=nv3/nv4
              jnh1=(math.ceil(jnh*100))


              if m_7 <= today_price <= highest_price_7 :
                    print ('قيمت نزديک مقاومت هفتگي ميباشد')
                    print (jnv1,'% : درصدتفاوت قيمت امروزبامقاومت هفتگي')
              else:
                   if h_7 >= today_price >= lowest_price_7 :
                         print ('قيمت نزديک حمايت هفتگي ميباشد')
                         print (jnh1,'% : درصدتفاوت قيمت امروزباحمايت هفتگي')


                          
              print ()
               #================================================================
              print ('='*40,' ميانگين قيمت')
               #ميانگين قيمت 10 و20 روزسهم
               # Calculate the 10-day moving average

               # Print the most recent price and the 10-day moving average
              print(f"today_price : {DF['Close'].iloc[-1]}       ,   moving_10 : {moving_10}")
              print(f"today_two_price : {DF['Close'].iloc[-3]}   ,   moving_103 : {moving_103}")
              print ()


              if today_price>moving_10>yesterday_price>today_two_price:
                    print ('قيمت امروزرفت بالاي ميانگين ده روزه')
              elif today_price>moving_103>yesterday_price>today_two_price:
                      print ('قيمت امروزرفت بالاي ميانگين 103')
              else:
                  if today_price > moving_3 > moving_10 > moving_103:
                         print ('قيمت بالاي ميانگين3و10و103ميباشد')
                  elif today_price > moving_3 > moving_10:
                          print ('قيمت بالاي ميانگين 3و10 ميباشد')       


                    
              if today_price<moving_10<yesterday_price<today_two_price:
                    print ('قيمت امروزرفت پايين ميانگين ده روزه')
              elif today_price<moving_103<yesterday_price<today_two_price:
                      print ('قيمت امروزرفت پايين ميانگين 103')
              else:
                   if today_price < moving_3 < moving_10 < moving_103:
                       print ('قيمت پايين ميانگين 3و10و103 ميباشد')
                   elif today_price < moving_3 < moving_10:
                         print ('قيمت پايين ميانگين 3و10 ميباشد')



              if today_price < moving_3 > moving_10 > moving_103:
                    print ('قيمت پايين ميانگين 3 وبالاي ميانگين 10و103 ميباشد')
              elif today_price < moving_3 > moving_10:
                      print ('قيمت پايين ميانگين 3 وبالاي ميانگين 10ميباشد')
              else:
                  if today_price > moving_3 < moving_10 < moving_103:
                         print ('قيمت بالاي ميانگين 3وپايين ميانگين10و103ميباشد')
                  elif today_price > moving_3 < moving_10:
                          print ('قيمت بالاي ميانگين 3وپايين ميانگين 10ميباشد')
                          


              if moving_3 >= moving_10 >= tenken8 > kijon26 <= ticker.yesterday_price < ticker.adj_close :
                   print ('تيک صعودي شده اگرحمايت تنکانسن هم باهاش باشه,خريد باکندل تاييد')
              else:
                  if moving_3 <= moving_10 <= tenken8 < kijon26 >= ticker.yesterday_price > ticker.adj_close :
                      print ('تيک نزولي شده اگرحمايت تنکانسن هم باهاش بود ,باکندل تاييدبفروش')
                         


              if moving_3 > moving_10 > tenken8 > kijon26 < ticker.yesterday_price < ticker.adj_close :
                    print ('قيمت بالاي ميانگين 3و10وتنکانسن هم بالاي کيجونسن ميباشد يک روند صعودي خوب')
              else:
                   if moving_3 < moving_10 < tenken8 < kijon26 > ticker.yesterday_price > ticker.adj_close :
                         print ('قيمت پايين ميانگين 3و10وتنکانسن هم پايين کيجونسن ميباشد يک روند نزولي قوي')
                         


              if moving_3 >= ticker.yesterday_price > ticker.adj_close >= moving_10 > tenken8 > kijon26 :
                    print (' احتمال ريزش ميباشد چون قيمت وميانگين 3روزه به سمت تنکانسن ميروند')
              else:
                  if moving_3 <= ticker.yesterday_price < ticker.adj_close <= moving_10 < tenken8 < kijon26 :
                        print (' احتمال صعودي شدن ميباشد چون قيمت وميانگين 3روزه به سمت تنکانسن ميروند')



               #------------------------------
               # تعيين فاصله ميانگين 3 و10
              num1 = moving_3
              num2 = moving_10

               # تعيين درصدفاصله بين ميانگين 3و10
              percent_1 = ((num2-num1)/((num2 + num1)/2))*100
              percent_2 = ((num1-num2)/((num1 + num2)/2))*100
               #-------------------------------
               #تعيين مقدارفاصله ميانگين 3و10
              moving_3_10 = moving_3 - moving_10
               #تعيين مقدارفاصله قيمت به تنکانسن
              price_ten8 = ticker.last_price - ten8
               #--------------------------------
              print (30*'-' ,nam)
              #تعيين روند ميانگين 3و10
              if moving_3 < moving_10 :
                    print ('حرکت قيمت نزولي')
                    print ('moving_3 < moving_10')
                    print ("{:.0f}%".format(percent_1),':  درصدفاصله مانده تاميانگين 3به 10برسد')
                    print (moving_3_10 , ' : مقدارفاصله مانده تاميانگين 3 به 10برسد')
                    print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')
              else:
                   if moving_10 > today_Final_price >= moving_3  :
                         print ('حالت استراحت درنزول ')
                         print ('moving_10 > price >= moving_3 ')
                         print ("{:.0f}%".format(percent_1),':  درصد فاصله مانده تاتنکانسن به کيجونسن برسد')
                         print (moving_3_10 , ' : مقدارفاصله مانده تاميانگين 10به 3برسد')
                         print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')




              if moving_3 > moving_10 :
                    print ('حرکت قيمت صعودي')
                    print ('moving_3 > moving_10')
                    print ("{:.0f}%".format(percent_2),':  درصدفاصله مانده تاميانگين 10به 3برسد')
                    print (moving_3_10 , ' : مقدارفاصله مانده تاميانگين 10به 3برسد')
                    print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')
              else:
                  if moving_10 < today_Final_price <= moving_3 :
                         print ('حالت استراحت درصعود ')
                         print ('moving_10 < price <= moving_3 ')
                         print ("{:.0f}%".format(percent_2),':  درصد فاصله مانده تاتنکانسن به کيجونسن برسد')
                         print (moving_3_10 , ' : مقدارفاصله مانده تاميانگين 10به 3برسد')
                         print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')

                         
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

              if ticker.sta_max == ticker.last_price:
                  print('صف خريدشده')
              else:
                   if ticker.sta_min == ticker.last_price:
                       print ('صف فروش شده')


              if omc < bmi :
                   print ('omc < bmi : به احتمال زيادفردا قيمت بالاترازامروزه')
              else:
                  if omc > bmi :
                      print ('omc > bmi : به احتمال زيادفردا قيمت پايين ترازامروزه')

               #----------------------------------

              print(40*"=",sahame,"For order")
              nimeh_price = ((ticker.high_price + ticker.low_price)/2)
              nimeh_ste = ((ticker.sta_max + ticker.sta_min)/2)


              if nimeh_ste < nimeh_price < ticker.adj_close > ticker.yesterday_price :
                 print ("ميتوني خريد کني فردا قيمت بالاترميره")
              else:
                  if nimeh_ste > nimeh_price > ticker.adj_close < ticker.yesterday_price :
                       print ("قيمت فرداپايين ترمياد براي خريد دست نگهدار")

                       

              if bmi > omc :
                   print ('bmi > omc',': for buy','   = موقعيت خريد')
              else:
                   if bmi < omc :
                       print ('bmi < omc',': for sell','   = موقعيت فروش')

                        
              print ()        
               #===============================================
              closing_prices7 = DF['Close'].iloc[-3:]       # قيمت بسته شدن 3روزگذشته
              closing_prices = DF['Close'].iloc[-10:]      # قيمت بسته شدن 10روز گذشته
              average_price = closing_prices.mean()   #محاسبه ميانگين قيمت بسته شدن 10 روز
              average_prices7 = closing_prices7.mean() #محاسبه ميانگين 3روزه

              print (30*'=','  moving',sahame,)

              if ticker.yesterday_price+400 > ticker.yesterday_price< moving_10 < ticker.adj_close :
                   print (' بعدازريزش 20درصدي که داشته price > moving_10 : موقع خريده')
              else:
                   if ticker.yesterday_price-400 < ticker.yesterday_price> moving_10 > ticker.adj_close :
                       print ('بعدازسعود 20درصدي که داشته price < moving_10 : موقع فروشه')
                       


              if moving_3<moving_10 >ticker.last_price <ticker.yesterday_price:
                   print (' ميانگين ها وقيمت همه نزولي شدن')
              else:
                   if moving_3>moving_10 <ticker.last_price >ticker.yesterday_price:
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


              max_price_b11 = max(DF['High'][-360:]) # max_price day360
              min_price_b12 = min(DF['Low'][-360:])  # min_price day360

                       
              print (30*'=','kanal ',sahame,)

              if ticker.adj_close > moving_10 :
                    print (' price > Em_10 ')
              else:
                  if ticker.adj_close < moving_10 :
                        print (' price < Em_10 ')


              if ticker.adj_close > moving_103 > ticker.yesterday_price:
                   print ('قيمت امروز ميانگين 103رو روبه بالاقطع کرد')
              else:
                   if ticker.adj_close < moving_103 < ticker.yesterday_price:
                       print ('قيمت امروزميانگين 103 رو روبه پايين قطع کرد')
                       


              if moving_103 < ticker.adj_close < ticker.yesterday_price < today_two_price:
                   print ('قيمت روبه پايين وبه سمت ميانگين   103 روزه ميرود')
              else:
                   if moving_103 > ticker.adj_close > ticker.yesterday_price > today_two_price:
                       print ('قيمت روبه بالا وبه سمت ميانگين   103 روزه ميرود')
                       


              if moving_103 < ticker.adj_close > ticker.yesterday_price :
                   print ('قيمت بالاي ميانگين 103 روزه است وداره بالاترميره')
              else:
                   if moving_103 > ticker.adj_close < ticker.yesterday_price :
                       print ('قيمت پايين ميانگين 103روزه است وداره پايين ترميره')
                       


              if ticker.low_price > yesterday_price_min > today_two_price_min6 :
                   print (' کف امروزبالاترازکف 6روزپيش شده ')
              else:
                   if ticker.low_price < yesterday_price_min < today_two_price_min6 :
                       print (' کف امروز پايين ترازکف 6 روزپيش شده')


                       
              if ticker.adj_close<min_price_b4<min_price_b8<min_price_b12:
                    print ("کانال وروند سه ماهه کاملا نزولي ميباشد ")
              else:
                   if ticker.adj_close<min_price_b4<min_price_b8:
                        print ("کانال وروند يک ماه همچنان نزولي ميباشد ")
                               


              if ticker.adj_close>min_price_b4>min_price_b8>min_price_b12:
                    print ("کانال وروند سه ماهه کاملاصعودي ميباشد")
              else:
                   if ticker.adj_close>min_price_b4>min_price_b8:
                        print ("کانال وروند يک ماه همچنال افزايشي ميباشد")



               #========================================================        
              print(40*"=","محاسبات قيمت خريد شمااز ",sahame,)
              
               # چکارن
              if index == 1:
                    p=0
                    s=0
                    v=0
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما') 
                         
                         
               # تليسه
              if index == 2:
                    p=4313
                    s=4251
                    v=5000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما') 
                        
                         
               # غمينو
              if index == 3:
                    p=11181
                    s=10020
                    v=4000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما') 
                         
                         
               # سيمانو
              if index == 4:
                    p=10990
                    s=0
                    v=910
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')
                    
                        
               # وسپه
              if index == 5:
                    p=4215
                    s=4151
                    v=12000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما') 
                        
                        
               # شپاکسا
              if index == 6:
                    p=1935
                    s=0
                    v=11000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')
                         
                        
                         
               # ومعادن
              if index == 7:
                    p=4874
                    s=4844
                    v=47000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')          
                        
                        
               # تاپيکو
              if index == 8:
                    p=0
                    s=17560
                    v=2000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')          
                         
                         
               # دسبحان
              if index == 9:
                    p=0
                    s=11650
                    v=10000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')           
                         
                        
               # کچاد
              if index == 10:
                    p=2847
                    s=3016
                    v=5000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')         
                         

               # شستا
              if index == 11:
                    p=940
                    s=0
                    v=22000
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')           
                         
                         
               # حتوکا
              if index == 12:
                    p=0 
                    s=0
                    v=0
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')           


               # خگستر
              if index == 13:
                    p=0 
                    s=0
                    v=0
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')           


               # فولاد
              if index == 14:
                    p=0 
                    s=0
                    v=0
                    psv=(s*v)-(p*v)
                    if p > 0 :
                         print (p , ': قيمت خريد شمااز',sahame )
                         print (v ,': تعداد سهام موجود')
                    if s > 0 :
                         print (s , ': قيمت فروش شمااز',sahame )
                         print (v ,': تعدادسهام فروخته شده')
                    if p>0 and s>0 :
                         print (s,'شمااين سهم رافروخته ايد به قيمت')
                    if s > p > 0 :
                         print (psv, 'مقدارسودشما')
                    if p > s > 0:
                         print (psv, 'مقدارزيان شما')           


                         
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
                    today_price = (math.ceil(ticker.last_price))     
                    price_kharid= (-0.003 * price)  #کارمزد خريد
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

                         
                    if today_price < stop_loss:
                         loss = str ( pk - pf )
                         loss_float = float(loss)
                         loss_percentage = (loss_float / pk) * 100
                         print (" جمع پرداختي شمابااحتساب قيمت خريدتان :" ,pk)
                         print (" اگرباقيمت امروزبفروشيد ميشه :" , pf)
                         print (" شماضرر ميکنيد به مبلغ :" ,pp)
                         print("The percentage of your loss :% درصدضررشماشده : {} ".format(math.ceil(loss_percentage)))
                         print(20*"-" )

                         
                    if pk > pf :
                         print("Price to limit")
                         print (" قيمت به حد سود20درصد نرسيده!  \n The price has not reached the profit of 20%")                             
                         print (sz ,": اگرامروزبفروشيد مقدارزيان شماميشود")
                         print(20*"-" )

                         
                    if pk < pf :
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
                         print (math.ceil(hs4),' : قيمت سربه سربراي فروش')
                         print (ticker.adj_close,' : قيمت بسته شدن امروز')
                         print (ticker.last_price,' : قيمت آخرين معامله امروز')
                         print ('-'*20)

                         
                    if pk == pf :
                         print (" اگرعلان بفروشيد سربه سرميشيد :" ,today_price )
                         print ('-------')
                         

                         
                         
                    #=================================================           
                         print(40*"=",nam,"Engulfing Calculations")

                         print (today_Open_price,': بازشدن ديروز')
                         print (today_price_max,': بالاترين ديروز')
                         print (today_price_min,': پايين ترين ديروز')
                         print (today_price,': بسته شدن ديروز')
                         print (ticker.open_price,': بازشدن امروز')
                         print (ticker.high_price,': بالاترين امروز')
                         print (ticker.low_price,': پايين ترين امروز')
                         print (ticker.adj_close,': بسته شدن امروز')
                         print (ticker.last_price,' : قيمت آخرين معامله امروز')
                         print ()
                              
                         print (20*'-','Bullish Harami - for buy')
                         #--------------------------------------------

                    if today_Open_price<today_price_max>ticker.high_price>ticker.adj_close>ticker.open_price>today_price>today_price_min :
                        print ('signal buy : هارامي')
                        

                    print (20*'-','Bearish Harami - for sell')

                    if today_Open_price<today_price_max<ticker.high_price>ticker.adj_close<ticker.open_price<today_price>today_price_min :
                        print ('signal sell : هارامي ')
                        

                    print (20*'-','Bullish Engulfing - for buy')

                    if today_Open_price<today_price_max<ticker.high_price>=ticker.adj_close>today_price_max>today_price>ticker.open_price>=ticker.low_price :
                        print ('signal buy : اينگل فينگ')
                        

                    print (20*'-','Bearish Engulfing - for sell')

                    if today_Open_price<today_price_max<ticker.high_price>ticker.adj_close<today_price_max>=today_price<ticker.open_price>ticker.low_price :
                        print ('signal sell : اينگل فينگ')


                    print ()
                    print (30*'-')
                   #--------------------------
                   # Engulfing  ascending صعودي
                   # Bullish Engulfing Support level
                    h1 = ticker.adj_close > ticker.open_price
                    h2 = yesterday_Open_price > yesterday_price
                    h3 = yesterday_price > ticker.open_price
                    h4 = ticker.adj_close > yesterday_Open_price
                    h5 = (ticker.adj_close - ticker.open_price) > 5*(yesterday_Open_price - yesterday_price)

                    h_ascending = h1 and h2 and h3 and h4 and h5
                    

                   # Engulfing  Descending نزولي
                   # Bullish Engulfing Resistance level 
                    h6 = ticker.adj_close < ticker.open_price
                    h7 = yesterday_Open_price < yesterday_price
                    h8 = yesterday_price < ticker.open_price
                    h9 = ticker.adj_close < yesterday_Open_price
                    h10 = (ticker.adj_close - ticker.open_price) < 5*(yesterday_Open_price - yesterday_price)

                    h_Descending = h6 and h7 and h8 and h9 and h10



                    if ticker.adj_close > highest_price_90 :
                        print (' مقاومت سه ماه شکسته شد')

                    if ticker.adj_close < lowest_price_90 :
                        print (' حمايت سه ماه ازدست رفت')
                        

                    if  h_ascending:
                       c = "Engulfing :"
                       print (c , "hemer ascending !  صعودي مناسب خريد" )
                    elif  h_Descending :
                       c = "Engulfing :"
                       print (c , "hemer Descending !  نزولي وقت فروش" )
                    else:
                       c = "hold :"
                       print (c , "not Engulfing !")
                       print ("نمودارهاي قيمت هنوزاينگل فينگي تشکيل ندادند")
                       
                       
                    print ()
                    print ('~'*10)
                    print ('بودن روند False يا True دقت کنيدبه')
                    print (h5 ,': ascending روند صعودي ')
                    print (h10 ,': Descending روند نزولي')
                    print ()
                                  
                   #=======================================================

                    print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')
                   #------------------------------------------------
                    print ('       ','-'*30)

                   # پرسيدن براي خارج شدن ازبرنامه يا نمايش رسم نمودارايچيموکوانجام شود
                    sentence1 = "1 . for Charts ichimoku : "
                    sentence2 = "2 . for Continue the program : "

                   # Print the characters of the first prompt with a delay of 0.2 seconds
                    for char in sentence1:
                       print(char, end="")
                       time.sleep(0.2)
                    print()

                   # Print the characters of the second prompt with a delay of 0.2 seconds
                    for char in sentence2:
                       print(char, end="")
                       time.sleep(0.2)
                    print()

                   # Get the user's input
                    user_input = input("Enter 1 or 2 : ")
                    print ('       ','-'*30)
                   #================================================

                   #بازدن شماره 2 نمودارايچيموکو ونمودارميانگين هارسم ميشود
                   # Check if the user wants to plot the stock price
                    if user_input == "1":
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

                        print ('it was shown ')      
                        #===================================================

                        print(40*"=",nam," EMA_3,10,20 نمايش نمودارقيمت و ")        
                        # EMA_3,10,20 نمايش نمودارقيمت و
                        DF.index = DF['Date']
                        mplf.plot(DF[-200:], type='candle', mav=(50, 10, 20))
                        plt.show()

                        print ('it was shown ')
                        #=================================================
                        #بازدن شماره 2ازبرنامه خارچ ميشويم
                        # Check if the user wants to calculate the volume and channel
                        if user_input == "2":
                             print (' Continue the program ')
                             
                             

                             
          except (TypeError , Exception) as te:
                   print ()
                   print (te)
                   print ('TypeError or Exception : لطفادوباره سعي کنيد')
                   print ()

