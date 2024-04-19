import epd2in13_V4 as display #For 2.13inch screen.
from PIL import Image, ImageDraw, ImageFont
import time
import datetime
import textwrap
from bs4 import BeautifulSoup
import requests

epd = display.EPD() # get the display
epd.init()           # initialize the display
#print("Clear...")    # prints to console, not the display, for debugging
#epd.Clear()      # clear the display

def get_wotd():
    url='https://www.dictionary.com/e/word-of-the-day/'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    wotd=soup.find(class_="wotd-item").get_text().split("\n")
    wotd=[item for item in wotd if item!=""]
    wotd=[wotd[i] for i in (0,1,2,7,8)]
    wotd[0] = ', '.join(wotd[0].split(', ')[1:]) #Remove day.
    wotd[1] = wotd[1].strip().title() #clean big space and capitalize first letter.
    wotd[2] = wotd[2].lstrip() #Get rid of leading long blank space.
    wotd[3] = wotd[3].rstrip() #Get rid of following blank space.
    return wotd

def wotd_to_display(wotd):
    date, word, phonetic, word_type, definition = wotd
    word_type = "("+word_type+")"

    epd_w, epd_h = display.EPD_HEIGHT, display.EPD_WIDTH #reverse for lanscape orientation. 
    HBlackImage = Image.new('1', (epd_w, epd_h), 255) #255(white)

    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer.
    font_date = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 14)
    font_word = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 20)
    font_def = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 12)

    draw.text((2, 2), "--Word of the Day-- "+date, font = font_date, fill = 0) #draw date
    draw.text((2,42), word_type+" "+phonetic, font=font_def, fill=0) #draw word type and phonetic.
    draw.text((5, 20), word, font = font_word, fill = 0) #draw word
    definition = textwrap.wrap(definition,width=36) #draw meaning
    y=0
    for def_line in definition:
        draw.text((5, 60+y), def_line, font = font_def, fill = 0)
        y+=11

    HBlackImage = HBlackImage.rotate(180, expand=1)
    epd.display(epd.getbuffer(HBlackImage))

def check_and_call():
    #Call for first time after reboot.
    print("Clear...")    # prints to console, not the display, for debugging
    epd.Clear()      # clear the display
    wotd_to_display(get_wotd())
    # Get the current time
    current_time = datetime.datetime.now()
    print("Function called on:", current_time)

    # Define the specific time of the new day when you want to call the function
    specific_time = datetime.time(8, 0, 0)  # Adjust this to your desired time (hour, minute, second)
    # Check if the current time is equal to or after the specific time

    if current_time.time() >= specific_time:
        # Wait until the next day
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        next_day_time = datetime.datetime.combine(tomorrow, specific_time)
        time_difference = (next_day_time - current_time)
        print("Sleep until ", next_day_time)
        time.sleep(time_difference.total_seconds())
    else:
        # Wait until specific refresh time.
        today = datetime.date.today()
        next_refresh = datetime.datetime.combine(today, specific_time)
        time_difference = (next_refresh - current_time)
        print("Sleep until ", next_refresh)
        time.sleep(time_difference.total_seconds())

# Run the loop continuously
while True:
    check_and_call()