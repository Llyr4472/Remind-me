import time 
import datetime
import winsound
import os
from tkinter import *


#functions
def main ():
    print(time.ctime(), " \n \n")
    remind = input("When do u want to be reminded? (e.g.2h 30m 45s) \n")
    timi = input("What do you want to be reminded of \n") +  ' :D'
    sec = ''
    sec_h=sec_m= sec_s=0
    i=""
    for i in remind:
        if i.isdigit():
            sec += i
        elif str.capitalize(i)=='H':
            sec_h = int(sec)*60*60
            sec = ''
        elif str.capitalize(i)=='M':
            sec_m = int(sec)*60
            sec = ''
        elif str.capitalize(i)=="S":
            sec_s = int(sec)
            pass
        else:
            print(" \n Invalid input.")
            break
    total = sec_s + sec_m + sec_h
    print(f'\n \nYour reminder has been set. You will be reminded after {remind}. Please dont close this window. \n ')
    body(timi,total)


def body(timi,delay):
    time.sleep(delay)
    root = Tk()
    root.title(string="Remind me")
    root.geometry("585x340")
    canvas = Canvas(root,height='2000',width='2000',bg='#202020')
    canvas.pack()
    canvas.create_rectangle(0, 100, 5000, 2080, fill='#303030')
    canvas.create_text(300, 50, text="REMINDER", fill="white", font=('Helvetica 15 bold'))
    canvas.create_text(260, 150, text=timi, fill="white", font=('Arial','25'))
    sound()
    root.mainloop()

def sound():
    winsound.PlaySound(sound='tone.wav',flags=winsound.SND_FILENAME)


#main
main()


