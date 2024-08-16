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
    print("4 . گزارش وضعيت حجم وقيمت سهام انتخابي : ")
    print ()
    print("5 . گزارشي ازوضعيت حمايت ومقاومت ها : ")
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

def Condition_candle_Volume_stock():
    # 4 . گزارش وضعيت حجم وقيمت سهام انتخابي
    pass

def Condition_Protection_resistance():
    # 5 . گزارشي ازوضعيت حمايت ومقاومت ها
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
        #print ('براي درصدگيري ازدوعدد')
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
            
        # Calculate percentage
        percent = (num2 / num1) * 100
        print ()
        # Print the percentage
        print("{:.0f}%".format(percent),': مقداردرصد')
        print ('-'*10)

        
    elif user_input == "2":
        Create_file_and_read()
        print ()
        # درست کردن فايل ماي فايل دردرايواي درپوشه فيلم
        with open ('E:/film/myfile.ipynb','w') as f :
            line1 = 'Hello word\n'
            line2 = 'python3\n'
            line3 = 'with\n'
            line4 = 'myfile.ipynb\n'
            line5 = 'salam agha\n'
            f.write (line1)
            f.write (line2)
            f.write (line3)
            f.write (line4)
            f.write (line5)

        # خواندن فايل ماي فايل ازدرايو اي درپوشه فيلم
        with open ('E:/film/myfile.ipynb','r') as f :
            for line in f :
                print (line, end ='')
        print ('-'*10)
        
    elif user_input == "3":
        Delete_the_file_from_the_drive()
        print ()
        # پاک کردن فايل ماي فايل ازدرايو اي درپوشه فيلم
        import os
        n = 'E:/film/myfile.ipynb'
        print (os.path.exists(n))
        os.remove(n)
        print ('-'*10,' فايل پاک شد')
        
    elif user_input == "4":
        Condition_candle_Volume_stock()
        print ()
        print ('-'*10,"Report on the volume and price of selected stocks" ,'-'*10)
    elif user_input == "5":
        Condition_Protection_resistance()
        print ()
        print ('-'*10,"Report on the status of support and resistance" ,'-'*10)
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


