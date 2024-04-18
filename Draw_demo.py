import epd2in13_V4 as display #For 2.13inch screen.
from PIL import Image, ImageDraw, ImageFont
from WotD import get_wotd
import textwrap

epd = display.EPD() # get the display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear()      # clear the display

def printToDisplay(wotd):
    date, word, phonetic, word_type, definition = wotd
    word_type = "("+word_type+")"

    epd_w, epd_h = display.EPD_HEIGHT, display.EPD_WIDTH #reverse for lanscape orientation. 
    HBlackImage = Image.new('1', (epd_w, epd_h), 255) #255(white)

    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer.
    font_date = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 15)
    font_word = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 20)
    font_def = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 10)

    draw.text((2, 2), date, font = font_date, fill = 0) #draw date
    draw.text((2,22), word_type, font=font_def, fill=0) #draw word type.
    draw.text((4, 20), word, font = font_word, fill = 0) #draw word
    definition = textwrap.wrap(definition,width=38) #draw meaning
    y=0
    for def_line in definition:
        draw.text((5, 60+y), def_line, font = font_def, fill = 0)
        y+=10

    HBlackImage = HBlackImage.rotate(180, expand=1)
    epd.display(epd.getbuffer(HBlackImage))



printToDisplay(get_wotd())