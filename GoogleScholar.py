import os
import re
import requests
from utils import *
import pandas as pd
from CONFIG import *
from pyquery import PyQuery as pq
NOWFILEPATH=os.path.dirname(__file__)
PARENTFILEPATH=os.path.dirname(os.path.dirname(__file__))
def search(KeyWords,saveFile=False):
    InfoList=[]
    nowPage = 0
    while True:
        if nowPage==0:
            url = GoogleScholarSearch +'q='+KeyWords.replace(' ', '+')
        else:
            url=GoogleScholarSearch+'start='+str(nowPage*10)+'&q='+KeyWords.replace(' ', '+')
        print('正在爬取第' + str(nowPage + 1) + '页')
        nowPage += 1
        try:
            response = requests.get(url,headers=GoogleScholarHeaders)
        except:
            print('第'+str(nowPage)+'页爬取失败')
            continue
        html = pq(response.text)
        resultList=getInfo(html,url)
        if resultList==[]:
            if saveFile:
                data=pd.DataFrame(InfoList)
                data.to_csv(PaperInfoAddr+KeyWords.replace(' ', '+')+'.csv',index=None)
            return InfoList
        InfoList.extend(resultList)
#从html中获取到详细信息
def getInfo(html,url):
    if isEndUrl(html,GoogleEndStrList):
        return []
    contents = html('#gs_res_ccl_mid>div')
    for i in range(10):#允许重试10次
        if len(contents)==0:#Cookie过期，重新设置
            print("Ops!!!你的Cookie过期了，请到这个网站复制一下Cookie吧"+url)
            newCookie=input("请输入你复制好的Cookie吧：")
            GoogleScholarHeaders['cookie']=newCookie
            response=requests.get(url,headers=GoogleScholarHeaders)
            html=pq(response.text)
            contents = html('#gs_res_ccl_mid>div')
        else:
            break
    resultList = []
    for content in contents.items():
        linkAndTitle = content('div.gs_ri>h3>a')
        link = linkAndTitle.attr('href')
        title = linkAndTitle.text()
        if title == '':
            continue
        authorAndJournal = content('div.gs_ri > div.gs_a').text()
        authorAndJournalList = authorAndJournal.split('-')
        author = safeIndex(authorAndJournalList, 0).strip()
        journal = safeIndex(authorAndJournalList, 1).strip()
        website = safeIndex(authorAndJournalList, 2).strip()
        abstract = content('div.gs_ri > div.gs_rs').text()
        referenced = content('div.gs_ri > div.gs_fl').text()
        referenced = re.findall('被引用(.*?)次', referenced, re.S)
        referenced = safeIndex(referenced, 0).strip()
        resultList.append({
            InfoColumns.TITLE:title,
            InfoColumns.LINK:link,
            InfoColumns.AUTHOR:author,
            InfoColumns.JOURNAL:journal,
            InfoColumns.WEBSITE:website,
            InfoColumns.ABSTRACT:abstract,
            InfoColumns.REFERENCED:referenced
        })
    return resultList
#KeyWords='Curie temperature'
#result=search(KeyWords,saveFile=True)
