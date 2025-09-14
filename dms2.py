from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time 
from time import sleep
from bs4 import BeautifulSoup
import itertools, sys, requests, mechanize, os, re, email, smtplib, ssl, selenium
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.webdriver.firefox.options import Options
import logging
import selenium.webdriver
import selenium.webdriver.firefox.service
from wakeonlan import send_magic_packet

# Replace with the actual MAC address of your target computer
mac_address = "XX:XX:XX:XX:XX:XX" 

options = Options()
options.add_argument("--headless")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://discord.com/login")
time.sleep(6)

#--------------- Edit Here -------------------------------------------------------------

# Enter your account details here 

username = "krarktel@gmail.com"

password = "04hp9004"

# Copy the URL of channel where you wanna send messages and paste below

channelURL = "https://discord.com/channels/@me/1385695239330725920"

#-------------- Edit End ----------------------------------------------------------------

# Initialize and input email

username_input = driver.find_element(by = By.NAME, value = "email")

username_input.send_keys(username)

# Initialize and input password

password_input = driver.find_element(by = By.NAME, value= "password")

password_input.send_keys(password)
password_input.submit()

# Initialize and login

print(">>Login Complete!")

time.sleep(10)

print(">Opening link")
driver.get(channelURL)

# Function to get the last message
def get_last_message(driver):
    try:
        # XPath to find the last message content (adjust based on Discord's 
        last_message_xpath = "//ol[@data-list-id='chat-messages']/li[last()]//div[contains(@class,'messageContent')]"
        time.sleep(5)
        last_message_element = driver.find_element(by = By.XPATH, value = last_message_xpath)
        return last_message_element.text
    except Exception:
        return None

last_known_message = get_last_message(driver)
print(f"Initial last message: {last_known_message}")

while True:
    time.sleep(5)  # Check for new messages every 5 seconds
    current_last_message = get_last_message(driver)

    if current_last_message and current_last_message != last_known_message:
        print(f"New message detected: {current_last_message}")
        last_known_message = current_last_message
        os.system("python3 Messages.py 2603417581 verizon Dm")
        send_magic_packet(mac_address)
    else:
        print("No new messages.", end='\r')

driver.quit()
