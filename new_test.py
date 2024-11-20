



#==================================================

#آخرين کار

# سيگنالهاي خريد وفروش با انديکاتورهاي 
# RSI and Stochastic and MACD and ichimoku and SMA_3,9

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
    print()
    print(10 * "*", 'لطفا انتخاب کنید', 10 * "*")

def open_testnew_py():
    # 1 . test.py محاسبات سهام در بورس ایران با فایل
    pass

def for_exit_tsenew_py():
    # 2 . برای خارج شدن از برنامه
    pass

while True:
    main_menu()
    user_input = input("Enter 1 ؟ new_test.py برنامه را ادامه میدهید با \nEnter 2 یا از برنامه خارج میشوید؟ : ")
    print('*' * 10)
    print()

    if user_input == "2":
        for_exit_tsenew_py()
        print('شما از برنامه خارج شدید')
        exit()

    elif user_input == "1":
        open_testnew_py()

        try:
            print("=" * 15, "(ichimoku-Stochastic-MACD-RSI-SMA)برسي سهام بورس ايران با", "=" * 15)
            print()

            nam = input("لطفا نام سهام مورد نظرتان را بنویسید : ")

            # تبدیل تاریخ شمسی به میلادی
            start_date = jdatetime.datetime(1401, 1, 1).togregorian()
            end_date = jdatetime.datetime(1403, 9, 1).togregorian()

            # اطمینان از اینکه تاریخ‌ها در محدوده مجاز قرار دارند
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')

            DF = tse.Get_Price_History(stock=nam,
                                        start_date=start_date_str,
                                        end_date=end_date_str,
                                        ignore_date=True,
                                        adjust_price=True,
                                        show_weekday=True,
                                        double_date=True)

            DropList = ['Open', 'High', 'Low', 'Close', 'Final']
            DF.drop(columns=DropList, axis=1, inplace=True)

            RenameDict = {
                'Adj Open': 'Open',
                'Adj High': 'High',
                'Adj Low': 'Low',
                'Adj Close': 'Close',
                'Adj Final': 'Final',
                'Adj Max ': 'Max '
            }
            
            DF.rename(columns=RenameDict, inplace=True)

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

            # Ichimoku  ترکيب سه کندل آخربا
            # در داخل تابع main_menu یا بعد از محاسبات ایچیموکو، این تابع را فراخوانی کنید:
            #trend_last_three, ichimoku_signal = analyze_last_three_candles_with_ichimoku(DF)
            #print(f"وضعیت سه کندل آخر: {trend_last_three}, سیگنال ایچیموکو: {ichimoku_signal}")
            

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
        
            today_Volume = DF['Volume'].iloc[-1] # حجم امروز
            today_Volume_yesterday = DF['Volume'].iloc[-2] # حجم ديروز
            today_Volume_yesterday2 = DF['Volume'].iloc[-3] # حجم سه روزقبل


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

            
        except Exception as e:
              print(f"یک خطا رخ داد: {e}")



#==================================================
              
#Stochastic             

# سيگنالهاي خريد وفروش با انديکاتورهاي 
# RSI and Stochastic and MACD and ichimoku and SMA_3,9

import time
import numpy as np
import pandas as pd
import finpy_tse as tse
from datetime import datetime
import warnings
import jdatetime  # اضافه کردن کتابخانه jdatetime

warnings.filterwarnings("ignore", category=FutureWarning)

def main_menu():
    print()
    print(10 * "*", 'لطفا انتخاب کنید', 10 * "*")

def open_testnew_py():
    # 1 . test.py محاسبات سهام در بورس ایران با فایل
    pass

def for_exit_tsenew_py():
    # 2 . برای خارج شدن از برنامه
    pass

