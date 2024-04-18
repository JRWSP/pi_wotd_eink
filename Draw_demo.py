import epd2in13_V4 #For 2.13inch screen.
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13_V4.EPD() # get the display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear()      # clear the display

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in13_V4.EPD_HEIGHT, epd2in13_V4.EPD_WIDTH), 255) #255(white)

    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype('./Bangers-Regular.ttf', 30) # Create our font, passing in the font file and font size

    draw.text((25, 65), string, font = font, fill = 0)

    epd.display(epd.getbuffer(HBlackImage))

printToDisplay("Hello, World!")