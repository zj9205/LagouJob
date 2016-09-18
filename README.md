# LagouJob
## data analysis of Lagou

![LagouIcon](http://pstatic.lagou.com/www/static/common/widgets/header_c/modules/img/logo_d0915a9.png)
###Main Function

1. 利用爬虫获取[拉勾网](www.lagou.com)招聘数据，了解互联网行业最新职位动向

2. 统计分析与可视化

3. 对每个职位的详情数据进行二次抓取，进行分词、统计，获取标签云，生成对于每类职位的__职位印象__


###Install Prerequisition
1. Python Version >= 3.4
2. Third Party Library: 
  pip install requests
  pip install BeautifulSoup
  pip install jieba
  pip install openpyxl

###Basic Usage
1. clone this project from [github](https://github.com/EclipseXuLu/LagouJob.git)

2. change the path of __job.xml__ 

3. run __lagouspider.py__ to get job data in JSON

4. run __excelhelper.py__ to generate every Excel file towards each job

5. run __jobdetailspider.py__ to get job recruitment details ----V1.3 updated

6. run __analyser.py__ to cut sentences, and return TOP20 hot words ----V1.3 updated