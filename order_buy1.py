
# برنامه نوشته شده براي پايتون 3
# بازدن شماره سهم دستور خريد يا فروش صادرميشود
# ودلايل خريد يافروش روهم مينويسد  order_buy   

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


print(10*"-", ' \\\\\  برسي سهام بورس ايران  ///// ' ,10*"-")
print()   
print("1 . براي انتخاب سهام موردنظرتان اول يک رابزنيد  : ")
print (30*'=')      


print()
time.sleep(4)

def main_menu(): 
    print()
    print(5*"-" ,'\\\\\ براي انتخاب مجددسهم شماره يک رابزنيد /////',5*"-")
    print(5*"-" ,' درغيراين صورت شماره هاي ديگرراانتخاب کنيد ',5*"-")
    print()
    print("2 . نوع کندل امروزودرصدفاصله بالاوپايين کندل : ")
    print (20*'-')
    print("3 . حجم ومحاسبات قيمت ها : ")
    print (20*'-')
    print("4 . bmi and omc انجام محاسبات با : ")
    print (20*'-')
    print("5 . True and False مقادير sma3-10 and sma3-10 : ")
    print (20*'-')
    print("6 . محاسبات سودوزيان خريد باقيمت امروز : ")
    print (20*'-')
    print("7 . EXIT براي خروج")
    print()


def plot_Information_RSI():
    # 1 . لطفابراي انتخاب سهم مورد نظرتان اول يک رابزنيد
    pass

def calculate_Average_the_chart():
    # 2 . نوع کندل امروزودرصدفاصله بالاوپايين کندل
    pass

def Condition_candle_take_stock():
    # 3 . حجم ومحاسبات قيمت ها
    pass

def Condition_candle_Volume_stock():
    # 4 . bmi and omc انجام محاسبات با 
    pass

def Condition_Protection_resistance():
    # 5 . True and False مقادير sma3-10 and sma3-10
    pass

def Calculations_Ichimoku_Engulfing():
    # 6 . محاسبات سودوزيان خريد باقيمت امروز
    pass


