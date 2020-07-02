from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import time


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def waitTime(request):
    return render(request, 'wait.html', {})

def optionselect(request):
    option = request.GET['option']
    qqNum = request.GET['qqNum']
    print(option)
    if qqNum == "":
        return render(request, 'error.html', {})
    if option == 'QQ':
        result = findQQ(qqNum)
        return render(request, 'findQQ.html', {'result': result, 'qqNum': qqNum})
    else:
        result = finQun(qqNum)
        return render(request, 'findQun.html', {'result': result, 'qqNum': qqNum})


def findQQ(qqNum):
    import pymssql
    conn = pymssql.connect(host='127.0.0.1:12356',
                           user='sa',
                           password='123456',
                           database='master',
                           charset='utf8')
    # qqNum = request.POST['qqNum']
    qqNum = qqNum
    ba = 1
    l = []
    for ku in range(1, 12):
        for i in range(100):
            a = "select * FROM [GroupData{}].[dbo].[Group{}]  where QQNum = '{}'".format(ku, ba, qqNum)
            ba = ba + 1
            l.append(a)
    cursor = conn.cursor()
    result = []
    i = 1
    for sql in l:
        print(sql)
        cursor.execute(sql)
        rs = cursor.fetchall()
        i += 1
        if rs is None:
            continue
        else:
            for item in rs:
                result.append(item)
    # return render(request, 'findQQ.html', {'result': result, 'qqNum': qqNum})
    return result


def finQun(qunNum):
    import pymssql
    conn = pymssql.connect(host='127.0.0.1:12356',
                           user='sa',
                           password='123456',
                           database='master',
                           charset='utf8')
    ba = 1
    l = []
    qunNum = qunNum
    for ku in range(1, 12):
        for i in range(100):
            a = "select * FROM [GroupData{}].[dbo].[Group{}]  where QunNum = '{}'".format(ku, ba, qunNum)
            ba = ba + 1
            l.append(a)
    cursor = conn.cursor()
    result = []
    for sql in l:
        print(sql)
        cursor.execute(sql)
        rs = cursor.fetchall()
        if not rs:
            continue
        else:
            for item in rs:
                result.append(item)
            break
    return result
