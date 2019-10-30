import json

from apitest.TestdataNodeDao import isExitPath, isExitApiStatistics
from apitest.requestUitls import doRequest

swaggerList = doRequest("GET", "http://47.112.0.183:8801/swagger-resources", {}, {}, {})

def getSwaggerApi():
    serviceCount = 0
    apiCounts = 0
    undoneCounts = 0
    unStatisticsCounts = 0
    undoneList = []
    unStatisticsList = []
    for path in json.loads(swaggerList):
        if path["url"] != "/web-backend/v2/api-docs" and path["url"] != "/service-monitor/v2/api-docs":
            respon = doRequest("GET", "http://47.112.0.183:8801" + path["url"], {}, {}, {})
            responJson = json.loads(respon)
            serviceCount = serviceCount + 1
            #服务api数量
            apiCount = 0
            #服务未实现接口
            undoneCount = 0
            #服务未统计接口
            unStatisticsCount = 0
            #服务名称
            serviceName = path["name"]
            for paths in list(responJson["paths"].keys()):
                if paths != "/checkalive" and paths!= "/service/weixin/api":
                    apiCount = apiCount + 1
                    if isExitPath(paths)<=0:
                        # print("未实现-->"+str(paths))
                        undoneCount = undoneCount +1
                        undoneList.append(paths)
                    if isExitApiStatistics(paths)<=0:
                        print("未统计-->"+str(paths))
                        unStatisticsCount = unStatisticsCount +1
                        unStatisticsList.append(paths)
            undoneCounts = undoneCounts+undoneCount
            apiCounts = apiCounts + apiCount
            unStatisticsCounts = unStatisticsCounts + unStatisticsCount
            # print("=============="+str(serviceName)+"==============")
    print("======================================")
    print("微服务数量-->", serviceCount)
    print("接口总数-->", apiCounts)
    print("未实现接口总数-->", undoneCounts)
    print("未统计接口总数-->", unStatisticsCounts)
    print("======================================")
    return {
        "serviceCount": serviceCount,
        "apiCounts": apiCounts,
        "undoneCounts": undoneCounts,
        "unStatisticsCounts": unStatisticsCounts,
        "undoneList": undoneList,
        "unStatisticsList": unStatisticsList,
        }


# getSwaggerApi()

#
# f2 = open("F:\\code\\testPlatforms\\nodes\\2.txt", mode='r', encoding='utf-8').read()
# with open("F:\\code\\testPlatforms\\nodes\\1.txt", mode='r', encoding='utf-8') as ss:
#     for line in ss:
#         if line not in f2:
#             # print("已统计接口"+ line)
#             print(line.strip())
#





# from redminelib import Redmine
# import json
#
# redMineURL = "red.shiguangxu.com"
# userName = "liujun"
# passWord = "lj111235422@a"
#
# redmine = Redmine(redMineURL, username=userName, password=passWord)
# project = redmine.project.get("livelihood")
# print(project.id)
#
# print(redmine.issue.get(11939))