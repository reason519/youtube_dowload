from pytube import YouTube
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import bs4
import traceback
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return None
def fillVideoList(html):
    soup = BeautifulSoup(html, "html.parser")
    # for tr in soup.find('tbody').children:
    #     if isinstance(tr, bs4.element.Tag):
    #         tds = tr('td')
    #         ulist.append([tds[0].string, tds[1].string, tds[3].string])
    return soup.find_all("a",class_="pl-video-title-link")



def printVideoList(ulist):
    for v in ulist:
        print(v)

def downloadVideo(ulist):
    for v in ulist:
        print(v.attrs['href'])
        try:
            yt = YouTube('https://www.youtube.com/'+v.attrs['href'])
            yt.set_filename(yt.filename)
            #print(yt.get_videos())
            video=yt.filter(resolution='360p')
            video[0].download("H://guest//Videos")
        except:
            print(yt.filename)
            traceback.print_exc()

uinfo = []
url = 'https://www.youtube.com/playlist?list=PLwRcUH0jYu_ehApWDQogoq7x97MMYa14T'
html = getHTMLText(url)
if html is None:
    print(traceback.print_exc())
else:
    uinfo=fillVideoList(html)
    #printVideoList(uinfo)
    downloadVideo(uinfo)

#yt =YouTube('https://www.youtube.com//watch?v=T4y-QYJsLCQ&amp;t=6s&amp;list=PLwRcUH0jYu_ehApWDQogoq7x97MMYa14T&amp;index=1')
# 显示所有可以下载的视频文件
#pprint(yt.get_videos())

# 显示视频文件名
#print(yt.filename)

# 设置视频文件名
# yt.set_filename(yt.filename)
# video=yt.filter(resolution='720p')
# video[0].download("D://")


