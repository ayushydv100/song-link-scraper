from flask import Flask
from flask import request
import requests
import bs4
import requests,pprint,webbrowser
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return 'v 1.0.0'

@app.route('/link/')
def getLink():
    link = request.args.get('link')
    service = request.args.get('service')
    print(link)
    print(service)
    
    n = getApi(link)
    print(n)

    if n == 'spotify':
        link = list(link.split())
        link = link[len(link)-1:]
        link = ' ' .join(i for i in link)
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hi = soup.select('h1')
        hi
        hi[0]
        hi[0].getText()
        a = hi[0].getText()

        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hey = soup.select('h2')
        hey
        hey[0]
        b = hey[0].getText()
        b = b[3:]
        
        c = a + ' ' + b
        print(c)

    elif n == 'jiosaavn':
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hi = soup.select('h1')
        hi
        hi[0]
        hi[0].getText()
        a = hi[0].getText()

        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hey = soup.find('p',{'class':'u-color-js-gray-alt-light u-ellipsis@lg u-margin-bottom-tiny@sm'})
        hey
        hey = hey.getText()
        hey = list(hey.split())
        b = hey[2:]

        c = a +' '+' '  .join(i for i in b)
        print(c)
        
    elif n == 'gaana':
        link1=requests.get(link)
        parser=BeautifulSoup(link1.text,"html.parser")

        div=parser.find("a",class_="sng_c")

        a = div.getText()
    
        div1=parser.find("a",class_="mobile")
        b = div1.getText()
    
        c = a + ' ' + b


        print(c)
    
    elif n == 'applemusic':
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hi = soup.find('div',{'class':'song-name typography-label'})
        hi
        a = hi.getText()

        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hey = soup.select('h2')
        hey
        hey[0]
        b = hey[0].getText()
        b = b[23:]
        b = b[:23]
        
        c = a + ' ' + b
        print(c)

    if service == 'gaana':
        
        url="https://gaana.com/search/"+c
        print(url)
        link=requests.get(url)
        parser=BeautifulSoup(link.text,"html.parser")

        div=parser.find("div",class_="card_layout")
        sub_div=div.find_all("li",class_="list") 
        songs=[]

        for i in sub_div:
            urls=i.find("a").get("href")
            songs.append(urls)
        finalLink = "https://gaana.com"+songs[0]
        # print(finallink)
        
    elif service == 'apple music':
        url='https://google.com/search?q=' + c + '"music.apple.com"'
        link=requests.get(url)
        parser=BeautifulSoup(link.text,"html.parser")

        div=parser.find("div", id="main")
        sub_div=div.find("div", class_="kCrYT") 
        song=sub_div.find("a").get("href")
        
        song

        urls="https://google.com"+song

        urls

        link = urls
        data = requests.request("GET", link)
        finalLink = data.url
        # print(finalLink)
        
    elif service == 'jiosaavn':
        url='https://google.com/search?q=' + c + '"jiosaavn.com"'
        link=requests.get(url)
        parser=BeautifulSoup(link.text,"html.parser")

        div=parser.find("div", id="main")
        sub_div=div.find("div", class_="kCrYT") 
        song=sub_div.find("a").get("href")
        
        song

        urls="https://google.com"+song

        urls

        link = urls
        data = requests.request("GET", link)
        finalLink = data.url
        # print(finalLink)
        
    elif service == 'spotify':
        url='https://google.com/search?q=' + c + '"open.spotify.com"'
        link=requests.get(url)
        parser=BeautifulSoup(link.text,"html.parser")

        div=parser.find("div", id="main")
        sub_div=div.find("div", class_="kCrYT") 
        song=sub_div.find("a").get("href")
        
        song

        urls="https://google.com"+song

        urls

        link = urls
        data = requests.request("GET", link)
        finalLink = data.url
        # print(finalLink)
    return finalLink

def getAlbumArt():
    link = request.args.get('link')
    service = request.args.get('service')
    print(link)
    print(service)
    
    n = getApi(link)
    print(n)

    if n == 'spotify':
        link = list(link.split())
        link = link[len(link)-1:]
        link = ' ' .join(i for i in link)
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hi = soup.select('h1')
        hi
        hi[0]
        hi[0].getText()
        a = hi[0].getText()

        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hey = soup.select('h2')
        hey
        hey[0]
        b = hey[0].getText()
        b = b[3:]
        
        c = a + ' ' + b
        print(c)

    elif n == 'jiosaavn':
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hi = soup.select('h1')
        hi
        hi[0]
        hi[0].getText()
        a = hi[0].getText()

        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hey = soup.find('p',{'class':'u-color-js-gray-alt-light u-ellipsis@lg u-margin-bottom-tiny@sm'})
        hey
        hey = hey.getText()
        hey = list(hey.split())
        b = hey[2:]

        c = a +' '+' '  .join(i for i in b)
        print(c)
        
    elif n == 'gaana':
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hi = soup.select('h1')
        hi
        hi[0]
        hi[0].getText()
        hii = hi[0].getText()
        hii = hii.replace('|  ','')
        a = hii
        
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hey = soup.find('div',{'class':'composedBy'})
        hey
        hey = hey.getText()
        hey = hey.replace(',','')
        hey = list(hey.split())
        b = hey[2:]
        
        b = ' '.join(i for i in b)
        
        c = a + ' ' + b

        print(c)
    
    elif n == 'applemusic':
        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hi = soup.find('div',{'class':'song-name typography-label'})
        hi
        a = hi.getText()

        res = requests.get(link)
        type(res)
        res.text
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        type(soup)
        hey = soup.select('h2')
        hey
        hey[0]
        b = hey[0].getText()
        b = b[23:]
        b = b[:23]
        
        c = a + ' ' + b
        print(c)

    urlAlbumArt="https://www.google.com/search?tbm=isch&q="+c+"album+art"
    link=requests.get(urlAlbumArt)
    parser=BeautifulSoup(link.text,"html.parser")
    tab = parser.find("table",{"class":"TxbwNb"})
    img= tab.find("img").get("src")
    return img



def getApi(url):
    spotifyApi="spotify"
    gaanaApi="gaana"
    jiosaavnApi="jiosaavn"
    appleApi="applemusic"
    apiDict={"apple":appleApi,
        "spotify":spotifyApi,
        "jiosaavn":jiosaavnApi,
        "https://gaana":gaanaApi}

    urls=url.split(".")
    for i in apiDict:
        if i in urls or i.split() in url.split():
            return apiDict[i]

if __name__ == '__main__':
    app.run(debug=True)
