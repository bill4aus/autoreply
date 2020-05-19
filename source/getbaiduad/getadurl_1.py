#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.proxy import Proxy,ProxyType

from selenium.common.exceptions import NoSuchElementException 
import time
from bs4 import BeautifulSoup
import sys
import io
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import urllib
import urllib2
import threading
import json
import random
import math
import urlparse

import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

import requests

import hashlib   
from selenium.webdriver.common.keys import Keys  

# from PIL import Image
from PIL import Image

# import pytesseract
# from kmeans import invokefunc

import threading
from selenium.webdriver.support.wait import WebDriverWait

# import damatu

m2 = hashlib.md5()   

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='adver',
        charset="utf8"
        )


print(conn)


# for x in xrange(1,10):
# 	pass

# 	cur = conn.cursor()
# 	# sqli="insert into ad values(%s,%s,%s,%s)"
# 	sqli="insert into ad(title,adurl,domain,status) values ('test','test','test',0)"
# 	print(cur.execute(sqli))
# 	conn.commit()

# 	cur.close()

# time.sleep(10)


isfinished=0
ip_proxy=''

ismobile=True
# ismobile=False

# browser=''
# browser = webdriver.Chrome()

keywords=[

# '人流 医院',
# '不孕不育 医院',
# '试管婴儿 医院',
# '月经不调 医院',
# '卵巢囊肿 医院',
# '子宫肌瘤 医院',
# '妇产 医院',
# '妇科 医院',
# '四维彩超 医院',
# '白带增多 医院',
# '精索静脉曲张 医院',
# '产科 医院',
# '包皮过长 医院',
# '前列腺炎 医院',
# '男科 医院',
# '性功能障碍 医院',
# '拔牙多少钱 医院',
# '口腔 医院',
# '牙科 医院',
# '烤瓷牙多少钱 医院',
# '整形 医院',
# '美白 医院',
# '玻尿酸 医院',
# '双眼皮 医院',
# '结石 医院',
# '美容 医院',
# '激光脱毛 医院',
# '腋臭 医院',
# '疤痕 医院',
# '耳鼻喉 医院',
# '皮肤病 医院',
# '隆鼻多少钱 医院',
# '乳腺增生 医院',
# '玻尿酸 医院',
# '增高 医院',
# '肛肠 医院',
# '肾病 医院',
# # '肌酐高 医院',
# '尿蛋白高 医院',
# '肝病 医院',
# '骨科 医院',
# '肿瘤 医院',
# '鼻炎 医院',
# '耳鼻喉 医院',
# '眼科 医院',
# '近视 手术 医院',
# '干眼 医院',
# '白内障 医院',
# '白癜风 医院',
# '咽炎 医院',
# '痔疮 医院',
# '过敏 医院',
# '祛疤 医院',
# # '康复 医院',
# '骨科 医院',
# '风湿 医院',
# '减肥 医院',
# '隆胸 医院',
# '抽脂 医院',
# '内分泌 医院',
# '失眠 医院',
# '胃病 医院',


"鼻炎医院排名",
"鼻炎去哪个医院好",
"最好的鼻炎医院",
"鼻炎 医院",
"鼻炎哪家医院能治好",
"整容医院排名",
"美容医院哪家最好",
"正规美容医院排行",
"正规医院可以激光脱毛",
"医院里有激光脱毛吗",
"激光脱毛 医院",
"激光脱毛哪个医院好",
"医院腋下脱毛要多少钱",
"医院全身脱毛要多少钱",
"激光脱毛 医院",
"耳鼻喉医院",
"耳鼻喉医院排名",
"同仁医院耳鼻喉的专家",
"地坛医院有耳鼻喉科吗",
"301医院鼻科怎么样",
"黄芪能降尿蛋白吗",
"孕妇尿蛋白高怎么办",
"孕妇尿蛋白高要多喝水",
"孕妇尿蛋白高怎样缓解",
"尿蛋白的原因及治疗",
"中医治疗尿蛋白高",
"拜博口腔医院怎么样",
"口腔专科医院排名",
"口腔医院哪家好些",
"口腔 外科",
"口腔医院 太原",
"文安 口腔",
"口腔医院",
"口腔医院 营业时间",
"怀孕白带会增多吗",
"白带突然增多是怀孕吗",
"来例假前白带会增多吗",
"白带突然增多无异味",
"白带增多",
"白带多是什么原因",
"白带多是怀孕了吗",
"白带发黄",
"不孕不育 比例",
"不孕不育21步排查法",
"不孕不育医院排名",
"不孕不育医院哪最好",
"紧急避孕药不孕不育",
"不孕不育检查基本费用",
"不孕不育",
"试管婴儿医院排名",
"省试管婴儿的排名",
"第三代试管婴儿医院",
"十大试管婴儿医院",
"做试管婴儿排名",
"看结石哪家医院好",
"专治结石的医院",
"私立医院 结石",
"24小时碎石的医院",
"结石治疗费用多钱",
"肾结石治疗费用多少钱",
"周末 碎石",
"医院周末有门诊吗",
"最好的骨科医院排名榜",
" 市骨科医院排名",
"最好骨科医院排名",
"骨科医院排名榜",
"骨科医院前十名",
"骨科 医院 ",
"骨科 医院 内乡",
"骨科哪个医院好",
"咽炎去医院做什么检查",
"治疗慢性咽炎的特效药",
"咽炎做什么检查",
"咽炎什么科室",
"慢性咽炎挂什么科室",
"去医院查咽炎要多少钱",
"中医能根治慢性咽炎吗",
"眼耳鼻喉医院",
"市肿瘤医院 pet ct",
"petct医院",
"肿瘤医院petct",
"肿瘤医院前十名",
"pet-ct 医院",
"乳腺结节怎样治疗好",
"恶性肿瘤治疗",
"第二人民医院妇科",
"传染病医院",
"三甲医院",
"中医 减肥 医院",
"减肥方法",
"健身 减肥",
"康复医院的特点",
"骨病康复医院",
"安康 医院",
"康复医院排名",
"疗养 医院",
"治疗白颠疯最好的医院",
"白殿疯费用表",
"看白殿疯到什么医院好",
"正规的白殿疯医院",
"二医院皮肤科地址",
"皮肤病 医院",
"治疗白瘢风医生",
"治失眠的三甲医院",
"失眠专科医院",
"专治失眠的医院",
" 失眠 医院",
"治失眠的好医院",
"失眠专科医院排名",
"失眠 医院  ",
"失眠症专科 瑞金医院",
"最权威的胃病医院",
"排名前十胃病医院",
"胃病 医院 知道",
"胃病医院排名",
"治胃病哪家医院好",
"胃病 医院 ",
"十大肛腸医院排名",
"内痔微创手术 医院",
"疤痕增生怎么治疗",
"治疗疤痕医院哪家好",
"疤痕体质",
"祛疤痕的药膏",
"祛疤痕哪家医院好",
"韩式整形医院",
"八大处整形外科医院",
"整形医院",
"整形医院排名前十",
" 整形医院",
"最好整形医院",
"八大处整容医院",
"白内障手术费多少钱",
"白内障免费治疗的医院",
"白内障医院排名",
"治白内障哪家医院好",
"县级医院有生长激素吗",
"生长激素可以长高吗",
"生长激素多少钱一针",
"生长激素价格表",
"医院打生长激素",
"去医院打生长激素",
"卵巢囊肿 医院",
"附件囊肿哪家医院好",
"卵巢囊肿哪个医院最好",
"治疗卵巢囊肿最好医院",
"治疗卵巢囊肿要多少钱",
"卵巢囊肿的手术指征",
"性功能障碍性疾病",
"性功能障碍怎么治疗",
"性功能障碍吃什么药好",
"性功能障碍的缩写",
"性功能障碍具体表现",
"近视手术医院排名",
"近视手术后遗症",
"近视手术最佳年龄",
"近视眼手术利与弊",
"近视手术吧",
"激光近视手术价格表",
"最有名的隆胸医院",
"大连那个医院隆胸好",
"隆胸 拍片看出来",
"整容医院",
"丰胸医院哪家好",
"假体隆胸 永久",
"看乳腺增生哪医院好",
"乳腺增生 医院 ",
"乳腺科医院排名",
"乳腺增生 哪个科",
"乳腺增生治好的表现",
"乳腺增生哪家医院好",
"乳腺科哪个医院好",
"小孩 医院 如何挂号",
"同仁医院",
"耳鼻喉科",
"耳鼻喉医院",
"耳鼻喉医院排名",
"天津 耳鼻喉",
"八大处整形隆鼻多少钱",
"做鼻子大概多少钱",
"永久隆鼻要多少钱",
"玻尿酸多少钱一支",
"无痛人流要多少钱",
"附属第一医院隆鼻",
"最知名隆鼻医院",
"假体隆鼻",
"皮肤病哪家医院好",
"人民医院皮肤科怎么样",
"皮肤病 哪家医院好",
"最好皮肤医院排名",
"国家皮肤医院",
"皮肤病哪个医院好",
"熊猫血 医院",
"子宫肌瘤怎么治最好",
"子宫肌瘤哪家医院好",
"子宫肌瘤手术住院几天",
"治疗子宫肌瘤哪家医院好",
"什么是子宫肌瘤",
"子宫肌瘤图片",
"甲级眼科医院",
"儿科医院 眼科 急症",
"眼科医院排名",
"看眼科的医院",
"眼科医院地址",
"牙科医院排名",
"牙科 医院 沈阳",
"牙科 医院 吉祥物",
"牙科诊所 医院哪个靠谱",
"公立医院 牙科",
"牙科三甲医院",
"最好口腔医院排名",
"妇产科正规医院",
" 医院 妇产 好",
" 妇产 医院",
"妇产科医院咨询",
"抽脂 医院 ",
"抽脂哪个医院好",
"抽脂 医院 公立 ",
"三甲医院有抽脂吗",
"西南医院",
"中山男性医院",
"包茎切割医院",
"医院等级划分标准",
"妇科医院",
"人流 医院 ",
"人工流产  医院",
"妇科医院排行榜",
"海淀医院人流价格",
"什么情况下要住院人流",
"流产的医院哪家好",
"三甲医院人流多少钱",
"月经不调去哪家医院",
"月经不调去哪个医院",
"月经不调  医院",
" 月经不调 医院",
"看月经不调哪个医院好",
"月经不调中医院",
"月经不调医院挂哪个科",
"四维彩超预约",
"三甲医院 玻尿酸 ",
"正规玻尿酸一般多少钱",
"打了假的玻尿酸会怎样",
"玻尿酸下巴",
"鼻子打玻尿酸对比照片",
"假的玻尿酸是什么症状",
"工作室打玻尿酸靠谱么",
"看风湿的专科医院",
" 风湿免疫科 医院",
"风湿 医院排名",
" 风湿 医院排名",
"风湿去医院检查什么",
"主治风湿的医院",
"医院 类风湿科",
"男科医院哪家最好",
"正规男科",
" 男科 排名",
"最权威的男科医院",
"男科医院",
"医院美白皮肤",
"美白的医院在哪里",
"医院牙齿美白多少钱",
"医院有哪些美白方法",
"医院美白价格",
"皮肤美白医院",
"医院开的美白",
"精索静脉曲张 手术 ",
"精索静脉曲张能自愈",
"精索静脉曲张",
"精索曲张 手术",
"肾病医院排名",
"肾病哪个医院最好",
"肾病 医院主任医师",
"医院治疗肾病",
"肾病医院",
"看肾病最权威医院",
"国内治痔疮最好的医院",
"痔疮医院排名",
"肛肠科最好的医院",
"痔疮医院排名",
"私立医院治痔疮",
"看痔疮多少钱啊",
"注射隆胸修复医院",
"哪家医院治疗疤痕修复",
"痘坑怎么修复",
"烧伤疤痕修复 医院",
"疤痕修复  医院",
"双眼皮修复的医院",
"妇产科医院排名",
"在线产科医院",
"产科医生 电视剧",
"眼干眼涩用什么眼药水",
"眼干眼涩是什么原因",
"医院拔牙  多少钱",
"医院儿童拔牙视频",
"医院是怎么拔牙的",
"拔牙后多久可以吃东西",
"肝病那医院看的好",
"丙肝 医院",
"广东省三甲肝病医院",
"肝胆医院 安亭",
"治疗肝病最好的医院",
"十大肺科医院排名",
"治疗肝医院排名",
"去医院检查丙肝",
"三甲医院割双眼皮流程",
"双眼皮医院排名",
"做双眼皮医院排行榜",
"割双眼皮 价格",
"八大处双眼皮医生排行",
"双眼皮著名医生",
"肌酐高 症状 ",
"肌酐和尿酸偏高的原因",
"不同年龄段肌酐正常值",
"肌肝高了怎么治疗",
"各个年龄的肌酐",
"肌酐400 透析",
"中医骨科医院排名",
"全烤瓷牙多少钱一颗",
"烤瓷牙和全瓷牙区别",
"全瓷牙多少钱一颗2017",
"全瓷牙和烤瓷牙哪个好",
"种植牙多少钱一颗",
"烤瓷牙和种植牙哪样好",
"牙套多少钱",
"去狐臭的正规医院",
"省立医院 腋臭",
"狐臭权威医院",
" 最好 外科医院",
"前列腺最好的医院",
"前列腺炎 治",
"中医治疗前列腺炎",
"年轻人 前列腺炎 ",
"前列腺炎相关检查",
"治过敏最好的医院",
"过敏专科医院",
"过敏去哪家医院看",
"过敏去哪个医院",
"过敏 医院",
"过敏去哪家医院最好",
"过敏去医院做什么检查",
"过敏急诊挂什么科",
"内分泌科哪家医院好",
"内分泌专科医院",
"内分泌 医院",
"协和医院 妇科内分泌",
"协和医院内分泌科专家",
"301医院内分泌科专家",
"协和内分泌科专家",
"协和内分泌科主任",
"治疤痕最好的医院",
"疤痕修复三甲医院",
"公立疤痕医院排名",
"疤痕医院",
"疤痕医院排名",
"10年的疤痕怎么去除",
"耳鼻喉 医院 咽炎",
"看鼻炎哪家医院",
"嗅觉失灵哪家医院",
"卫生部试管婴儿医院",
"第三代试管最权威医院",
"试管婴儿专科医院",
"试管婴儿 医院",
"试管婴儿私人医院排名",
"乳腺增生 最好医院",
"乳腺增生 医院 ",
"看乳腺哪家医院好",
"乳腺增生的医院",
"哪个医院乳腺科好",
"乳腺科 医院排名",
"牙科 医院 ",
"口腔粘膜科哪个医院好",
"口腔医院哪个好",
"胃病的症状",
"看头疼最好的医院",
"胃病什么科",
"治疗胃病的最佳方法",
"胃病吃什么食物好",
"胃病吃什么药",
"月经不调哪个医院最好",
"去检查月经不调多少钱",
"月经没来去医院咋检查",
"月经期间去医院查什么",
"痔疮哪家医院治疗的好",
"痔疮交道口医院",
"隆胸哪家医院好",
"隆胸多少钱",
"隆胸视频",
"假体隆胸",
"隆胸硅胶",
"隆胸手术",
"注射隆胸",
"卵巢囊肿手术方式",
"治疗骨癌哪个医院最好",
"开白内障哪家医院好",
"哪里医院眼科比较好",
"白内障手术失败 眼镜",
"口腔保险",
"风湿",
"包茎",
"无痛人流 乙肝",
"医院 修复 角质层 ",
"创伤修复医院",
"十佳前列腺医院",
"前列腺哪家医院最权威",
"前列腺炎三甲医院",
"做狐臭哪家医院好",
"腋臭 医院 ",
"腋臭看什么门诊",
"11个除狐臭简单的方法",
"治疗骨质增生",
"医院怎么检查出狐臭",
"狐臭怎么彻底去除",
"看男科哪个医院好",
"男性 孕检 医院",
"2017医院排名榜",
"减肥医院哪家好",
"减肥医院  价格",
"最好中医医院排名",
"肿瘤医院排名",
"恶性肿瘤治",
"试管婴儿医院排名",
"割双眼皮医院",
"去眼袋手术医院",
"治疗眼袋医院",
"哪家医院做双眼皮最好",
"治疗尿蛋白最好的医院",
"肾虚 尿蛋白高",
"尿蛋白高是怎么回事",
" 肾病医院十大排名",
"肾病 医院",
"肾病比较好的医院",
"肝病医院",
"肝病权威医院",
"治痔疮去哪个医院",
"治痔疮最好医院",
"整形外科 医院排名",
"痤疮  医院",
"皮肤医院美白",
"全身激光美白",
"美白牙齿的价格",
"全身美白 医院",
"美白针",
"鼻炎医院哪家好",
"鼻炎专科医院",
"最权威的口腔医院",
"神经康复医院",
"人流费用",
"风湿医院",
"做风湿检查",
"男科医院哪家好",
"最好疤痕医院排名",
"疤痕医院排名榜",
"激光祛疤",
"最好的疤痕治疗",
"去疤痕最好的医院",




# '传染病 医院',
]
# keywords_bak=[]
word_count=0

