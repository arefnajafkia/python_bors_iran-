
#ازکاربرپرسيده ميشود شماره اول رابگو وبعد دوم را حالا دوعدد رادرهم
# ضرب ميکند وجواب راميدهد ميتوان چهارعمل رياضيات راباپرسيدن ازکاربرامجام داد
# واين هرچندبارکه بخواهد ميتواند تکرارکند

def mdarsad(a, b):
    percents = (a * b)/100
    return ("{:.0f}".format(percents))

def darsad(a, b):
    percent = (a * 100)/b
    return ("%{:.0f}".format(percent))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b

def Calculations():
    while True:
        print ("="*15,"ومحاسبه درصددوعدد انجام چهارعمل اصلي","="*15)
        print ()
        txt = int(input(" 1. ضرب دوعدد \n 2. جمع دوعدد \n 3. تقسيم دوعدد \n 4. تفريق دوعدد \n 5. عدداول چنددرصددوميه \n 6. درصد دومي چقدرميشه n:  "))

        if txt == 1 :
            print ("="*15,"ضرب دوعدد","="*15)
            a = int(input("Enter the first number \n اولين عدد رابنويس : "))
            b = int(input("Enter the second number \n حالا دومين عدد رابنويس : "))

            result = multiply(a, b)

            print("The result is \n جواب ميشود :", result)

        elif txt == 2 :
            print ("="*15,"جمع دوعدد","="*15)
            a = int(input("Enter the first number \n اولين عدد رابنويس : "))
            b = int(input("Enter the second number \n حالا دومين عدد رابنويس : "))

            result = add(a, b)

            print("The result is \n جواب ميشود :", result)

        elif txt == 3 :
            print ("="*15,"تقسيم دوعدد","="*15)
            a = int(input("Enter the first number \n اولين عدد رابنويس : "))
            b = int(input("Enter the second number \n حالا دومين عدد رابنويس : "))

            result = divide(a, b)

            print("The result is \n جواب ميشود :", result)

        elif txt == 4 :
            print ("="*15,"تفريق دوعدد","="*15)
            a = int(input("Enter the first number \n اولين عدد رابنويس : "))
            b = int(input("Enter the second number \n حالا دومين عدد رابنويس : "))

            result = subtract(a, b)

            print("The result is \n جواب ميشود :", result)

        elif txt == 5 :
            print ("="*15,"محاسبه درصد عدداول به دوم","="*15)
            a = int(input("Enter the first number \n اولين عدد رابنويس : "))
            b = int(input("Enter the second number \n حالا دومين عدد رابنويس : "))

            result = darsad(a, b)

            print("The result is \n جواب ميشود :", result)

        elif txt == 6 :
            print ("="*15," درصد دومي چقدرميشه n","="*15)
            a = int(input("Enter the first number \n اولين عدد رابنويس : "))
            b = int(input("Enter the second number \n حالا دومين عدد رابنويس : "))

            result = mdarsad(a, b)

            print("The result is \n جواب ميشود :", result) 

        else :
            print ("Error! Invalid choice.")
            break

        play_again = input("Do you want to perform another operation? (y / n): ")
        if play_again.lower() != "y":
            break

Calculations()
#==================================================

import time

sentence = "بااين کد کلمات با مکث تايپ ميشوند"
words = sentence.split()

for word in words:
    print(word, end=" ")
    time.sleep(0.5)

#==================================================
print ()
print ()
print ('درچند خط کدجديد')
print ()
print ()
#================================================

import time

sentence1 = "========== برسي سهام بورس ايران  =========="
sentence2 = "Please write the name of the stock you want : "

for sentence in [sentence1, sentence2]:
    words = sentence.split()

    for word in words:
        for char in word:
            print(char, end="")
            time.sleep(0.1)
        print(" ", end="")

    print()

nam = input("لطفا نام سهام موردنظرتان رابنويسسد :")
print (nam)
#=====================================================
time.sleep(5)
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
    print ("="*15,"Performing BMO and OMC calculations" , nam,"="*15)
    print ()
    print(20*"-",nam,"کانال وکندلهاي امروز")

#-------------------

# Check if the user wants to calculate the volume and channel
elif user_input == "2":
    print ()
    print ('-'*10,"Report on the volume and price of selected stocks" , nam,'-'*10)
    print ()

#========================================
