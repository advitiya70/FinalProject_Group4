from getData import getreport


def getall():
    return getreport(False)


def gettemprange(min, max):
    res = getreport(False)
    newres = []
    for i in res:
        if max >= int(i['temperature']) and min <= int(i['temperature']):
            newres.append(i)
    return newres


def getbyid(id):
    res = getreport(False)
    newres = []
    for i in res:
        if id == i['city']:
            newres.append(i)
    return newres
