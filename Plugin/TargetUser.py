import os
from alright import WhatsApp
#msgr=WhatsApp()
#whatsap web opens
numb=["9645703000","9847171069","9207473682"]
num=10
#msgr.get_first_chat()
for num in numb:
	msgr.find_user(num)
	msgr.send_message('Testing')
	#i++
	#msgr.find_user(numb[i])
	#for i in range(s):
		#msgr.send_message(';)')
#os.system('wmctrl -c')
