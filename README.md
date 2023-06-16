# WhatsApp Sender

WhatsApp Sender is a Python script and GUI application that automates sending messages to multiple phone numbers using WhatsApp Web.

## Features

- Allows sending messages to multiple recipients from an Excel file.
- Utilizes Selenium WebDriver for web automation.
- Supports Chrome browser.
- Provides a GUI interface for selecting the input file and sending messages.
- Displays the result of the message-sending process.

## Requirements

- Python 3.6+
- Selenium
- pandas
- Chrome browser
- Chrome WebDriver

## Installation

1. Clone the repository:

2. Install the required Python packages:
 ```
pip install -r requirements.txt
```

3. Download and install the Chrome browser: [Download Chrome](https://www.google.com/chrome/)

4. Download the Chrome WebDriver:
- Make sure to download the Chrome WebDriver that matches your Chrome browser version.
- You can download it from the official website: [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads){:target="_blank"}.
- Extract the WebDriver executable and place it in a directory accessible to your system's PATH.

## Usage

1. Prepare the input Excel file:
- Create an Excel file with two columns: "Number" and "Message".
- Enter the phone numbers and corresponding messages in the respective columns.

2. Run the script:
- Execute the following command:
  ```
  python main.py
  ```
- The GUI window will open.
- choose the input Excel file.
- The script will open a Chrome browser window with WhatsApp Web.
- Complete the QR code scan.
- You will need to log in to your WhatsApp account by scanning the QR code using your phone.
- Once you complete the QR code scan.
- AFTER logging into Whatsapp Web is complete and your chats are visible,
- go to Command and press ENTER.
- the script will proceed to send messages to the specified phone numbers.

3. Monitor the progress:
- The result of each message-sending attempt will be displayed in the console.
- Once all messages are sent, the result will be saved into a new file in the same directory.

