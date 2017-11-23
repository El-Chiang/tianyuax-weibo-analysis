# coding=utf-8
import re
import time
import requests

url = 'https://m.weibo.cn/api/container/getIndex?display=0&retcode=6102&type=uid&value=1733474277&containerid=1076031733474277&page={}'
headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Host': 'm.weibo.cn',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '_T_WM=e25a28bec35b27c72d37ae2104433873; WEIBOCN_WM=3349; H5_wentry=H5; backURL=http%3A%2F%2Fm.weibo.cn%2F; SUB=_2A250zXayDeThGeVJ7VYV8SnJyTuIHXVUThr6rDV6PUJbkdBeLRDzkW1FrGCo75fsx_qRR822fcI2HoErRQ..; SUHB=0sqRDiYRHXFJdM; SCF=Ag4UgBbd7u4DMdyvdAjGRMgi7lfo6vB4Or8nQI4-9HQ4cLYm_RgdaeTdAH_68X4EbewMK-X4JMj5IQeuQUymxxc.; SSOLoginState=1506346722; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D3638527344076162%26luicode%3D10000011%26lfid%3D1076031239246050; H5_INDEX=3; H5_INDEX_TITLE=%E8%8A%82cao%E9%85%B1',
    'DNT': '1',
    'Connection': 'keep-alive',
}
all_source = []  # 保存所有微博来源
all_time = []  # 保存所有微博发送时间
all_text = []  # 保存所有微博内容
flag = 1
page = 1

while True:
    print('正在爬取第%s页' % page)
    try:
        req = requests.get(url=url.format(page), headers=headers)
        weibo_content = req.json()['cards']
    except:
        pass
    if req.status_code == 200:
        for i in weibo_content:
            try:
                weibo_text = re.sub('<.*?>', '', i['mblog']['text'])  # 文本内容
                weibo_source = i['mblog']['source']  # 来源
                weibo_time = i['mblog']['created_at']  # 时间
                if weibo_time[:4] == '2016':  # 如果时间为2016年，结束
                    flag = 0
                    break
                all_source.append(weibo_source)
                all_time.append(weibo_time)
                all_text.append(weibo_text)
            except:
                pass
    if flag == 0:
        break
    page += 1
    time.sleep(3)

# 将数据写入到文件
with open('tianyuax_weibo.txt', 'w+', encoding='utf-8') as f:
    for i in range(len(all_source)):
        f.writelines("[" + all_time[i] + " from: " +
                     all_source[i] + "] " + all_text[i] + '\n')
