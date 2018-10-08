import schedule
import time

def job():
    from datetime import datetime
    import os

    print("於{}開始抓取資料".format(datetime.now()))
    load()
    print("於{}結束抓取資料\n".format(datetime.now()))
    os.system("git add .")
    os.system("git commit -m \"更新於{}\"".format(datetime.now()))
    os.system("git push -f origin master")
    os.system("git reset HEAD~1")

def load():
    import requests
    import json

    fstr = "{\n"
    for i in range(1, 369):
        r = requests.get('https://works.ioa.tw/weather/api/weathers/{}.json'.format(i))
        h = r.text
        j = json.loads(h)
        fstr += "\"{}\":[{},{},{},\"{}\"]".format(i,i,j['temperature'],j['humidity'],j['at'])
        if i != 368:
            fstr += ","
        fstr += '\n'

    fstr += '}'

    fo = open('data.json', 'w')
    fo.write(fstr)
    fo.close()

schedule.every(30).minutes.do(job)
#schedule.every().day.at("07:12").do(job)
#schedule.every().day.at("07:42").do(job)
#schedule.every().day.at("08:12").do(job)
job()

while True:
    schedule.run_pending()
    time.sleep(1)