print()


def changeAciton(strSql):
    f = open("G:\\svn\\自动化测试\\API-Test\\业务流程-整合.jmx", mode='r', encoding='utf-8')
    d = open("G:\\svn\\自动化测试\\API-Test\\业务流程-整合1.jmx", mode='w', encoding='utf-8')

    for s in f.readlines():
        if "提醒" in s:
            s.replace(s[s.find("and"):s.find("order by") - 1], "")
            s = s.replace(s[s.find("and"):s.find("order by") - 1], strSql)
        d.write(s)

listSql = ["提醒", "重复维护", "清单维护"]
strSql = "and flow_name in "+str(tuple(listSql)[0:])

changeAciton(strSql)

# changeAciton("and flow_name in (\"提醒\")")
