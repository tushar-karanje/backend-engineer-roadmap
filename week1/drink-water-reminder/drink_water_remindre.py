import time 
from pync import Notifier
ONE_HOUR=60*60

try :
    while True :
        print("Please Relax and Sip a glass of water")
        Notifier.notify("Relax! Please sip some water!", title = "Water Reminder")
        time.sleep(ONE_HOUR)
except KeyboardInterrupt:
    print("\nStopping Reminder! But stay hydrated!")
