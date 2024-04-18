import epd2in13_V4 #For 2.13inch screen.
from PIL import Image, ImageDraw, ImageFont
from WotD import get_wotd

epd = epd2in13_V4.EPD() # get the display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear()      # clear the display

def printToDisplay(wotd):
    date, word, phonetic, word_type, definition = wotd

    HBlackImage = Image.new('1', (epd2in13_V4.EPD_HEIGHT, epd2in13_V4.EPD_WIDTH), 255) #255(white)

    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 15) # Create our font, passing in the font file and font size

    
    draw.text((10, 15), date, font = font, fill = 0)

    HBlackImage = HBlackImage.rotate(180, expand=1)
    epd.display(epd.getbuffer(HBlackImage))


printToDisplay(get_wotd())