#coding=utf-8
import re
import jieba.analyse
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread
from snownlp import SnowNLP
from wordcloud import ImageColorGenerator, WordCloud

del_words = ['虾米音乐', '分享图片', '分享自', '转发微博', '网页链接', '怪貓X亖號機', '分享.*的歌曲', '//@.*:']

def read_file(fname='tianyuax_weibo.txt'):
    all_text = []
    with open(fname, 'rb') as f:
        for line in f:
            text = re.sub('\[.*\]|\n', '', line.decode('utf-8'))
            for w in del_words:
                text = re.sub(w, '', text)
            all_text.append(text)
        f.close()
    return all_text

# 生成词云
def word2cloud(textlist):
    fulltext = ''
    isCN = 1
    back_coloring = imread("img/bg.png")
    cloud = WordCloud(font_path='font.ttf', # 若是有中文必须添加font.tff
            background_color="white",  # 背景颜色
            max_words=1800,  # 词云显示的最大词数
            mask=back_coloring,  # 背景图片
            max_font_size=100,  # 字体最大值
            random_state=42,
            width=1000, height=860, margin=2,  # 设置图片大小和词边距
            )
    for li in textlist:
        fulltext += ' '.join(jieba.analyse.extract_tags(li,topK=4))
    wc = cloud.generate(fulltext)
    image_colors = ImageColorGenerator(back_coloring)
    plt.figure("wordc")
    plt.imshow(wc.recolor(color_func=image_colors))
    wc.to_file('img/weibo_wc.png')

def snow_analysis(textlist):
    sentimentslist = []
    for li in textlist:
        s = SnowNLP(li)
        sentimentslist.append(s.sentiments)
    fig1 = plt.figure("sentiment")
    plt.hist(sentimentslist, bins=np.arange(0,1,0.02), color='#B28FCE')
    plt.xlabel('Sentiment Value')
    plt.ylabel('Weibo Amount')
    plt.savefig('img/Sentiment Analysis')

if __name__ == '__main__':
    all_text = read_file()
    word2cloud(all_text)
    snow_analysis(all_text)
