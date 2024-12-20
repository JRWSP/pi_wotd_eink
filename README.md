If this project helpful, you can donate me a cup of coffee, or some beers so I can code more :)

BTC: bc1q2zpmmlz7ujwx2ghsgw5j7umv8wmpchplemvhtu <br>
ETH: 0x80e98FcfED62970e35a57d2F1fefed7C89d5DaF4

<a href="https://www.buymeacoffee.com/jrwsp" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 30px !important;width: 108px !important;" ></a>
# Get smarter everyday by leaning Word of the Day.

Display a word of the day from [Dictionary.com](https://www.dictionary.com/e/word-of-the-day/) when start running. 
Refresh again for a new word every day morning at 8am. 

This project aim for simplicity. Only 1 micro-USB is needed. Once installed, just plug-and-learn, thanks to very low energy needed for both Raspberry Pi and e-ink display. The word will not disappear even if turned off.

![wotd picture](/wotd_picture.jpg)

# Hardware
- Raspberry Pi Zero W/WH (Zero 2 might work as well)
- Waveshare 2.13inch e-ink display (epd2in13_V4)
  - Black/white only. Tested with [touch version](https://www.waveshare.com/product/2.13inch-touch-e-paper-hat-with-case.htm) but should work on with [no-touch version](https://www.waveshare.com/product/2.13inch-e-paper-hat.htm). There is no touch function used.
- 32GB+ Micro SD card.
# Requirement
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
# Installation
This setup of Pi zero is based on [dr-mod](https://github.com/dr-mod/zero-btc-screen) repo. Thanks!
1. Turn on SPI via `sudo raspi-config`.
  ```
  Interfacing Options -> SPI
  ```
2. Install dependencies.
  ```
  sudo apt update
  sudo apt-get install python3-pip python3-pil python3-numpy git
  pip3 install RPi.GPIO spidev
  ```
3. Install Waveshare drivers.
  ```
  git clone https://github.com/waveshare/e-Paper.git ~/e-Paper
  pip3 install ~/e-Paper/RaspberryPi_JetsonNano/python/
  ```
4. Download WotD.
  ```
  git clone https://github.com/JRWSP/pi_wotd_eink.git ~/wotd
  ```
5. Run.
  ```
  python ~/wotd/WotD.py
  ```
# Autorun on reboot
1. Create a new service configuration file
  ```
   sudo nano /etc/systemd/system/btc-screen.service
  ```
2. Copy and paste the following into the service configuration file and change any settings to match your environment
  ```
   [Unit]
   Description=word-of-the-day
   After=network.target
  
   [Service]
   ExecStart=/usr/bin/python3 -u WotD.py
   WorkingDirectory=/home/pi/wotd
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=pi
  
   [Install]
   WantedBy=multi-user.target
  ```
3. Enable the service so that it starts whenever the RPi is rebooted
  ```
  sudo systemctl enable btc-screen.service
  ```
4. Start the service
  ```
  sudo systemctl start btc-screen.service
  ```
5. If you need to troubleshoot you can use the logging configurations of this program (mentioned below). Alternatively, you can check to see if there is any output in the system service logging.
  ```
  sudo journalctl -f -u btc-screen.service
  ```
