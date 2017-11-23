# tianyuax-weibo-analysis
## 简介

爬取天喵2017年微博并进行分析。  

## 安装环境

- numpy

- jieba

- matplotlib

- wordcloud

- snownlp

## 功能

- weibo_spider

    爬取天猫2017年微博并保存所有文本到`weibo_text.txt`

- data_visualization.py
    对17年的所有微博发布时间做可视化分析，包括：

    - 月分布柱状图 `amount_month.png`
    - 天分布折现图`amount_day.png`

- weibo_nlp.py

    - 利用`wordcloud`制作词云图
    - 利用`snownlp`做情感分析

## 盲目分析

### 时间分布

根据以下的天分布图和月分布图可以看出，在6月发的微博最多，一共发了206条，在11月最少。之所以只有两条是因为在10月24日那天他的微博总数达到了9999条而他想一直保持这个数量，所以在这之后每发一条又删掉。回头再分析一下每个月的词频最高的是哪些词。

![天分布图](https://github.com/El-Chiang/tianyuax-weibo-analysis/blob/master/img/amount_day.png?raw=true)

![月分布图](https://github.com/El-Chiang/tianyuax-weibo-analysis/blob/master/img/amount_month.png?raw=true)

### 词云统计

再对他微博出现频率比较高的词语进行统计，可以大致罗列以下几类：

- 电子产品产品（最多）：iPhone iPad Mac SONY 索尼 Mac 耳机 键盘  手机 硬盘 希捷 降噪 蓝牙 BeatX Apple USB 米家 Intel NUC airpods...
- 信用卡与优惠券系列（第二多）：账单 中信 银联 叠加 信用卡 白金 JCB...
- 买买买系列：免息 购物车 快递 支付宝 立减 省钱 京东 下单
- 死宅系列：视频 正片 更新 女主  影评 食毕 电影 哔哩哔哩
- 就是只知道吃系列：炸鸡 汉堡 炒饭 肯德基 好吃 维导
- 还有些乱七八糟的主题：陈奕迅 知乎 抽奖 

![weibo_wc](https://github.com/El-Chiang/tianyuax-weibo-analysis/blob/master/img/weibo_wc.png?raw=true)

### 情感分析

这是AI分析的跟我没有关系，横轴情感值纵轴微博条数，情感值越低越消极（

![Sentiment Analysis](https://github.com/El-Chiang/tianyuax-weibo-analysis/blob/master/img/Sentiment%20Analysis.png?raw=true)

## 总结

In summary，这是一个经常丧里丧气，以研究信用卡与优惠券管理为乐，生活充斥着买买买和炸鸡，日常就是看剧追番看电影，很温软，的猫！