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

def fuck_time():
    head={
        'Host': 'www.cqooc.com',
        'Content-Length': '30',
        'Connection': 'keep-alive',
        'Origin': 'http://www.cqooc.com',
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Referer': 'http://www.cqooc.com/learn/mooc/structure?id=' + courseId,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'player=1; xsid=' + cookie_xsid,
    }
    data = {
        "username": username
    }
    ps = requests.post(url='http://www.cqooc.com/account/session/api/login/time', json=data, headers=head, timeout=None)
    print(ps.text)

def get_log(sectionId):
    head={
        'Host': 'www.cqooc.com',
        'Connection': 'keep-alive',
        'Origin': 'http://www.cqooc.com',
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        'Accept': '*/*',
        'Referer': 'http://www.cqooc.com/learn/mooc/structure?id=' + courseId,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'player=1; xsid=' + cookie_xsid,
    }
    r = requests.get('http://www.cqooc.com/json/learnLogs?sectionId=' + sectionId + '&username=' + username, headers=head)
    print(r.text)

def fuck(courseId, sectionId, chapterId):
    head={
            'Host': 'www.cqooc.com',
            'Content-Length': '156',
            'Connection': 'keep-alive',
            'Origin': 'http://www.cqooc.com',
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'http://www.cqooc.com/learn/mooc/structure?id=' + courseId,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'player=1; xsid=' + cookie_xsid,
    }

    data={
        "action": 0, "category": 2, "chapterId": str(chapterId), "courseId": str(courseId), "ownerId": ownerId,
        "parentId": str(parentId), "sectionId": int(sectionId), "username": username
    }

    fuck_time()
    get_log(sectionId)
    time.sleep(2)
    get_log(sectionId)
    time.sleep(2)
    get_log(sectionId)
    time.sleep(2)
    fuck_time()
    time.sleep(1)
    ps = requests.post(url=postapi, json=data, headers=head, timeout=None)
    print('starting', chapterId, sectionId)
    print('current sectionId: ' + sectionId)
    print('current chapterId: ' + chapterId)
    print(ps.reason)
    print(ps.cookies)
    print(ps.text)
    print('\n')
    

def learn_course(courseId):
    endpoint = 'http://www.cqooc.com/json/chapter/lessons?courseId='+courseId
    j = session.get(endpoint).json()['data'][0]['body']
    for chapterId, sectionIds in j.items():
        for sectionId in sectionIds:
            fuck(courseId, sectionId, chapterId)
            # print(fuck(courseId, sectionId, chapterId).text)


learn_course(courseId)
