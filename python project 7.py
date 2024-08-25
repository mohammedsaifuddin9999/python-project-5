#Alram Clock
from playsound import playsound
import time 

CLEAR ="\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alram(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN}Alram will sound in: {minutes_left:02d}:{seconds_left}")
    playsound("alram.mp3")

minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))
total_seconds = minutes * 60 + seconds
alram(total_seconds)