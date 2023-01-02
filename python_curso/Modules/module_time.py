import time as t

def addDays(days):
    current_time = t.time()
    delivery_time = current_time + (86400 *days)
    return delivery_time

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
print ("In 'main' delivery date: ", delivery_date)

functionDeliver_date = t.localtime(addDays(7))

print ("Function delivery time: ", functionDeliver_date)