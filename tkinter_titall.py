import time
import math

# نه تابع مختلف باکارايي هاي متفاوت
def main_menu():
    print(10*"-" , 'لطفا انتخاب کنيد',10*"-")
    print ()   
    print("1 . براي درصدگيري ازدوعدد : ")
    print ()
    print("2 . درست کردن فايل وخواندنش دردرايو اي : ")
    print ()
    print("3 . پاک کردن فايل ماي فايل ازدرايو اي درپوشه فيلم : ")
    print ()
    print("4 . test.py محاسبات سهام دربورس ايران بافايل: ")
    print ()
    print("5 . بازشدن اسکريپ موزيک : ")
    print ()
    print("6 . محاسبات ايچيموکو و اينکل فينگ : ")
    print ()
    print("7 . bmi and omc انجام محاسبات با : ")
    print ()
    print("8 . نتيجه محاسبات ميانگين 103وکانالها : ")
    print ()
    print("9 .  --- EXIT  --- ")


def Percentage_two_numbers():
    # 1 . براي درصدگيري ازدوعدد
    pass

def Create_file_and_read():
    # 2 . درست کردن فايل وخواندنش دردرايو اي 
    pass

def Delete_the_file_from_the_drive():
    # 3 . پاک کردن فايل ماي فايل ازدرايو اي درپوشه فيلم
    pass

def open_test_py():
    # 4 .  test.py محاسبات سهام دربورس ايران بافايل
    pass

def Skripe_Music_azad():
    # 5 . بازشدن اسکريپ موزيک
    pass

def Calculations_Ichimoku_Engulfing():
    # 6 . محاسبات ايچيموکو و اينکل فينگ
    pass

def Calculations_omc_bmi():
    # 7 . bmi and omc انجام محاسبات با
    pass

def Result_Average_channels():
    # 8 . نتيجه محاسبات ميانگين 103وکانالها
    pass


