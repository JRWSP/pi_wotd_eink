import epd2in13_V4 as display #For 2.13inch screen.
from PIL import Image, ImageDraw, ImageFont
import datetime
import textwrap
from bs4 import BeautifulSoup
import requests

epd = display.EPD() # get the display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear()      # clear the display

def get_wotd():
    url='https://www.dictionary.com/e/word-of-the-day/'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    wotd=soup.find(class_="wotd-item").get_text().split("\n")
    wotd=[item for item in wotd if item!=""]
    wotd=[wotd[i] for i in (0,1,2,7,8)]
    wotd[0] = ', '.join(wotd[0].split(', ')[1:]) #Remove day.
    wotd[1] = wotd[1].strip().title() #clean big space and capitalize first letter.
    wotd[2] = wotd[2].lstrip() #Get rid of loeading long blank space.
    return wotd

def wotd_to_display(wotd):
    date, word, phonetic, word_type, definition = wotd
    word_type = "("+word_type+")"

    epd_w, epd_h = display.EPD_HEIGHT, display.EPD_WIDTH #reverse for lanscape orientation. 
    HBlackImage = Image.new('1', (epd_w, epd_h), 255) #255(white)

    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer.
    font_date = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 15)
    font_word = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 20)
    font_def = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 12)

    draw.text((2, 2), date, font = font_date, fill = 0) #draw date
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
    global last_call_date
    today = datetime.date.today()
    if last_call_date is None or today > last_call_date:
        # Your function logic goes here
        wotd_to_display(get_wotd())
        print("Function called on:", datetime.datetime.now())
        last_call_date = datetime.date.today()

# Global variable to keep track of the last call date
last_call_date = None
# Initial call to set the last_call_date
check_and_call()

# Simulation of the passage of time
# You can replace this with your actual code or use a scheduler to run this periodically
# For example, you can run this code in a loop with a sleep interval
for _ in range(2):
    # Simulating the passage of time by adding a day
    last_call_date += datetime.timedelta(days=1)
    check_and_call()