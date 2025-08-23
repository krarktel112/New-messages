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

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
#driver.get("https://www.google.com")
driver.get("https://discord.com/login")
time.sleep(6)

#--------------- Edit Here -------------------------------------------------------------

# Enter your account details here 

username = "krarktel@yahoo.com"

password = "04hp9004"

# Copy the URL of channel where you wanna send messages and paste below

channelURL = "https://discord.com/channels/775349757060186142/77535656021144289331"

#-------------- Edit End ----------------------------------------------------------------

# Initialize and input email

username_input = driver.find_element(by = By.NAME, value = 'email')

username_input.send_keys(username)

# Initialize and input password

password_input = driver.find_element(by = By.NAME, value= 'password')

password_input.send_keys(password)
password_input.submit()

# Initialize and login

print(">>Login Complete!")

time.sleep(10)

#driver.get(channelURL)

#print(">Opening The Server Link...")

#time.sleep(5)

# Msg Sending

#msgoutput = driver.find_element(by = By.XPATH, value = //ol[@data-list-id="chat-messages"]/li[last()]//div[contains(@class,'messageContent')

#print("last message is")

#print(msgoutput)
