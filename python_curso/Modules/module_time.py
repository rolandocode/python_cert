import time as t
print(t.localtime())

time_now = t.localtime()
print ("Transaction complete ", 
str(time_now.tm_hour) + " HR" + " : " + str(time_now.tm_min) + " MIN" + " Day:" + str(time_now.tm_mday))
#seconds since 1 January 1970
print("Time stamp: ", t.time())

#product delivery in 7 days
current_time = t.time()
delivery_time = current_time + (86400 *7)

delivery_date = t.localtime(delivery_time)
print (delivery_date)