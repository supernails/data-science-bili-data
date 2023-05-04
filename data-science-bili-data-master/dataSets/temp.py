def generator():
    birthdayFile = open("./birthday.txt", 'r', encoding='utf-8')
    birthday = eval(str(birthdayFile.read()))
    birthdayNumFile = open("./birthdayNum.txt", 'r', encoding='utf-8')
    birthdayNum = eval(str(birthdayNumFile.read()))
    distList = []
    for index in range(len(birthday)):
        name = birthday[index]
        value = birthdayNum[index]
        dist = {"name": name, "value": value}
        distList.append(dist)
    file = open("./birthdayAndNum.txt", 'w', encoding="utf-8")
    file.write(str(distList))
    file.close()
    birthdayFile.close()
    birthdayNumFile.close()


def toYear():
    yearFile = open("../processedData/birthday-year.txt", 'w', encoding="utf-8")
    birFile = open("./birthday.txt", 'r', encoding='utf-8')
    numFile = open("./birthdayNum.txt", 'r', encoding='utf-8')
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


if __name__ == '__main__':
    toYear()
