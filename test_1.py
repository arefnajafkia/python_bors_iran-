     
# برسي سهام دربورس ايران باپايتون3 فقط باتايپ نام سهم به فارسي
# محاسبات ايچيمکو راانجام ميدهد ودرمرحله دوم
# فقط بازدن شماره کنارسهم محاسبات راانجام داده ونتيجه رااغلام مي کند
# RSI-ichimoku-EMA-Volume-Profit and loss-Charts-Canal-Moving 103-Candel

def main_menu():
    print(10*"-" , 'لطفا انتخاب کنيد',10*"-")
    print ()

def open_testnew_py():
    # 1 .  test.py محاسبات سهام دربورس ايران بافايل
    pass

def for_exit_tsenew_py():
    # 2 . براي خارج شدن ازبرنامه
    pass


while True:
    main_menu()
    print ('-'*10)
    user_input = input("Enter 1 ؟ test_1.py برنامه راادامه ميدهيدبا \nEnter 2 ياازبرنامه خارج ميشويد؟ : ")
    print ('-'*10)
    print ()

    if user_input == "2":
        for_exit_tsenew_py()
        print ('شماازبرنامه خارج شديد')

        exit()
        

    elif user_input == "1":
          open_testnew_py()
          
          
          try:


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
                                           end_date='1403-06-01',
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
                    print (' :اگرفاصله تنکانسن با کيجونسن از 3- بيشترباشد , احتمال برگشت روندميباشد')
                    print (percent_1)
               else:
                    if kijon28 < tenken12 < today_Final_price :
                         print ('روند صعوديه')
                         print ('kijon26 < tenken8 < price')
                         print ("{:.0f}%".format(percent_2),':  درصدفاصله مانده تاکيجونسن به تنکانسن برسد')
                         print (ten8_kij26 , ' : مقدارفاصله مانده تاکيجونسن به تنکانسن برسد')
                         print (price_ten8 , ' : فاصله مابين تنکانسن وقيمت از50 کمترباشد')
                         print (' :اگرفاصله تنکانسن با کيجونسن از 3+ بيشترشد , احتمال برگشت روندميباشد')
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

               #-------------------------------------
                         

               if today_Final_price < moving_3 <=ten8<ten9 < moving_10 < kij26 :
                    print ('قيمت زيرميانگين 3و10روزه وهمچنين تنکانسن وکيجونسن ميباشد وشروع ريزش ادامه داراست')
               else:
                    if today_Final_price < moving_3 <=ten8<ten9 :
                         print ('قيمت زيرميانگين 3روزه وتنکانسن ميباشد وشروع ريزش بشرط حمايت تنکانسن')


               if today_Final_price > moving_3 >=ten8<ten9 > moving_10 > kij26 :
                    print ('قيمت بالاي ميانگين 3و10روزه وهمچنين تنکانسن وکيجونسن ميباشدوشروع روند صعودي ادامه داراست')
               else:
                    if today_Final_price > moving_3 >=ten8>ten9 :
                         print ('قيمت بالاي ميانگين 3روزه وتنکانسن ميباشد وشروع روندصعودي بشرط حمايت تنکانسن')
                         

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


               print ()
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
               piercing_1= (yesterday_Open_price+yesterday_price)/2



               if yesterday_price_max > yesterday_Open_price > yesterday_price > yesterday_price_min and today_price == today_price_max > today_Open_price > today_price_min :
                    print ('Harami patterns Bullish الگوي برگشتي صعودي (مادرباردار) ')



               if yesterday_price_max > yesterday_price > yesterday_Open_price > yesterday_price_min and today_price == today_price_min < today_Open_price < today_price_max :
                    print ('Harami patterns Bearish الگوي برگشتي نزولي (مادرباردار) ')



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
               #====================================================
               # برسي سهام فقط بازدن شماره کنارسهم قابل برسي است
               namad =["چکارن","تلیسه","غمینو","وسپه","غکورش","شپاکسا","ثبهساز","تاپیکو",
                       "دسبحان","ومعادن","فصبا","حتوکا","خگستر","فولاد","شپنا","فملی","شستا",
                       "فسبزوار","خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور","فپنتا",
                       "شبندر","فارس","غفارس","وبصادر","کچاد","کگل","داتام","نخريس","پاکشو",
                       "درازک","كپارس","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
                       "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
                       "تاصيكو","نخريس","قهكمت","تكشا","شاروم","مارون","آريا","اپال"]


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
               print(ticker.adj_close,' :  adj cloes ')  
               print(ticker.yesterday_price,' : yesterday price ')
               print(ticker.open_price,' : open price')   
               print()
               print(ticker.high_price,' :  high price')  
               print(ticker.low_price,' :  Low price')
               print(math.ceil(ticker.sta_max),' :  ste max ')  
               print(math.ceil(ticker.sta_min),' :  sta min')
               print()
               print(today_Open_price,': yesterday open price')
               print(today_price_max,': yesterday price max')
               print(today_price_min,': yesterday price min')
               print(today_price,': yesterday price')
               print()
               print(ticker.volume,' :  volume ')
               print(ticker.month_average_volume,' :  month average volume')
               print()


               print('-*'*20)
               if ticker.adj_close > ticker.max_year :
                    print (' break ticker max year')
               else:
                    if ticker.adj_close < ticker.max_year :
                         print (' down ticker max year')



               if (ticker.min_week)>(ticker.adj_close):
                    print(' ticker min week > ticker adj close ')
               else:
                    if (ticker.min_week)<(ticker.adj_close):
                         print(' ticker min week < ticker adj close ')



               if (ticker.max_week)<(ticker.adj_close):
                    print(' ticker max week < ticker adj close')
               else:
                    if (ticker.max_week)>(ticker.adj_close):
                          print(' ticker max week > ticker adj close')



               if ticker.adj_close > today_price :
                    print (' price > today_price')
               else:
                    if ticker.adj_close < today_price :
                         print (' price < today_price')
                           

                    
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



               #=====================================================
               print ('='*30,' hammer candle and Doji ')
               DOje1= (ticker.high_price+ticker.low_price)/2


               if ticker.last_price == DOje1 :
                   print (' کندل دوجي شکل گرفته')
               else:
                    if ticker.high_price >ticker.adj_close<= DOje1 >ticker.low_price:
                        print (' معتبرترین کندل دوجي شکل گرفته')
                        


               if ticker.high_price >= ticker.last_price>=ticker.adj_close >= DOje1>=ticker.open_price:
                   print (' کندل دوجي سبزشکل گرفته')
               else:
                    if ticker.low_price <= ticker.last_price<=ticker.adj_close <= DOje1<=ticker.open_price:
                         print (' کندل دوجي قرمزشکل گرفته')




               if ticker.open_price < ticker.adj_close > DOje1:
                    print (' candle Green')
               else:
                    if ticker.open_price > ticker.adj_close < DOje1:
                         print (' candle Red')
                       



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


               print ()
               #================================================
               print(25*"-")     
               if ticker.adj_close > ticker.yesterday_price:
                    print (' قيمت امروزبالاترازديروزه ')
               else :
                    if ticker.adj_close < ticker.yesterday_price:
                         print (' قيمت امروزپايين ترازديروزه ')


               if ticker.volume > today_Volume_yesterday and ticker.adj_close < ticker.yesterday_price :
                   print ("sell : قيمت داره ميادپايين حجم ميره بالابفروش")
               else:
                   if ticker.volume < today_Volume_yesterday and ticker.adj_close > ticker.yesterday_price :
                       print ("sell : حجم داره ميادپايين قيمت ميره بالا بفروش")


               if ticker.volume > today_Volume_yesterday and ticker.adj_close > ticker.yesterday_price :
                   print ("buy : حجم وقيمت هردوميره بالا يااول حمايت بخرياباشکست مقاومت بخر")
               else:
                   if ticker.volume < today_Volume_yesterday and ticker.adj_close < ticker.yesterday_price :
                       print ("buy : حجم وقيمت هردوداره ميادپايين نزديک حمايت بخر")
                       

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
                        
               #=================================================           
               print(40*"=",nam,"Engulfing Calculations")
               print ()
                      
               print (20*'-','Bullish Harami - for buy')

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
               #----------------------------------------------
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

               #=====================================================          
               print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')

          except (TypeError , Exception) as te:
               print ()
               print (te)
               print ('TypeError or Exception : لطفادوباره سعي کنيد')
               print ()               

