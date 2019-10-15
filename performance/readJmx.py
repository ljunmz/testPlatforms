import os
import xml.etree.ElementTree as ET

fileName = "测试流.jmx"


def _encode(s, encoding):
    try:
        if isinstance(s, str):
            return s
        return s.encode(encoding)
    except AttributeError:
        return s

ET._encode = _encode

def changeAciton(newStr, path):
    f = open(path + fileName, mode='r', encoding='utf-8').read()
    oldStr = f[f.find("获取流程数据"):f.find("order by") - 1][f[f.find("获取流程数据"):f.find("order by")].find("and") + 4:]
    fileData = ''
    print(oldStr)
    with open(path + fileName, mode='r', encoding='utf-8') as ff:
        for line in ff:
            if oldStr in line:
                line = line.replace(oldStr, newStr)
            fileData += line
    with open(path + fileName, mode='w', encoding='utf-8') as ww:
        ww.write(fileData)


def changeServiceInfo(newServerName, newPort, newProtocol, path):
    f = open(path + fileName, mode='r', encoding='utf-8').read()
    oldStr = f[f.find("<ConfigTestElement"):f.find("</ConfigTestElement>") + len("</ConfigTestElement>")]
    oldServerName = oldStr[oldStr.find("<stringProp name=\"HTTPSampler.domain\">") + len("<stringProp name=\"HTTPSampler.domain\">"):oldStr.find("</stringProp>")]
    oldPort = oldStr[oldStr.find("<stringProp name=\"HTTPSampler.port\">") + len("<stringProp name=\"HTTPSampler.port\">"):oldStr.find("<stringProp name=\"HTTPSampler.port\">")+oldStr[oldStr.find("<stringProp name=\"HTTPSampler.port\">"):].find("</stringProp>")]
    oldProtocol = oldStr[oldStr.find("<stringProp name=\"HTTPSampler.protocol\">") + len("<stringProp name=\"HTTPSampler.protocol\">"):oldStr.find("<stringProp name=\"HTTPSampler.protocol\">")+oldStr[oldStr.find("<stringProp name=\"HTTPSampler.protocol\">"):].find("</stringProp>")]
    fileData = ''
    with open(path + fileName, mode='r', encoding='utf-8') as ff:
        for line in ff:
            if "<stringProp name=\"HTTPSampler.domain\">"+oldServerName in line:
                line = line.replace(oldServerName, newServerName)
            if "<stringProp name=\"HTTPSampler.port\">"+oldPort in line:
                line = line.replace(oldPort, newPort)
            if "<stringProp name=\"HTTPSampler.protocol\">"+oldProtocol in line:
                line = line.replace(oldProtocol, newProtocol)
            fileData += line
    with open(path + fileName, mode='w', encoding='utf-8') as ww:
        ww.write(fileData)

def changeSThread(loops, num_threads, ramp_time,  path):
    f = open(path + fileName, mode='r', encoding='utf-8').read()
    oldStr = f[f.find("guiclass=\"ThreadGroupGui\""):f.find("</ThreadGroup>") + len("</ThreadGroup>")]
    old_loops = oldStr[oldStr.find("name=\"LoopController.loops\">") + len("name=\"LoopController.loops\">"):oldStr.find("name=\"LoopController.loops\">")+oldStr[oldStr.find("name=\"LoopController.loops\">"):].find("</")]
    old_num_threads = oldStr[oldStr.find("<stringProp name=\"ThreadGroup.num_threads\">") + len("<stringProp name=\"ThreadGroup.num_threads\">"):oldStr.find("<stringProp name=\"ThreadGroup.num_threads\">")+oldStr[oldStr.find("<stringProp name=\"ThreadGroup.num_threads\">"):].find("</stringProp>")]
    old_ramp_time = oldStr[oldStr.find("<stringProp name=\"ThreadGroup.ramp_time\">") + len("<stringProp name=\"ThreadGroup.ramp_time\">"):oldStr.find("<stringProp name=\"ThreadGroup.ramp_time\">")+oldStr[oldStr.find("<stringProp name=\"ThreadGroup.ramp_time\">"):].find("</stringProp>")]
    fileData = ''
    print(old_loops)
    print(old_ramp_time)
    print(old_num_threads)
    with open(path + fileName, mode='r', encoding='utf-8') as ff:
        for line in ff:
            if "name=\"LoopController.loops\">"+old_loops+"</" in line:
                line = line.replace(old_loops, loops)
            if "<stringProp name=\"ThreadGroup.num_threads\">"+old_num_threads+"</" in line:
                line = line.replace(old_num_threads, num_threads)
            if "<stringProp name=\"ThreadGroup.ramp_time\">"+old_ramp_time+ "</" in line:
                line = line.replace(old_ramp_time, ramp_time)
            fileData += line
    with open(path + fileName, mode='w', encoding='utf-8') as ww:
        ww.write(fileData)

# changeSThread("false", "111", "3", "2", "G:\\svn\\自动化测试\\API-Test\\")

# changeServiceInfo("172.16.10.172", "8080", "https", "G:\\svn\\自动化测试\\API-Test\\")