# 城市名称
china_city_list=[

# '北京',
# '天津',
# '沈阳',
# '长春',
# '哈尔滨',
# '上海',
# '南京',
# '武汉',
# '广州',
# '重庆',
# '成都',
# '西安',
# '石家庄',
# '唐山',
# '太原',
# '包头',
# '大连',
# '鞍山',
# '抚顺',
# '吉林',
# '齐齐哈尔',
# '徐州',
# '杭州',
# '福州',
# '南昌',
# '济南',
# '青岛',
# '淄博',
# '郑州',
# '长沙',
# '贵阳',
# '昆明',
# '兰州',
# '乌鲁木齐',
# '邯郸',
# '保定',
# '张家口',
# '大同',
# '呼和浩特',
# '本溪',
# '丹东',
# '锦州',
# '阜新',
# '辽阳',
# '鸡西',
# '鹤岗',
# '大庆',
# '伊春',
# '佳木斯',
# '牡丹江',
# '无锡',
# '常州',
# '苏州',
# '宁波',
# '合肥',
# '淮南',
# '淮北',
# '厦门',
# '枣庄',
# '烟台',
# '潍坊',
# '泰安',
# '临沂',
# '开封',
# '洛阳',
# '平顶山',
# '安阳',
# '新乡',
# '焦作',
# '黄石',
# '襄樊',
# '荆州',
# '株洲',
# '湘潭',
# '衡阳',
# '深圳',
# '汕头',
# '湛江',
# '南宁',
# '柳州',
# '西宁',
# '秦皇岛',
# '邢台',
# '承德',
# '沧州',
# '廊坊',
# '衡水',
# '阳泉',
# '长治',
# '乌海',
# '赤峰',
# '营口',
# '盘锦',
# '铁岭',
# '朝阳',
# '葫芦岛',
# '四平',
# '辽源',
# '通化',
# '白山',
# '松原',
# '白城',
# '双鸭山',
# '七台河',
# '南通',
# '连云港',
# '淮阴',
# '盐城',
# '扬州',
# '镇江',
# '泰州',
# '温州',
# '嘉兴',
# '湖州',
# '绍兴',
# '台州',
# '芜湖',
# '蚌埠',
# '马鞍山',
# '铜陵',
# '安庆',
# '阜阳',
# '泉州',
# '漳州',
# '南平',
# '龙岩',
# '景德镇',
# '萍乡',
# '九江',
# '新余',
# '东营',
# '济宁',
# '威海',
# '日照',
# '莱芜',
# '德州',
# '鹤壁',
# '濮阳',
# '许昌',
# '漯河',
# '南阳',
# '商丘',
# '十堰',
# '宜昌',
# '鄂州',
# '荆门',
# '孝感',
# '黄冈',
# '邵阳',
# '岳阳',
# '常德',
# '益阳',
# '郴州',
# '永州',
# '怀化',
# '韶关',
# '珠海',
# '佛山',
# '江门',
# '茂名',
# '肇庆',
# '惠州',
# '梅州',
# '阳江',
# '东莞',
# '中山',
# '潮州',
# '桂林',
# '梧州',
# '贵港',
# '海口',
# '自贡',
# '攀枝花',
# '泸州',
# '德阳',
# '绵阳',
# '广元',
# '遂宁',
# '内江',
# '乐山',
# '南充',
# '宜宾',
# '六盘水',
# '遵义',
# '曲靖',
# '铜川',
# '宝鸡',
# '咸阳',
# '汉中',
# '白银',
# '天水',
# '银川',
# '石嘴山',
# '克拉玛依',
# '晋城',
# '朔州',
# '通辽',
# '黑河',
# '宿迁',
# '金华',
# '衢州',
# '舟山',
# '黄山',
# '滁州',
# '宿州',
# '巢湖',
# '六安',
# '莆田',
# '三明',
# '鹰潭',
# '赣州',
# '聊城',
# '三门峡',
# '信阳',
# '咸宁',
# '张家界',
# '娄底',
# '汕尾',
# '河源',
# '清远',
# '揭阳',
# '云浮',
# '北海',
# '防城港',
# '钦州',
# '玉林',
# '三亚',
# '达州',
# '玉溪',
# '渭南',
# '延安',
# '榆林',
# '嘉峪关',
# '金昌',
# '吴忠',
# '辛集',
# '藁城',
# '晋州',
# '新乐',
# '鹿泉',
# '遵化',
# '丰南',
# '迁安',
# '武安',
# '南宫',
# '沙河',
# '涿州',
# '定州',
# '安国',
# '高碑店',
# '泊头',
# '任丘',
# '黄骅',
# '河间',
# '霸州',
# '三河',
# '冀州',
# '深州',
# '古交',
# '潞城',
# '高平',
# '忻州',
# '原平',
# '孝义',
# '离石',
# '汾阳',
# '榆次',
# '介休',
# '临汾',
# '侯马',
# '霍州',
# '运城',
# '永济',
# '河津',
# '霍林郭勒',
# '海拉尔',
# '满洲里',
# '扎兰屯',
# '牙克石',
# '根河',
# '额尔古纳',
# '乌兰浩特',
# '二连浩特',
# '锡林浩特',
# '集宁',
# '丰镇',
# '东胜',
# '临河',
# '新民',
# '瓦房店',
# '普兰店',
# '庄河',
# '海城',
# '东港',
# '凤城',
# '凌海',
# '北宁',
# '盖州',
# '大石桥',
# '灯塔',
# '铁法',
# '开原',
# '北票',
# '凌源',
# '兴城',
# '九台',
# '榆树',
# '德惠',
# '蛟河',
# '桦甸',
# '舒兰',
# '磐石',
# '公主岭',
# '双辽',
# '梅河口',
# '集安',
# '临江',
# '洮南',
# '大安',
# '延吉',
# '图们',
# '敦化',
# '珲春',
# '龙井',
# '和龙',
# '阿城',
# '双城',
# '尚志',
# '五常',
# '讷河',
# '虎林',
# '密山',
# '铁力',
# '同江',
# '富锦',
# '绥芬河',
# '海林',
# '宁安',
# '穆棱',
# '北安',
# '五大连池',
# '绥化',
# '安达',
# '肇东',
# '海伦',
# '江阴',
# '宜兴',
# '锡山',
# '新沂',
# '邳州',
# '溧阳',
# '金坛',
# '武进',
# '常熟',
# '张家港',
# '昆山',
# '吴江',
# '太仓',
# '吴县',
# '启东',
# '如皋',
# '通州',
# '海门',
# '淮安',
# '东台',
# '大丰',
# '仪征',
# '高邮',
# '江都',
# '丹阳',
# '扬中',
# '句容',
# '兴化',
# '靖江',
# '泰兴',
# '姜堰',
# '萧山',
# '建德',
# '富阳',
# '余杭',
# '临安',
# '余姚',
# '慈溪',
# '奉化',
# '瑞安',
# '乐清',
# '海宁',
# '平湖',
# '桐乡',
# '诸暨',
# '上虞',
# '嵊州',
# '兰溪',
# '义乌',
# '东阳',
# '永康',
# '江山',
# '温岭',
# '临海',
# '丽水',
# '龙泉',
# '桐城',
# '天长',
# '明光',
# '亳州',
# '界首',
# '宣州',
# '宁国',
# '贵池',
# '福清',
# '长乐',
# '永安',
# '石狮',
# '晋江',
# '南安',
# '龙海',
# '邵武',
# '武夷山',
# '建瓯',
# '建阳',
# '漳平',
# '宁德',
# '福安',
# '福鼎',
# '乐平',
# '瑞昌',
# '贵溪',
# '瑞金',
# '南康',
# '宜春',
# '丰城',
# '樟树',
# '高安',
# '上饶',
# '德兴',
# '吉安',
# '井冈山',
# '临川',
# '章丘',
# '胶州',
# '即墨',
# '平度',
# '胶南',
# '莱西',
# '滕州',
# '龙口',
# '莱阳',
# '莱州',
# '蓬莱',
# '招远',
# '栖霞',
# '海阳',
# '青州',
# '诸城',
# '寿光',
# '安丘',
# '高密',
# '昌邑',
# '曲阜',
# '兖州',
# '邹城',
# '新泰',
# '肥城',
# '文登',
# '荣成',
# '乳山',
# '乐陵',
# '禹城',
# '临清',
# '滨州',
# '菏泽',
# '巩义',
# '荥阳',
# '新密',
# '新郑',
# '登封',
# '偃师',
# '舞钢',
# '汝州',
# '林州',
# '卫辉',
# '辉县',
# '济源',
# '沁阳',
# '孟州',
# '禹州',
# '长葛',
# '义马',
# '灵宝',
# '邓州',
# '永城',
# '周口',
# '项城',
# '驻马店',
# '大冶',
# '丹江口',
# '枝城',
# '当阳',
# '枝江',
# '老河口',
# '枣阳',
# '宜城',
# '钟祥',
# '应城',
# '安陆',
# '广水',
# '汉川',
# '石首',
# '洪湖',
# '松滋',
# '麻城',
# '武穴',
# '恩施',
# '利川',
# '随州',
# '仙桃',
# '潜江',
# '天门',
# '浏阳',
# '醴陵',
# '湘乡',
# '韶山',
# '耒阳',
# '常宁',
# '武冈',
# '汩罗',
# '临湘',
# '津',
# '沅江',
# '资兴',
# '洪江',
# '冷水江',
# '涟源',
# '吉首',
# '番禺',
# '花都',
# '增城',
# '从化',
# '乐昌',
# '南雄',
# '潮阳',
# '澄海',
# '顺德',
# '南海',
# '三水',
# '高明',
# '台山',
# '新会',
# '开平',
# '鹤山',
# '恩平',
# '廉江',
# '雷州',
# '吴川',
# '高州',
# '化州',
# '信宜',
# '高要',
# '四会',
# '惠阳',
# '兴宁',
# '陆丰',
# '阳春',
# '英德',
# '连州',
# '普宁',
# '罗定',
# '岑溪',
# '东兴',
# '桂平',
# '北流',
# '凭祥',
# '合山',
# '贺州',
# '百色',
# '河池',
# '宜州',
# '通什',
# '琼海',
# '儋州',
# '琼山',
# '文昌',
# '万宁',
# '东方',
# '江津',
# '合川',
# '永川',
# '南川',
# '都江堰',
# '彭州',
# '邛崃',
# '崇州',
# '广汉',
# '什邡',
# '绵竹',
# '江油',
# '峨眉山',
# '阆中',
# '华蓥',
# '万源',
# '雅安',
# '西昌',
# '巴中',
# '资阳',
# '简阳',
# '清镇',
# '赤水',
# '仁怀',
# '铜仁',
# '兴义',
# '毕节',
# '安顺',
# '凯里',
# '都匀',
# '福泉',
# '安宁',
# '宣威',
# '昭通',
# '楚雄',
# '个旧',
# '开远',
# '思茅',
# '景洪',
# '大理',
# '保山',
# '瑞丽',
# '潞西',
# '日喀则',
# '兴平',
# '韩城',
# '华阴',
# '安康',
# '商州',
# '玉门',
# '酒泉',
# '敦煌',
# '张掖',
# '武威',
# '平凉',
# '西峰',
# '临夏',
# '合作',
# '格尔木',
# '德令哈',
# '青铜峡',
# '灵武',
# '吐鲁番',
# '哈密',
# '昌吉',
# '阜康',
# '米泉',
# '博乐',
# '库尔勒',
# '阿克苏',
# '阿图什',
# '喀什',
# '和田',
# '奎屯',
# '伊宁',
# '塔城',
# '乌苏',
# '阿勒泰',
# '北京',
# '北京',
# '天津',
# '天津',
# '石家庄',
# '唐山',
# '秦皇岛',
# '邯郸',
# '邢台',
# '保定',
# '张家口',
# '承德',
# '沧州',
# '廊坊',
# '衡水',
# '辛集',
# '藁城',
# '晋州',
# '新乐',
# '鹿泉',
# '遵化',
# '丰南',
# '迁安',
# '武安',
# '南宫',
# '沙河',
# '涿州',
# '定州',
# '安国',
# '高碑店',
# '泊头',
# '任丘',
# '黄骅',
# '河间',
# '霸州',
# '三河',
# '冀州',
# '深州',
# '太原',
# '大同',
# '阳泉',
# '长治',
# '晋城',
# '朔州',
# '古交',
# '潞城',
# '高平',
# '忻州',
# '原平',
# '孝义',
# '离石',
# '汾阳',
# '榆次',
# '介休',
# '临汾',
# '侯马',
# '霍州',
# '运城',
# '永济',
# '河津',
# '呼和浩特',
# '包头',
# '乌海',
# '赤峰',
# '通辽',
# '霍林郭勒',
# '海拉尔',
# '满洲里',
# '扎兰屯',
# '牙克石',
# '根河',
# '额尔古纳',
# '乌兰浩特',
# '二连浩特',
# '锡林浩特',
# '集宁',
# '丰镇',
# '东胜',
# '临河',
# '沈阳',
# '大连',
# '鞍山',
# '抚顺',
# '本溪',
# '丹东',
# '锦州',
# '营口',
# '阜新',
# '辽阳',
# '盘锦',
# '铁岭',
# '朝阳',
# '葫芦岛',
# '新民',
# '瓦房店',
# '普兰店',
# '庄河',
# '海城',
# '东港',
# '凤城',
# '凌海',
# '北宁',
# '盖州',
# '大石桥',
# '灯塔',
# '铁法',
# '开原',
# '北票',
# '凌源',
# '兴城',
# '长春',
# '吉林',
# '四平',
# '辽源',
# '通化',
# '白山',
# '松原',
# '白城',
# '九台',
# '榆树',
# '德惠',
# '蛟河',
# '桦甸',
# '舒兰',
# '磐石',
# '公主岭',
# '双辽',
# '梅河口',
# '集安',
# '临江',
# '洮南',
# '大安',
# '延吉',
# '图们',
# '敦化',
# '珲春',
# '龙井',
# '和龙',
# '哈尔滨',
# '齐齐哈尔',
# '鸡西',
# '鹤岗',
# '双鸭山',
# '大庆',
# '伊春',
# '佳木斯',
# '七台河',
# '牡丹江',
# '黑河',
# '阿城',
# '双城',
# '尚志',
# '五常',
# '讷河',
# '虎林',
# '密山',
# '铁力',
# '同江',
# '富锦',
# '绥芬河',
# '海林',
# '宁安',
# '穆棱',
# '北安',
# '五大连池',
# '绥化',
# '安达',
# '肇东',
# '海伦',
# '上海',
# '上海',
# '南京',
# '无锡',
# '徐州',
# '常州',
# '苏州',
# '南通',
# '连云港',
# '淮阴',
# '盐城',
# '扬州',
# '镇江',
# '泰州',
# '宿迁',
# '江阴',
# '宜兴',
# '锡山',
# '新沂',
# '邳州',
# '溧阳',
# '金坛',
# '武进',
# '常熟',
# '张家港',
# '昆山',
# '吴江',
# '太仓',
# '吴县',
# '启东',
# '如皋',
# '通州',
# '海门',
# '淮安',
# '东台',
# '大丰',
# '仪征',
# '高邮',
# '江都',
# '丹阳',
# '扬中',
# '句容',
# '兴化',
# '靖江',
# '泰兴',
# '姜堰',
# '杭州',
# '宁波',
# '温州',
# '嘉兴',
# '湖州',
# '绍兴',
# '金华',
# '衢州',
# '舟山',
# '台州',
# '萧山',
# '建德',
# '富阳',
# '余杭',
# '临安',
# '余姚',
# '慈溪',
# '奉化',
# '瑞安',
# '乐清',
# '海宁',
# '平湖',
# '桐乡',
# '诸暨',
# '上虞',
# '嵊州',
# '兰溪',
# '义乌',
# '东阳',
# '永康',
# '江山',
# '温岭',
# '临海',
# '丽水',
# '龙泉',
# '合肥',
# '芜湖',
# '蚌埠',
# '淮南',
# '马鞍山',
# '淮北',
# '铜陵',
# '安庆',
# '黄山',
# '滁州',
# '阜阳',
# '宿州',
# '巢湖',
# '六安',
# '桐城',
# '天长',
# '明光',
# '亳州',
# '界首',
# '宣州',
# '宁国',
# '贵池',
# '福州',
# '厦门',
# '莆田',
# '三明',
# '泉州',
# '漳州',
# '南平',
# '龙岩',
# '福清',
# '长乐',
# '永安',
# '石狮',
# '晋江',
# '南安',
# '龙海',
# '邵武',
# '武夷山',
# '建瓯',
# '建阳',
# '漳平',
# '宁德',
# '福安',
# '福鼎',
# '南昌',
# '景德镇',
# '萍乡',
# '九江',
# '新余',
# '鹰潭',
# '赣州',
# '乐平',
# '瑞昌',
# '贵溪',
# '瑞金',
# '南康',
# '宜春',
# '丰城',
# '樟树',
# '高安',
# '上饶',
# '德兴',
# '吉安',
# '井冈山',
# '临川',
# '济南',
# '青岛',
# '淄博',
# '枣庄',
# '东营',
# '烟台',
# '潍坊',
# '济宁',
# '泰安',
# '威海',
# '日照',
# '莱芜',
# '临沂',
# '德州',
# '聊城',
# '章丘',
# '胶州',
# '即墨',
# '平度',
# '胶南',
# '莱西',
# '滕州',
# '龙口',
# '莱阳',
# '莱州',
# '蓬莱',
# '招远',
# '栖霞',
# '海阳',
# '青州',
# '诸城',
# '寿光',
# '安丘',
# '高密',
# '昌邑',
# '曲阜',
# '兖州',
# '邹城',
# '新泰',
# '肥城',
# '文登',
# '荣成',
# '乳山',
# '乐陵',
# '禹城',
# '临清',
# '滨州',
# '菏泽',
# '郑州',
# '开封',
# '洛阳',
# '平顶山',
# '安阳',
# '鹤壁',
# '新乡',
# '焦作',
# '濮阳',
# '许昌',
# '漯河',
# '三门峡',
# '南阳',
# '商丘',
# '信阳',
# '巩义',
# '荥阳',
# '新密',
# '新郑',
# '登封',
# '偃师',
# '舞钢',
# '汝州',
# '林州',
# '卫辉',
# '辉县',
# '济源',
# '沁阳',
# '孟州',
# '禹州',
# '长葛',
# '义马',
# '灵宝',
# '邓州',
# '永城',
# '周口',
# '项城',
# '驻马店',
# '武汉',
# '黄石',
# '十堰',
# '宜昌',
# '襄樊',
# '鄂州',
# '荆门',
# '孝感',
# '荆州',
# '黄冈',
# '咸宁',
# '大冶',
# '丹江口',
# '枝城',
# '当阳',
# '枝江',
# '老河口',
# '枣阳',
# '宜城',
# '钟祥',
# '应城',
# '安陆',
# '广水',
# '汉川',
# '石首',
# '洪湖',
# '松滋',
# '麻城',
# '武穴',
# '赤壁',
# '恩施',
# '利川',
# '随州',
# '仙桃',
# '潜江',
# '天门',
# '长沙',
# '株洲',
# '湘潭',
# '衡阳',
# '邵阳',
# '岳阳',
# '常德',
# '张家界',
# '益阳',
# '郴州',
# '永州',
# '怀化',
# '娄底',
# '浏阳',
# '醴陵',
# '湘乡',
# '韶山',
# '耒阳',
# '常宁',
# '武冈',
# '汩罗',
# '临湘',
# '津',
# '沅江',
# '资兴',
# '洪江',
# '冷水江',
# '涟源',
# '吉首',
# '广州',
# '韶关',
# '深圳',
# '珠海',
# '汕头',
# '佛山',
# '江门',
# '湛江',
# '茂名',
# '肇庆',
# '惠州',
# '梅州',
# '汕尾',
# '河源',
# '阳江',
# '清远',
# '东莞',
# '中山',
# '潮州',
# '揭阳',
# '云浮',
# '番禺',
# '花都',
# '增城',
# '从化',
# '乐昌',
# '南雄',
# '潮阳',
# '澄海',
# '顺德',
# '南海',
# '三水',
# '高明',
# '台山',
# '新会',
# '开平',
# '鹤山',
# '恩平',
# '廉江',
# '雷州',
# '吴川',
# '高州',
# '化州',
# '信宜',
# '高要',
# '四会',
# '惠阳',
# '兴宁',
# '陆丰',
# '阳春',
# '英德',
# '连州',
# '普宁',
# '罗定',
# '南宁',
# '柳州',
# '桂林',
# '梧州',
# '北海',
# '防城港',
# '钦州',
# '贵港',
# '玉林',
# '岑溪',
# '东兴',
# '桂平',
# '北流',
# '凭祥',
# '合山',
# '贺州',
# '百色',
# '河池',
# '宜州',
# '海口',
# '三亚',
# '通什',
# '琼海',
# '儋州',
# '琼山',
# '文昌',
# '万宁',
# '东方',
# '江津',
# '合川',
# '永川',
# '南川',
# '成都',
# '自贡',
# '攀枝花',
# '泸州',
# '德阳',
# '绵阳',
# '广元',
# '遂宁',
# '内江',
# '乐山',
# '南充',
# '宜宾',
# '广安',
# '达州',
# '都江堰',
# '彭州',
# '邛崃',
# '崇州',
# '广汉',
# '什邡',
# '绵竹',
# '江油',
# '峨眉山',
# '阆中',
# '华蓥',
# '万源',
# '雅安',
# '西昌',
# '巴中',
# '资阳',
# '简阳',
# '贵阳',
# '六盘水',
# '遵义',
# '清镇',
# '赤水',
# '仁怀',
# '铜仁',
# '兴义',
# '毕节',
# '安顺',
# '凯里',
# '都匀',
# '福泉',
# '昆明',
# '曲靖',
# '玉溪',
# '安宁',
# '宣威',
# '昭通',
# '楚雄',
# '个旧',
# '开远',
# '思茅',
# '景洪',
# '大理',
# '保山',
# '瑞丽',
# '潞西',
# '西安',
# '铜川',
# '宝鸡',
# '咸阳',
# '渭南',
# '延安',
# '汉中',
# '榆林',
# '兴平',
# '韩城',
# '华阴',
# '安康',
# '商州',
# '兰州',
# '嘉峪关',
# '金昌',
# '白银',
# '天水',
# '玉门',
# '酒泉',
# '敦煌',
# '张掖',
# '武威',
# '平凉',
# '西峰',
# '临夏',
# '合作',
# '西宁',
# '格尔木',
# '德令哈',
# '银川',
# '石嘴山',
# '吴忠',
# '青铜峡',
# '灵武',
# '乌鲁木齐',
# '克拉玛依',
# '吐鲁番',
# '哈密',
# '昌吉',
# '阜康',
# '米泉',
# '博乐',
# '库尔勒',
# '阿克苏',
# '阿图什',
# '喀什',
# '和田',
# '奎屯',
# '伊宁',
# '塔城',
# '乌苏',
# '阿勒泰',

'北京',
'上海',
'天津',
'重庆',
'深圳',
'广州',
'成都',
'昆明',
'石家庄',
'沈阳',
'长春',
'哈尔滨',
'呼和浩特',
'乌鲁木齐 ',
'兰州',
'西宁',
'武汉',
'长沙',
'南京',
'南昌',
'太原',
'济南',
'合肥',
'杭州',
'福州',
'银川',
'南宁',
'青岛',
'珠海',
'贵阳',
'无锡',
'东莞',
'厦门',
'苏州',

# '',
# '',
# '',
# '',

]
city_count=0

