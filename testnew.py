
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

#نوشته درسه خط ظاهرميشه وبعد از5 ثانيه محوميشه 
import tkinter as tk

def close_window():
    window.after(8000, window.destroy)

# Create the main window
window = tk.Tk()

# Configure the background color
window.config(bg='#f0f0f0')  # Use a very light gray color

# Create a label
label = tk.Label(window, text="هيچ وقت بي خيال چيزي که ميخواهي نشو \n " " \n صبرکن ولي فراموشش نکن \n " " \n صبرکردن سخته،ولي حسرت خوردن سخت تره \n "" ", fg='green')

# Configure the font size and style
label.config(font=("Helvetica", 60))

# Add the label to the window
label.pack()

# Close the window after 5 seconds
close_window()

# Start the main loop
window.mainloop()

exit()
#======================================


