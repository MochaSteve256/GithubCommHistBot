from PIL import Image
import datetime
#load image
img = Image.open("mochasteve.png")
pixels = img.load()

week = datetime.datetime.now().isocalendar()[1] - 1
weekday = datetime.datetime.now().weekday() + 1
if weekday == 7:
    weekday = 0
    week += 1

print("week: " + str(week))
print("weekday: " + str(weekday))

if pixels[week, weekday] == 1:
    print("black")
else:
    print("not black")
