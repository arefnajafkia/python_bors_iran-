

# برسي سهام دربورس ايران باپايتون3 فقط باتايپ نام سهم به فارسي
# وبازدن اينتر محاسبات راانجام داده وبه شمانشان ميدهد
# درمرحله دوم نام سهام انتخاب شده ازتي ام سي ونوشته فارسي آن کپي شده
# شماهم ميتوانيد هرسهمي راکه ميخواهيد نام آن رابراي مرحله دوم کپي کنيد
# محاسبات RSI - ichimoku - EMA - Volume - Profit and loss - Charts - Canal - Moving 103 - Candel

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
    user_input = input("Enter 1 ؟ bors_iran برنامه راادامه ميدهيدبا \nEnter 2 ياازبرنامه خارج ميشويد؟ : ")
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
                

                sentence1 = " \\\\\\\\\\\\\\\\ برسي سهام بورس ايران  ///////////////"
                print()
                sentence2 = "Please write the name of the stock you want : "

                for sentence in [sentence1, sentence2]:
                    words = sentence.split()

                    for word in words:
                        for char in word:
                            print(char, end="")
                            time.sleep(0.1)
                        print(" ", end="")
                        
                        

                    print () 
                nam = input ("لطفا نام سهام موردنظرتان رابنويسسد :")

                print ()
                DF = tse.Get_Price_History(stock=nam,
                                            start_date='1401-05-01',
                                            end_date='1402-12-07',
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

                # Get today's price قيمتهاي روزانه 
                today_price_max = DF['High'].iloc[-1] # بالاترين قيمت امروز
                today_price_min = DF['Low'].iloc[-1]  # پايين ترين قيمت امروز
                today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
                today_price = DF['Close'].iloc[-1] # قيمت بسته شدن امروز
                today_Final_price = DF['Final'].iloc[-1] # قيمت آخرين معامله امروز
                today_price_max4 = DF['High'].iloc[-4]    #بالاترين قيمت 4روزپيش
                today_price_min4 = DF['Low'].iloc[-4]      #پايين ترين قيمت 4روزپيش
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
                today_two_price_min6 = DF['Low'].iloc[-6]  # پايين ترين قيمت 6روزقبل

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
                sentence = "RSI محاسبات انجام شده براي "
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.7)
                print(20*"-")
                print(10*" ","rsi value")
                time.sleep(2)
                rsi = ta.momentum.rsi(DF['Close'], length=14)

                rsi_diff = rsi
                print(rsi.tail(3))


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
                         

                print(30*"-")
                sentence = " تمام اطلاعات قيمتي سهام شما  "
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.5)
                    
                    
                print(20*"-")

                #-----------------------------------------------
                time.sleep(3)

                # First row information اطلاعات کامل رديف اول سهم
                nemone = DF.iloc[-1]
                print (nemone)

                #============================================
                time.sleep(3)


                print(30*"-")
                sentence = 'محاسبه 10روزمتوالي ميانگين 103'
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.7)
                print(20*"-")

                time.sleep(3)
                def moving_average(symbol, window_size):


                    moving_averages = DF["Close"].rolling(window_size).mean()

                    return moving_averages

                # Example usage:
                symbol = nam  # Iran Fara Bourse Index
                window_size = 103
                moving_averages = moving_average(symbol, window_size)
                print(moving_averages.tail(10)) 
                print(30*"-") 
                #==============================================
                time.sleep(3)
                sentence = 'لطفا انتخاب کنيد'
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.8)
                print(30*"-")
                print ()

                sentence1 = "رسم نمودارمانگينهاي 10و20و50 و ايچيموکو   =1 : "
                sentence2 = "انجام محاسبات حجم وکانالهاي سهام   =2 : "

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


                # Check if the user wants to plot the stock price
                if user_input == "1":
                    print ("="*15,"Drawing moving average charts" , nam,"="*15)
                    print ()
                #===============================================
                   # EMA_3,10,20 نمايش نمودارقيمت و
                    DF.index = DF['Date']
                    mplf.plot(DF[-200:], type='candle', mav=(50, 10, 20))
                    plt.show()
                   # Calculate the average price for ten days
                    ten_day_average = DF['Close'].rolling(10).mean()
                    today_price_scalar = today_price.item()
                # Check if the user wants to calculate the volume and channel
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
                #======================================================
                elif user_input == "2":
                        print ()
                        sentence = "----------Thanks for the explanation about your stock----------"
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.8)

                print ()
                        
                #=====================================================
                print ('='*30,' candle DOje')
                DOje1= (today_price_max+today_price_min)/2
                DOje2= DOje1 + 20
                DOje3= DOje1 - 20

                if today_Final_price == DOje1 :
                    print (' کندل دوجي شکل گرفته')


                if today_price_max > today_Final_price >= DOje2:
                    print (' کندل دوجي سبزشکل گرفته')
                else:
                    if today_price_min < today_Final_price <= DOje3:
                        print (' کندل دوجي قرمزشکل گرفته')


                if today_Open_price < today_Final_price > DOje1:
                    print (' candle Green')
                else:
                    if today_Open_price > today_Final_price < DOje1:
                        print (' candle Red')


                if today_Open_price < today_Final_price == today_price_max > (today_price_min+150):
                    print (' candle marabozo Green')
                else:
                    if today_Open_price > today_Final_price == today_price_min < (today_price_max-150):
                        print (' candle marabozo Red')

                     
                    
                #=================================================
                time.sleep(5)        
                        
                print(40*"=",nam,"Volume")

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

                #================================================
                print(25*"-")     
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
                print (math.ceil(j2) ,': درصدتفاوت قيمت ديروزبه امروز')
                print (n1 ,' : تفاوت قيمت ديروزبه امروزبه ريا ل')
                print (math.ceil(jnv1) ,': درصدنوسان قيمتي امروز')

                #================================================
                time.sleep(5)
                          
                print(40*"=",nam,"order sell and buy")
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
                #=============================================
                print (20*'-')

                if today_price_max>today_price_max4>today_price_max8>today_price_max12:
                    print ("دوازده روزه سقف جديد بالاترميزنه")
                else:
                    if today_price_min<today_price_min4<today_price_min8<today_price_min12:
                        print ("دوازده روزه کف جديد پايين ترميزنه")


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
                print (today_Volume , 'حجم امروز')
                print (today_Volume_yesterday , 'حجم ديروز')
                print (today_Volume_yesterday2 , 'حجم پريروز')
                print (today_price , 'قيمت امروز')
                print (yesterday_price , 'قيمت ديروز')
                print (today_two_price , 'قيمت پريروز')
                #==================================================
                time.sleep(5)

                print(40*"=",nam,"Moving Average")
                # Calculate the average price for ten days
                ten_day_average = DF['Close'].rolling(10).mean()
                # Calculate the average price for twenty-six days
                twenty_six_day_average = DF['Close'].rolling(26).mean()
                # Get today's 26-day average price
                today_twenty_six_day_average = twenty_six_day_average.iloc[-1]         
                # Compare the average price to today's price      
                          

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


                if today_price > average_prices3 :
                     print (' EM_10 > EM_50 ')
                else:
                     if today_price < average_prices3 :
                          print (' EM_10 < EM_50 ')


                if today_price > average_prices4 :
                     print (' EM_10 > EM_103 ')
                else:
                     if today_price < average_prices4 :
                          print (' EM_10 < EM_103 ')


                if today_price<=today_Final_price > average_price > yesterday_price:
                    print (' price > sma_10 : موقع خريده')
                else:
                    if today_price>=today_Final_price < average_price < yesterday_price:
                        print (' price < sma_10 : موقع فروشه')


                if average_prices7<average_price >today_Final_price <yesterday_price:
                    print (' ميانگين ها وقيمت همه نزولي شدن')
                else:
                    if average_prices7>average_price <today_Final_price >yesterday_price:
                        print (' ميانگين هاوقيمت همه صعودي شدن')

                #==================================================
                time.sleep(5)
                        
                print(40*"=",nam,"One year support and resistance")
                # Engulfing Calculations  محاسبات اينگل فينگ
                today_price = DF['Close'].iloc[-1]   # آخرین قیمت امروز
                today_Open_price = DF['Open'].iloc[-1] # قيمت بازشدن امروز
                yesterday_price = DF['Close'].iloc[-2] # آخرین قیمت دیروز
                yesterday_Open_price = DF['Open'].iloc[-2] # قيمت بازشدن ديروز
                yesterday_two_price = DF['Close'].iloc[-3] # آخرين قيمت پريروز
                moving_3 = (today_price + yesterday_price + yesterday_two_price )/3 # ميانگير3 روز
                
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
                

                if today_price > yesterday_price > today_two_price:
                    print (today_price,' قيمت سه روزه افزايشي ميباشد')
                else:
                    if today_price < yesterday_price < today_two_price:
                        print (today_price,' قيمت سه روزه کاهشي ميباشد')
                        

                if highest_price_360 > today_Final_price > mohasebeh1:
                    print (mohasebeh1,':بالاي ميانه ساليانه هستيم ',highest_price_360,' قيمت ميان اين دودرحرکت است')
                else:
                    if mohasebeh1 > today_Final_price > mohasebeh :
                        print (mohasebeh,':بالاي ميانه ساليانه هستيم ',mohasebeh1,' قيمت ميان اين دودرحرکت است')


                if mohasebeh2 < today_Final_price < mohasebeh:
                    print (mohasebeh2,':پايين ميانه ساليانه هستيم ',mohasebeh,' قيمت ميان اين دودرحرکت است')
                else:
                    if mohasebeh2 > today_Final_price > lowest_price_360 :
                        print (mohasebeh2,':پايين ميانه ساليانه هستيم ',lowest_price_360,' قيمت ميان اين دودرحرکت است')
                        

                if today_Final_price > yesterday_Final_price :
                    print (today_Final_price,' قيمت امروزبه سمت بالادرحرکت است')
                else:
                    if today_Final_price < yesterday_Final_price :
                        print (today_Final_price,' قيمت امروزبه سمت پايين درحرکت است')
                        

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
                if today_price < lowest_price_7 > yesterday_price:
                    print ('قيمت حمايت هفتگي راردکرد')
                else:
                    if today_price > highest_price_7 < yesterday_price:
                        print ('قيمت مقاومت هفتگي رو ردکرد')


                if today_price < lowest_price_30 > yesterday_price:
                    print ('قيمت حمايت ماهيانه راردکرد')
                else:
                    if today_price > highest_price_30 < yesterday_price:
                        print ('قيمت مقاومت ماهيانه راردکرد')


                if today_price < lowest_price_280 > yesterday_price:
                    print ('قيمت حمايت ساليانه راازدست داد')
                else:
                    if today_price > highest_price_280 < yesterday_price:
                        print ('قيمت مقاومت ساليانه راازدست داد')
                        

                if highest_price_280 < highest_price_90 < highest_price_30 and lowest_price_280 > lowest_price_90 > lowest_price_30:
                    print (" کف وسقف يکساله دارن بهم نزديک ميشن")


                if highest_price_30 >  highest_price_90:
                    print ("ومقاومت درسه ماه کلا افزايشي  است  7>30>90")
                else:
                    if highest_price_30 <  highest_price_90:
                        print ("ومقاومت درسه ماه کلاکاهشي شده 7<30<90")
                        

                # فاصله مقاومت هفتگي باساليانه
                resistance= highest_price_7 - highest_price_360
                resistance_1= highest_price_10 - highest_price_360
                

                if resistance < resistance_1 :
                    print (resistance_1 ,": فاصله مقاومت هفتگي باساليانه داره کم ميشه")
                else:
                    if resistance > resistance_1 :
                        print (resistance_1 ,": فاصله مقاومت هفتگي باساليانه داره زيادميشه")
                 

                if highest_price_30 < highest_price_33 :
                    print ("مقاومت يکماه شروع کرده روبه بالابره")
                else:
                    if highest_price_30 > highest_price_33 :
                        print ("مقاومت يکماهه شروع کرده روبه پايين بره")


                if highest_price_7 < highest_price_10:
                    print ("مقاومت هفتگي شروع کرده روبه بالابره")
                else:
                    if highest_price_7 > highest_price_10:
                        print ("مقاومت هفتگي شروع کرده روبه پايين بره")


                if highest_price_30 == highest_price_7 :
                    print (highest_price_7 , ": مقاومت هفتگي باماهيانه برابرشده")
                    

                if lowest_price_30 < lowest_price_33 :
                    print ("حمايت يکماه شروع کرده روبه بالابره")
                else:
                    if lowest_price_30 > lowest_price_33 :
                        print ("حمايت يکماه شروع کرده روبه  پايين بره")


                if lowest_price_7 < lowest_price_10 :
                    print ("حمايت هفتگي شروع کرده روبه بالابره")
                else:
                    if lowest_price_7 > lowest_price_10 :
                        print ("حمايت هفتگي شروع کرده روبه پايين بره")
                        
                   
                # فاصله حمايت هفتگي باساليانه
                support= lowest_price_7 -lowest_price_360
                support_1= lowest_price_10 -lowest_price_360
                

                if support < support_1:
                    print (support_1 ,": فاصله حمايت هفتگي باساليانه داره زيادميشه")
                else:
                    if support > support_1:
                        print (support_1 ,": فاصله حمايت هفتگي باساليانه داره کم ميشه")    


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


                if lowest_price_7 > lowest_price_30 > lowest_price_90:
                    print (" ودرکل حمايت سه ماه افزايشي است 7>30>90 ")
                else:
                    if lowest_price_7 < lowest_price_30 < lowest_price_90:
                        print ("ودرکل حمايت سه ماه کاهشي است  7<30<90 ")


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


                if m_7 <= today_price <= highest_price_7 :
                     print ('قيمت نزديک مقاومت هفتگي ميباشد')
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

                #==================================================
                time.sleep(5)
                    
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



                if today_price > highest_price_90 :
                     print (' مقاومت سه ماه شکسته شد')
                else:
                    if today_price < lowest_price_90 :
                         print (' حمايت سه ماه ازدست رفت')
                     

                if h_ascending and h5:
                    c = "Engulfing :"
                    print (c , "hemer ascending !  صعودي مناسب خريد" )
                elif h_Descending and h10 :
                    c = "Engulfing :"
                    print (c , "hemer Descending !  نزولي وقت فروش" )
                else:
                    c = "hold :"
                    print (c , "not Engulfing !")
                    print ("نمودارهاي قيمت هنوزاينگل فينگي تشکيل ندادند")
                    
                print ('~'*10)
                print ('روند False يا True دقت کنيدبه')
                print (h5,': ascending روند صعودي ')
                print (h10 ,': Descending روند نزولي')
                #=====================================================
                time.sleep(5)

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
                kijon29 = (math.ceil(kij29))

                window_size = 30
                past_30_days_high = DF['High'].rolling(window_size).max().iloc[-1]
                past_30_days_low = DF['Low'].rolling(window_size).min().iloc[-1]
                kij30 = (past_30_days_high + past_30_days_low)/2
                kijon30 = (math.ceil(kij30))

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
                kij52 = (past_52_days_high + past_52_days_low)/2
                komu52_max = (math.ceil(past_52_days_high))
                komu52_min = (math.ceil(past_52_days_low))

                print(f"komu52_max: {komu52_max}  ,  komu52_min: {komu52_min} ")


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
                    if kij30>=kij29>=kij28>=kij27>=kij26 <today_price<yesterday_price> ten8<=ten9<=ten10<=ten11<=ten12 :
                         print ('قيمت بالاي تنکانسن ميباشد وروبه پايين بطرف کيجونسن ميرود')



                if kij30>=kij29>=kij28>=kij27>=kij26>yesterday_price and kij26 < today_price :
                     print ('--- Signal buy :خيلي خيلي مهم : قيمت کيجونسن رو روبه بالا قطع کرد ---')
                else:
                     if kij30<=kij29<=kij28<=kij27<=kij26<yesterday_price and kij26> today_price :
                          print ('--- Signal sell :خيلي خيلي مهم : قيمت کيجونسن رو روبه پايين قطع کرد ---')



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
                   

                # تقاطع تنکانسن وميانگين 103روزه سيگنال خريد يافروش
                if tenken8>average_prices4>=tenken9>tenken10 and today_price>average_prices4>=yesterday_price>=today_two_price:
                     print ('Signal buy : تنکانسن وقيمت ميانگين 103راروبه بالا قطع کردن')
                else:
                     if tenken8<average_prices4<=tenken9<tenken10 and today_price<average_prices4<=yesterday_price<=today_two_price:
                          print ('Signal sell : تنکانسن وقيمت ميانگين 103راروبه پايين قطع کردن')


                if tenken8>average_prices4<kij26>=kij27 and today_price>average_prices4>=yesterday_price>=today_two_price:
                     print ('Signal buy : کيجونسن وتنکانسن وقيمت ميانگين 103راروبه بالاقطع کردن')


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



                if today_Open_price > yesterday_price < yesterday_Open_price > today_price > today_Open_price :
                    print ('_ مهم _ Harami patterns Bullish الگوي برگشتي صعودي (مادرباردار) ')



                if today_price > yesterday_Open_price < yesterday_price > today_Open_price > today_price :
                    print ('_ مهم _ Harami patterns Bearish الگوي برگشتي نزولي (مادرباردار) ')



                if today_Open_price < yesterday_price < yesterday_Open_price < today_price > today_Open_price :
                    print ('_ مهم _ Bullish Engulfing الگوي برگشتي صعودي معتبر')



                if today_price < yesterday_Open_price < yesterday_price <  today_Open_price > today_price :
                   print ('_ مهم _ Bearish Engulfing الگوي برگشتي نزولي معتبر')



                if today_price >= yesterday_price_max < today_price_max and today_Open_price >= yesterday_price_min > today_price_min and yesterday_Open_price > yesterday_price:
                    print ('Bullish Engulfing الگوي برگشتي صعودي معمولادرکف رخميده')



                if today_price <= yesterday_price_min > today_price_min and today_Open_price <= yesterday_price_max < today_price_max and yesterday_Open_price < yesterday_price:
                    print ('Bearish Engulfing الگوي برگشتي نزولي درکف رخميده')



                if yesterday_price_max > today_price_max > piercing_1 < today_price and yesterday_price_min > today_price_min < yesterday_price > today_Open_price <yesterday_Open_price :
                    print ('piercing patterns الگوي برگشتي صعودي پرسينگ (کندل دومي پايين ترازنيمه اولي)')



                if yesterday_price_max < today_price_max > piercing_1 > today_price and yesterday_price_min < today_price_min < yesterday_price < today_Open_price > yesterday_Open_price:
                    print ('Dark Cloud patterns الگوي برگشتي نزولي دارک کلود (کندل دومي بالاترازنيمه اولي)')     



                if today_two_price_max <= today_price_max > yesterday_price_max > today_two_price_min < today_price_min > yesterday_Open_price == yesterday_price_min < yesterday_price and today_price_min > yesterday_price_max:
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
                     
                          
                print ('-'*30)
                #===============================================
                time.sleep(3)

                sentence = 'لطفا انتخاب کنيد'
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.8)
                    
                print ()

                sentence1 = "1 . bmi and omc انجام محاسبات : "
                sentence2 = "محاسبات روند,کف وسقفها  . 2 : "

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

                # Check if the user wants to plot the stock price
                if user_input == "1":
                    print ("="*15,"Drawing moving average charts" , nam,"="*15)
                    print ()
                    #print(20*"-",nam,"bmi محاسبه")
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



                # Check if the user wants to calculate the volume and channel
                elif user_input == "2":
                    print ()
                    print ('-'*10,"Thanks for the explanation about your stock" , nam,'-'*10)
                    print ()

                #================================================================
                time.sleep(3)
                        
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
                    print (" قيمت ازميانگين هفتگي بالاتره")
                    print ('-'*20)
                else:
                    if today_price < week7_mean:
                        print (" قيمت ازميانگين هفتگي پايين تره")
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
                else:
                    if today_price_max < max_price_b1 <= yesterday_price:
                         print (" سقف کانال هفتگي روبه پايين زده شد======>", max_price_b1)
                         print('-'*20)


                if today_price_min > min_price_b2 >= yesterday_price:
                     print ("کف کانال هفتگي روبه بالازده شد =====>", min_price_b2)
                     print('-'*20)
                else:
                    if today_price_min < min_price_b2 <= yesterday_price:
                         print ("کف کانال هفتگي روبه پايين زده شد =====>", min_price_b2)
                         print ('احتمال ريزش تا : ',min_price_b4,)
                         print('-'*20)


                if today_price_max > max_price_b5 >= yesterday_price:
                     print ("سقف کانال ماهيان روبه بالازده شد =====>", max_price_b5)
                     print('-'*20)
                else:
                    if today_price_max < max_price_b5 <= yesterday_price:
                         print ("سقف کانال ماهيانه روبه پايين زده شد =====>", max_price_b5)
                         print('-'*20)


                if today_price_min > min_price_b6 >= yesterday_price:
                     print ("کف کانال ماهيانه روبه بالازده شد =====>", min_price_b6)
                     print('-'*20)
                else:
                    if today_price_min < min_price_b6 <= yesterday_price:
                         print ("کف کانال ماهيانه روبه پايين زده شد =====>", min_price_b6)
                         print('-'*20)


                if today_price_max > Month103_mean < yesterday_price:
                    print ('حداکثرقيمت امروزبالاي ميانگين  103')
                    print ('-'*20)
                else:
                    if today_price_min < Month103_mean > yesterday_price:
                        print ('حداقل قيمت امروززير ميانگين  103')
                        print ('-'*20)

                        
                if Month103_mean < today_price < yesterday_price < today_two_price:
                    print ('قيمت روبه پايين وبه سمت ميانگين   103 روزه ميرود')
                    print ('-'*20)
                else:
                    if Month103_mean > today_price > yesterday_price > today_two_price:
                        print ('قيمت روبه بالا وبه سمت ميانگين   103 روزه ميرود')
                        print ('-'*20)


                if Month103_mean < today_price > yesterday_price > today_two_price:
                    print ('قيمت بالاي ميانگين 103 روزه است وداره بالاترميره')
                    print ('-'*20)
                else:
                    if Month103_mean > today_price < yesterday_price < today_two_price:
                        print ('قيمت پايين ميانگين 103روزه است وداره پايين ترميره')
                        print ('-'*20)


                if today_price_min > yesterday_price_min > today_two_price_min6 :
                    print (' روندروزانه افزايشي شده ')
                else:
                    if today_price_min < yesterday_price_min < today_two_price_min6 :
                        print (' روند روزانه کاهشي شده')


                if today_price_max > Month30 >= yesterday_price:
                    print ('Month60 شروع روند افزايشي بااحتياط خريدکن')
                    print ('-'*20)
                else:
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


                if max_price_b1 > max_price_b3 > max_price_b5 < today_price_max > yesterday_price:
                    print ("کانال وروند يک ماه همچنال افزايشي ميباشد")
                    print ('-'*20)
                else:
                    if min_price_b2 < min_price_b4 < min_price_b6 > today_price_max < yesterday_price:
                        print ("کانال وروند يک ماه همچنان نزولي ميباشد ")
                        print ('-'*20)
                        

                if max_price_b1 < max_price_b3 > max_price_b5 > today_price_max < yesterday_price:
                    print ("روند صعودي يکماه نزولي شد")
                    print ('-'*20)
                else:
                    if min_price_b2 > min_price_b4 < min_price_b6 < today_price_max > yesterday_price:
                        print ("روند نزولي يکماه صعودي شد")
                        print ('-'*20)


                if average_prices4 == average_prices79 == average_prices89 < today_Final_price:
                    print ('قيمت بالاي ميانگين 103 که يکماه فلت شده ميباشد')
                else:
                    if average_prices4 == average_prices79 == average_prices89 > today_Final_price:
                        print ('قيمت پايين ميانگين 103 که يکماه فلت شده ميباشد')


                if average_prices4 == average_prices99 == average_prices94 < today_Final_price:
                    print ('قيمت بالاي ميانگين 103 که 10 روزفلت شده')
                else:
                    if average_prices4 == average_prices99 == average_prices94 > today_Final_price:
                        print ('قيمت پايين ميانگين 103 که 10 روزفلت شده')


                if average_prices4 == average_prices94 == average_prices84 < today_Final_price:
                    print ('قيمت بالاي ميانگين 103 که 15 روزفلت شده')
                else:
                    if average_prices4 == average_prices94 == average_prices84 > today_Final_price:
                        print ('قيمت پايين ميانگين 103 که 15 روزفلت شده')


                time.sleep(3)
                #-------------------------------------------
                # بدست آوردن ميانگين هاي 3و10و20 روزه
                ma3 = (math.ceil(average_prices7))
                ma10 = (math.ceil(average_price))
                ma20 = (math.ceil(average_prices8))

                #for signal Buy or Sell (ma10 , ma3)
                    
                if ma3 > ma10 > ma20 :
                    print (' ascending Hold ميانگين هاعلامت صعودميدن')
                    print ('-'*20)
                else:
                    if ma3 < ma10 < ma20 :
                        print (" signal Sell  ميانگين هاعلامت خروج ميدن")
                        print ('-'*20)
                    
                    
                if today_Volume > today_Volume_yesterday:
                    print (" حجم افزايشي است")
                    print ('-'*20) 
                else:
                    if today_Volume < today_Volume_yesterday:
                        print (" حجم کاهشي است")
                        print ('-'*20)


                if today_price < ma10 :
                    print (' قيمت زيرميانگين 10 روزه')
                else:
                    if today_price > ma10 :
                        print (' قيمت بالاي ميانگين 10 روزه')


                if ma3 < today_Final_price:
                    print (' price > ma3 : قيمت بالاي ميانگين 3 روزه')
                else:
                    if ma3 > today_Final_price:
                        print (' price < ma3 : قيمت زيرميانگين 3 روزه')


                if ma10 > ma3 > today_Final_price < yesterday_price:
                    print (' روند قيمت وميانگين ها نزولي شده')
                else:
                    if ma10 < ma3 < today_Final_price > yesterday_price:
                        print (' روند قيمت وميانگين ها صعودي شده')
                        
                #------------------------------------------------
                time.sleep(3)
                        
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
                    if today_price1 < today_price6 and today_Volume > today_Volume_yesterday :
                        print ('حجم وقيمت 6 روزه داره بالاميره')
                    else:
                        if today_price1 < today_price2 < today_price3 and today_price_min1 < today_price_min2:
                            if today_price1 > today_price6 and today_Volume < today_Volume_yesterday:
                                print ('حجم وقيمت 6 روزه داره پايين ميره')
                                

                if today_price_min9 < today_price_min1 > today_price_min6 :
                    if today_price1 < today_price2 and today_price_min1 < today_price_min2 :
                        print ('بانواسانات انجام شده احتمالا ريزشيه')
                    else:
                        if today_price_min9 > today_price_min1 < today_price_min6:
                            if today_price1 > today_price2 and today_price_min1 > today_price_min2 :
                                print ('بانوسانات انجام شده احتمالا افزايشيه') 

                            
                print (20*'-')
                if today_price1 > today_price6 and today_Volume > today_Volume_yesterday:
                    print ('حجم افزايشي وقيمت امروزاز 6 روزقبل هم بالاتره')
                else:
                    if today_price1 < today_price6 and today_Volume < today_Volume_yesterday:
                        print ('حجم کاهشي وقيمت امروزاز 6 روزقبل هم کمترشده')

                        
                if today_price1 > today_price9 and today_Volume > today_Volume_yesterday:
                    print ('حجم افزايشي وقيمت امروزاز 9 روزقبل هم بالاتررفت')
                else:
                    if today_price1 < today_price9 and today_Volume < today_Volume_yesterday:
                        print ('حجم کاهشي وقيمت امروزاز 9 روزقبل هم پايين تررفت')

                #محاسبه درصدسودوزيان امروزبراي فردا
                zarar1 = (math.ceil((today_price*-3)/100)+today_price)    
                zarar2 = (math.ceil((today_price*-5)/100)+today_price)
                sood1 = (math.ceil((today_price*3)/100)+today_price)
                sood2 = (math.ceil((today_price*5)/100)+today_price)

                if today_price_max2>today_price_max1 and today_Volume > today_Volume_yesterday and today_price2>today_price1:
                    print (" به احتمال قوي فرداقيمت ميريزه")
                    print (  zarar1,'تا3درصد ضررميشه')
                    print (  zarar2,'تا5درصد ضررميشه')

                if today_price_max2<today_price_max1 and today_Volume > today_Volume_yesterday and today_price2<today_price1:
                    print (" به احتمال قوي فردا قيمت ميره بالاتر")
                    print (  sood1 , 'تا3درصدسودميشه')
                    print (  sood2 , 'تا5درصدسودميشه')
                        
                print (40*'=')
                print()
                #===================================================

                time.sleep(5)
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
                                print ("----- اينگل فينگ صعودي شده خريدکن-----")
                                print ("-"*10)


                if today_two_price_max < yesterday_price_max > today_price_max:
                    if today_two_price_min > yesterday_price_min > today_price_min:
                        if today_two_price > yesterday_price > today_price:
                            if highest_price_7 or highest_price_30 or highest_price_90 >= yesterday_price_min:
                                print ("EngulFing Resistance level")
                                print ("----- اينگل فينگ نزولي شده بفروش -----")
                                print ("-"*10)

                #-------------------------

                def main_menu():
                    print ()   


                def plot_Information_repeat_again():
                    # 1 . دوباره تکرار کنيم
                    pass
                                

                #=======================================================
                time.sleep(5)
                                
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
                         "دسبحان","ومعادن","شستا","حتوکا","خگستر","فولاد","شپنا","فملی","فصبا",
                         "فسبزوار","خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور","فپنتا",
                         "شبندر","فارس","غفارس","وبصادر","کچاد","کگل","داتام","نخريس","پاکشو",
                         "درازک","کچاد","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
                         "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
                         "تاصيكو","حكشتي","قهكمت","تكشا","شاروم","مارون","آريا","اپال",
                         "واعتبار","اطلس","شپترو","سمگا","نخريس","سبزوا"]

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
                print(ticker.best_demand_price," : آخرين تقاضاي خريد")
                print(ticker.yesterday_price,' : قیمت دیروز')  
                print(ticker.open_price,' : قيمت بازشدن')   
                print()
                print(ticker.high_price,' : حداکثرقيمت امروز')  
                print(ticker.low_price,' : حداقل قيمت امروز')
                print(ticker.sta_max,' : حداکثر قیمت مجاز')  
                print(ticker.sta_min,' : حداقل قیمت مجاز')
                print()
                print(ticker.count,' : تعداد معاملات ')
                print(ticker.value,' :  ارزش معاملات ')
                print(ticker.volume,' : حجم معاملات امروز ')
                print(today_Volume_yesterday,"حجم ديروز")
                print(today_Volume_yesterday2,"حجم سه روزقبل")
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
                time.sleep(3)

                print(30*"=",sahame,"RSI value")
                DF.rename(columns=RenameDict, inplace=True)
                rsi = ta.momentum.rsi(DF['Close'], length=14)
                rsi_diff = rsi.diff()
                print(rsi.tail(3))

                # واگرايي منفي درفله ها
                if (ticker.last_price<ticker.yesterday_price>today_two_Final_price) > (Month_price<Month_price1>Month_price2): 
                    if (rsi_Month26 < rsi_Month25 > rsi_Month24) < 50<=(rsi_Month < rsi_Month1 > rsi_Month2)>=70:
                        print ('sell down price : واگرايي منفي rsi')
                    else:
                        if (ticker.last_price<ticker.yesterday_price>today_two_Final_price) < (Month_price<Month_price1>Month_price2):
                            if 50<=(rsi_Month26 < rsi_Month25 > rsi_Month24)>=70 > (rsi_Month < rsi_Month1 > rsi_Month2):
                                print ('sell down price : واگرايي منفي rsi')
                                

                #واگرايي مثبت دردره ها
                if (ticker.last_price>ticker.yesterday_price<today_two_Final_price) > (Month_price>Month_price1<Month_price2): 
                    if (rsi_Month26 > rsi_Month25 < rsi_Month24) < 50>=(rsi_Month > rsi_Month1 < rsi_Month2)<=30:
                        print ('Buy top price: واگراي مثبت شده rsi')
                    else:
                        if (ticker.last_price>ticker.yesterday_price<today_two_Final_price) < (Month_price>Month_price1<Month_price2):
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
                     if rsi_diff.iloc[-2] < rsi_diff.iloc[-1] >= 70 :
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

                print ('-'*20)
                #===============================================
                time.sleep(3)

                sentence = 'لطفا انتخاب کنيد'
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.8)
                    
                print ()

                sentence1 = "کانالها وکندلها وحجم امروز . 1 : "
                sentence2 = "2 . گزارش وضعيت حجم وقيمت سهام انتخابي : "

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
                #-------------------
                # Check if the user wants to plot the stock price
                if user_input == "1":
                    print ("="*15,"Performing BMO and OMC calculations" , sahame,"="*15)
                    print ()
                    print(20*"-",sahame,"کانال وکندلهاي امروز")
                              
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
                     if ticker.open_price < ticker.adj_close > DOje1:
                          print (' candle Green')




                if ticker.low_price <= ticker.last_price<=ticker.adj_close <= DOje1<=ticker.open_price:
                     print (' کندل دوجي قرمزشکل گرفته')
                else:
                     if ticker.open_price > ticker.adj_close < DOje1:
                          print (' candle Red')
                        



                if ticker.open_price < ticker.high_price == ticker.adj_close > ticker.low_price :
                    print (' candle marabozo Green معتبرترين')


                         
                if ticker.open_price > ticker.high_price > ticker.adj_close > ticker.low_price :
                     print (' candle marabozo Red معتبرترين')



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



                print('-'*30)
                #======================================================
                # تشخيص بسته شدن قيمت بالا ياپايين قيمت هفتگي است ياخير
                week_min = ticker.adj_close - ticker.min_week
                week_max = ticker.adj_close - ticker.max_week       
                # محاسبه بدست آوردن فاصله بين حداکثروحداقل قيمت به درصد
                Percent =((((ticker.high_price)-(ticker.low_price))/(ticker.high_price))*100)
                Percent_last =((((ticker.last_price)-(ticker.adj_close))/(ticker.last_price))*100)                                                                         
                tik_close_low = ((((ticker.adj_close)-(ticker.low_price))/(ticker.adj_close))*100)
                tik_open_low = ((((ticker.open_price)-(ticker.low_price))/(ticker.open_price))*100)
                tik_ascending = ((math.ceil(tik_close_low))-(math.ceil(tik_open_low)))
                tik_close_high = ((((ticker.high_price)-(ticker.adj_close))/(ticker.high_price))*100)
                tik_open_high = ((((ticker.high_price)-(ticker.open_price))/(ticker.high_price))*100)
                tik_Descending =((math.ceil(tik_close_high))-(math.ceil(tik_open_high)))
                #محاسبه قدرت هرسهامداروتعداد سهام معامله شده توسط يک نفرازسهامداران
                godrat = ticker.count / ticker.volume 
                tedad = ticker.volume / ticker.count


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
                time.sleep(3)
                          
                print(35*"=",nam,"Process Stock trends")
                if ticker.last_price > week7_mean:
                    print (" قيمت ازميانگين هفتگي بالاتره")
                    print (week_max," : فاصله قيمت بابالاترين قيمت هفتگي")
                else:
                    if ticker.last_price < week7_mean:
                        print (" قيمت ازميانگين هفتگي پايين تره")
                        print (week_min," : فاصله قيمت باپايين ترين قيمت هفتگي ") 


                if ticker.yesterday_price > ticker.last_price < ticker.min_week  :
                     print (' قيمت ازپايين ترين قيمت هفتگي پايين تررفت')
                     print ((math.ceil(tedad))," : هرسهامدارامروزاين تعداد سهم فروخته")
                     print ((math.ceil(godrat))," : قدرت سهامداران براي فروش")
                else:
                    if ticker.yesterday_price < ticker.last_price > ticker.max_week  :
                         print (' قيمت ازبالاترين قيمت هفتگي بالاتررفت')
                         print ((math.ceil(tedad))," : هرسهامدارامروزاين تعدادسهام خريده")
                         print ((math.ceil(godrat))," : قدرت سهامدارن براي خريد")
                     

                print(20*"-")
                print (ticker.max_week," : بالاترين قيمت هفتگي ")
                print (ticker.min_week," : پايين ترين قيمت هفتگي ")
                #=====================================================
                print(20*"-")
                # بالاترين وپايين ترين قيمت ساليانه تقسيم بردوشده
                ravand =(ticker.max_year + ticker.min_year)/2
                # بالاترين وپايين ترين قيمت هفتگي تقسيم بردوشده
                ravand_2 =(ticker.max_week + ticker.min_week)/2


                if ticker.yesterday_price > ticker.last_price > ravand :
                    print (" قيمت بالاي نيمه ساليانه است وبه سمت پايين ميره")
                else:
                    if ticker.yesterday_price < ticker.last_price > ravand  :
                        print (" قيمت بالاي نيمه ساليانه است وبه سمت بالاميره")
                    

                if ticker.yesterday_price < ticker.last_price < ravand :
                    print (" قيمت پايين نيمه ساليانه است وبه سمت بالاميره")
                else:
                    if ticker.yesterday_price > ticker.last_price < ravand :
                        print (" قيمت پايين نيمه ساليانه است وبه سمت پايين ميره")
                    

                if ravand < ticker.last_price :
                     print ('***** توجه داشته باشيد روند قيمتي ساليانه صعوديه *****')
                     print ()
                else :
                     if ravand > ticker.last_price :
                          print ('***** توجه داشته باشيد روند قيمتي ساليانه نزوليه *****')
                          print ()


                if ticker.yesterday_price > ticker.last_price > ravand_2 :
                    print (" قيمت بالاي نيمه هفتگي است ولي به سمت پايين ميره")
                else:    
                    if ticker.yesterday_price < ticker.last_price > ravand_2 :
                        print (" قيمت بالاي نيمه هفتگي است وبه سمت بالاميره")


                if ticker.yesterday_price < ticker.last_price < ravand_2 :
                    print (" قيمت پايين نيمه هفتگي است ولي به سمت بالاميره")
                else:   
                    if ticker.yesterday_price > ticker.last_price < ravand_2 :
                        print (" قيمت پايين نيمه هفتگي است وبه سمت پايين ميره")
                          

                if ticker.max_year > ticker.last_price > ticker.min_year :
                    print (" قيمت درمحدوده رنج ساليانه حرکت ميکنه  بالا  و پايين  ميره")


                if ticker.yesterday_price < ticker.max_year < ticker.last_price > ticker.min_year :
                    print ('بالاترين قيمت ساليانه راروبه بالا شکستيم ')
                else:
                    if ticker.max_year > ticker.last_price < ticker.min_year < ticker.yesterday_price :
                        print (" پايين ترين قيمت ساليانه را روبه پايين شکستيم")
                    

                if ticker.max_year == ticker.last_price :
                    print (" خيلي مهم به سقف قيمت ساليانه رسيديم")
                else:
                    if ticker.last_price == ticker.min_year :
                        print (" خيلي مهم به کف قيمت ساليانه رسيديم")
                    
                print(20*"-",nam,"Tik Top or Down")
                print(ticker.max_year,' : حداکثر قیمت بازه سال')
                print(ticker.min_year,' : حداقل قیمت بازه سال')

                               
                if ticker.last_price > ticker.open_price > ticker.yesterday_price > ticker.low_price:
                    print (" امروزتيک صعودي داريم")
                else:
                    if ticker.last_price < ticker.open_price < ticker.yesterday_price < ticker.high_price:           
                        print (" امروزتيک نزولي داريم")


                #-------------------
                # Check if the user wants to calculate the volume and channel
                if user_input == "2":
                    print ()
                    print ('-'*10,"Report on the volume and price of selected stocks" , sahame,'-'*10)
                    print ()
                    
                #===============================================
                time.sleep(3)
                        
                print (35*'=',sahame,'volume',"and order sell and buy")
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

                #===============================================
                time.sleep(3)
                    
                print(35*"=",sahame,"price_max,min,Close  6yers")
                                
                if today_price_min9 < ticker.low_price > today_price_min6 :
                    if ticker.last_price < ticker.yesterday_price and ticker.low_price < today_price_min2 :
                        print ('روبه پايين نوسان داشته احتمالا ريزشيه')
                    else:
                        if today_price_min9 > ticker.low_price < today_price_min6:
                            if ticker.last_price > ticker.yesterday_price and ticker.low_price > today_price_min2 :
                                print ('روبه بالانوسان داشته احتمالا افزايشيه') 

                            
                print (20*'-')
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

                #================================================
                print(20*"-")
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
                #=================================================
                print(40*"=")
                time.sleep(3)
                sentence = 'لطفا انتخاب کنيد'
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.8)
                    
                print ()

                sentence1 = "1 . bmi and omc انجام محاسبات : "
                sentence2 = "2 .  Moving 103 ,محاسبه سودوزيان : "

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
                #-------------------
                # Check if the user wants to plot the stock price
                if user_input == "1":
                    print ("="*15,"Performing BMO and OMC calculations" , sahame,"="*15)
                    print ()

                #===============================================
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
                    if ticker.open_price < bmi < ticker.adj_close:
                        print("امکان داره قيمت پايين تربره")
                    elif ticker.open_price > bmi > ticker.adj_close:
                          print("امکان داره قيمت برگرده")
                    elif bmi == adj_close:
                          print("قيمت درجاميزنه گيجه")
                    elif ticker.adj_close <= bmi < ticker.yesterday_price:
                         print ("احتمال ريزش شديدخارج شو")
                    else:
                         print("مراقب باش معامله نکن")
                    

                    if ticker.yesterday_price > ticker.open_price:
                         print(" قيمت بازشدن امروزکمترازبسته شدن ديروزاست")
                    else:
                        if ticker.yesterday_price < ticker.open_price:
                            print(" قيمت بازشدن امروز بيشترازبسته شدن ديروزشده")
                          

                    if ticker.sta_max == ticker.high_price:
                         print(' صف خريدشده')
                    else:
                        if ticker.sta_min == ticker.low_price:
                             print (' صف فروش شده')

                #-------------------------------------
                             print(40*"=",sahame,"omc محاسبه")
                             # تعريف يک تابع براي محاسبه او ام سي (حدس زدن قيمت بسته شدن)
                             def cmo(open_price, price_min):

                                 omc = (((ticker.high_price *2 )+ price_min)/3)-(ticker.adj_close - yesterday_price)
                     
                                 # برگرداندن او ام سي براي خروجي تابع
                                 return omc

                             # دريافت قيمت بازشدن با پايين ترين قيمت امروز
                             open_price = ticker.open_price
                             price_min = ticker.low_price
                             price_max = ticker.high_price
                             yesterday_price = ticker.yesterday_price # قيمت ديروز
                             #فراخاني تابع او ام سي باقيمت بازشدن وپايين ترين قيمت روز
                             omc = cmo(open_price, price_min)
                             # نمايش اوام سي به کاربر
                             print(f" او ام سي شما {omc:.2f} است ")
                             print ('-'*15)
                             # شروع شرط براي ادامه کار

                             if omc >= price_max :
                                 print ('صبرکن وآماده خريد باش')
                             elif omc < price_min < yesterday_price :
                                  print (' شروع ريزش هفتگي ميتوني بفروشي')
                             elif omc > open_price > yesterday_price :     
                                  print ('ميتوني نگهداري اگرمنفي زدبفروشي')


                             if ticker.last_price == price_max:
                                 print('صف خريدشده')

                     
                             if ticker.last_price == price_min:
                                 print ('صف فروش شده')


                             if omc < bmi :
                                print ('به احتمال زيادفردا قيمت بالاترازامروزه')

                        
                             if omc > bmi :
                                print ('به احتمال زيادفردا قيمت پايين ترازامروزه')



                             if omc > ticker.adj_close > yesterday_price <= ticker.min_week:
                                 print (ticker.max_week,": تا قيمت پايين تريامساوي کمترين قيمت هفتگيه وشروع کرده بره بالا")
                             if omc < ticker.adj_close < yesterday_price <= ticker.max_week:
                                 print(ticker.min_week,": قيمت ازبالاتري قيمت هفتگي پايين ترآمد امکان ريزش تا ")    

                #-------------------

                # Check if the user wants to calculate the volume and channel
                elif user_input == "2":
                    print ()
                    print ('-'*10,"Thanks for the explanation about your stock" ,sahame,'-'*10)
                    print ()
                #======================================================
                time.sleep(3)
                        
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
                print(buy_signals.tail(2))

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
                print(buy_signals.tail(2))
                #=======================================================
                time.sleep(3)

                print (30*'=','  moving',sahame,)

                if ticker.adj_close<=ticker.last_price > ma10 > ticker.yesterday_price:
                    print (' price > sma_10 : موقع خريده')
                else:
                    if ticker.adj_close>=ticker.last_price < ma10 < ticker.yesterday_price:
                        print (' price < sma_10 : موقع فروشه')


                if ma3<ma10 >ticker.last_price <ticker.yesterday_price:
                    print (' ميانگين ها وقيمت همه نزولي شدن')
                else:
                    if ma3>ma10 <ticker.last_price >ticker.yesterday_price:
                        print (' ميانگين هاوقيمت همه صعودي شدن')

                        
                #==========================================================
                time.sleep(3)
                        
                print (30*'=','kanal ',sahame,)

                if ticker.adj_close > average_price :
                     print (' price > Em_10 ')
                else:
                     if ticker.adj_close < average_price :
                         print (' price < Em_10 ')


                if ticker.adj_close > ticker.max_year :
                     print (' مقاومت يک ساله شکسته شد')
                else:
                    if ticker.adj_close < ticker.min_year :
                        print (' حمايت يک ساله شکسته شد')


                if ticker.high_price > Month103_mean < ticker.yesterday_price:
                    print ('حداکثرقيمت امروزبالاي ميانگين  103')
                    print ('-'*20)
                else:
                    if ticker.low_price < Month103_mean > ticker.yesterday_price:
                        print ('حداقل قيمت امروززير ميانگين  103')
                        print ('-'*20)


                if average_prices4 == average_prices79 == average_prices89 < ticker.last_price:
                    print ('قيمت بالاي فلت يکماه ميانگين 103روزه است')
                else:
                    if average_prices4 == average_prices79 == average_prices89 > ticker.last_price:
                        print ('قيمت پايين فلت يکماه ميانگين 103روزه است')


                if average_prices4 == average_prices99 < ticker.last_price:
                    print ('قيمت بالاي فلت 5روزه ميانگين 103 روزه است')
                else:
                    if average_prices4 == average_prices99 > ticker.last_price:
                        print ('قيمت پايين فلت 5 روزه ميانگين 103 روزه است')


                if average_prices4 == average_prices99 == average_prices94 < ticker.last_price:
                    print ('قيمت بالاي فلت ده روزه ميانگين103 روزه است')
                else:
                    if average_prices4 == average_prices99 == average_prices94 > ticker.last_price:
                        print ('قيمت پايين فلت ده روزه ميانگين 103 روزه است')


                if average_prices4 == average_prices94 == average_prices84 < ticker.last_price:
                    print ('قيمت بالاي فلت 15 روزه ميانگين 103 روزه است')
                else:
                    if average_prices4 == average_prices94 == average_prices84 > ticker.last_price:
                        print ('قيمت پايين فلت 15 روزه ميانگين 103 روزه است')


                       
                if Month103_mean < ticker.adj_close < ticker.yesterday_price < today_two_price:
                    print ('قيمت روبه پايين وبه سمت ميانگين   103 روزه ميرود')
                    print ('-'*20)
                else:
                    if Month103_mean > ticker.adj_close > ticker.yesterday_price > today_two_price:
                        print ('قيمت روبه بالا وبه سمت ميانگين   103 روزه ميرود')
                        print ('-'*20)


                if Month103_mean < ticker.last_price > ticker.yesterday_price > today_two_price:
                    print ('قيمت بالاي ميانگين 103 روزه است وداره بالاترميره')
                    print ('-'*20)
                else:
                    if Month103_mean > ticker.last_price < ticker.yesterday_price < today_two_price:
                        print ('قيمت پايين ميانگين 103روزه است وداره پايين ترميره')
                        print ('-'*20)


                if ticker.low_price > yesterday_price_min > today_two_price_min6 :
                    print (' کف امروزبالاترازکف 6روزپيش شده ')
                else:
                    if ticker.low_price < yesterday_price_min < today_two_price_min6 :
                        print (' کف امروز پايين ترازکف 6 روزپيش شده')


                if ticker.high_price > Month30 >= ticker.yesterday_price:
                    print ('Month30 شروع روند افزايشي بااحتياط خريدکن')
                    print ('-'*20)
                else:
                    if ticker.low_price < Month30 <= ticker.yesterday_price:
                        print ('Month30 شروع روند کاهشي مراقب باش ')
                        print ('-'*20)


                if max_price_b1 < max_price_b3 < max_price_b5 < max_price_b7 < max_price_b9 :
                    if ticker.last_price < ticker.yesterday_price:
                        print ("کانال وروند سه ماهه نزولي است")
                        print ('-'*20)
                    else:
                        if min_price_b2 > min_price_b4 > min_price_b6 > min_price_b8 > min_price_b10 :
                            if ticker.last_price > ticker.yesterday_price:
                                print ("کانال وروند سه ماهه صعودي است ")
                                print ('-'*20)


                if max_price_b1 > max_price_b3 > max_price_b5 < ticker.high_price > ticker.yesterday_price:
                    print ("کانال وروند يک ماه همچنال افزايشي ميباشد")
                    print ('-'*20)
                else:
                    if min_price_b2 < min_price_b4 < min_price_b6 > ticker.high_price < ticker.yesterday_price:
                        print ("کانال وروند يک ماه همچنان نزولي ميباشد ")
                        print ('-'*20)
                        

                if max_price_b1 < max_price_b3 > max_price_b5 > ticker.high_price < ticker.yesterday_price:
                    print ("روند صعودي يکماه نزولي شد")
                    print ('-'*20)
                else:
                    if min_price_b2 > min_price_b4 < min_price_b6 < ticker.high_price > ticker.yesterday_price:
                        print ("روند نزولي يکماه صعودي شد")
                        print ('-'*20)


                print ((math.ceil( Month103_mean),' : ميانگين 103'))

                # محاسبه قيمتي مابين حمايت ومقاومت يکساله
                mohasebeh = (highest_price_360 + lowest_price_360)/2
                # محاسبه قيمتي مابين نيمه حمايت ومقاومت بامقاومت يکساله
                mohasebeh1= (mohasebeh + highest_price_360)/2
                # محاسبه قيمتي مابين نيمه حمايت ومقاومت باحمايت يکساله
                mohasebeh2= (mohasebeh + lowest_price_360)/2

                if highest_price_360 > ticker.last_price > mohasebeh1:
                    print (mohasebeh1,':بالاي ميانه ساليانه هستيم ',highest_price_360,' مابين اين دوقيمت')
                else:
                    if mohasebeh1 > ticker.last_price > mohasebeh :
                        print (mohasebeh,':بالاي ميانه ساليانه هستيم ',mohasebeh1,' مابين اين دوقيمت')


                if mohasebeh2 < ticker.last_price < mohasebeh:
                    print (mohasebeh2,':پايين ميانه ساليانه هستيم ',mohasebeh,' مابين اين دوقيمت')
                else:
                    if mohasebeh2 > ticker.last_price > lowest_price_360 :
                        print (mohasebeh2,':پايين ميانه ساليانه هستيم ',lowest_price_360,' مابين اين دوقيمت')
                        

                print (20*'-')
                if ticker.last_price > ticker.yesterday_price :
                    print (ticker.last_price,' قيمت امروزبه سمت بالادرحرکت است')
                else:
                    if ticker.last_price < ticker.yesterday_price :
                        print (ticker.last_price,' قيمت امروزبه سمت پايين درحرکت است')

                #========================================================
                time.sleep(3)
                        
                print(40*"=","محاسبات قيمت خريد شمااز ",sahame,)
                # چکارن
                if index == 1:
                     p=0
                     s=4591
                     v=20000
                     psv=(s*v)-(p*v)
                     if p > 0 :
                          print (p , ': قيمت خريد شمااز',sahame )
                          print (v ,': تعداد سهام موجود')
                     if s > 0 :
                          print (s , ': قيمت فروش شمااز',sahame )
                          print (v ,': تعدادسهام فروخته شده')
                     if p>0 and s>0 :
                          print (s,'شمااين سهم رافروخته ايد به قيمت')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
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
                     if p>0 and s>0 :
                          print (s,'شمااين سهم رافروخته ايد به قيمت')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
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
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
                          print (psv, 'مقدارزيان شما') 
                          
                          
                # وسپه
                if index == 4:
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
                     if p>0 and s>0 :
                          print (s,'شمااين سهم رافروخته ايد به قيمت')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
                          print (psv, 'مقدارزيان شما') 
                         
                         
                # غکورش
                if index == 5:
                     p=9352
                     s=7260
                     v=26000
                     psv=(s*v)-(p*v)
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
                     if p>0 and s>0 :
                          print (s,'شمااين سهم رافروخته ايد به قيمت')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
                          print (psv, 'مقدارزيان شما') 
                         
                         
                # شپاکسا
                if index == 6:
                     p=1844
                     s=0
                     v=5000
                     psv=(s*v)-(p*v)
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
                     if p>0 and s>0 :
                          print (s,'شمااين سهم رافروخته ايد به قيمت')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
                          print (psv, 'مقدارزيان شما') 
                         
                          
                # ثبهساز
                if index == 7:
                     p=3207
                     s=3324
                     v=30000
                     psv=(s*v)-(p*v)
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
                     if p>0 and s>0 :
                          print (s,'شمااين سهم رافروخته ايد به قيمت')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
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
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
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
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
                          print (psv, 'مقدارزيان شما')           
                          
                          
                # ومعادن
                if index == 10:
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
                     if 4066>ticker.adj_close>2526:
                          print ("مابين حمايت 2526 ومقاومت 4066 هستيم درميانه 3198 روداريم") 
                     if 5610>ticker.adj_close>4066:
                          print ("مابين حمايت  4066 ومقاومت 5610 هستيم درميانه  4763 روداريم")
                     if 7184>ticker.adj_close>5610:
                          print ("مابين حمايت 5610 ومقاومت 7184 هستيم درميانه  6343  روداريم")
                     if p>0 and s>0 :
                          print (s,'شمااين سهم رافروخته ايد به قيمت')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
                          print (psv, 'مقدارزيان شما')           
                          

                # شستا
                if index == 11:
                     p=1127
                     s=0
                     v=8000
                     psv=(s*v)-(p*v)
                     if p > 0 :
                          print (p , ': قيمت خريد شمااز',sahame )
                          print (v ,': تعداد سهام موجود')
                     if s > 0 :
                          print (s , ': قيمت فروش شمااز',sahame )
                          print (v ,': تعدادسهام فروخته شده')
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
                          print (psv, 'مقدارزيان شما')           
                          
                          
                # حتوکا
                if index == 12:
                     p=0 
                     s=3400
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
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
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
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
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
                     if p < s :
                          print (psv, 'مقدارسودشما')
                     if p > s :
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
                          if pk > (today_price * vol) :
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
                          print (' : تعيين حدسودوزيان بااحتساب قيمت خريد شمااز ',sahame)
                          print (hs1,'حدسود20درصد')
                          print (hs2,'حدسود10درصد')
                          print (hs3,'حدسود5درصد') 
                          print (hz,'حدضرر 3درصد')
                          print (hs4,'قيمت سربه سربراي فروش')
                          print (ticker.adj_close,' : قيمت بسته شدن امروز')
                          print (ticker.last_price,' : قيمت آخرين معامله امروز')
                          print ('-'*20)

                          
                     if pk == pf :
                          print (" اگرعلان بفروشيد سربه سرميشيد :" ,today_price )
                          print ('-------')

                #=====================================================
                time.sleep(3)
                          
                print ('='*10,sahame,'fibonacci')
                #کد برنامه نویسی در پایتون برای سری فیبوناچی

                def fibonacci(n):
                    fib_series = [ticker.adj_close, ticker.yesterday_price]
                    while len(fib_series) < n:
                        fib_series.append(fib_series[-1] + fib_series[-2])
                    return fib_series
                num_terms = 7
                #num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
                print(fibonacci(num_terms))

                print ('-'*10)
                #=====================================================      

                #هرموقع باريش هارامي صعودي يانزولي صورت بگيرد پرينت ميکند درغيراين
                #صورت چيزي نشان نميدهد 
                # Bullish Harami EngulFing support or Resistance level

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


                #==================================================
                time.sleep(3)
                                
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
                print (h5, ' :ascending   روند صعودي ')
                print (h10 , ' :Descending   روند نزولي')
                               
                #=======================================================
                time.sleep(3)

                print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')
                #------------------------------------------------
                print ()
                time.sleep(3)
                sentence = 'لطفا انتخاب کنيد'
                words = sentence.split()

                for word in words:
                    print(word, end=" ")
                    time.sleep(0.8)
                    
                print ()
                print ("1 . رسم نمودارايچيموکو ")
                print ()
                print ("2 . ياادامه برنامه ازاول")
                def main_menu():
                    print ()   


                def plot_Information_repeat_again():
                    # 1 . رسم نمودارايچيموکو
                    
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

                              
                def Or_leave_the_program():
                    # 2 . ياازبرنامه خارج شيم
                    exit ()
                    pass



                while True:
                    main_menu()
                    user_input = input("Enter 1 or 2 : ")

                    if user_input == "1":
                        plot_Information_repeat_again()
                        

                        
                        
                    if user_input == "2":
                        Or_leave_the_program()
                        


          except (TypeError , Exception) as te:
               print ()
               print (te)
               print ('TypeError or Exception : لطفادوباره سعي کنيد')
               print ()                        
        



