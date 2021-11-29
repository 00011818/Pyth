print("CW deadline (sample: 20.02.2020 24:12:55)")

time=str(input())

def input_time(str):
    return int(time[11:13]), int(time[14:16]), int(time[0:2]), int(time[3:5]), int(time[6:10])

cw_deadline = []

for i in input_time(time):
    cw_deadline.append(i)


print("CW submission (sample: 20.02.2020 24:12:55)")
stime=str(input())

submission_date = []
for i in input_time(stime):
    submission_date.append(i)