random.shuffle(china_city_list)
random.shuffle(keywords)
# qq=Image.open('code.jpg')
# print qq
# text=pytesseract.image_to_string(qq,lang="eng") #使用image_to_string识别验证码
# print pytesseract
# print 'code:'
# print text

keywordlist=keywords

# 基本配置
# logging.basicConfig(level=logging.INFO)
openurlstring=''
# openurlstring='http://www.ipip.net/'
cityname=''


def settimeout(timeset,func):
	global isfinished
	global threading
	global browser
	timer = threading.Timer(timeset,func)
	timer.start()


def getelement(source,selector):
	global browser
	# browser.implicitly_wait(10)
	
	# res=WebDriverWait(source,3).until(lambda source:source.find_elements_by_css_selector(selector) , " open fail")
	res=True
	try:
		res=WebDriverWait(source,0.5).until(lambda source:source.find_element_by_css_selector(selector) , " open fail")
		# print(res)
		if res==False:
			return None
		else:
			# print(selector)
			elem=source.find_element_by_css_selector(selector)
			# elem=source.find_elements_by_css_selector(selector)
			return elem
	except Exception, e:
		return None

def getelements(source,selector):
	global browser
	# browser.implicitly_wait(10)
	# res=WebDriverWait(source,3).until(lambda source:source.find_elements_by_css_selector(selector) , " open fail")
	res=True
	try:
		res=WebDriverWait(source,0.5).until(lambda source:source.find_elements_by_css_selector(selector) , " open fail")
		
		# print(res)
		if res==False:
			return []
		else:
			elem=source.find_elements_by_css_selector(selector)
			# print(selector)
			# elem=source.find_elements_by_css_selector(selector)
			return elem
	except Exception, e:
		return []

