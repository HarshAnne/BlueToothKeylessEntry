#!/usr/bin/python

import bluetooth
import time
from gpiozero import LED


print "BlueToothKeylessEntry"
ledUnlock = LED(17) #GPIO pin 17 on rpizero set to unlock
ledLock = LED(27) #GPIO pin 27 on rpizero set to lock
lockStatus = 0
while True:
    result = bluetooth.lookup_name('98:E7:F5:FB:XX:XX', timeout=5)
    if (result != None):  			#mac address found within proximity

	if (lockStatus == 0): 			#If car is not already unlocked
		ledUnlock.on()
		time.sleep(2)
		ledUnlock.off()
		time.sleep(2)
		lockStatus = 1
#						print "Car was locked, now it is unlocked"
    else:					#mac address not found

	if (lockStatus == 1):			#if car is not already locked
		ledLock.on()
		time.sleep(2)
		ledLock.off()
		time.sleep(2)
		lockStatus = 0
#						print "Car was unlocked, now it is locked"
    time.sleep(15)				#search for phone every 15 seconds

