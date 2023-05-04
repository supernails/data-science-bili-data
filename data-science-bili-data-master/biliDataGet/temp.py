def processUserAgent():
    new_list = []
    with open('./user_agents.txt', 'r') as f:
        # 逐行读取文件内容
        for line in f:
            # 对每行内容进行处理，例如打印出来
            new_list.append(line[4:])
        f.close()
    with open("processed_user_agents.txt", "w") as f:
        for item in new_list:
            f.write("%s" % item)
        f.close()




if __name__ == '__main__':
    processUserAgent()

