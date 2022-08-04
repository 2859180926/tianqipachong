import requests
from bs4 import BeautifulSoup
import re
import json

def gettxt(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    with open('gtr.txt','w',encoding='utf-8') as f:
        f.write(r.text)
    return r.text

def readtxt(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def getInfo(txt):    
    newlist=[[ '日期','质量等级','AQI指数','当天AQI排名','PM25','PM10','So2','No2','Co','O3']]
    soup = BeautifulSoup(txt, 'html.parser')
    trs=soup.find_all('tr')
    for date in trs[1:]:
        sub_date=[date.text.split()]
        newlist+=sub_date
    return newlist

def Turnpage():
    url=r'http://www.tianqihoubao.com/aqi/beijing-202011.html'
    newlist=[]
    newsall=[]
    for i in range(202000,202012):
        if i==202000:
            txt=gettxt(url)
        else:
            url=r'http://www.tianqihoubao.com/aqi/beijing-'+str(i)+'.html'
            txt=gettxt(url)
            nlist=getInfo(txt)
            newsall.append(nlist)
    return newsall

def writethree():
    url=r'http://www.tianqihoubao.com/aqi/beijing-202011.html'
    newlist=[]
    newsall=[]
    for i in range(201900,201912):
        if i==201900:
            txt=gettxt(url)
        else:
            url=r'http://www.tianqihoubao.com/aqi/beijing-'+str(i)+'.html'
            txt=gettxt(url)
            nlist=getInfo(txt)
            newsall.append(nlist)
            b=newsall
    return b
    

def writeFile(file, data,b):
    with open(file, 'w', encoding='gbk') as f:
        for i in data:
            for j in i:
                f.write(','.join(j)+'\n')
                
def main():
    pass

if __name__ == '__main__':
    gettxt('http://www.tianqihoubao.com/aqi/beijing-202011.html')
    txt = readtxt('gtr.txt')
    print(getInfo(txt))
    a=Turnpage()
    print(a[0])
    b=writethree()
    print(b[0])
    writeFile('gtr.csv',a,b)
