
import time

# جدول ضرب اعداد درپايتون

print (20*"-",'جدول ضرب اعداد باپايتون',20*"-")
print ()

for i in range(1,10):
   for j in range(1,10):
 
     print( "{:3d}".format(i*j),end =" " )
   print()
#------------------------------------------------
time.sleep(5)

def multiple_arguments(val1, val2, val3, calcSum = True):
    # Calculate the sum
    if calcSum:
        return val1 + val2 + val3
    # Calculate the average instead
    else:
        return (val1 + val2 + val3) / 3
 
var1 = multiple_arguments(-5, 7.9, 10)
var2 = multiple_arguments(-5, 7.9, 10, False)
print("var1 should be the sum of (-5, 7.9, 10): ", var1)
print("var2 should be the average of (-5, 7.9, 10):", var2)
 
#------------------------------------------------
time.sleep(5)

import random
 
def random_number():
    my_number = random.randint(1, 100)
    return my_number
 
varns = random_number()
print("the random number is equal to", varns)
 
# output: the random number is equal to 67

#----------------------------------------------
time.sleep(5)

def say_hello():
    for i in range(0,3):
        print("hello!")
 
say_hello()

#--------------------------------------------
time.sleep(5)

import tkinter as tk

# Create the main window
window = tk.Tk()

# Set window title
window.title("My Tkinter Window")

# Set window geometry (width x height + x-coordinate + y-coordinate)
window.geometry("800x400+200+200")

# Create a label
label = tk.Label(window, text="سلام به ويندوز10خوش آمديد \n hello in Windows 10 \n لطفا انتخاب کنيد")

# Configure the font size and style
label.config(font=("Helvetica", 60))

# Add the label to the window
label.pack()

# Start the main loop
window.mainloop()

exit ()

#-------------------------------------------------
time.sleep(5)

import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a label
label = tk.Label(window, text="سلام به ويندوز10خوش آمديد")

# Configure the font size and style
label.config(font=("Helvetica", 50))

# Add the label to the window
label.pack()

# Start the main loop
window.mainloop()

exit ()
#---------------------------------------------------
time.sleep(5)

import tkinter as tk

def close_window():
    window.destroy()

# Create the main window
window = tk.Tk()

# Create a label
label = tk.Label(window, text="تست برنامه جديد")

# Configure the font size and style
label.config(font=("Helvetica", 60))

# Add the label to the window
label.pack()

# Close the window after 5 seconds
window.after(5000, close_window)

# Start the main loop
window.mainloop()

exit ()
#---------------------------------------
#==============================
time.sleep(5)

#نوشته درسه خط ظاهرميشه وبعد از5 ثانيه محوميشه 
import tkinter as tk

def close_window():
    window.after(5000, window.destroy)

# Create the main window
window = tk.Tk()

# Configure the background color
window.config(bg='#f0f0f0')  # Use a very light gray color

# Create a label
label = tk.Label(window, text="سلام به ويندوز10خوش آمديد \n Hello, welcome to Windows 10 \n لطفا انتخاب کنيد", fg='green')

# Configure the font size and style
label.config(font=("Helvetica", 60))

# Add the label to the window
label.pack()

# Close the window after 5 seconds
close_window()

# Start the main loop
window.mainloop()

exit()
#============================
#-----------------------------------------------------------

import tkinter as tk

def close_window():
    window.after(5000, window.destroy)

# Create the main window
window = tk.Tk()

# Configure the background color
window.config(bg='black')

# Create a label
label = tk.Label(window, text="سلام به ويندوز10خوش آمديد \n hello in Windows 10 \n لطفا انتخاب کنيد", fg='green')

# Configure the font size and style
label.config(font=("Helvetica", 60))

# Add the label to the window
label.pack(pady=50)

# Create a button
button = tk.Button(window, text="بستن", command=close_window)

# Add the button to the window
button.pack(pady=50)

# Start the main loop
window.mainloop()

#-------------------------------------
import tkinter as tk

def close_window():
    window.after(5000, window.destroy)

def write_word(index):
    if index >= 0:
        label.config(text=words[index])
        window.after(1000, write_word, index - 1)

# Create the main window
window = tk.Tk()

# Configure the background color
window.config(bg='black')

# Create a label
label = tk.Label(window, text="", fg='green')

# Configure the font size and style
label.config(font=("Helvetica", 60))

# Add the label to the window
label.pack()

# The words to be written
words = ["سلام به ويندوز 10 خوش آمديد \n لطفاانتخاب کنيد", "Hello welcome to Windows 10"]

# Start writing the words
write_word(len(words) - 1)

# Close the window after 5 seconds
close_window()

# Start the main loop
window.mainloop()

exit()

#-----------------------------------------------------------------
import math

def calculate_percentage(num1, num2):
    try:
        # Check if num1 is zero to avoid division by zero error
        if num1 == 0:
            return "Error: Division by zero is not allowed."
        else:
            # Calculate percentage
            percentage = (num2 / num1) * 100
            return "{:.0f}%".format(percentage)
    except TypeError:
        return "Error: Both inputs must be numbers."

# Test the function
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(calculate_percentage(num1, num2))
#================================
# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate percentage
percent = (num2 / num1) * 100

# Print the percentage
print("{:.0f}%".format(percent))
#-------------------------------
print ("python", end = '')
print ("3","and windows 10 - ",(3+2)*100/2+12596842)
print ("or bama bashid",end = '')
print ("zam zam ab beheshte")

#===================================================