def sendkeyto(selector,keycode):
	pass

# changeiprandom
def changeiprandom(ctname):
	pass
	#new
	# http://www.xdaili.cn/ipagent//privateProxy/getDynamicIP/DD2017757426QjI7RV/9f7cecf0160211e79ff07cd30abda612?returnType=2
	# http://www.xdaili.cn/ipagent/greatRecharge/getGreatIp?spiderId=4511abc0f70a4214a355e31dac534d3d&orderno=YZ20177540498bQeWf&returnType=2&count=1
	url = 'http://www.xdaili.cn/ipagent//privateProxy/getDynamicIP/DD2017757426QjI7RV/9f7cecf0160211e79ff07cd30abda612?returnType=2'
	req = urllib2.Request(url)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	ip_proxy=json.loads(res)
	iipp=ip_proxy['RESULT']['wanIp']
	# iipp=ip_proxy['RESULT'][0]['ip']
	portport=ip_proxy['RESULT']['proxyport']
	# portport=ip_proxy['RESULT'][0]['port']
	print('ip_proxy')
	print(iipp+':'+portport)
	return iipp+':'+portport

# changeipbycity
def changeipbycity(ctname):
	global ip_proxy
	# city=urllib.quote(urllib.quote(ctname))
	url = "http://tvp.daxiangdaili.com/ip/?tid=555527369568174&num=1&delay=1&area="+ctname+"&foreign=none&exclude_ports=80,22&filter=on"
	# print(url)
	print('get ip proxy')
	# time.sleep(0.1)
	try:
		req = urllib2.Request(url)
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		ip_proxy=res
	except Exception, e:
		
		ip_proxy=''
		pass
		print('browser.quit() changeip')
		# browser.quit()
		print(str(e))
		# loop()
		print('\n')
		print('\n')
		print('\n')
		# raise e

	# print('ip_proxy')
	print('new proxy ip::'+ip_proxy)
	return ip_proxy

