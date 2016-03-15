import json, csv
import os
import pandas


def salary_analysis(filedir):
    for each_job_set in os.listdir(filedir):
        print('正在分析 ' + each_job_set + ' 的数据...')
        for each_job_json in os.listdir(filedir + '/' + each_job_set):
            with open(filedir + '/' + each_job_set + '/' + each_job_json, 'r', encoding='utf-8') as f:
                job_list = f.readlines()
                f.flush()
                temp_str = job_list[0].replace('[', '').replace(']', '')
                if len(job_list) > 0 and temp_str != '':
                    str_json = json.loads(temp_str)
                    print(str_json)

                    # # 发布时间
                    # formatCreateTime = each_line['formatCreateTime']
                    #
                    # # 企业ID
                    # companyId = each_line['companyId']
                    #
                    # # 企业简称
                    # companyShortName = each_line['companyShortName']
                    #
                    # # 所属行业
                    # industryField = each_line['industryField']
                    #
                    # # 公司标签
                    # companyLabelList = each_line['companyLabelList']
                    #
                    # # 工作年限
                    # workYear = each_line['workYear']
                    #
                    # # 工作优势
                    # positionAdvantage = each_line['positionAdvantage']
                    #
                    # # 职位类别
                    # positionType = each_line['positionType']
                    #
                    # # 薪水
                    # salary = each_line['salary']
                    #
                    # # 发展级别
                    # financeStage = each_line['financeStage']
                    #
                    # # 地点
                    # city = each_line['city']
                    #
                    # # 教育程度
                    # education = each_line['education']
                    #
                    # # 职位名称
                    # positionName = each_line['positionName']
                    # print(salary)


if __name__ == '__main__':
    salary_analysis('H:/lagou')
