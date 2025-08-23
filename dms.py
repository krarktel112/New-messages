import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os, shutil

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

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

username_input = driver.find_element_by_name('email')

username_input.send_keys(username)

# Initialize and input password

password_input = driver.find_element_by_name('password')

password_input.send_keys(password)

# Initialize and login

login_button = login_button.click()

print(">>Login Complete!")

time.sleep(10)

driver.get(channelURL)

print(">Opening The Server Link...")

time.sleep(5)

# Msg Sending
try:
    # Find all message elements (adjust XPath based on your HTML structure)
    # This example assumes messages are <p> tags within a <div> with class 'chat-messages'
    message_elements = driver.find_elements(By.XPATH, "//div[@class='chat-messages']/p")

    if message_elements:
        # Get the last message element from the list
        last_message_element = message_elements[-1]

        # Extract the text content of the last message
        last_message_content = last_message_element.text
        print(f"Content of the last message: {last_message_content}")
    else:
        print("No messages found.")

except Exception as e:
    print(f"An error occurred: {e}")

print("last message is")
