
from alright import WhatsApp
msgr = WhatsApp()


import time
from selenium import webdriver
#from simon.accounts.pages import LoginPage
#from simon.header.pages import HeaderPage
#from simon.pages import BasePage
#from simon.chat.pages import ChatPage
#from simon.chats.pages import PanePage

msg_txt=[]
msgs=driver.find_elements_by_xpath('//div[contains(@class, "message-in")]//div[@class="copyable-text")')
moji=re.search(r'[\U0001F600-\U0001F6FF]{10,}',txt)
for msg in msgs:
	txt=msg.txt
	msg_txt.append(txt)

for txt in msg_txt:
	if len(txt)>fact:
		printf('Bomb Message Detected!')

# Creating the driver (browser)
#driver = webdriver.Firefox()
#driver.maximize_window()
#pane_page=PanePage(driver)
#op_cht=pane_page.opened_chats
#fact=10
#for oc in op_cht:
#	if oc.last_message.count(op_cht) > fact:
		
# 1. Login
#       and uncheck the remember check box
#       (Get your phone ready to read the QR code)
#login_page = LoginPage(driver)
#login_page.load()
#login_page.remember_me = False
#time.sleep(7)


# 2. The base page is inherited by all pages
#       and here you can check whether any
#       page is available on the screen of
#       the browser.

# we don't need to load the pages as whatsapp
# web works as one-page web app
#base_page = BasePage(driver)
#base_page.is_title_matches()
#base_page.is_welcome_page_available()
#base_page.is_nav_bar_page_available()
#base_page.is_search_page_available()
#base_page.is_pane_page_available()
# chat is only available after you open one
#base_page.is_chat_page_available()


# 3. Logout
#header_page = HeaderPage(driver)
#header_page.logout()

# Close the browser
#driver.quit()


#numbers = ['9645703000','8943246025','9074777986','9846511016']
#'9645703000','8943246025','9526851724','
#for number in numb:
#s=10
#msgr.find_user("9645703000")
#for i in range(s):
	#msgr.send_message("hlo")
#for number in numbers:
	#print('Test')
#for i in range(len(numbers)):
	#print(numbers[i])
#	msgr.find_user(numbers[i])
#	for j in range(0,5):
	#	print('Test')	
#		msgr.send_message('Test')
	#i=i+1
#			
#			msgr.send_message('Test')
#msgr.find_user('9645703000','8943246025')
#msgr.send_message('Test')
#msgr.find_user('8943246025')
#msgr.send_message('Test')
#i=0
#j=0
#count=15
#msgr.find_user('9645703000')
#msgr.send_message('Test') 
#msgr.send_picture('/home/user/423529.jpeg',"*Spam Message Here*")
#msgr.send_file('/home/user/423529.jpeg')


#for j in range(0,count):
#	for i in range(len(numbers)):
#		msgr.send_direct_message(numbers[i],'sheoruheskug',saved='true')

#msgr.send_direct_message('8943246025','Hacked',saved='true')
#msgr.send_direct_message('9539852159','Hacked',saved='true')
#msgr.send_direct_message('9645703000','Test',saved='true')
#       messenger.find_user(number)
#      messenger.send_message("Test")
