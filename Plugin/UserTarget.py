import os
from alright import WhatsApp
msgr=WhatsApp()
#whatsap web opens
numb=['9645703000','9072001357','9207473682']
s=5
i=0
number=0
msg="Test"
l=len(numb)
for i in range(0,l):
        msgr.find_user(numb[i])
        msgr.send_message(msg)
	#number++
#msgr.get_first_chat()
#for i in numb:
#	print(i)
#	for j in range(0,50):
#			msgr.find_user(numb)
#			msgr.send_message('Test')
	#i++
	#msgr.find_user(numb[i])
	#for i in range(s):
		#msgr.send_message(';)')
#os.system('wmctrl -c')
