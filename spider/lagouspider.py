import requests
import json
import os
from util import toolkit

req_url = 'http://www.lagou.com/jobs/positionAjax.json?'
headers = {'content-type': 'application/json;charset=UTF-8'}


def scrapy(jobname):
    maxpagenum = \
        requests.post(req_url, params={'first': 'false', 'pn': 1, 'kd': jobname}, headers=headers).json()['content'][
            'totalPageCount']

    flag = True
    num = 1

    filedir = 'h:/' + jobname

    if os.path.exists(filedir) is not True or os.path.isdir(filedir) is not True:
        os.mkdir(filedir)

    while flag:
        payload = {'first': 'false', 'pn': num, 'kd': jobname}

        response = requests.post(req_url, params=payload, headers=headers)
        if num > maxpagenum:
            flag = False

        if response.status_code == 200:
            job_json = response.json()['content']['result']
            print(job_json)

            with open('h:/' + jobname + '/' + str(num) + '.json', 'wt', encoding='utf-8') as f:
                f.write(str(job_json))
                f.flush()
                f.close()

        else:
            print('connect error! url = ' + req_url)

        num += 1


if __name__ == '__main__':
    configmap = toolkit.readconfig('D:/Users/XuLu/PycharmProjects/LagouJob/job.xml')

    for item, value in configmap.items():
        for job in value:
            print('start crawl ' + str(job.pinyin) + ' ...')
            scrapy(job.pinyin)
