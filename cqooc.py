import requests
import time

# config
username = 'xxxx'    # your username used to login
ownerId = int(xxx)    # should be a integer
courseId = '93248234'
cookie_xsid = 'XXXXXXXX'    # find it in your browser after logging in
finish_time = '20191223'    # e.g. 20191223
parentId = '21342353'
postapi='http://www.cqooc.com/learnLog/api/add'

# session init
session = requests.Session()
session.cookies['xsid'] = cookie_xsid

def fuck(courseId, sectionId, chapterId):
    cookie = {
            'player':'1',
            'xsid': cookie_xsid
    }
    head={
            'Host': 'www.cqooc.com',
            'Content-Length': '159',
            'Origin': 'http://www.cqooc.com',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'http://www.cqooc.com/learn/mooc/structure?id=' + courseId,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
            'Cookie': 'xsid=' + cookie_xsid + '; player=1',
    }

    data={
        "username": username, "ownerId": ownerId, "parentId": parentId, "action": 0,
        "courseId": courseId, "sectionId": sectionId, "chapterId": chapterId, "category": "2",        
    }
    ps = requests.post(url=postapi, json=data, headers=head, timeout=None)
    #time.sleep(5)
    print('current sectionId: ' + sectionId)
    print('current chapterId: ' + chapterId)
    print(ps.reason)
    print(ps.cookies)
    print(ps.text)
    print('\n')
    #time.sleep(10)

def learn_course(courseId):
    endpoint = 'http://www.cqooc.com/json/chapter/lessons?courseId='+courseId
    j = session.get(endpoint).json()['data'][0]['body']
    for chapterId, sectionIds in j.items():
        for sectionId in sectionIds:
            print('starting', chapterId, sectionId)
            fuck(courseId, sectionId, chapterId)
            # print(fuck(courseId, sectionId, chapterId).text)


learn_course(courseId)
