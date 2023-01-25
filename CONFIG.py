import os
NOWFILEPATH=os.path.dirname(__file__)
PARENTFILEPATH=os.path.dirname(os.path.dirname(__file__))
PaperInfoAddr=NOWFILEPATH+'\\data\\PaperInfo\\'
PaperAddr=NOWFILEPATH+'\\data\\Paper\\'
#PaperInfo文件夹中文件的列名
class InfoColumns():
    TITLE='title'
    LINK='link'
    AUTHOR='author'
    JOURNAL='journal'
    WEBSITE='website'
    ABSTRACT='abstract'
    REFERENCED='referenced'
#谷歌学术地址
GoogleScholar='https://scholar.google.com/'
#谷歌学术搜索
GoogleScholarSearch='https://scholar.google.com/scholar?'
#谷歌学术Headers，后续cookie尝试生成
GoogleScholarHeaders={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                      'cache-control': 'max-age=0',
                      'cookie':'GSP=LM=1674612470:S=DEe5KQBAcU31qkiT; NID=511=cr2nw8iFHBDtZNXDVyjcorGTuVfky7QZAkB3JfWjAA4JGLAeK-tNQ-NiU81HnVGIwmLlhVJs1YcevOCtLys2evkxGj5EJZFGHTVoz1-uHxrKVi5JqtcRTvquc9tpFdzIvXA4KMhiQggbKbX2krQecVaj0CkOepqCCUstZMg-9ao'}
GoogleEndStrList=['服务器错误','伺服器錯誤']
#SCIHUB地址
SCIHUB='https://sci-hubtw.hkvisa.net/'
#SCIHUB提交的表单
SCIHUBPostItem={
    'sci-hub-plugin-check': '',
    'request': 'https://iopscience.iop.org/article/10.1088/0305-4608/17/12/016/meta'
}
#SCIHUB Headers,后续cookie尝试生成
SCIHUBHeaders={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cache-control': 'max-age=0',
    'cookie':'__gads=ID=f948d23a1265423f-22cde03364d900ab:T=1674613224:RT=1674613224:S=ALNI_MYmHIP6BQMWuoQ3qu2oiIYgE3NOfQ; __gpi=UID=00000bac1de20add:T=1674613224:RT=1674613224:S=ALNI_MbL89vjMM_HX9ai2-pU3oX0wyOrOg'
}
PDFHeaders={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'
}
def strToDict(strInfo:str):
    lines=strInfo.split('\n')
    headers={}
    for line in lines:
        if len(line)==0:
            continue
        key,value=line.split(':')
        headers[key.strip()]=value.strip()
    print(headers)
    return headers