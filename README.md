#Data analysis of [Lagou](http://www.lagou.com/)
![LagouIcon](http://pstatic.lagou.com/www/static/common/widgets/header_c/modules/img/logo_d0915a9.png)
###Main Function

1. scrape data from [Lagou](www.lagou.com), and know the latest info of Internet career

2. data analysis and visualize

3. crawl job details info and generate word cloud as __Job Impression__


###Install Prerequisition
1. Python Version >= 3.4
2. Third Party Library: 
  > pip install requests
  > pip install beautifulsoup4
  > pip install jieba
  > pip install openpyxl

###Basic Usage
1. clone this project from [github](https://github.com/EclipseXuLu/LagouJob.git)

2. change the path of __job.xml__ in lagouspider.py readconfig() method
   configmap = toolkit.readconfig(__YourLocalPath__)
    
3. run __lagouspider.py__ to get job data in JSON

4. run __excelhelper.py__ to generate every Excel file towards each job

5. run __jobdetailspider.py__ to get job recruitment details ----V1.3 updated

6. run __analyser.py__ to cut sentences, and return TOP20 hot words ----V1.3 updated

###Analysis Results
> ![Image1](https://pic2.zhimg.com/a0c42bc6bd7c8743687ba50305c85821_b.jpg)
> ![Image2](https://pic3.zhimg.com/f89ca5a008f8ad84a1a2121888aa10c2_b.jpg)
> ![Image3](https://pic1.zhimg.com/85b930c6aff823a3b8ee73973d20f274_b.jpg)
> ![Image4](https://pic2.zhimg.com/0ce1858e3f261f0a90e50e79bd057e8d_b.png)
> ![Image5](https://pic3.zhimg.com/3854e7ca5a8c53e5bb98a2ae3add4a8e_b.png)

For more information, please visit my answer at [Zhihu](https://www.zhihu.com/question/36132174/answer/94392659)
