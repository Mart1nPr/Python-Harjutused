# Countdown timer
# 11/27/2024

import time
t = 1 # 1 Second

timeSelection = int(input("Select how long the countdown would be (In Seconds): "))
timeLeft = timeSelection

for i in range(timeSelection):
    time.sleep(t)
    timeLeft = timeLeft - 1
    print("Time left from:",timeSelection,"/",timeLeft)