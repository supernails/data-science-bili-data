import pandas as pd
import numpy as  np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import cm
# 导入数据
blilist = pd.read_csv(r'data.csv')
blilist.head(10)

#mid 用户id
#name 昵称
#sign 签名
#sex 性别
#birthday 生日
#level 等级
#following 关注数
#fans 粉丝数
#vipType 会员类型
#vipStatus 会员状态

#数据的一些基本情况
blilist.describe()

blilist.info()

#数据各项属性数量
blilist.count()

#空值最多的属性
blilist.isnull().sum().sort_values(ascending = False).head(10)
#如图所见，最多的是birthday（生日）和sign（签名）

max_data = blilist.max()
min_data = blilist.min()
null_data = blilist.isnull().sum()
data_count = pd.DataFrame({'max_data':max_data,'min_data':min_data,'null_data':null_data})
print(data_count)

#清洗：过滤未填生日数据且等级为1的僵尸用户
blilist_clear = blilist[blilist['birthday'].notnull()*blilist['level']!= 1 ]
blilist_clear.head()

#处理生日月份 便于统计
blilist_clear['birthday']=pd.to_datetime(blilist_clear['birthday'],format='%m-%d').dt.month
blilist_clear.head()

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

blilist_clear['birthday'].hist(color='#66ccff', alpha=0.9,bins=23, figsize=(16,8))
plt.title("用户月份生日统计图")
plt.xlabel("生日月份")
plt.ylabel("人数")
plt.show()

#性别统计 账号默认性别为保密 男女由用户手动选择
blilist['sex'].value_counts()

plt.pie(blilist['sex'].value_counts(),
        explode = (0.1,0.2,0.3),labels=["保密","男","女"],
        autopct='%1.1f%%',
        shadow=True,
        radius=2,
        textprops={'fontsize': 20, 'color': 'black'})
plt.show()

blilist_clear_pie = blilist[blilist['sex']!= '保密' ]
plt.pie(blilist_clear_pie['sex'].value_counts(),
        explode = (0.1,0.2),labels=["男","女"],
        autopct='%1.1f%%',
        shadow=True,
        radius=2,
        textprops={'fontsize': 20, 'color': 'black'})
plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax=Axes3D(fig)
x=blilist['level']
y=blilist['fans']
z=blilist['following']
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.scatter(x,y,z, s=10, c='r', alpha=0.3)
ax.set_xlabel('等级', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('粉丝', fontdict={'size': 15, 'color': 'red'})
ax.set_zlabel('关注', fontdict={'size': 15, 'color': 'red'})

import jieba
from wordcloud import WordCloud
import wordcloud
import collections # 词频统计库
from PIL import Image # 图像处理库

#blilist_clear_word = blilist[blilist['sign']!= '' ]
#new_text = "".join(str(blilist_clear_word[['sign']]))

word = [i[0] for i in blilist[['name']].values]
#new_text = "".join(str(word))
#print(new_text)
mask = np.array(Image.open('a.jpg')) # 定义词频背景

# 文本分词
seg_list_exact = jieba.cut(str(word), cut_all = False) # 精确模式分词
object_list = []
remove_words = [' ',',','【','】','《','》','nan','的','啦','啊','呀','我','是','你'] # 自定义去除词库
for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表


# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(500) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

#wordcloud = WordCloud(font_path="simhei.ttf",background_color="white",mask=mask,max_words=200,max_font_size=500).generate(new_text)
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()

wc = wordcloud.WordCloud(
    background_color='white',
    font_path='simhei.ttf', # 设置字体格式
    mask=mask, # 设置背景图
    max_words=500, # 最多显示词数
    max_font_size=500 # 字体最大值
)


wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.figure(dpi=216)
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像