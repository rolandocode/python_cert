#https://es.stackoverflow.com/questions/348101/error-al-instalar-paquetes-pip-no-se-reconoce-como-un-comando-interno-o-exte
#py -m pip install matplotlib
import matplotlib.pyplot as plt
import time as tmodule

time_attempt = [1,2,3,4,5]
time_records = []
attempt_counter = 0

word = "magazine"

while attempt_counter < len(time_attempt):
    time_stamp_start = tmodule.time()
    user_keyword = input("Type the word 'magazine': ")
    if (user_keyword != word):
        print("Word is incorrect, please type again!: ")
        continue
    time_stamp_end = tmodule.time()
    elapsedTime = time_stamp_end- time_stamp_start
    time_records.append(elapsedTime)
    attempt_counter = attempt_counter+1

legend = ["1 try", "2 try", "3 try", "4 try", "5 try"]

plt.xticks(time_attempt, legend)
plt.ylabel("Time in seconds")

plt.bar(time_attempt, time_records)
# plt.plot(time_attempt, time_records)
plt.show()