#
# def changeEmail(email, path):
#     tree = ET.parse(path + 'build.xml')
#     root = tree.getroot()
#     print('tag:', root.tag, 'attrib:', root.attrib, 'text:', root.text)
#     for elm in root:
#         if elm.attrib.get("name") == "mail_to":
#             print(elm.attrib.get("value"))
#             elm.attrib["value"] = email
#             print(elm.attrib.get("value"))
#     tree.write(path + 'build.xml')




def changeEmail(email, path):
    f = open(path + "build.xml", mode='r', encoding='utf-8').read()
    oldStr = f[f.find("<property name=\"mail_to\" value=")+len("<property name=\"mail_to\" value="):f.find("<property name=\"mailsubject\"")-7]
    print(oldStr)
    fileData = ''
    with open(path + "build.xml", mode='r', encoding='utf-8') as ff:
        for line in ff:
            if "<property name=\"mail_to\" value=" + oldStr in line:
                line = line.replace(oldStr, "\""+email+"\"")
            fileData += line
    with open(path + "build.xml", mode='w', encoding='utf-8') as ww:
        ww.write(fileData)

# changeEmail("","G:\\svn\\自动化测试\\API-Test\\")




def getEmailList(path):
    tree = ET.parse(path + 'build.xml')
    root = tree.getroot()
    print('tag:', root.tag, 'attrib:', root.attrib, 'text:', root.text)

    for elm in root:
        if elm.attrib.get("name") == "mail_to":
            return elm.attrib.get("value")


def getDefaultVariable(path):
    print("/getPerformanceDefaultVar=====================")
    f = open(path + fileName, mode='r', encoding='utf-8').read()
    oldStr = f[f.find("默认全局变量"):][f[f.find("默认全局变量"):].find("elementProp") - 12:][
             :f[f.find("默认全局变量"):][f[f.find("默认全局变量"):].find("elementProp") - 12:].find("collectionProp") - 2].split(
        "</elementProp>")
    variableList = []
    for elementProp in oldStr:
        argumentName = elementProp[elementProp.find("Argument.name") + 15:][
                       :elementProp[elementProp.find("Argument.name") + 15:].find("stringProp") - 2]
        argumentValue = elementProp[elementProp.find("Argument.value") + 16:][
                        :elementProp[elementProp.find("Argument.value") + 16:].find("stringProp") - 2]
        variableList.insert(1000,
                            {
                                "argumentName": argumentName,
                                "argumentValue": argumentValue
                            }
                            )
    return variableList


# getDefaultVariable("G:\\svn\\自动化测试\\API-Test\\")


def formElementProp(argumentName, argumentValue):
    elementPropStr = "          <elementProp name=" + "\"" + argumentName + "\"" + " elementType=\"Argument\">"
    argumentNameStr = "            <stringProp name=\"Argument.name\">" + argumentName + "</stringProp>"
    argumentValueStr = "            <stringProp name=\"Argument.value\">" + argumentValue + "</stringProp>"
    argumentMetadataStr = "            <stringProp name=\"Argument.metadata\">=</stringProp>"
    elementPropStrEnd = "          </elementProp>"
    return "\n" + elementPropStr + "\n" + argumentNameStr + "\n" + argumentValueStr + "\n" + argumentMetadataStr + "\n" + elementPropStrEnd + "\n"


def addDefaultVariable(argumentName, argumentValue, path):
    keyword = "<elementProp name=" + "\"" + argumentName + "\""
    f = open(path + fileName, mode='r', encoding='utf-8')
    fr = f.read()
    post = fr.find("testname=\"默认全局变量\" enabled=\"true\">") + fr[
                                                              fr.find("testname=\"默认全局变量\" enabled=\"true\">"):].find(
        "<collectionProp name=\"Arguments.arguments\">") + len("<collectionProp name=\"Arguments.arguments\">")
    print(post)
    f.close()
    if fr.find(keyword) == -1:
        newStr = fr[:post] + formElementProp(argumentName, argumentValue) + fr[post:]
        with open(path + fileName, 'w', encoding='utf-8') as ww:
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
    f = open(path + fileName, mode='r', encoding='utf-8')
    fr = f.read()
    post = fr.find(keyword)
    if post != -1:
        newStr = fr[:post] + formElementProp(newKey, value) + fr[post:][
                                                              fr[post:].find("</elementProp>") + len("</elementProp>"):]
        f.close()
        print(fr[:post])
        with open(path + fileName, mode='w', encoding='utf-8') as ww:
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
    f = open(path + fileName, mode='r', encoding='utf-8')
    fr = f.read()
    post = fr.find(keyword)
    if post != -1:
        newStr = fr[:post] + fr[post:][fr[post:].find("</elementProp>") + len("</elementProp>"):]
        f.close()
        print(fr[:post])
        with open(path + fileName, mode='w', encoding='utf-8') as ww:
            ww.truncate()
            ww.write(newStr)
            ww.close()
        return 200
    else:
        print("不存在该变量,无法删除")
        f.close()
        return 601


def removeFile(path):
    listFile = os.listdir(path)
    for fileName in listFile:
        os.remove(path+fileName)