# changeipbycityVIP
def changeip(ctname):
	global ip_proxy
	# city=urllib.quote(urllib.quote(ctname))
	url = "http://vtp.daxiangdaili.com/ip/?tid=559604433454279&num=1&delay=1&area="+ctname+"&filter=on"
	# print(url)
	print('get ip proxy')
	# time.sleep(0.1)
	try:
		req = urllib2.Request(url)
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		ip_proxy=res
	except Exception, e:
		
		ip_proxy=''
		pass
		print('browser.quit() changeip')
		# browser.quit()
		print(str(e))
		# loop()
		print('\n')
		print('\n')
		print('\n')
		# raise e

	# print('ip_proxy')
	print('new proxy ip::'+ip_proxy)
	return ip_proxy

def openbrowser():
	pass
	global browser
	global china_city_list
	global city_count
	global word_count
	global cityname
	global ip_proxy
	global keywordlist
	print('opening browser...')
	# print len(china_city_list)
	if len(china_city_list)<city_count:
		pass
		print('city_count > china_city_list ')
		# city_count=0
		# ip_proxy=china_city_list[city_count]
		# keywords_bak.append(msgstring)
		print('browser.quit() 1')	
		browser.quit()		
		# browser.close()
		print('\n')
		print('\n')
		print('\n')
		print('\n')
		city_count=0
		word_count=0
		# quit
		loop()
	else:
		try:
			pass
			cityname=china_city_list[city_count]
		except Exception, e:
			# raise e
			print('clear city_count')
			random.shuffle(china_city_list)
			print(str(e))
			city_count=0
			word_count=0
			cityname=china_city_list[city_count]
			# loop()
		
		# keywords_bak.append(msgstring)

	
	# city_count+=1
	print('words count')
	print (word_count)
	print (keywordlist[word_count].encode('gbk'))


	print('city count')
	print (city_count)
	print (cityname.encode('gbk'))

	print('ip_proxy')
	print(ip_proxy)

	# 进入浏览器设置
	chome_options = webdriver.ChromeOptions()
	# 设置中文
	chome_options.add_argument('lang=zh_CN.UTF-8')
	#设置不显示图片
	# ,"profile.managed_default_content_settings.javascript":2
	prefs = {"profile.managed_default_content_settings.images":2}
	chome_options.add_experimental_option("prefs",prefs)
	# 更换头部
	# 移动版没有广告地址了，需要点击了
	if ismobile:
		chome_options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"')


	# useproxy=False
	useproxy=True

	if useproxy:
		# ip_proxy=changeip(cityname)
		# if ip_proxy=='':
		# 	ip_proxy=changeip(cityname)

		while ip_proxy=='' or 'ERROR' in ip_proxy:
			print('now changeip ....')
			word_count=0
			city_count+=1
			cityname=china_city_list[city_count]
			print(city_count)
			print(cityname.encode('gbk'))
			ip_proxy=changeip(cityname)
			print('now the new ip_proxy is:')
			print(ip_proxy)

		# if 'ERROR' in ip_proxy:
		# 	print('browser.quit() ERROR ip_proxy')
		# 	# ip_proxy=''
		# 	# city_count+=1
		# 	# if city_count==len(china_city_list)-1:
		# 	# 	city_count=0
		# 	# 	print('clear city_count')
		# 	# time.sleep(0.1)
		# 	# browser.quit()
		# 	print('change city name1')
		# 	print('change city name1')
		# 	print('change city name1')
		# 	print('change city name1')
		# 	print('change city name1')
		# 	print('\n')
		# 	print('\n')
		# 	print('\n')
		# 	word_count=0
		# 	city_count+=1
		# 	ip_proxy=''
			# loop()
		# print (ip_proxy)
		
		#2
		# 进入浏览器设置
		# chome_options = webdriver.ChromeOptions()  
		
		chome_options.add_argument(('--proxy-server=http://' + ip_proxy))  
		# os.environ["webdriver.chrome.driver"] = chromedriver 
		 
		browser = webdriver.Chrome(chrome_options=chome_options)  
	else:
		cityname="成都"
		browser = webdriver.Chrome(chrome_options=chome_options)



	browser.implicitly_wait(30)
	browser.set_script_timeout(30)
	browser.set_page_load_timeout(40)
	try:
		# browser = webdriver.Chrome(desired_capabilities=capabilities)
		browser.get(openurlstring)
	except Exception, e:
		# raise e
		# word_count-=1

		# logging.info(browser.title)
		# browser.close()
		print('browser.quit() page load time out!')
		browser.quit()
		print('\n')
		print('\n')
		print('\n')

		city_count+=1
		# if city_count==len(china_city_list)-1:
		# 	print('clear city_count')
		# 	city_count=0
		word_count=0
		ip_proxy=''
		# loop()



	# print(browser.find_element_by_css_selector('#kw'))
	# time.sleep(1)
	# 确认没问题 并做网络缓冲
	# try:
	# 	WebDriverWait(browser,10).until(lambda source:browser.find_element_by_css_selector('#kw') , " open fail")
	# except Exception, e:
	# 	raise e
	# 	print('browser.quit() error open')
	# 	browser.quit()
	# 	print('page opend error ,change city')

	# 	print('change city name error')
	# 	print('change city name error')
	# 	print('change city name error')
	# 	print('change city name error')
	# 	print('\n')
	# 	print('\n')
	# 	print('\n')
	# 	city_count+=1
	# 	if city_count==len(china_city_list)-1:
	# 		city_count=0
	# 	word_count=0
	# 	ip_proxy=''
	# 	loop()
		
	

	# time.sleep(2)
	time.sleep(0.1)

