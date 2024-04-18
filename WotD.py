from bs4 import BeautifulSoup
import requests

import textwrap

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

if __name__=="__main__":
    date, word, phonetic, word_type, definition = get_wotd()
    #date = date.split(', ')
    #date = ', '.join(date[1:])
    print(date)
    print(word)
    print(phonetic.lstrip())
    print(word_type)
    print(definition)