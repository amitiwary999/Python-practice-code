import time
import os
from gi.repository import Notify

true = 1
hr=input("Enter hour: ")
mn=input("Enter minute: ")
msg=input("Enter alarm message: ")
while(true):
	dt = list(time.localtime())
	hour = dt[3]
	minute = dt[4]
	if hour == hr and minute == mn:
		Notify.init("Start")
		st=Notify.Notification.new("Alarm",msg,"dialog-information")
		st.show()
		#os.popen2("open /Users/rudra/alarm.mp3")
		true = 0
