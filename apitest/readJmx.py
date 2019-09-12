import xml.etree.ElementTree as ET


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


def changeEmail(email, path):
    tree = ET.parse(path + 'build.xml')
    root = tree.getroot()
    print('tag:', root.tag, 'attrib:', root.attrib, 'text:', root.text)
    for elm in root:
        if elm.attrib.get("name") == "mail_to":
            print(elm.attrib.get("value"))
            elm.attrib["value"] = email
            print(elm.attrib.get("value"))
    tree.write(path + 'build.xml')


def getEmailList(path):
    tree = ET.parse(path + 'build.xml')
    root = tree.getroot()
    print('tag:', root.tag, 'attrib:', root.attrib, 'text:', root.text)

    for elm in root:
        if elm.attrib.get("name") == "mail_to":
            return elm.attrib.get("value")


def getDefaultVariable(path):
    f = open(path + "业务流程-整合.jmx", mode='r', encoding='utf-8').read()
    oldStr = f[f.find("默认全局变量"):][f[f.find("默认全局变量"):].find("elementProp") - 12:][
             :f[f.find("默认全局变量"):][f[f.find("默认全局变量"):].find("elementProp") - 12:].find("collectionProp") - 2].split(
        "</elementProp>")
    variableList = []
    for elementProp in oldStr:
        argumentName = elementProp[elementProp.find("Argument.name") + 15:][
                       :elementProp[elementProp.find("Argument.name") + 15:].find("stringProp") - 2]
        argumentValue = elementProp[elementProp.find("Argument.value") + 16:][
                        :elementProp[elementProp.find("Argument.value") + 16:].find("stringProp") - 2]
        print(argumentName)
        print(argumentValue)
        variableList.insert(1000,
                            {
                                "argumentName": argumentName,
                                "argumentValue": argumentValue
                            }
                            )
    print(variableList)
    return variableList

# getDefaultVariable("G:\\svn\\自动化测试\\API-Test\\")


def formElementProp(argumentName, argumentValue):
    elementPropStr = "          <elementProp name=" + "\"" + argumentName + "\"" + " elementType=\"Argument\">"
    argumentNameStr = "            <stringProp name=\"Argument.name\">" + argumentName + "</stringProp>"
    argumentValueStr = "            <stringProp name=\"Argument.value\">" + argumentValue + "</stringProp>"
    argumentMetadataStr = "            <stringProp name=\"Argument.metadata\">=</stringProp>"
    elementPropStrEnd = "          </elementProp>"
    return "\n" + elementPropStr + "\n" + argumentNameStr + "\n" + argumentValueStr + "\n" + argumentMetadataStr + "\n" + elementPropStrEnd+ "\n"


def addDefaultVariable(argumentName, argumentValue, path):
    keyword = "<elementProp name=" + "\"" + argumentName + "\""
    f = open(path + "业务流程-整合.jmx", mode='r', encoding='utf-8')
    fr = f.read()
    post = fr.find("testname=\"默认全局变量\" enabled=\"true\">") + fr[
                                                              fr.find("testname=\"默认全局变量\" enabled=\"true\">"):].find(
        "<collectionProp name=\"Arguments.arguments\">") + len("<collectionProp name=\"Arguments.arguments\">")
    print(post)
    f.close()
    if fr.find(keyword) == -1:
        newStr = fr[:post] + formElementProp(argumentName, argumentValue) + fr[post:]
        with open(path + "业务流程-整合.jmx", 'w', encoding='utf-8') as ww:
            ww.write(newStr)
            ww.close()
        return 200
    else:
        print("变量已存在")
        return 601

#
# addDefaultVariable("importance11112", "importance1", "G:\\svn\\自动化测试\\API-Test\\")


def editDefaultVariable(oldKey, newKey, value, path):
    keyword = "<elementProp name=" + "\"" + oldKey + "\""
    print(keyword)
    f = open(path + "业务流程-整合.jmx", mode='r', encoding='utf-8')
    fr = f.read()
    post = fr.find(keyword)
    if post != -1:
        newStr = fr[:post] + formElementProp(newKey, value) + fr[post:][fr[post:].find("</elementProp>")+len("</elementProp>"):]
        f.close()
        print(fr[:post])
        with open(path + "业务流程-整合.jmx", mode='w', encoding='utf-8') as ww:
            ww.truncate()
            ww.write(newStr)
            ww.close()
        return 200
    else:
        print("不存在该变量")
        f.close()
        return 601
# editDefaultVariable("importance", "importance1", "1${__Random(1,4,)}", "G:\\svn\\自动化测试\\API-Test\\")


def deleteDefaultVariable(key, path):
    keyword = "<elementProp name=" + "\"" + key + "\""
    print(keyword)
    f = open(path + "业务流程-整合.jmx", mode='r', encoding='utf-8')
    fr = f.read()
    post = fr.find(keyword)
    if post != -1:
        newStr = fr[:post] + fr[post:][fr[post:].find("</elementProp>")+len("</elementProp>"):]
        f.close()
        print(fr[:post])
        with open(path + "业务流程-整合.jmx", mode='w', encoding='utf-8') as ww:
            ww.truncate()
            ww.write(newStr)
            ww.close()
        return 200
    else:
        print("不存在该变量,无法删除")
        f.close()
        return 601

