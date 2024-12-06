# Alarm clock
# Started: 11/27/2024
# Finished: 12/07/2024

from datetime import datetime
import time
import winsound
   
def timeSet(alarmSet):
    while True:
        now = datetime.now().strftime("%H:%M")
        nowStats = datetime.now().strftime("%H:%M:%S")
        if alarmSet == now:
            print()
            print("Alarm went off!")
            for i in range(10):
                winsound.Beep(500, 100) # Works only on Windows :(
            break
        else:
            print(f"Alarm was set for: {alarmSet} | Current time: {nowStats}")
        
        time.sleep(1) # Checks every 1 second

alarmTime = input("Enter time (00:00 - 23:59) (HH:MM): ")
alarmSet = datetime.strptime(alarmTime, "%H:%M").strftime("%H:%M")

# Start
timeSet(alarmSet)