while True:
    main_menu()
    print ('-'*10)
    user_input = input("Enter 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 : ")
    print ('-'*10)
    print ()

    if user_input == "1":
        Percentage_two_numbers()
        #براي درصدگيري ازدوعدد
        print ('tkinter_titall.py براي درصدگيري دوعدد با ')
        print ('   لطفا شروع کنيد  ' )
        print ()
        print (' one number')
        num1 = float(input("Enter first number: "))
        print ()
        print (' Two number')
        num2 = float(input("Enter second number: "))
            
        # Calculate percentage
        percent = ((num2 / num1) * 100)-100
        print ()
        # Print the percentage
        print (' Answer for you')
        print("{:.0f}%".format(percent),': مقداردرصد')
        print ('-'*10)

        
    elif user_input == "2":
        Create_file_and_read()
        print ()
        # درست کردن فايل ماي فايل دردرايواي درپوشه فيلم
        with open ('E:/film/myfile.ipynb','w') as f :
            line1 = 'print ("marhale one_1")\n'
            
            line2 = 'import time\n'
            
            line3 = '# پرسيدن براي خارج شدن ياادامه عمليات درصدگيري\n'
            line4 = 'sentence1 = "1 . for anjame dobareh : \n'
            line5 = 'sentence2 = "2 . for get out : "\n'
            
            line6 = '# Print the characters of the first prompt with a delay of 0.2 seconds \n'
            line7 = 'for char in sentence1:\n'
            line8 = '    print(char, end="")\n'
            line9 = '    time.sleep(0.2)\n'
            line10 = 'print()\n'
            
            line11 = '# Print the characters of the second prompt with a delay of 0.2 seconds\n'
            line12 = 'for char in sentence2:\n'
            line13= '    print(char, end="")\n'
            line14 = '    time.sleep(0.2)\n'
            line15 = 'print()\n'
            
            line16 = "# Get the user's input\n"
            line17 = 'user_input = input("Enter 1 or 2 : ")\n'
            line18 = "print ('       ','-'*30)\n"
            
            line19 = '# Check if the user wants to plot the stock price\n'
            line20 = 'if user_input == "1":\n'
            line21 = '     print("for anjame dobareh ")\n'

            
            line22 = '     num1 = float(input("Enter first number: "))\n'
            line23 = '     num2 = float(input("Enter second number: "))\n'

            
            line24 = '     # Calculate percentage\n'
            line25 = '     percent = (num2 / num1) * 100\n'
            
            line26 = '     # Print the percentage\n'
            line27 = '     print("{:.0f}%".format(percent))\n'
            
            line28 = '#بازدن شماره 2ازبرنامه خارچ ميشويم\n'
            line29 = 'if user_input == "2":\n'
            line30 = "    print ('-'*10,' شماازبرنامه خارج ميشويد')\n"
            
            line31 = '    exit ()\n'
            
            line32 = 'print ("marhale tow_2")\n'
            line33 = 'import math\n'
            
            line34 = '#براي درصدگيري ازدوعدد ميباشد عددبزرگ اول تايپ شود\n'
            line35 = '# وبازدن عدد1 دوباره تکرارميشود وعدد2ازبرنامه خارج ميشود\n'
            line36 = 'def main_menu():\n'
            line37 = '    print(10*"-" , "لطفا انتخاب کنيد",10*"-")\n'
            line38 = '    print ()\n'
            line39 = '    print ("براي درصدگيري دوعدد ")\n'
            line40 = '    print ("To begin with = 1  and  exit = 2" )\n'

            line41 = 'def calculate_percentage():\n'
            line42 = '    pass\n'

            
            line43 = 'while True :\n'
            line44 = '    main_menu()\n'
            line45 = '    print ("-"*10)\n'
            line46 = '    user_input = input("Enter 1 or 2 : ")\n'
            line47 = '    print ("-"*10)\n'
            
            line48 = '    if user_input == "1":\n'
            line49 = '        calculate_percentage()\n'
            line50 = '        #print ("براي درصدگيري ازدوعدد")\n'
            line51 = '        num1 = float(input("Enter first number: "))\n'
            line52 = '        num2 = float(input("Enter second number: "))\n'
            
            line53 = '        # Calculate percentage\n'
            line54 = '        percent = (num2 / num1) * 100\n'
            line55 = '        print ()\n'
            line56 = '        # Print the percentage\n'
            line57 = '        print("{:.0f}%".format(percent),": مقداردرصد")\n'
            line58 = '        print ("-"*10)\n'

            
            line59 = '    if user_input == "2":\n'
            line60 = '        print ("-"*10," شماازبرنامه خارج شديد")\n'
            
            line61 = '        exit()\n'

            line62 = '------------------\n'
            line63 = 'فايل درآدرس زير ساخته شد \n'
            line64 = ' E:/film/myfile.ipynb \n'
            
            f.write (line1)
            f.write (line2)
            f.write (line3)
            f.write (line4)
            f.write (line5)
            f.write (line6)
            f.write (line7)
            f.write (line8)
            f.write (line9)
            f.write (line10)
            f.write (line11)
            f.write (line12)
            f.write (line13)
            f.write (line14)
            f.write (line15)
            f.write (line16)
            f.write (line17)
            f.write (line18)
            f.write (line19)
            f.write (line20)
            f.write (line21)
            f.write (line22)
            f.write (line23)
            f.write (line24)
            f.write (line25)
            f.write (line26)
            f.write (line27)
            f.write (line28)
            f.write (line29)
            f.write (line30)
            f.write (line31)
            f.write (line32)
            f.write (line33)
            f.write (line34)
            f.write (line35)
            f.write (line36)
            f.write (line37)
            f.write (line38)
            f.write (line39)
            f.write (line40)
            f.write (line41)
            f.write (line42)
            f.write (line43)
            f.write (line44)
            f.write (line45)
            f.write (line46)
            f.write (line47)
            f.write (line48)
            f.write (line49)
            f.write (line50)
            f.write (line51)
            f.write (line52)
            f.write (line53)
            f.write (line54)
            f.write (line55)
            f.write (line56)
            f.write (line57)
            f.write (line58)
            f.write (line59)
            f.write (line60)
            f.write (line61)
            f.write (line62)
            f.write (line63)
            f.write (line64)
            
        
        import os
        # خواندن فايل ماي فايل ازدرايو اي درپوشه فيلم
        with open ('E:/film/myfile.ipynb','r') as f :
            for line in f :
                print (line, end ='')
                
        print ()
    elif user_input == "3":
        Delete_the_file_from_the_drive()
        print ()
        # پاک کردن فايل ماي فايل ازدرايو اي درپوشه فيلم
        import os
        
        n = 'E:/film/myfile.ipynb'
        print (os.path.exists(n))
        os.remove(n)
        print ('-'*10,' E:/film/myfile.ipynb فايل موجوددراين آدرس پاک شد ')
        print ()
    elif user_input == "4":
        open_test_py()
        # بازکردن test.py
        print ()
        try :
            

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
            namad =["چکارن","تلیسه","غمینو","غکورش","وسپه","شپاکسا","ومعادن","تاپیکو",
                    "دسبحان","کچاد","شستا","حتوکا","خگستر","فولاد","شپنا","فملی","فصبا",
                    "فسبزوار","خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور","فپنتا",
                    "شبندر","فارس","غفارس","وبصادر","کچاد","درازک","داتام","نخريس","پاکشو",
                    "کگل","ثبهساز","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
                    "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
                    "تاصيكو","حكشتي","قهكمت","تكشا","شاروم","مارون","آريا","اپال",
                    "واعتبار","اطلس","شپترو","سمگا","سبزوا","سيمانو","استيل"]

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

            # Calculate the closing price for yesterday and three days ago

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


            #=====================================================
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
            print (40*'=',sahame,'volume',"and order sell and buy")
            print (ticker.volume ,'حجم امروز')
             
            if ticker.adj_close > ticker.yesterday_price:
                 print (' قيمت امروزبالاترازديروزه ')
            else :
                 if ticker.adj_close < ticker.yesterday_price:
                      print (' قيمت امروزپايين ترازديروزه ')
            #================================================
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
                      
            print ()
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
            if open_price > yesterday_price:
                print ('open_price > yesterday_price')
            if open_price < yesterday_price:
                print ('open_price < yesterday_price')


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
                
            print ()
            print (math.ceil(ticker.max_week),": بالاترين قيمت هفتگي ")
            print (math.ceil(ticker.min_week),": پايين ترين قيمت هفتگي")
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
            print ()
            #--------------------------------------------
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
            print(buy_signals.tail(2))

            print ()          
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

            #-------------------------------------
            print(40*"=","حدود حمايت ومقاومت باقيمت",sahame,)
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
                 p=4331
                 s=4431
                 v=75000
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
                 p=4408
                 s=0
                 v=80000
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
                
            # غکورش
            if index == 5:
                 p=9435
                 s=0
                 v=25000
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

            # شپاکسا
            if index == 6:
                 p=1925
                 s=0
                 v=7800
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
                 p=4931
                 s=0
                 v=1500
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
                      print (ticker.last_price,' : قيمت آخرين معامله امروز') 
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
            print ()
        except TypeError as te:
            print ()
            print (te)
            print ('TypeError : لطفادوباره سعي کنيد')
            print ()
    elif user_input == "5":
        Skripe_Music_azad()
        # بازشدن اسکريپ موزيک
        print ()

        import os
        
        m = 'E:\Trader\cmd\music.bat'
        print (os.path.abspath(m))
        os.open(m)
        print ()
    elif user_input == "6":
        Calculations_Ichimoku_Engulfing()
        print ()
        print ('-'*10,"Ichimoku and Engulfing calculations" ,'-'*10)
    elif user_input == "7":
        Calculations_omc_bmi()
        print ()
        print ('-'*10,"Performing BMO and OMC calculations" ,'-'*10)
    elif user_input == "8":
        Result_Average_channels()
        print ()
        print ('-'*10,"The result of 103 average calculations and channels" ,'-'*10)
    elif user_input == "9":
        print ('-'*10,' شماازبرنامه خارج شديد')
        break
    else:
        print ()
        print ('-'*25)
        print("Invalid input. Please try again.")
        print ('-'*10)

