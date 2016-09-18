# LagouJob
## data analysis of Lagou

![LagouIcon](http://pstatic.lagou.com/www/static/common/widgets/header_c/modules/img/logo_d0915a9.png)
###Main Function

1. scrape data from [Lagou](www.lagou.com), and know the latest info of Internet career

2. data analysis and visualize

3. crawl job details info and generate word cloud as __Job Impression__


###Install Prerequisition
1. Python Version >= 3.4
2. Third Party Library: 
  pip install requests
  pip install BeautifulSoup
  pip install jieba
  pip install openpyxl

###Basic Usage
1. clone this project from [github](https://github.com/EclipseXuLu/LagouJob.git)

2. change the path of __job.xml__ in lagouspider.py readconfig() method
    
    configmap = toolkit.readconfig('D:/Users/PythonProject/LagouJob/job.xml')
    
3. run __lagouspider.py__ to get job data in JSON

4. run __excelhelper.py__ to generate every Excel file towards each job

5. run __jobdetailspider.py__ to get job recruitment details ----V1.3 updated

6. run __analyser.py__ to cut sentences, and return TOP20 hot words ----V1.3 updated