import json

import pandas as pd


def departAndNum():
    weekDf = pd.read_excel("./dataSets/week_bilibili_popular.xlsx", 'r')
    departAndNum = weekDf.groupby("分区")
    departAndNumValue = weekDf.groupby("分区")['标题'].count()
    departAndNumList = list(departAndNum)
    distList = []
    for index in range(len(list(departAndNum))):
        name = departAndNumList[index][0]
        value = departAndNumValue[index]
        dist = {"name": name, "value": value}
        distList.append(dist)
    distList.sort(key=lambda s: int(s["value"]))
    file = open("./processedData/departAndNum.txt", "w", encoding="utf-8")
    file.write(str(distList))
    file.close()


def getDepartAndNum():
    openFile = open("./processedData/departAndNum.txt", 'r', encoding="utf-8")
    content = openFile.read()
    # print(content)
    openFile.close()
    return eval(content)


def genderList():
    file = open("./user/buser.json", 'r', encoding='utf-8')
    lines = file.readlines()
    # maleCount, femaleCount, unknowSexCount
    genderCountList = [0, 0, 0]
    # 0,1,2,3,4,5,6
    levelCountList = [0, 0, 0, 0, 0, 0, 0]
    maleLevelList = [0, 0, 0, 0, 0, 0, 0]
    femaleLevelList = [0, 0, 0, 0, 0, 0, 0]
    for line in lines:
        lineJson = json.loads(line)
        if lineJson['sex'] == '男':
            genderCountList[0] += 1
            maleLevelList[lineJson['level']] += 1
        elif lineJson['sex'] == '女':
            genderCountList[1] += 1
            femaleLevelList[lineJson['level']] += 1
        else:
            genderCountList[2] += 1
        levelCountList[lineJson['level']] += 1
    # genderDir = {"男": genderCountList[0], "女": genderCountList[1], "保密": genderCountList[2]}
    genderDir = [
        {"name": "男", "value": genderCountList[0]},
        {"name": "女", "value": genderCountList[1]},
        {"name": "保密", "value": genderCountList[2]}
    ]
    genderFileProcessed = open("./processedData/genderNum.txt", 'w', encoding='utf-8')
    genderFileProcessed.write(str(genderDir))
    genderFileProcessed.close()
    # 等级
    # levelDir = {"0": levelCountList[0], "1": levelCountList[1], "2": levelCountList[2],
    #             "3": levelCountList[3], "4": levelCountList[4], "5": levelCountList[5], "6": levelCountList[6]}
    levelDir = [
        {"name": 0, "value": levelCountList[0]}, {"name": 1, "value": levelCountList[1]},
        {"name": 2, "value": levelCountList[2]}, {"name": 3, "value": levelCountList[3]},
        {"name": 4, "value": levelCountList[4]}, {"name": 5, "value": levelCountList[5]},
        {"name": 6, "value": levelCountList[6]}
    ]
    levelFileProcessed = open("./processedData/levelNum.txt", 'w', encoding='utf-8')
    levelFileProcessed.write(str(levelDir))
    levelFileProcessed.close()
    # 性别和等级
    maleLevelDir = [
        {"name": 0, "value": maleLevelList[0]}, {"name": 1, "value": maleLevelList[1]},
        {"name": 2, "value": maleLevelList[2]}, {"name": 3, "value": maleLevelList[3]},
        {"name": 4, "value": maleLevelList[4]}, {"name": 5, "value": maleLevelList[5]},
        {"name": 6, "value": maleLevelList[6]}
    ]
    maleLevelFileProcessed = open("./processedData/maleLevelNum.txt", 'w', encoding='utf-8')
    maleLevelFileProcessed.write(str(maleLevelDir))
    maleLevelFileProcessed.close()
    femaleLevelDir = [
        {"name": 0, "value": femaleLevelList[0]}, {"name": 1, "value": femaleLevelList[1]},
        {"name": 2, "value": femaleLevelList[2]}, {"name": 3, "value": femaleLevelList[3]},
        {"name": 4, "value": femaleLevelList[4]}, {"name": 5, "value": femaleLevelList[5]},
        {"name": 6, "value": femaleLevelList[6]}
    ]
    femaleLevelFileProcessed = open("./processedData/femaleLevelNum.txt", 'w', encoding='utf-8')
    femaleLevelFileProcessed.write(str(femaleLevelDir))
    femaleLevelFileProcessed.close()
    file.close()


def getGenderList():
    file = open("./processedData/genderNum.txt", 'r', encoding='utf-8')
    fileStr = file.read()
    res = eval(fileStr)
    file.close()
    return res


def getLevel():
    file = open("./processedData/levelNum.txt", 'r', encoding='utf-8')
    fileStr = file.read()
    res = eval(fileStr)
    file.close()
    return res


def getMaleLevel():
    file = open("./processedData/maleLevelNum.txt", 'r', encoding='utf-8')
    fileStr = file.read()
    res = eval(fileStr)
    file.close()
    return res


def getFemaleLevel():
    file = open("./processedData/femaleLevelNum.txt", 'r', encoding='utf-8')
    fileStr = file.read()
    res = eval(fileStr)
    file.close()
    return res


