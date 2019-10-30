from apitest.dbUitls import MysqlHelper

mh = MysqlHelper('47.112.0.183', 'planadmin', 'pL%5^an3a$4in', 'automation')

def getPathByTestDataNode():
    sql = "SELECT path FROM automation.testdata_node"
    return mh.find(sql, None)

def getPathByApiStatistics():
    sql = "SELECT path FROM automation.api_statistics"
    return mh.find(sql, None)


testDataNodePath = getPathByTestDataNode()
apiStatisticsPath = getPathByApiStatistics()

def isExitPath(path):
    k = ()
    for paht in testDataNodePath:
        k = k + (paht[0],)
    return k.count(path)


def isExitApiStatistics(path):
    k = ()
    for paht in apiStatisticsPath:
        k = k + (paht[0],)
    return k.count(path)
