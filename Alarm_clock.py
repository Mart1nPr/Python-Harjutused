# Alarm clock
# Started: 11/27/2024
# Finished: 

from datetime import datetime

current_time = datetime.now()

print(current_time.time())

hourSelection = int(input("Enter hour/hours (0-12): "))
if hourSelection in (0,12):
    pass
else:
    print("Over 12!")

minuteSelection = int(input("Enter minute/minutes (0-59): "))
if minuteSelection in (0,59):
    pass
else:
    print("Over 59!")

meridiemSelection = input("Enter meridian (AM/PM): ").upper()