while True:
    main_menu()
    user_input = input("Enter 1 ؟ new_test.py برنامه را ادامه میدهید با \nEnter 2 یا از برنامه خارج میشوید؟ : ")
    print('*' * 10)
    print()

    if user_input == "2":
        for_exit_tsenew_py()
        print('شما از برنامه خارج شدید')
        exit()

    elif user_input == "1":
        open_testnew_py()

        try:
            print("=" * 15, "(ichimoku-Stochastic-MACD-RSI-SMA)برسي سهام بورس ايران با", "=" * 15)
            print()

            nam = input("لطفا نام سهام مورد نظرتان را بنویسید : ")

            # تبدیل تاریخ شمسی به میلادی
            start_date = jdatetime.datetime(1401, 1, 1).togregorian()
            end_date = jdatetime.datetime(1403, 9, 1).togregorian()

            # اطمینان از اینکه تاریخ‌ها در محدوده مجاز قرار دارند
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')

            DF = tse.Get_Price_History(stock=nam,
                                        start_date=start_date_str,
                                        end_date=end_date_str,
                                        ignore_date=True,
                                        adjust_price=True,
                                        show_weekday=True,
                                        double_date=True)

            DropList = ['Open', 'High', 'Low', 'Close', 'Final']
            DF.drop(columns=DropList, axis=1, inplace=True)

            RenameDict = {
                'Adj Open': 'Open',
                'Adj High': 'High',
                'Adj Low': 'Low',
                'Adj Close': 'Close',
                'Adj Final': 'Final',
                'Adj Max ': 'Max '
            }
            
            DF.rename(columns=RenameDict, inplace=True)

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

            # نمایش نتایج نهایی فقط برای آخرین سه روز
            last_three_days = DF.tail(3)
            
            print(30*'-')
            print(last_three_days[['Tenkan-sen', 'Kijun-sen', 'Signal']])
            print(last_three_days[['EMA_3', 'EMA_9', 'EMA_Signal']])
            print(last_three_days[['SMA_3', 'SMA_9', 'SMA_Signal']])
            print(last_three_days[['RSI', 'RSI_Signal']])
            print(last_three_days[['MACD', 'Signal_MACD', 'MACD_Signal']])
            print(last_three_days[['%K', '%D', 'Stochastic_Signal']])
            print(last_three_days[['Close', 'Volume']])
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

            if last_day.get('Stochastic_Signal') == 1:
                 print(f"در تاریخ {last_day_date.date()} : ('Stochastic') بخر")
            elif last_day.get('Stochastic_Signal') == -1:
                 print(f"در تاریخ {last_day_date.date()} : ('Stochastic') بفروش")

            if last_day.get('SMA_Signal') == 1:
                 print(f"در تاریخ {last_day_date.date()} : ('SMA') بخر")
            elif last_day.get('SMA_Signal') == -1:
                 print(f"در تاریخ {last_day_date.date()} : ('SMA') بفروش")

            if last_day.get('EMA_Signal') == 1:
                 print(f"در تاریخ {last_day_date.date()} : ('EMA') بخر")
            elif last_day.get('EMA_Signal') == -1:
                 print(f"در تاریخ {last_day_date.date()} : ('EMA') بفروش")

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

            
        except Exception as e:
              print(f"یک خطا رخ داد: {e}")


#===================================================

print ('marhale one_1')

import time

# پرسيدن براي خارج شدن ياادامه عمليات درصدگيري
sentence1 = "1 . for anjame dobareh (new_test.py درصدگيري با): "
sentence2 = "2 . for get out : "

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
     print("for anjame dobareh ")
     print ('اين برنامه براي درصدگيري ازدوعددميباشد')

     
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))


     # Calculate percentage
     percent = (num2 / num1) * 100

     # Print the percentage
     print("{:.0f}%".format(percent))

#بازدن شماره 2ازبرنامه خارچ ميشويم
if user_input == "2":
    print ('-'*10,' شماازبرنامه خارج شديد\n')

    exit ()

#------------------------------
print ('marhale tow_2')
import math
     

#براي درصدگيري ازدوعدد ميباشد عددبزرگ اول تايپ شود
# وبازدن عدد1 دوباره تکرارميشود وعدد2ازبرنامه خارج ميشود
def main_menu():
    print(10*"-" , 'لطفا انتخاب کنيد',10*"-")
    print ()
    print ('new_test.py براي درصدگيري دوعدد با ')
    print ('To begin with = 1  and  exit = 2' )


def calculate_percentage():
    pass


while True :
    main_menu()
    print ('-'*10)
    user_input = input("Enter 1 or 2 : ")
    print ('-'*10)

    if user_input == "1":
        calculate_percentage()
        #print ('براي درصدگيري ازدوعدد')
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
            
        # Calculate percentage
        percent = (num2 / num1) * 100
        print ()
        # Print the percentage
        print("{:.0f}%".format(percent),': مقداردرصد')
        print ('-'*10)

        
    if user_input == '2':
        print ('-'*10,' شماازبرنامه خارج شديد')
        
        exit()


