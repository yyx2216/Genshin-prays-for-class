import json
from pypinyin import lazy_pinyin
import matplotlib.pyplot as plt
import os
add = os.path.abspath('..')
def l0():
    with open(f'{add}\log.txt') as f:
        word = f.read()
    with open(f'{add}\student.json') as j:
        bname = json.load(j)
        cname = list(set(bname))  #把相同的名字去掉
        cname.sort(reverse=True,key=lambda char: lazy_pinyin(char))  # 排序
        lst = []
        P = []
        numname = len(cname)
        for bname in cname:
            num = len(word.split(bname)) - 1
            allnum = len(word.split())
            p1 = (num / allnum*100)
            p = round(p1,3)
            lst.append(num)
            P.append(p)
    maxlst = max(lst)
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize = (12,7))
    rect = fig.patch
    rect.set_facecolor('#111111') #背景颜色
    ax=plt.gca()
    ax.patch.set_alpha(0)
    ax.spines['top'].set_visible(False) #去掉上边框
    ax.spines['right'].set_visible(False) #去掉右边框
    ax.spines['bottom'].set_color('#2997ff')
    ax.spines['left'].set_color('#2997ff')
    ax.tick_params(axis='y',labelsize=9, # y轴字体大小设置#
                    color='#23ff78',    # y轴标签颜色设置
                    labelcolor='#d5d1cc', # y轴字体颜色设置
                    direction='in' # y轴标签方向设置
                    )
    ax.tick_params(axis='x',
                    labelsize=9,
                    color='#23ff78',
                    labelcolor='#d5d1cc',
                    direction='in'
                    )
    plt.title(f'祈愿次数:{allnum}',color='#d5d1cc',fontsize=15)
    plt.barh(cname,lst,height=numname*0.02,color='#cecece') #条形颜色
    plt.xlim(0,maxlst*2.2)
    plt.ylim(-0.4,numname)
    for i, v in enumerate(lst):
        plt.text(v + maxlst/40, i + -0.34, str(v), color='#2997ff',fontsize=9)
    for i, v in enumerate(P):
        plt.text(0+maxlst/40, i + -0.34, f'{v}%', color='#2997ff',fontsize=8.5)
    plt.show()
valist = []
with open(f'{add}\student.json') as j:
    cname2 = json.load(j)
    bname2 = list(set(cname2))
def l1():
    bname2.sort(reverse=True,key=lambda char: lazy_pinyin(char))  # 排序
    num = len(cname2)
    num2 = len(bname2)
    dict={}
    for item in bname2:
        dict.update({item:cname2.count(item)})
    for val in dict.values():
        valist.append(val)
    new_list = [i/num for i in valist]
    list = [float('{:.4f}'.format(i)) for i in new_list]
    List = [i * 100 for i in list]
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize = (12,7))
    rect = fig.patch
    rect.set_facecolor('#111111') #背景颜色
    ax=plt.gca()
    ax.patch.set_alpha(0)
    ax.spines['top'].set_visible(False) #去掉上边框
    ax.spines['right'].set_visible(False) #去掉右边框
    ax.spines['bottom'].set_color('#2997ff')
    ax.spines['left'].set_color('#2997ff')
    ax.tick_params(axis='y',labelsize=9, # y轴字体大小设置#
                    color='#23ff78',    # y轴标签颜色设置
                    labelcolor='#d5d1cc', # y轴字体颜色设置
                    direction='in' # y轴标签方向设置
                    )
    ax.tick_params(axis='x',
                    labelsize=9,
                    color='#23ff78',
                    labelcolor='#d5d1cc',
                    direction='in'
                    )
    plt.barh(bname2,List,color='#cecece') #条形颜色
    maxlst = max(List)
    plt.xlim(0,maxlst*2.2)
    plt.ylim(-0.4,num2)
    for i, v in enumerate(List):
        plt.text(0+maxlst/40, i + -0.34, f'{v}%', color='#2997ff',fontsize=8.5)
    plt.show()
with open(f'{add}\\var.json','r') as var:
    vars = json.load(var)
    look_var = vars['l_var']
    if look_var == 0:
        l0()
    if look_var == 1:
        l1()