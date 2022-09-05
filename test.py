import requests
import time
import pymysql
import json
file = open('result.json', 'w', encoding='utf-8')
con = pymysql.connect(host='120.27.162.128', user='root', password='ggsggs555')
cursor = con.cursor()
cursor.execute('use apps;')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
           'Accept': '*/*',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Accept-Encoding': 'gzip, deflate, br',
           'Referer': 'https://appfigures.com/top-apps/google-play/united-states/top-overall',
           'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'keep-alive'}
sql = '''insert into app (name, developer) values ('{}', '{}');'''

url = 'https://appfigures.com/_u/api/ranks/snapshots?category=100&country=US&count=50&start={}&fields=results,id,entries,name,developer,developer_id,price,currency,storefront,vendor_identifier,category,subtype,timestamp,total_count'
for i in range(50, 700, 50):
    request_url = url.format(i)
    response = requests.get(url=request_url, headers=headers)
    data = response.json()
    time.sleep(2)
    for d in data['results']:
        for j in d['entries']:
            datas = {
                "name": j['name'],
                "developer": j['developer']
            }
            print(j['name'], '***', j['developer'])
            file.write(json.dumps(datas)+'\n')
            # try:
            #     cursor.execute(sql.format(j['name'].replace("'", "\\\'"), j['developer'].replace("'", "\\\'")))
            #     print(2)
            # except:
            #     print(sql.format(j['name'].replace("'", "\\\'"), j['developer'].replace("'", "\\\'")))
            #     exit(0)
con.commit()
