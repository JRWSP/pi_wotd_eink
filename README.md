# Word of the Day with E-Ink display and Raspberry Pi

Display word of the day from [Dictionary.com](https://www.dictionary.com/e/word-of-the-day/) when start running. 
Refresh again for a new word every day morning at 8am. 

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
   ExecStart=/usr/bin/python3 -u main.py
   WorkingDirectory=/home/pi/word-of-the-day
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

## Support
If this project help you reduce time to develop, you can give me a cup of coffee, or some beers so I can code more :)

<a href="https://www.buymeacoffee.com/jrwsp" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 30px !important;width: 108px !important;" ></a>
<a href='https://ko-fi.com/R5R5R7C6Y' target='_blank'><img height='30' style='border:0px;height:30px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
