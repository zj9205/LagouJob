import requests
from bs4 import BeautifulSoup


def auto_commit(answer):
    headers = {'content-type': 'application/json;charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'}

    payload = {'name': '徐璐', 'schsrc': '湖北工业大学', 'schdst': '武汉大学信息管理学院', 'course': '管理学[12]', 'major': '电子商务',
               'phone': '13207145966', 'email': '249048056@qq.com', 'zzscore': 63, 'wyname': '英语', 'wyscore': 75,
               'zyscore1': 108, 'zyscore2': 130, 'remark': '管理科学与工程、电子商务、情报学、计算机 等相关专业',
               'question': answer,
               'emuchuid': 0}

    response = requests.post('http://ntiaoji.kaoyan.com/post', data=payload, headers=headers)
    if response.status_code == 200 and '请输入' not in response.text:
        print('发布成功!!')
        # print(response.text)
    else:
        print('发布失败...')


def getanswer():
    req_url = 'http://ntiaoji.kaoyan.com/post'
    html = requests.get(req_url).text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='tiaoji-td-left')
    question = items[(len(items) - 1)].text

    if '除以' in question.split(':')[1]:
        num1 = int(question.split(':')[1].split('除以')[0])
        num2 = int(question.split(':')[1].split('除以')[1].split('等于')[0])
        devide = num1 // num2
        print('问题: ' + question.split(':')[1])
        print('自动回答: ' + str(devide))
        return devide

    elif '乘以' in question.split(':')[1]:
        num1 = int(question.split(':')[1].split('乘以')[0])
        num2 = int(question.split(':')[1].split('乘以')[1].split('等于')[0])
        result = num1 * num2
        print('问题: ' + question.split(':')[1])
        print('自动回答: ' + str(result))
        return result


if __name__ == '__main__':
    calc = getanswer()
    auto_commit(calc)
