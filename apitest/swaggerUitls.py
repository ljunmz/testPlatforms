import json

from apitest.TestdataNodeDao import isExitPath, isExitApiStatistics, getRemarks
from apitest.requestUitls import doRequest

swaggerList = doRequest("GET", "http://47.112.0.183:8801/swagger-resources", {}, {}, {})


def getSwaggerApi():
    serviceCount = 0
    apiCounts = 0
    undoneCounts = 0
    unStatisticsCounts = 0
    undoneList = []
    unStatisticsList = []
    id = 0
    ids = 0
    ignoreList = ["/web-backend/v2/api-docs", "/service-monitor/v2/api-docs", "/base-water/v2/api-docs", "/base-work/v2/api-docs", "/base-book/v2/api-docs", "/base-lifeday/v2/api-docs", "/base-healthy/v2/api-docs"]
    for path in json.loads(swaggerList):
        if path["url"] not in ignoreList:
            respon = doRequest("GET", "http://47.112.0.183:8801" + path["url"], {}, {}, {})
            responJson = json.loads(respon)
            serviceCount = serviceCount + 1
            # 服务api数量
            apiCount = 0
            # 服务未实现接口
            undoneCount = 0
            # 服务未统计接口
            unStatisticsCount = 0
            # 服务名称
            serviceName = str(path["location"]).split("/")[1]
            print("================" + str(serviceName))
            for paths in list(responJson["paths"].keys()):
                if paths != "/checkalive" and paths != "/service/weixin/api":
                    apiCount = apiCount + 1
                    if "post" in responJson["paths"][paths]:
                        if isExitPath(paths) <= 0:
                            # print("未实现-->"+str(paths))
                            undoneCount = undoneCount + 1
                            ids = ids + 1
                            undoneList.append({"id": ids,
                                               "serviceName": serviceName,
                                               "apiName": responJson["paths"][paths]["post"]["summary"],
                                               "url": paths,
                                               "remark": getRemarks(paths)})
                        if isExitApiStatistics(paths) <= 0:
                            print("未统计-->" + str(paths))
                            unStatisticsCount = unStatisticsCount + 1
                            id = id + 1
                            unStatisticsList.append({"id": id,
                                                     "serviceName": serviceName,
                                                     "apiName": responJson["paths"][paths]["post"]["summary"],
                                                     "url": paths})
                    elif "get" in responJson["paths"][paths]:
                        if isExitPath(paths) <= 0:
                            # print("未实现-->"+str(paths))
                            undoneCount = undoneCount + 1
                            ids = ids + 1
                            undoneList.append({"id": ids, "serviceName": serviceName,
                                               "apiName": responJson["paths"][paths]["get"]["summary"],
                                               "url": paths,
                                               "remark": getRemarks(paths)})
                        if isExitApiStatistics(paths) <= 0:
                            print("未统计-->" + str(paths))
                            unStatisticsCount = unStatisticsCount + 1
                            id = id + 1
                            unStatisticsList.append({"id": id,
                                                     "serviceName": serviceName,
                                                     "apiName": responJson["paths"][paths]["get"]["summary"],
                                                     "url": paths})
            undoneCounts = undoneCounts + undoneCount
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
