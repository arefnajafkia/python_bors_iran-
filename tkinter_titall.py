import time


def main_menu():
    print(10*"-" , 'لطفا انتخاب کنيد',10*"-")
    print ()   
    print("1 . RSI اطلاعات اوليه سهام شماومحاسبات : ")
    print("2 . رسم نمودارميانگين هاي 10/20/50 : ")
    print("3 . وضعيت کندلهاي سهام انتخابي شما : ")
    print("4 . گزارش وضعيت حجم وقيمت سهام انتخابي : ")
    print("5 . گزارشي ازوضعيت حمايت ومقاومت ها : ")
    print("6 . محاسبات ايچيموکو و اينکل فينگ : ")
    print("7 . bmi and omc انجام محاسبات با : ")
    print("8 . نتيجه محاسبات ميانگين 103وکانالها : ")
    print("9 . EXIT ")


def plot_Information_RSI():
    # 1 . RSI اطلاعات اوليه سهام شماومحاسبات
    pass

def calculate_Average_the_chart():
    # 2 . رسم نمودارميانگين هاي 10/20/50
    pass

def Condition_candle_take_stock():
    # 3 . وضعيت کندلهاي سهام انتخابي شما
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
    user_input = input("Enter 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 : ")

    if user_input == "1":
        plot_Information_RSI()
        print ()
        print ("="*15,"Basic information of your stock and rsi" ,"="*15)
    elif user_input == "2":
        calculate_Average_the_chart()
        print ()
        print ('-'*10,"Drawing average graphs 10/20/50" ,'-'*10)
    elif user_input == "3":
        Condition_candle_take_stock()
        print ()
        print ('-'*10,"The status of your selected stock candles" ,'-'*10)
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

