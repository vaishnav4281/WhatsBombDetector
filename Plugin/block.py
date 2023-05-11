from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()  # or any other browser of your choice
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and log in
input('Press Enter after scanning QR code')

# Navigate to the chat you want to check
chat_name = 'Mine'
search_box = driver.find_element_by_xpath('//input[@title="Search or start new chat"]')
search_box.send_keys(chat_name)
chat = driver.find_element_by_xpath(f'//span[@title="{chat_name}"]')
chat.click()

# Get the sender's phone number or name
sender = driver.find_element_by_xpath('//span[@class="_3-cMa _3Whw5"]')
sender_text = sender.text

# Navigate to the "Settings" page
settings_button = driver.find_element_by_xpath('//div[@title="Menu"]')
settings_button.click()
settings_link = driver.find_element_by_xpath('//div[@title="Settings"]')
settings_link.click()

# Search for the sender in the "Blocked contacts" list
search_box = driver.find_element_by_xpath('//input[@type="text"]')
search_box.send_keys('Blocked contacts')
search_box.send_keys(Keys.RETURN)

blocked_contacts = driver.find_element_by_xpath('//div[@class="_2CwG7"]')
blocked_contacts.click()

blocked_list = driver.find_element_by_xpath('//div[@class="_2ZvKl"]')
if sender_text not in blocked_list.text:
    # Block the sender
    add_blocked_button = driver.find_element_by_xpath('//div[@title="Add blocked contact"]')
    add_blocked_button.click()

    input_field = driver.find_element_by_xpath('//input[@type="text"]')
    input_field.send_keys(sender_text)

    block_button = driver.find_element_by_xpath('//div[@class="_3GI3v"]')
    block_button.click()
















#from selenium import webdriver

#driver = webdriver.Chrome()  # or any other browser of your choice
#driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and log in
#input('Press Enter after scanning QR code')

# Navigate to the chat you want to report
#chat_name = 'John Doe'
#search_box = driver.find_element_by_xpath('//input[@title="Search or start new chat"]')
#search_box.send_keys(chat_name)
#chat = driver.find_element_by_xpath(f'//span[@title="{chat_name}"]')
#chat.click()

# Report the contact
#more_button = driver.find_element_by_xpath('//span[@data-testid="more"]')
#more_button.click()

#report_button = driver.find_element_by_xpath('//div[@title="Report contact"]')
#report_button.click()

#reason_dropdown = driver.find_element_by_xpath('//div[@class="_2b1wj"]')
#reason_dropdown.click()

# Choose the appropriate reason for reporting the contact
#reason_option = driver.find_element_by_xpath('//div[@class="_1wQgY"]')
#reason_option.click()

# Click on the "Report" button to submit the report
#report_button = driver.find_element_by_xpath('//div[@class="_3xev8"]')
#report_button.click()


