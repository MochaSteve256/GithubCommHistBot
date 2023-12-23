import os
import datetime
import schedule
import time
from PIL import Image

img = Image.open("mochasteve.png")
pixels = img.load()

def commit():
    #modify a file
    filedata = ""
    with open("modifiedFile.txt", "r") as file:
        filedata = file.read()
    with open("modifiedFile.txt", "w") as file:
        file.write(filedata + "\n" + str(datetime.datetime.now()))
    #commit changes
    os.system("git add modifiedFile.txt")
    os.system("git commit -m \"Automated commit at " + str(datetime.datetime.now()) + "\"")
    os.system("git push")
    pass

def dailyTask():
    #check if there's a black pixel for the current day
    ##get calendar week
    week = datetime.datetime.now().isocalendar()[1] - 1
    ##get week day
    weekday = datetime.datetime.now().weekday() + 1
    if weekday == 7:#github week starts on sunday
        weekday = 0
        week += 1
    ##check if there's a black pixel
    if pixels[week, weekday] == 1:
        commit()

#set up daily task
schedule.every().day.at("12:00").do(dailyTask)

while datetime.datetime.now().year != 2024:
    print("Waiting for 2024...")
    time.sleep(3600)

while datetime.datetime.now().year == 2024:
    schedule.run_pending()
    time.sleep(3600)
