import xml.etree.ElementTree as et

from entity.job import Job


def readconfig(configpath):
    configmap = {}
    root = et.parse(configpath)
    for jobs in root.iterfind('type'):
        jobtype = jobs.get('name')
        joblist = list()
        for job in jobs:
            job_obj = Job(job.text, job.get('pinyin'))
            joblist.append(job_obj)
        configmap[jobtype] = joblist
    return configmap


if __name__ == '__main__':
    mapjobconfig = readconfig('D:/Users/XuLu/PycharmProjects/LagouJob/job.xml')

    for item, value in mapjobconfig.items():
        print(item, end=' : ')
        for each_item in value:
            print(each_item.name + '--' + each_item.pinyin, end='\t')
