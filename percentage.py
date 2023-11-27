import psutil, time, pyttsx3, winsound

def convertTime(seconds):
    minutes,seconds=divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "%d:%02d:%02d"% (hours, minutes, seconds)

battery = psutil.sensors_battery()
percent = battery.percent
time_left= convertTime(battery.secsleft)

#Display time left in hours and mins
print("Made by Steve \nBattery left: ", time_left)
print("Battery percentage: ", percent)

#initiate audio engine
engine= pyttsx3.init()

#logic
if(battery.power_plugged==True and percent==100):
    winsound.MessageBeep()
    engine.say("Battery is fully charged")
    engine.runAndWait()
elif(battery.power_plugged==True and percent>=98):
    winsound.MessageBeep()
    text ="Battery is almost full "+str(percent)+ " percent charged"
    engine.say(text)
    engine.runAndWait()
elif(battery.power_plugged==False and percent<20):
    winsound.MessageBeep()
    text ="Your battery is at "+str(percent)+ " percent, please charge"
    engine.say(text)
    engine.runAndWait()

# time.sleep(5)