from bs4 import BeautifulSoup
import requests

def get_wotd():
    url='https://www.dictionary.com/e/word-of-the-day/'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    wotd=soup.find(class_="wotd-item").get_text().split("\n")
    wotd=[item for item in wotd if item!=""]
    wotd=[wotd[i] for i in (0,1,2,7,8)]
    wotd[2] = wotd[2].strip() #clean big space
    return wotd

if __name__=="__main__":
    date, word, phonetic, word_type, definition = get_wotd()
    print(date)
    print(word)
    print(phonetic)
    print(word_type)
    print(definition)