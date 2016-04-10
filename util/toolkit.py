import xml.etree.ElementTree as et

from entity.job import Job


def readconfig(configpath):
    configmap = {}
    root = et.parse(configpath)
    for jobs in root.iterfind('type'):
        jobtype = jobs.get('name')
        joblist = list()
        for job in jobs:
            job_obj = Job(job.text, job.get('parameter'))
            joblist.append(job_obj)
        configmap[jobtype] = joblist
    return configmap


def normalize(value):
    if '-' in value:
        values = value.split('-')
        min = int(values[0].split('k')[0]) * 1000
        max = int(values[1].split('k')[0]) * 1000

        result = int((min + max) / 2)
    else:
        result = int(value.split('k')[0]) * 1000

    return result
