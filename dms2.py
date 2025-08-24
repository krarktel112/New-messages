from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver (replace with your WebDriver path)
driver = webdriver.Chrome()

# Navigate to Discord (and handle login if not already logged in)
driver.get("https://discord.com/login") 
# ... (add login automation here if needed)

# Navigate to a specific channel (replace with actual channel element locator)
# Example: locating a channel by its name in a specific server
# You'll need to inspect Discord's HTML to find the correct locators for your setup
try:
    channel_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'channelName') and text()='your-channel-name']"))
    )
    channel_element.click()
except Exception as e:
    print(f"Could not find or click the channel: {e}")
    driver.quit()
    exit()

# Function to get the last message
def get_last_message(driver):
    try:
        # XPath to find the last message content (adjust based on Discord's current HTML)
        last_message_xpath = "//ol[@data-list-id='chat-messages']/li[last()]//div[contains(@class,'messageContent')]"
        last_message_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, last_message_xpath))
        )
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
    else:
        print("No new messages.")

driver.quit()
