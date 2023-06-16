from tkinter import *
from tkinter import filedialog
import pandas as pd
from msg import send_messages # previous code is in a file called "msg.py"

# create the main window
root = Tk()
root.title("WhatsApp Sender")

# create a variable to store the file path
file_path = StringVar()

# create a function to handle the "Select File" button click event
def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    file_path_label.config(text=file_path)

# create a function to handle the "Send Messages" button click event
def send_messages_gui():
    global file_path
    send_messages(file_path)
    result_label.config(text="Messages sent successfully.")

# create a label and button to select the input file
file_path_label = Label(root, text="")
file_path_label.pack()
select_file_button = Button(root, text="Select File", command=select_file)
select_file_button.pack()

# create a label and button to send the messages
send_messages_button = Button(root, text="Send Messages", command=send_messages_gui)
send_messages_button.pack()
result_label = Label(root, text="")
result_label.pack()

# start the main loop
root.mainloop()