while True:
    main_menu()
    user_input = input("Enter 1 or 2 or 3 or 4 or 5 or 6 or 7 : ")

    if user_input == "1":
        plot_Information_RSI()   
        #===================================================
        print ()
        print(22*"=","Stock and OTC symbols of Iran",22*"=")
        print()
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
        namad =["چکارن","تلیسه","غمینو","وسپه","غکورش","شپاکسا","ثبهساز","تاپیکو",
                "دسبحان","ومعادن","فصبا","حتوکا","خگستر","فولاد","شپنا","فملی","شستا",
                "فسبزوار","خودرو","تیپیکو","خساپا","سرچشمه","نیان","ختور","فپنتا",
                "شبندر","فارس","غفارس","وبصادر","کچاد","کگل","داتام","نخريس","پاکشو",
                "درازک","كپارس","عيار","اهرم","غگيلا","توان","غشهداب","سحرخيز","دعبيد",
                "بركت","وملل","كروي","كدما","پارس","شيران","ساروم","سدشت","كماسه",
                "تاصيكو","نخريس","قهكمت"] 

        # Divide the list into three rows
        rows = [namad[i:i+5] for i in range(0, len(namad), 5)]

        # Print the rows next to each other with numbers
        for i, row in enumerate(rows):
            for j, stock in enumerate(row):
                stock_number = i*5 + j + 1
                print(f"{stock_number}. {stock}", end="\t")
            print()

        print ('-'*20) 
        # Ask the user to enter a valid index
        index = int(input(" Overwrite the symbol number :"))
        # Run Python for the selected stock    
        stock = namad[index-1]

        choice = index
        sahame = namad[choice-1]
        # Do some analysis or visualization here
        tse.download(symbols=sahame,
                     write_to_csv=True,
                     adjust=True)
        ticker = tse.Ticker(sahame)

        print()
        print(ticker.last_date,': تاريخ وساعت آخرين اطلاعات قيمت پاياني ومعاملاتي')
        print ('-'*20)
        print(ticker.title,' : نام شرکت ')
        print(ticker.state,ticker.flow,ticker.group_name)     
        print(ticker.fiscal_year,' : سال مالی ')  
        print(ticker.eps ,'  :  EPS  ')  
        print(ticker.p_e_ratio ,' :   P/E')  
        print(ticker.group_p_e_ratio, '  :  group P/E ')
        print()
        print(ticker.float_shares,' : درصد سهام شناور')   
        print(ticker.base_volume,' : حجم مبنا ')
        print(ticker.volume,' : حجم معاملات امروز ')
        print(ticker.month_average_volume,' : میانگین حجم ماه')
        print()  
        print(ticker.last_price,' : آخرین معامله ')  
        print(ticker.adj_close,' : قیمت پایانی ')  
        print(ticker.yesterday_price,' : قیمت دیروز ')
        print(ticker.open_price,' : قيمت بازشدن')   
        print()

        
        print (20*'*','End of this episode (1)',20*'*',sahame)      
        #=====================================================
    elif user_input == "2":
        calculate_Average_the_chart()
        #=====================================================
        print ()
        print ('='*30,' candel DOje')
        DOje1= (ticker.high_price+ticker.low_price)/2
        DOje2= DOje1 + 20
        DOje3= DOje1 - 20

        if ticker.last_price == DOje1>DOje3<DOje2 :
            print (' کندل دوجي شکل گرفته')


        if ticker.high_price > ticker.last_price >= DOje1:
            print (' کندل دوجي سبزشکل گرفته')
        else:
            if ticker.low_price < ticker.last_price <= DOje1:
                print (' کندل دوجي قرمزشکل گرفته')
                

        if ticker.open_price < ticker.last_price > DOje2:
            print (' candle Green')
        else:
            if ticker.open_price > ticker.last_price < DOje3:
                print (' candle Red')


        if ticker.open_price < ticker.last_price == ticker.high_price > (ticker.low_price+150):
            print (' candle marabozo Green')
        else:
            if ticker.open_price > ticker.last_price == ticker.low_price < (ticker.high_price-150):
                print (' candle marabozo Red')
            
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


        print()
        print (20*'*','End of this episode (2)',20*'*',sahame)
        #==============================================
    elif user_input == "3":
        Condition_candle_take_stock()
        #==============================================
        print(40*"=",sahame,"Process and Volume")

        if ticker.yesterday_price > ticker.low_price < ticker.min_week :
             print (' روند قيمتي هفتگي نزولي شد')
             print ((math.ceil(tedad))," : هرسهامدارامروزاين تعداد سهم فروخته")
             print ((math.ceil(godrat))," : قدرت سهامداران براي فروش")


        if ticker.yesterday_price < ticker.low_price > ticker.min_week :
             print (' روند قيمتي هفتگي صعودي شد')
             print ((math.ceil(tedad))," : هرسهامدارامروزاين تعدادسهام خريده")
             print ((math.ceil(godrat))," : قدرت سهامدارن براي خريد")
             
        #================================================
        print(25*"-")     
        if ticker.adj_close > ticker.yesterday_price:
             print (' قيمت امروزبالاترازديروزه ')
        else :
             if ticker.adj_close < ticker.yesterday_price:
                  print (' قيمت امروزپايين ترازديروزه ')

        print(20*"-")     
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
        ravand =(ticker.max_year + ticker.min_year)/2 # محاسبه قيمت نيمه ساليانه
        ravand_2 =(ticker.max_week + ticker.min_week)/2 # محاسبه قيمت نيمه هفتگي


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
            
             
        print(35*"=",sahame,"Tik Top or Down") 
        print(ticker.max_year,' : حداکثر قیمت بازه سال')
        print(ticker.min_year,' : حداقل قیمت بازه سال')


        if ticker.last_price > ticker.open_price > ticker.yesterday_price > ticker.low_price:
            print (" امروزتيک صعودي داريم")
        else:
            if ticker.last_price < ticker.open_price < ticker.yesterday_price < ticker.high_price:           
                print (" امروزتيک نزولي داريم")

                
        print()
        print (20*'*','End of this episode (3)',20*'*',sahame)
        #===============================================
    elif user_input == "4":
        Condition_candle_Volume_stock()
        #===============================================
        print ()
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

        print ()
        print (math.ceil(ticker.max_week),": بالاترين قيمت هفتگي ")
        print (math.ceil(ticker.min_week),": پايين ترين قيمت هفتگي")

        #------------------------------------------------
        print(40*"=",sahame,"For order")
        nimeh_price = ((ticker.high_price + ticker.low_price)/2)
        nimeh_ste = ((ticker.sta_max + ticker.sta_min)/2)

        if nimeh_ste < nimeh_price < ticker.adj_close > ticker.yesterday_price :
            print ("ميتوني خريد کني فردا قيمت بالاترميره")

        if bmi > omc :
            print ('bmi > omc',': for buy')
        if bmi < omc :
            print ('bmi < omc',': for sell')
            

        if nimeh_ste > nimeh_price > ticker.adj_close < ticker.yesterday_price :
            print ("قيمت فرداپايين ترمياد براي خريد دست نگهدار")  
            print ()


        print()
        print (20*'*','End of this episode (4)',20*'*',sahame)
        #======================================================
    elif user_input == "5":
        Condition_Protection_resistance()
        #======================================================
        print ()
        print(30*"=",sahame," True and False مقادير sma3-10")          

        history = ticker.history


        def sma(series, periods: int, ):
            return series.rolling(window=periods, min_periods=periods).mean()


        sma_3 = sma(history.close, 3)
        sma_10 = sma(history.close, 10)
        buy_signals = (
                (sma_3 > sma_10) &
                (sma_10.shift(1) > sma_3.shift(1)))
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
                (sma_20.shift(1) > sma_3.shift(1)))
        print(buy_signals.tail(2))
        print ()
     
        #-----------------------------------------------------
        print (20*'*','End of this episode (5)',20*'*',sahame)
        #------------------------------------------------
    elif user_input == "6":
        Calculations_Ichimoku_Engulfing()
        #----------------------------------
        print(40*"=","حدود حمايت ومقاومت باقيمت",sahame,)
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
        print()          
        print(ticker.url,'\n :  TSETMC آدرس صفحه',sahame,'در')
        print ()
        print (20*'*','End of this episode (6)',20*'*',sahame)
        #=====================================================
    elif user_input == "7":
        print ('===  You have exited the program  ===')
        break
    else:
        print ()
        print ('-'*25)
        print("Invalid input. Please try again.")
        print ('-'*10)