def provinceList():
    data = [{"name": "广东", "value": 109530}, {"name": "四川", "value": 46416}, {"name": "湖北", "value": 35008},
            {"name": "浙江", "value": 67212}, {"name": "江苏", "value": 78431}, {"name": "上海", "value": 72515},
            {"name": "北京", "value": 51538}, {"name": "福建", "value": 32823}, {"name": "陕西", "value": 14355},
            {"name": "湖南", "value": 22037}, {"name": "河南", "value": 22448}, {"name": "广西", "value": 22258},
            {"name": "香港", "value": 6435}, {"name": "黑龙江", "value": 13583}, {"name": "辽宁", "value": 21035},
            {"name": "山东", "value": 32248}, {"name": "安徽", "value": 20623}, {"name": "重庆", "value": 22249},
            {"name": "江西", "value": 15674}, {"name": "云南", "value": 10755}, {"name": "台湾", "value": 4101},
            {"name": "吉林", "value": 8894}, {"name": "河北", "value": 16488}, {"name": "贵州", "value": 7723},
            {"name": "天津", "value": 14055}, {"name": "山西", "value": 7868}, {"name": "新疆", "value": 4481},
            {"name": "海南", "value": 3720}, {"name": "甘肃", "value": 3132}, {"name": "内蒙古", "value": 5522},
            {"name": "澳门", "value": 1110}, {"name": "宁夏", "value": 1556}, {"name": "青海", "value": 729},
            {"name": "西藏", "value": 309}]
    sorted_data = sorted(data, key=lambda x: x['value'], reverse=False)
    openfile = open("./processedData/province_data.txt", 'w', encoding="utf-8")
    openfile.write(str(sorted_data))
    openfile.close()


def getTopProvinceList(num):
    openfile = open("./processedData/province_data.txt", 'r', encoding='utf-8')
    content = openfile.read()
    openfile.close()
    provinceAndNumList = eval(content)
    return provinceAndNumList[len(provinceAndNumList) - num: len(provinceAndNumList)]


def getProvinceList():
    openfile = open("./processedData/province_data.txt", 'r', encoding='utf-8')
    content = openfile.read()
    openfile.close()
    provinceAndNumList = eval(content)
    return provinceAndNumList


def toYear():
    yearFile = open("./processedData/birthday-year.txt", 'w', encoding="utf-8")
    birFile = open("./dataSets/birthday.txt", 'r', encoding='utf-8')
    numFile = open("./dataSets/birthdayNum.txt", 'r', encoding='utf-8')
    birthdayList = eval(birFile.read())
    # print(birthdayList)
    yearList = []
    numList = eval(numFile.read())
    distList = []
    preYear = birthdayList[0].split('-')[0]
    dist = {"name": preYear, "value": 0}
    for index in range(len(birthdayList)):
        currentYear = birthdayList[index].split('-')[0]
        if currentYear == preYear:
            # 年份相同，值增加
            currentNum = numList[index]
            dist["value"] += currentNum
        else:
            # 年份不同，初始化
            # old_dist = {"name": dist["name"], "value": dist["value"]}
            distList.append(dist["value"])
            dist["name"] = currentYear
            dist["value"] = 1
            preYear = currentYear
    distList.append(dist["value"])
    yearFile.write(str(distList))
    yearFile.close()
    numFile.close()
    birFile.close()


def getBirthdayYearList():
    openfile = open("./processedData/birthday-year.txt", 'r', encoding='utf-8')
    content = openfile.read()
    openfile.close()
    # birthdayNumList = eval(content)
    return eval(content)


def calFans():
    fansX = open("./dataSets/fansX", 'r', encoding="utf-8")
    fansY = open("./dataSets/fansY", 'r', encoding="utf-8")
    fansXList = eval(fansX.read())
    fansYList = eval(fansY.read())
    distList = []
    for index in range(len(fansXList)):
        name = fansXList[index]
        value = fansYList[index]
        distList.append({"name": name, "value": value})
    fansNumAndUserNum = open("./processedData/fansNumAndUserNum.txt", 'w', encoding="utf-8")
    fansNumAndUserNum.write(str(distList))
    fansX.close()
    fansY.close()
    fansNumAndUserNum.close()
    print("示例数据：")
    print(distList[0:20])


def getFans(n):
    file = open("./processedData/fansNumAndUserNum.txt", 'r', encoding="utf-8")
    listStr = file.read()
    file.close()
    res = eval(listStr)
    if n > len(res):
        n = len(res)
    return res[0:n]


def calLevel():
    levelFile = pd.read_csv("./dataSets/Bilibili_User_Level.csv")
    levelAndNum = levelFile.groupby("level")
    levelAndNumValue = levelAndNum["mid"].count()
    levelAndNumList = list(levelAndNum)
    distList = []
    for index in range(len(list(levelAndNum))):
        name = levelAndNumList[index][0]
        value = levelAndNumValue[index]
        dist = {"name": name, "value": value}
        distList.append(dist)
    distList.sort(key=lambda s: int(s["value"]))
    file = open("./processedData/levelAndNum.txt", "w", encoding="utf-8")
    file.write(str(distList))
    file.close()


if __name__ == '__main__':
    file = open("./user/buser.json", 'r', encoding='utf-8')
    lines = file.readlines()
    print(len(lines))
