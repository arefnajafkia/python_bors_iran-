#--------------------------------------------
#رسم شکل هندسي باپايتون
import turtle
turtle.setup(width=1000, height=600)
screen = turtle.Screen()
screen.title("suherfe.blog.ir")
colors=['red','purple','blue','green','yellow','orange']
turtle.bgcolor('black')
turtle.speed("fastest")
for x in range(361):
    turtle.pencolor(colors[x%6])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)
turtle.hideturtle ()

print("Suherfe.blog.ir")
#--------------------------------------------
#رسم شکل هندسي باپايتون
import turtle
turtle.setup(width=1000, height=600)
screen = turtle.Screen()
screen.title("suherfe.blog.ir")
turtle.reset()
turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor('black')
c = 0
x = 0
colors = [
#reddish colors
(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
]
while x < 1000:
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x = x + 1
    c = c + 0.1
turtle.exitonclick()

print("Suherfe.blog.ir")
#--------------------------------------------


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
