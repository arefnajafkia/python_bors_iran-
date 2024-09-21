  
# برسی روند سهام باتایپ نام سهم
# محاسبات max - min - year - month - week and mean price

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
    user_input = input("Enter 1 ؟ bors1_iran برنامه راادامه ميدهيدبا \nEnter 2 ياازبرنامه خارج ميشويد؟ : ")
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


                print ("="*15,"برسي سهام در بورس ايران","="*15)
                print ()

                nam = input ("Hello,Please write the name of the stock you want : \n لطفا نام سهام موردنظرتان رابنويسسد :")

                DF = tse.Get_Price_History(stock=nam,
                                             start_date='1401-05-01',
                                             end_date='1402-12-20',
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

                # حجم هفتگي وروزانه وماهيانه Volume
                Volume_week = DF['Volume'].iloc[-5] # حجم هفتگي
                Volume_Month = DF['Volume'].iloc[-26] # حجم ماهيانهBase volume
                today_Volume = DF['Volume'].iloc[-1] # حجم امروز
                today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز
                today_Volume_yesterday2 = DF['Volume'].iloc[-3] # حجم سه روزقبل
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

                if today_Final_price > Month103_mean :
                    print ('قيمت بالاي ميانگين  103')
                    print ('-'*20)
                else:
                    if today_Final_price < Month103_mean :
                        print ('قيمت پايين ميانگين  103')
                        print ('-'*20)


                if  yesterday_Final_price < today_Final_price > Month103_mean :
                    print ("قيمت بالاي ميانگين  103 وروبه بالاميره")
                else:
                    if yesterday_price > today_price < Month103_mean :
                        print ("قيمت پايين ميانگين  103 وروبه پايين ميره")


                if  yesterday_Final_price > today_Final_price > Month103_mean :
                    print ("قيمت بالاي ميانگين  103 وروبه پايين ميره")
                else:
                    if yesterday_price < today_price < Month103_mean :
                        print ("قيمت پايين ميانگين  103 وروبه بالاميره")


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
                     

                if today_price_max > max_price_b3 >= yesterday_price:
                     print ("سقف کانال دوهفتگي روبه بالازده شد =====>", max_price_b3)
                     print('-'*20)
                else:
                    if today_price_max < max_price_b3 <= yesterday_price:
                         print ("سقف کانال دوهفتگي روبه پايين زده شد =====>", max_price_b3)
                         print('-'*20)
                         

                if today_price_min > min_price_b4 >= yesterday_price:
                     print ("کف کانال دوهفتگي روبه بالازده شد =====>", min_price_b4)
                     print('-'*20)
                else:
                    if today_price_min < min_price_b4 <= yesterday_price:
                         print ("کف کانال دوهفتگي روبه پايين زده شد =====>", min_price_b4)
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
                    if Month103_mean < today_price < yesterday_price < today_two_price:
                         print ('قيمت بالاي ميانگين 103روزه است وداره پايين ميره')
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
                    else:
                        if min_price_b2 > min_price_b4 > min_price_b6 > min_price_b8 > min_price_b10 :
                            if today_price > yesterday_price:
                                print ("کانال وروند سه ماهه صعودي است ")
                                print ('-'*20)
                 

                if max_price_b1 > max_price_b3 > max_price_b5 and today_price_max > yesterday_price:
                    print ("کانال وروند يک ماه همچنال افزايشي ميباشد")
                    print ('-'*20)
                else:
                    if min_price_b2 < min_price_b4 < min_price_b6 and today_price_max < yesterday_price:
                        print ("کانال وروند يک ماه همچنان نزولي ميباشد ")
                        print ('-'*20)
                        

                if max_price_b1 < max_price_b3 > max_price_b5 and today_price_max < yesterday_price:
                    print ("روند صعودي يکماه نزولي شد")
                    print ('-'*20)
                else:
                    if min_price_b2 > min_price_b4 < min_price_b6 and today_price_max > yesterday_price:
                        print ("روند نزولي يکماه صعودي شد")
                        print ('-'*20)
                 
                #=================================================
                time.sleep(3)
                        
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


                if today_price > 4*(average_Volume_week):
                    print (" حجم امروز 4برابر حجم هفتگي ميباشد")


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

                #================================================
                print(25*"-")     
                if today_price > yesterday_price:
                     print (' قيمت امروزبالاترازديروزه ')
                else :
                     if today_price < yesterday_price:
                          print (' قيمت امروزپايين ترازديروزه ')

                #================================================
                time.sleep(3)
                          
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

                #=======================================================
                time.sleep(3)
                          
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
                if today_Open_price < bmi > today_price:
                    print("امکان داره قيمت پايين تربره")
                elif today_Open_price > bmi < today_price:
                    print("امکان داره قيمت برگرده")
                elif bmi == adj_close:
                    print("قيمت درجاميزنه گيجه")
                elif today_price <= bmi < yesterday_price:
                    print ("احتمال ريزش شديدخارج شو")
                else:
                    print("مراقب باش معامله نکن")
                    
                if yesterday_price > today_Open_price:
                    print(" قيمت بازشدن امروزکمترازبسته شدن ديروزاست")

                if yesterday_price < today_Open_price:
                    print(" قيمت بازشدن امروز بيشترازبسته شدن ديروزشده")
                          

                if today_price_max == today_Final_price:
                    print(' صف خريدشده')

                if today_price_min == today_Final_price:
                    print (' صف فروش شده')

                #-------------------------------------
                # محاسبه بالاترين وپايين ترين قيمت يک هفته پيش    
                max_price_b1 = max(DF['High'][-7:]) # max_price day7
                min_price_b2 = min(DF['Low'][-7:])  # min_price day7
                print(40*"=",nam,"omc محاسبه")
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

                if omc > today_price :
                    print ('قيمت بسته شدن فردا بيشترازبسته شدن امروزميشه')

                if omc < today_price :
                    print ('قيمت بسته شدن فرداکمترازبسته شدن امروزميشه')
                     
                if omc >= today_price_max:
                     print (' صبرکن وآماده خريدباش')
                elif omc < today_price_min < yesterday_price :
                     print (' شروع ريزش هفتگي ميتوني بفروشي')
                elif omc > today_Open_price > yesterday_price:
                     print ('ميتوني نگهداري اگرمنفي زدبفروشي')

                     
                if today_Final_price == today_price_max:
                     print('صف خريدشده')
                     
                if today_Final_price == today_price_min:
                     print ('صف فروش شده')

                if omc > today_price > yesterday_price <= min_price_b2:
                    print (max_price_b1,": تا قيمت پايين تريامساوي کمترين قيمت هفتگيه وشروع کرده بره بالا")
                if omc < today_price < yesterday_price <= max_price_b1:
                    print(min_price_b2,": قيمت ازبالاتري قيمت هفتگي پايين ترآمد امکان ريزش تا ")
                     
                #------------------------------------------------
                time.sleep(3)
                    
                print(40*"=",nam,"signal buy and sell")

                ma3 = (math.ceil(average_prices7))
                ma10 = (math.ceil(average_price))
                #ma4 = (math.ceil(average_prices9))
                #ma11 = (math.ceil(average_price10))
                ma20 = (math.ceil(average_prices8))

                if today_price < ma10 :
                    print ('قيمت زير ميانگين 10روزميباشد')
                else:
                    if today_price > ma10 :
                        print ('قيمت بالاي ميانگين 10 روزه ميباشد')


                if ma3 < today_Final_price:
                    print ('ma3<price : قيمت بالاترميره')
                else:
                    if ma3 > today_Final_price:
                        print ('ma3>price : قيمت پايين ترميره')

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

                if today_price_max2>today_price_max1 and today_price_min2>today_price_min1 and today_price2>today_price1:
                    print (" به احتمال قوي فرداقيمت ميريزه")
                    print (  zarar1,'تا3درصد ضررميشه')
                    print (  zarar2,'تا5درصد ضررميشه')

                if today_price_max2<today_price_max1 and today_price_min2<today_price_min1 and today_price2<today_price1:
                    print (" به احتمال قوي فردا قيمت ميره بالاتر")
                    print (  sood1 , 'تا3درصدسودميشه')
                    print (  sood2 , 'تا5درصدسودميشه')
                    

                #==================================================
                time.sleep(3)
                    
                print(40*"=",nam,"One year support and resistance")
                # محاسبات مقاومت هفتگي تاساليانه 
                highest_price_7 = max(DF['High'][-7:])    #محاسبه مقاومت هفتگي
                highest_price_8 = max(DF['High'][-8:])
                highest_price_30 = max(DF['High'][-30:])
                highest_price_31 = max(DF['High'][-31:])
                highest_price_90 = max(DF['High'][-90:])
                highest_price_180 = max(DF['High'][-180:])
                highest_price_280 = max(DF['High'][-280:])
                highest_price_360 = max(DF['High'][-360:])    #محاسبه مقاومت ساليانه
                #------------------------
                # محاسبات حمايت هفتگي تاساليانه
                lowest_price_7 = min(DF['Low'][-7:])         #محاسبه حمايت هفتگي
                lowest_price_8 = min(DF['Low'][-8:])
                lowest_price_30 = min(DF['Low'][-30:])
                lowest_price_31 = min(DF['Low'][-31:])
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
                #================================

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
                time.sleep(3)
                    
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


                #=======================================================
                time.sleep(3)

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
                         "درازک","كپارس","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
                         "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
                         "تاصيكو","حكشتي","قهكمت","تكشا","شاروم","مارون","آريا","اپال",
                         "واعتبار","اطلس","شپترو","سمگا","نخريس"]

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
                print(ticker.month_average_volume,' : میانگین حجم ماه')
                print()
                time.sleep(3)

                print(30*"=",sahame,"RSI value")
                DF.rename(columns=RenameDict, inplace=True)
                rsi = ta.momentum.rsi(DF['Close'], length=14)
                rsi_diff = rsi.diff()
                print(rsi.tail(3))


                if rsi_diff.iloc[-1] >= 50 and rsi_diff.iloc[-2] < rsi_diff.iloc[-1]:      
                     print(" Rsi : ورود به بالاي 50 ")
                else:
                     if rsi_diff.iloc[-1] <= 50 and rsi_diff.iloc[-2] > rsi_diff.iloc[-1]:      
                          print(" Rsi : ريزش به زير50 ")
                                

                if rsi_diff.iloc[-1] <= 30 and rsi_diff.iloc[-2] > rsi_diff.iloc[-1]:      
                     print(" Rsi : ورود به منطقه اشباع فروش ")
                else:
                     if rsi_diff.iloc[-1] >= 70 and rsi_diff.iloc[-2] < rsi_diff.iloc[-1]:
                          print(" Rsi : ورود به منطقه اشباع خريد")
                                

                if rsi_diff.iloc[-1] >= 30 and rsi_diff.iloc[-2] < rsi_diff.iloc[-1]:      
                     print(" Rsi : خروج ازمنطقه اشباع فروش ")
                else:
                     if rsi_diff.iloc[-1] <= 70 and rsi_diff.iloc[-2] > rsi_diff.iloc[-1]:
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

                #=====================================================
                time.sleep(3)
                     
                print ('='*30,' candel DOje')
                DOje1= (ticker.high_price+ticker.low_price)/2
                DOje2= DOje1 + 20
                DOje3= DOje1 - 20

                if ticker.last_price == DOje1 :
                    print (' کندل دوجي شکل گرفته')


                if ticker.high_price > ticker.last_price >= DOje2:
                    print (' کندل دوجي سبزشکل گرفته')
                else:
                    if ticker.low_price < ticker.last_price <= DOje3:
                        print (' کندل دوجي قرمزشکل گرفته')
                        

                if ticker.open_price < ticker.last_price > DOje1:
                    print (' candle Green')
                else:
                    if ticker.open_price > ticker.last_price < DOje1:
                        print (' candle Red')


                if ticker.open_price < ticker.last_price == ticker.high_price > (ticker.low_price+150):
                    print (' candle marabozo Green')
                else:
                    if ticker.open_price > ticker.last_price == ticker.low_price < (ticker.high_price-150):
                        print (' candle marabozo Red')


                #============================================
                print ('='*30,' hammer candle and Doji ')


                if ticker.high_price > ticker.adj_close > ticker.open_price >= ticker.low_price :
                     print ('چکش سبز برگشتي درروند نزولي ')
                     print (' H > C > O >= L ')



                if ticker.high_price > ticker.open_price > ticker.adj_close >= ticker.low_price :
                     print ('چکش قرمزبرگشتي درروند صعودي ')
                     print (' H > O > C >= L ')



                if ticker.open_price <= ticker.high_price > ticker.adj_close > ticker.low_price :
                     print ('دوجي قرمزشد نزولي است ياادامه دهنده نزول واگرسبزشد صعودي ياادامه دهنده صعود')
                     print (' O <= H > C > L ')
                     


                if ticker.open_price > ticker.high_price > ticker.adj_close > ticker.low_price :
                     print ('مارابوزوي قرمز نزولي')
                     print (' O > H > C > L ')



                if ticker.open_price < ticker.high_price == ticker.adj_close > ticker.low_price :
                     print ('مارابوزوي سبز صعودي ')
                     print (' O < H = C > L ')
                     
                    
                #======================================================
                print('-'*30)
                week_min = ticker.adj_close - ticker.min_week
                week_max = ticker.adj_close - ticker.max_week
                if ticker.adj_close > ticker.max_year :
                     print (' مقاومت يک ساله شکسته شد')


                if (ticker.min_week)>(ticker.adj_close):
                     print(' قيمت امروز پايين ترازحداقل قيمت هفتگي است')
                     print (week_min," :فاصله قيمت امروزباهفتگي")
                else:
                     if (ticker.min_week)<(ticker.adj_close):
                          print(' قيمت امروز بالاترازحداقل قيمت هفتگي است')
                          print (week_min," :فاصله قيمت امروزباهفتگي")
                          

                if (ticker.max_week)<(ticker.adj_close):
                     print(' قيمت امروزبالاترازحداکثرقيمت هفتگي است')
                     print (week_max," :فاصله قيمت امروزباهفتگي")
                     
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
                if ticker.yesterday_price > ticker.low_price < ticker.min_week  :
                     print (' روند قيمتي هفتگي نزولي شد')
                     print ((math.ceil(tedad))," : هرسهامدارامروزاين تعداد سهم فروخته")
                     print ((math.ceil(godrat))," : قدرت سهامداران براي فروش")


                if ticker.yesterday_price < ticker.low_price > ticker.min_week  :
                     print (' روند قيمتي هفتگي صعودي شد')
                     print ((math.ceil(tedad))," : هرسهامدارامروزاين تعدادسهام خريده")
                     print ((math.ceil(godrat))," : قدرت سهامدارن براي خريد")
                     

                print(20*"-")
                print (ticker.max_week," : بالاترين قيمت هفتگي ")
                print (ticker.min_week," : پايين ترين قيمت هفتگي ")
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
                else:    
                    if ticker.adj_close > ravand_2 and ticker.yesterday_price < ticker.adj_close :
                        print (" قيمت بالاي نيمه هفتگي است وبه سمت بالاميره")


                if ticker.adj_close < ravand_2 and ticker.yesterday_price < ticker.adj_close :
                    print (" قيمت پايين نيمه هفتگي است ولي به سمت بالاميره")
                else:   
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


                #===============================================
                time.sleep(3)
                    
                print (40*'=',sahame,'volume',"and order sell and buy")
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

                #================================================
                print(25*"-")     
                if ticker.adj_close > ticker.yesterday_price:
                     print (' قيمت امروزبالاترازديروزه ')
                else :
                     if ticker.adj_close < ticker.yesterday_price:
                          print (' قيمت امروزپايين ترازديروزه ')

                #================================================
                print(20*"-")
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
                #=================================================
                time.sleep(3)
                        
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


                if ticker.yesterday_price < ticker.open_price:
                    print(" قيمت بازشدن امروز بيشترازبسته شدن ديروزشده")
                          

                if ticker.sta_max == ticker.high_price:
                    print(' صف خريدشده')


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

                if omc > ticker.adj_close > yesterday_price <= ticker.min_week:
                    print (ticker.max_week,": تا قيمت پايين تريامساوي کمترين قيمت هفتگيه وشروع کرده بره بالا")
                if omc < ticker.adj_close < yesterday_price <= ticker.max_week:
                    print(ticker.min_week,": قيمت ازبالاتري قيمت هفتگي پايين ترآمد امکان ريزش تا ")    

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

                          
                #==========================================================
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
                     p=2095
                     s=1586
                     v=236600
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
                          

                # فصبا
                if index == 11:
                     p=4893
                     s=4992
                     v=3000
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


          except (TypeError , Exception) as te:
               print ()
               print (te)
               print ('TypeError or Exception : لطفادوباره سعي کنيد')
               print () 

