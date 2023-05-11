from selenium import webdriver

driver = webdriver.Chrome()  # or any other browser of your choice
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and log in
input('Press Enter after scanning QR code')

# Navigate to the chat where you want to get the user's number
chat_name = 'John Doe'
search_box = driver.find_element_by_xpath('//input[@title="Search or start new chat"]')
search_box.send_keys(chat_name)
chat = driver.find_element_by_xpath(f'//span[@title="{chat_name}"]')
chat.click()

# Get the user's name or phone number
user = driver.find_element_by_xpath('//span[@class="_3-cMa _3Whw5"]')
user_text = user.text

# Click on the user's name to open their profile
user.click()

# Get the user's phone number from their profile, if available
try:
    profile_info = driver.find_element_by_xpath('//div[@class="_1WZqU PNlAR"]')
    phone_number = profile_info.text
    phone_number = phone_number.split('\n')[1]  # Assumes phone number is on the second line
    print(phone_number)
except:
    print('Phone number not available')