#===============================================================

# کدنوشته شده برای پایتون 3
#پرسیدن ازماوانتخاب ازکاربر 
# نوشتن پرسش بامکث انجام میشود


import time

sentence = 'لطفا انتخاب کنيد'
words = sentence.split()

for word in words:
    print(word, end=" ")
    time.sleep(0.8)
print(30*"-")
print ()

sentence1 = "رسم نمودارميانگين هاي 10,20,50 .1 : "
sentence2 = "2. محاسبات روندها وکف هاباکانال : "
sentence3 = "انجام محاسبات حجم وکانال سهام شما .3 : "
sentence4 = "4. Exit"

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

# Print the characters of the second prompt with a delay of 0.2 seconds
for char in sentence3:
    print(char, end="")
    time.sleep(0.2)
print()

# Print the characters of the first prompt with a delay of 0.2 seconds
for char in sentence4:
    print(char, end="")
    time.sleep(0.2)
print()


# Get the user's input
user_input = input("Enter 1 or 2 or 3 or 4: ")

# Check if the user wants to plot the stock price
if user_input == "1":
    print ("="*15,"Drawing moving average charts" ,"="*15)
# Check if the user wants to calculate the volume and channel
elif user_input == "2":
    print ()
    print ('-'*10,"Thanks for the explanation about your stock" ,'-'*10)
    print ()
# Check if the user wants to calculate the volume and channel
elif user_input == "3":
    print ()
    print ('-'*10,"Thanks for the explanation about your stock and good" ,'-'*10)
    print ()
# Check if the user wants to calculate the volume and channel
elif user_input == "4":
    exit()
else:
    print ()
    print("Invalid input. Continue the program in the next step.")



#==================================================

#بدست آوردن سيگنال خريد يافروش باايچيموکو

import pandas as pd
import ichimoku_cloud_indicator as ichimoku

# داده های تاریخچی نماد را بارگیری می کنیم
data = pd.read_csv('شستا')

# شاخص ICHIMOKU Cloud را محاسبه می کنیم
ichimoku_cloud = ichimoku.IchimokuCloud(data['Close'], conversion_line_periods=9, base_line_periods=26, lead_line_periods=52, displacement=26)
data['Conversion Line'] = ichimoku_cloud.conversion_line
data['Base Line'] = ichimoku_cloud.base_line
data['Lead Line 1'] = ichimoku_cloud.lead_line_1
data['Lead Line 2'] = ichimoku_cloud.lead_line_2
data['Cloud Top'] = ichimoku_cloud.cloud_top
data['Cloud Bottom'] = ichimoku_cloud.cloud_bottom

# نماد را بررسی می کنیم
if data['Conversion Line'][0] < data['Base Line'][0] and data['Base Line'][0] < data['Lead Line 1'][0] and data['Lead Line 1'][0] < data['Lead Line 2'][0] and data['Close'][0] > data['Cloud Top'][0]:
    print('سیگنال خرید برای نماد HCHMK.IR')
else:
    print('سیگنال خرید برای نماد HCHMK.IR وجود ندارد')


