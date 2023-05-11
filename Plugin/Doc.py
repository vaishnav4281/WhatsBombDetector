import os
from alright import WhatsApp
msgr=WhatsApp()
#whatsap web opens
numb=["9645703000","9847171069","9207473682"]
s=5
i=0
#msgr.get_first_chat()
for i in numb:
	print(i)
	for j in range(0,50):
                    msgr.find_user(numb)
                    msgr.send_message('HaCkEd!')
	#i++
	#msgr.find_user(numb[i])
	#for i in range(s):
		#msgr.send_message(';)')
#os.system('wmctrl -c')
