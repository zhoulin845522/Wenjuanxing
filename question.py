import requests
import urllib.request
from fake_useragent import UserAgent
import re
import random
import time
from question_information import question_url,question_coockie,submit_url,submit_times,createStr

requests.packages.urllib3.disable_warnings()
PostNum = 0


def Get_Headers():
    headers = {
        'Host': 'www.wjx.cn',
        'User-Agent': UserAgent().random,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': question_url,
        'Cookie': question_coockie,
        'X-Forwarded-For': Get_IP()
    }
    return headers


def Get_IP():
    headers = {
        'User-Agent': UserAgent().random
    }
    html = urllib.request.Request(url='https://www.xicidaili.com/nn/', headers=headers)
    html = urllib.request.urlopen(html).read().decode('utf-8')
    reg = r'<td>(.+?)</td>'
    reg = re.compile(reg)
    pools = re.findall(reg, html)[0:499:5]
    Random_IP = random.choice(pools)
    return Random_IP


def Auto_WjX():
    url = submit_url
    data = createStr().encode("utf-8").decode("latin1")
    r = requests.post(url, headers=Get_Headers(), data=data, verify=False)
    result = r.text[0:2]
    return result


def main():
    global PostNum
    for i in range(submit_times):
        result = Auto_WjX()
        if int(result) in [10]:
            print('[ Response : %s ]  ===> 提交成功！！！！' % result)
            PostNum += 1
        else:
            print('[ Response : %s ]  ===> 提交失败！！！！' % result)
        time.sleep(30)  # 设置休眠时间，这里要设置足够长的休眠时间
    print('脚本运行结束，成功提交%s份调查报告' % PostNum)  # 总结提交成功的数量，并打印


if __name__ == '__main__':
    main()
