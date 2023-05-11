from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Open browser and navigate to web page
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
abcclass="selectable-text copyable-text iq0m558w"
# Find all elements with class name "message"
messages = driver.find_element(By.CLASS_NAME,"selectable-text copyable-text iq0m558w")

# Extract text from each message element and add to list
message_texts = [message.text for message in messages]

# Print out the list of message texts
print(message_texts)

# Close the browser
#driver.quit()