def closebrowser():
	pass
	global browser
	global city_count
	# 关闭chrome 重新换IP代理
	# browser.close()
	print('browser.quit() 3')
	browser.quit()
	print('\n')
	print('\n')
	print('\n')
	openbrowser()
	city_count+=1
	# if city_count==len(china_city_list)-1:
	# 	city_count=0
	# 	print('clear city_count')




def loop():
	global browser
	global keywords
	global word_count
	global city_count
	global time
	global result
	global YDMApi
	global isfinished
	global openurlstring

	global keywordlist
	global keywordcolum
	global cityname
	global ip_proxy
	global china_city_list

	# isfinished=0

	# 关键词列表是否循环完毕
	if len(keywordlist)<=word_count:
		time.sleep(10)
		try:
			# 关闭所有窗口
			print('browser.quit() word loop over,change for next city...')
			browser.quit()
			print('\n')
			print('\n')
			print('\n')
			# city_count=0
			word_count=0
			loop()
		except Exception, e:
			# raise e
			print(str(e))
			print('browser.quit() 5')
			browser.quit()
			print('\n')
			print('\n')
			print('\n')
			pass
		# time.sleep(30)
		pass
		# word_count=0
		# msgstring=keywordlist[word_count]
	else:
		# 获取下一个关键词
		msgstring=keywordlist[word_count]

	
	# print('msgstring:')
	# print(msgstring.encode('gbk'))
	# time.sleep(0.1)

	# 打开浏览器
	# a=urllib.quote(urllib.quote(msgstring))

	# PC版
	openurlstring='http://www.baidu.com/s?wd='+msgstring+'&rsv_spt=1&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=8&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&prefixsug=shaoer&rsp=0&inputT=2051&rsv_sug4=12425'
	# 移动版
	if ismobile:
		# openurlstring='http://m.baidu.com/s?word='+msgstring
		# a=urllib.quote(urllib.quote(msgstring))
		openurlstring='https://m.baidu.com/s?word='+msgstring

	print(openurlstring)
	# time.sleep(0.1)
	print('start open browser')
	openbrowser()
	print('browser has opened')




	word_count+=1
	# if city_count==len(china_city_list)-1:
	# 	city_count=0
	# 	print('clear city_count')
	# city_count+=1

	time.sleep(0.1)
	try:
		# titleelm=browser.find_element_by_css_selector('#kw')
		titleelm=browser.find_element_by_css_selector('input')

		for x in xrange(1,30*10):
			try:
				browser.switch_to_active_element().send_keys(Keys.DOWN)
				# titleelm.send_keys(Keys.DOWN)
			except Exception, e:
				# raise e
				print(str(e))
		time.sleep(0.1)

	except Exception, e:
		# raise e
		print(str(e))
		print('browser.quit() cant find #kw')
		browser.quit()
		print('page opend error ,change city')
		print('change city name2')
		print('change city name2')
		print('change city name2')
		print('change city name2')
		city_count+=1
		word_count=0
		ip_proxy=''
		# loop()

	# PC版
	if not(ismobile):
		cur = conn.cursor()
		
		try:
			ad_list=getelements(browser,'#content_left h3 a')
			time.sleep(0.1)
		except Exception, e:
			ad_list=[]
			# raise e
			print(str(e))
			print('browser.quit() element get error')
			browser.quit()
			print('\n')
			print('\n')
			print('\n')

		for ad in ad_list:
			try:
				adurl=ad.get_attribute('data-landurl')
				if adurl!=None:
					print(adurl)
					domainurl=urlparse.urlparse(adurl).netloc
					domainurl=domainurl.replace('www.','')

					# cur = conn.cursor()
					# sqli="insert into ad values(%s,%s,%s,%s)"
					sqli="insert into ad (city,title,adurl,domain,status) values ('"+cityname+"','"+adurl+"','"+adurl+"','"+domainurl+"',0)"
					print(sqli)

					try:
						cur.execute(sqli)
						conn.commit()
					except Exception, e:
						# browser.quit()
						# raise e
						print(str(e))
						# 一个出错，其他的链接还要继续抓
						continue
					
					

			except Exception, e:
				# raise e
				print(str(e))
				pass
				print('word_count1')
				print(word_count)
				print('browser.quit() get ad list error')
				browser.quit()
				print('\n')
				print('\n')
				print('\n')
		cur.close()

	# 移动版
	if ismobile:
		cur = conn.cursor()

		# for x in xrange(1,2):
		ad_list=getelements(browser,'.ec_ad_results .c-container')
		try:
			for ad in ad_list:
				adurl=ad.get_attribute('data-lp')
				if adurl!=None:
					# print(adurl)
					adurlstr=urllib.unquote(adurl).decode('utf-8', 'replace').encode('gbk', 'replace')
					print('adurlstr')
					print(adurlstr)
					domainurl=urlparse.urlparse(adurlstr).netloc
					domainurl=domainurl.replace('www.','')

					sqli="insert into ad (city,title,adurl,domain,ismobile,status) values ('"+cityname+"','"+adurlstr+"','"+adurlstr+"','"+domainurl+"',1,0)"
					print('sqli')
					print(sqli)
					try:
						cur.execute(sqli)
						conn.commit()
					except Exception, e:
						
						print(str(e))
						print('word_count2')
						print(word_count)
						# print('browser.quit() sql error!')
						# browser.quit()
						# print('\n')
						# print('\n')
						print('\n')
						# raise e
						# 一个出错，其他的链接还要继续抓
						continue



					
					# browser.quit()
					# print('browser.quit() sql ok')
					# print('\n')
					# print('\n')
					# print('\n')
		except Exception, e:
			# raise e
			print(str(e))
			pass
			print('browser.quit() get ad list error')
			browser.quit()
			print('\n')
			print('\n')
			print('\n')



		# # next page
		# try:
		# 	getelement(browser,'.new-pagenav a.new-nextpage-only').click()
		# except Exception, e:
		# 	try:
		# 		getelement(browser,'.new-pagenav a.new-nextpage').click()
		# 	except Exception, e:
		# 		# raise e
		# 		pass
			

		# time.sleep(0.3)
			


		cur.close()

		#
		# reword
		# rw-item
		# cur = conn.cursor()
		# wd_list=getelements(browser,'#reword .rw-item')
		# for wd in wd_list:
		# 	pass
		# 	otherwd=wd.text
		# 	# print(otherwd)
		# 	print(otherwd.encode('gbk'))

		# 	sqli="insert into keyword (word) values ('"+otherwd+"')"
		# 	print(sqli)
		# 	try:
		# 		cur.execute(sqli)
		# 		conn.commit()
		# 	except Exception, e:
		# 		# raise e
		# 		print(str(e))
	print('browser.quit() ok')
	print('\n')
	print('\n')
	print('\n')
	print('\n')
	browser.quit()
	# browser.close()

while 1:
	try:
		print('loop start')
		loop()
		print('loop over')
	except Exception, e:
		# raise e
		# print(str(e))
		loop()
		pass
