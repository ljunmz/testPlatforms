


def changeAciton(newStr, path):
    f = open(path + "业务流程-整合.jmx", mode='r', encoding='utf-8').read()
    oldStr = f[f.find("获取流程数据"):f.find("order by") - 1][f[f.find("获取流程数据"):f.find("order by")].find("and") + 4:]
    fileData = ''
    print(oldStr)
    with open(path + "业务流程-整合.jmx", mode='r', encoding='utf-8') as ff:
        for line in ff:
            if oldStr in line:
                line = line.replace(oldStr, newStr)
            fileData += line
    with open(path + "业务流程-整合.jmx", mode='w', encoding='utf-8') as ww:
        ww.write(fileData)


