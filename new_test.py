



#==========================================
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
#===========================================
