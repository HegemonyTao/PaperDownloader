#从列表中获取指定位置的值，找不到会返回空字符串
def safeIndex(array,i):
    if len(array)==0 or len(array)<i:
        return ""
    return array[i]
#判断当前网页是否已经到结束位置
def isEndUrl(html,tagStrList):
    for tagStr in tagStrList:
        if tagStr in html.text():
            return True
    return False
