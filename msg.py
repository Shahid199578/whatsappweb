from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from time import sleep
from urllib.parse import quote
import os
import pandas as pd
from tkinter import Tk, filedialog
import sys


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# create a GUI window to select the input file
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])    
    
while True:
    try:
        # Read data from Excel file
        df = pd.read_excel(file_path)
        break
    except FileNotFoundError:
        print("File not found, make sure the file exists and is in the same directory as this script.")



# Extract phone numbers and messages from the data
numbers = df['Number'].tolist()
messages = df['Message'].tolist()

# Loop through the phone numbers and messages
#for idx, number in enumerate(numbers):
    #message = messages[idx]

#print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, number in enumerate(numbers):
    message = messages[idx]
    message = quote(message)
    number = str(number).strip()
    if number == "":
        continue
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                except Exception as e:
                    print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
                else:
                    sleep(1)
                    click_btn.click()
                    sent=True
                    sleep(3)
                    df = pd.read_excel(file_path)
                
    except Exception as e:
        print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

driver.close()

new_file_path = os.path.splitext(file_path)[0] + '_sent.xlsx'
df.to_excel(new_file_path, index=False)
print(f"Data saved to {new_file_path}")

sys.exit(0)
quit()
os.exit(0)
