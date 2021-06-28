import time
from playsound import playsound
from datetime import datetime
alarmtime = "07:00"
while True:
    lcltime = datetime.now().strftime('%H:%M')
    if lcltime == alarmtime:
        playsound("Batida eletronica 2018_160k.mp3")
        break
    else:
        print("ACORDA")
        time.sleep(10)