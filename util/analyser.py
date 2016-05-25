import jieba.analyse
import os


def analyse(strcontent, stopwordspath, userdictpath):
    # 加载用户词典
    jieba.load_userdict(userdictpath)
    # 加载停用词
    jieba.analyse.set_stop_words(stopwordspath)
    tags = jieba.analyse.extract_tags(strcontent, topK=20, withWeight=True, allowPOS=('n'))

    # 带词频
    for tag in tags:
        print(tag[0] + ',' + str(tag[1]))
    print('===========================')
    # 不带词频，仅用于生成TagCloud的...
    for tag in tags:
        print(tag[0], end=',')


def get_content(txtdir):
    content = []
    txts = os.listdir(txtdir)
    for each_txt in txts:
        with open(txtdir + os.sep + each_txt, mode='rt', encoding='utf-8') as f:
            str = "".join(f.readlines())
            content.append(str)
            f.close()

    return "".join(content)


if __name__ == '__main__':
    content_txt = get_content('D:\LagouJobInfo\lagou\details\网络爬虫')
    analyse(content_txt, 'C:/Users/XuLu/PycharmProjects/LagouJob/stopwords.txt',
            'C:/Users/XuLu/PycharmProjects/LagouJob/userdict.txt')
