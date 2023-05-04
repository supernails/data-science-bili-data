#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:
import getData


class SourceDataDemo:

    def __init__(self):
        # 默认的标题
        self.title = 'B站数据分析'
        # 两个小的form看板
        self.counter = {'name': '数据来源', 'value': '爬虫 \n 搜集数据'}
        self.counter2 = {'name': '技术栈', 'value': 'Flask \n pandas \n echarts'}
        # 总共是6个图表，数据格式用json字符串，其中第3个图表是有3个小的图表组成的
        departAndNum = open("./processedData/departAndNum.txt", 'r')
        self.echart1_data = {
            'title': 'B站每周必看分区数量',
            'data': getData.getDepartAndNum()
        }
        self.echart2_data = {
            'title': '用户粉丝数统计',
            'data': getData.getFans(1000000)
        }
        self.echarts3_1_data = {
            'title': '男性性别和等级',
            'data': getData.getMaleLevel()
        }
        self.echarts3_2_data = {
            'title': '性别分布',
            # 'data': getData.getFans()
            'data': getData.getGenderList()
        }
        self.echarts3_3_data = {
            'title': '女性性别和等级',
            'data': getData.getFemaleLevel()
        }
        self.echart4_data = {
            'title': '用户年龄分布',
            'data': [
                {"name": "年龄", "value": getData.getBirthdayYearList()},
                {"name": "年龄", "value": getData.getBirthdayYearList()},
            ],
            'xAxis': list(range(53, 13, -1)),
        }
        self.echart5_data = {
            'title': 'TOP省份',
            'data': getData.getTopProvinceList(10)
        }
        # 这是一个环状图，有颜色的加上没颜色的正好等于100，半径是外圈直径和内圈直径，猜测是左闭右开
        total = sum(item['value'] for item in getData.getFans(1000000))
        e6_data = getData.getFans(1000000)
        self.echart6_data = {
            'title': '用户关注数',
            'data': [
                {"name": '1', "value":  sum(e6_data[i]['value'] for i in range(1)) / total * 100, "value2": 100 - (sum(e6_data[i]['value'] for i in range(1)) / total), "color": "02", "radius": ['49%', '60%']},
                {"name": '2', "value":  sum(e6_data[i]['value'] for i in range(2)) / total * 100, "value2": 100 - (sum(e6_data[i]['value'] for i in range(2)) / total), "color": "03", "radius": ['39%', '50%']},
                {"name": '3', "value":  sum(e6_data[i]['value'] for i in range(3)) / total * 100, "value2": 100 - (sum(e6_data[i]['value'] for i in range(3)) / total), "color": "04", "radius": ['29%', '40%']},
                {"name": '4', "value":  sum(e6_data[i]['value'] for i in range(4)) / total * 100, "value2": 100 - (sum(e6_data[i]['value'] for i in range(4)) / total), "color": "05", "radius": ['19%', '30%']},
                {"name": '5', "value":  sum(e6_data[i]['value'] for i in range(5)) / total * 100, "value2": 100 - (sum(e6_data[i]['value'] for i in range(5)) / total), "color": "06", "radius": ['9%',  '20%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 2000,
            'data': getData.getProvinceList()
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            # 第一次get获取到的是许多键值对，所以需要对每个键值对再次get
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        # 返回的是标题和对应的数据，并没有说用什么方式展现！
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = 'B站数据分析'
