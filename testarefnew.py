#ادرس اين فايل ازپايتون درزيرنوشته شده
#C:\Users\aref\AppData\Local\Programs\Python\Python311\testarefnew.py

#باروشن کردن کامپيوتراين برنامه اجراميشودودرآدرس زيرميباشد
#C:\Users\aref\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\testarefnew.py


import tkinter as tk

def close_window():
    window.after(9000, window.destroy)

# Create the main window
window = tk.Tk()

# Configure the background color
window.config(bg='black')

# Create a label
label = tk.Label(window, text="هيچ وقت بي خيال چيزي که ميخواهي نشو \n " " \n صبرکن ولي فراموشش نکن \n " " \n صبرکردن سخته،ولي حسرت خوردن سخت تره \n ""\n به آغازاعتمادنکن حقيقت درآخرراه ", fg='green')

# Configure the font size and style
label.config(font=("Helvetica", 60))

# Add the label to the window
label.pack()

# Close the window after 5 seconds
close_window()

# Start the main loop
window.mainloop()

exit ()
