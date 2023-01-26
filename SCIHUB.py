from GoogleScholar import *
from pyquery import PyQuery as pq
def download(KeyWords):
    KeyWords=KeyWords.replace(' ','+')
    #链接文件不存在，生成链接文件
    if not os.path.exists(PaperInfoAddr+KeyWords+'.csv'):
        print('没有获取到论文链接等信息，正在爬取......')
        search(KeyWords,saveFile=True)
    if os.path.exists(PaperInfoAddr+KeyWords+'.csv'):
        data=pd.read_csv(PaperInfoAddr+KeyWords+'.csv')
        titles=data[InfoColumns.TITLE].tolist()
        links=data[InfoColumns.LINK].tolist()
        if not os.path.exists(PaperAddr+KeyWords):
            os.mkdir(PaperAddr+KeyWords)
        index=0
        while index<len(links):
            SCIHUBPostItem['request']=links[index]
            try:
                rsp = requests.post(SCIHUB, data=SCIHUBPostItem, headers=SCIHUBHeaders)
            except:
                print('链接不存在或cookie过期')
                newCookie=input('请输入新Cookie')
                SCIHUBHeaders['cookie']=newCookie
                over=input('是否尝试原失败链接：(1:是，0：不是)')
                if over!='1':
                    index+=1
                continue
            html = pq(rsp.text)
            paperAddr = html('#pdf').attr('src')
            if paperAddr==None:
                print('第{}篇文章{}获取失败'.format(index+1,titles[index]))
                index+=1
                continue
            if 'http' not in paperAddr and 'https' not in paperAddr:
                paperAddr='https:'+paperAddr
            paperContent=requests.get(paperAddr,headers=PDFHeaders)
            paperFile=open(PaperAddr+KeyWords+'\\paper'+str(index+1)+'.pdf','wb')
            paperFile.write(paperContent.content)
            paperFile.close()
            print('正在获取第{}篇文章：{}'.format(index+1,titles[index]))
            index += 1
    else:
        print('获取论文信息失败，请检查网络或重设cookie')
parser=argparse.ArgumentParser()
parser.add_argument('--keyword',default='',type=str,help='搜索的关键字')
args=parser.parse_args()
download(args.keyword)
