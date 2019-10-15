import datetime
import json
import os
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from performance.models import PerformanceFlow, PerformanceNode, Config, Testenv, User
from performance.readJmx import getEmailList, changeEmail, changeAciton, getDefaultVariable, addDefaultVariable, \
    editDefaultVariable, deleteDefaultVariable, changeServiceInfo, changeSThread, removeFile

# paths = 'D:\\时光序\\自动化测试\\API-Test\\'

paths = os.path.abspath(os.path.dirname(__file__)).split('testPlatforms')[0]+"testPlatforms\\data\\auto\\API-Performance\\"


@csrf_exempt
def performance(request):
    return render_to_response('performance.html', {})


@csrf_exempt
def getPerformanceFlowData(request):
    page_id = json.loads(request.body)["page_id"]
    page_size = json.loads(request.body)["page_size"]
    flowDataList = []
    for e in PerformanceFlow.objects.all().order_by("pk"):
        flowDataList.insert(10000,
                            {
                                'pk': e.pk,
                                'flow_name': e.flow_name,
                                'account': e.account,
                                'password': e.password,
                                'priority': e.priority,
                                'creater': e.creater,
                                'state': str(e.state),
                                'operation': "1"})
    flowData = flowDataList[(page_id - 1) * page_size:page_id * page_size]
    print(flowData)
    flowlistSize = len(PerformanceFlow.objects.all().order_by("pk"))
    response = [{"code": "200", "msg": "操作成功", "flowData": flowData, "size": flowlistSize}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getPerformanceEmail(request):
    email = getEmailList(paths)
    print(email)
    response = [{"code": "200", "msg": "邮箱获取成功", "email": email}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def performanceEmailChange(request):
    email = json.loads(request.body)["email"]
    changeEmail(email, paths)
    response = [{"code": "200", "msg": "邮箱修改成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getPerformanceNodeData(request):
    flow_id = json.loads(request.body)["flow_id"]
    data = PerformanceNode.objects.filter(flow_id__exact=flow_id).order_by("order_id")
    nodeDataList = []
    for e in data:
        nodeDataList.insert(10000, {
            'pk': e.pk,
            'flow_id': e.flow_id,
            'order_id': e.order_id,
            'node_name': e.node_name,
            'path': e.path,
            'method': e.method,
            'parameter': e.parameter,
            'expect_response': e.expect_response,
            'state': str(e.state),
            "ischechdb": str(e.ischechdb),
            "sql_str": e.sql_str,
            "sql_para": e.sql_para,
            "expect_db": e.expect_db,
            'pre_keys': e.pre_keys,
            'sleep_time': e.sleep_time,
            "isexcute_pre_sql": str(e.isexcute_pre_sql),
            "pre_sql_str": e.pre_sql_str,
            "pre_sql_para": e.pre_sql_para,
            "pre_sql_out": e.pre_sql_out,
            'post_keys': e.post_keys,
            'post_keys_extractor': e.post_keys_extractor,
            'post_keys_default': e.post_keys_default})
    return JsonResponse(nodeDataList, safe=False)


@csrf_exempt
def getPerformanceOutSql(request):
    node_id = json.loads(request.body)["node_id"]
    data = PerformanceNode.objects.filter(node_id__exact=node_id)
    outSqlDataList = []
    outSqlDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "ischechdb": str(data[0].ischechdb),
        "sql_str": data[0].sql_str,
        "sql_para": data[0].sql_para,
        "expect_db": data[0].expect_db,

    })
    return JsonResponse(outSqlDataList, safe=False)


@csrf_exempt
def editPerformanceOutSql(request):
    node_id = json.loads(request.body)["node_id"]
    ischechdb = json.loads(request.body)["ischechdb"]
    sql_str = json.loads(request.body)["sql_str"]
    sql_para = json.loads(request.body)["sql_para"]
    expect_db = json.loads(request.body)["expect_db"]
    PerformanceNode.objects.filter(node_id=node_id).update(
        ischechdb=ischechdb,
        sql_str=sql_str,
        sql_para=sql_para,
        expect_db=expect_db
    )
    response = [{"code": "200", "msg": "后置SQL校验配置成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getPerformancePreSql(request):
    node_id = json.loads(request.body)["node_id"]
    data = PerformanceNode.objects.filter(node_id__exact=node_id)
    preSqlDataList = []
    preSqlDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "isexcute_pre_sql": str(data[0].isexcute_pre_sql),
        "pre_sql_str": data[0].pre_sql_str,
        "pre_sql_para": data[0].pre_sql_para,
        "pre_sql_out": data[0].pre_sql_out,

    })
    print(preSqlDataList)
    return JsonResponse(preSqlDataList, safe=False)


@csrf_exempt
def editPerformancePreSql(request):
    node_id = json.loads(request.body)["node_id"]
    isexcute_pre_sql = int(json.loads(request.body)["isexcute_pre_sql"])
    print(type(isexcute_pre_sql))
    pre_sql_str = json.loads(request.body)["pre_sql_str"]
    pre_sql_para = json.loads(request.body)["pre_sql_para"]
    pre_sql_out = json.loads(request.body)["pre_sql_out"]
    PerformanceNode.objects.filter(node_id=node_id).update(
        isexcute_pre_sql=isexcute_pre_sql,
        pre_sql_para=pre_sql_para,
        pre_sql_str=pre_sql_str,
        pre_sql_out=pre_sql_out
    )
    response = [{"code": "200", "msg": "前置SQL查询配置成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def changePerformanceFlowState(request):
    state = json.loads(request.body)["state"]
    flow_id = json.loads(request.body)["flow_id"]
    PerformanceFlow.objects.filter(flow_id=flow_id).update(
        state=state
    )
    response = [{"code": "200", "msg": "测试流状态修改成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def changePerformanceNodeState(request):
    state = json.loads(request.body)["state"]
    node_id = json.loads(request.body)["node_id"]
    PerformanceNode.objects.filter(node_id=node_id).update(
        state=state
    )
    response = [{"code": "200", "msg": "接口状态修改成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def savePerformancePostKey(request):
    node_id = json.loads(request.body)["node_id"]
    post_keys = json.loads(request.body)["post_keys"]
    post_keys_extractor = json.loads(request.body)["post_keys_extractor"]
    post_keys_default = json.loads(request.body)["post_keys_default"]
    PerformanceNode.objects.filter(node_id=node_id).update(
        post_keys=post_keys,
        post_keys_extractor=post_keys_extractor,
        post_keys_default=post_keys_default
    )
    response = [{"code": "200", "msg": "后置变量提取配置成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getPerformancePostKey(request):
    node_id = json.loads(request.body)["node_id"]
    data = PerformanceNode.objects.filter(node_id__exact=node_id)
    postKeyDataList = []
    postKeyDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "post_keys": data[0].post_keys,
        "post_keys_extractor": data[0].post_keys_extractor,
        "post_keys_default": data[0].post_keys_default,
    })
    return JsonResponse(postKeyDataList, safe=False)


@csrf_exempt
def getPerformanceCreater(request):
    creater = json.loads(request.body)["creater"]
    page_size = json.loads(request.body)["page_size"]
    if creater == "全部负责人":
        data = PerformanceFlow.objects.all()[0:page_size]
        print(data)
    else:
        data = PerformanceFlow.objects.filter(creater__exact=creater)[0:page_size]
    flowDataListForCreater = []
    for e in data:
        flowDataListForCreater.insert(10000,
                                      {
                                          'pk': e.pk,
                                          'flow_name': e.flow_name,
                                          'account': e.account,
                                          'password': e.password,
                                          'priority': e.priority,
                                          'creater': e.creater,
                                          'state': str(e.state),
                                          'operation': 1})
    print(flowDataListForCreater)
    return JsonResponse(flowDataListForCreater, safe=False)


@csrf_exempt
def getPerformanceParameter(request):
    node_id = json.loads(request.body)["node_id"]
    data = PerformanceNode.objects.filter(node_id__exact=node_id)
    parameterDataList = []
    parameterDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "parameter": data[0].parameter,
    })
    return JsonResponse(parameterDataList, safe=False)


@csrf_exempt
def editPerformanceParameter(request):
    node_id = json.loads(request.body)["node_id"]
    parameter = json.loads(request.body)["parameter"]
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    PerformanceNode.objects.filter(node_id=node_id).update(
        node_id=node_id,
        parameter=parameter,
        update_time=update_time
    )
    response = [{"code": "200", "msg": "请求参数配置成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def addPerformanceFlow(request):
    flow_id = PerformanceFlow.objects.all().order_by("-flow_id")[0].flow_id + 1
    flow_code = "TEST_FLOW_0" + str(flow_id)
    flow_name = json.loads(request.body)["flow_name"]
    password = json.loads(request.body)["password"]
    priority = json.loads(request.body)["priority"]
    creater = json.loads(request.body)["creater"]
    state = json.loads(request.body)["state"]
    account = json.loads(request.body)["account"]
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    addFlowData = PerformanceFlow.objects.create(
        flow_id=flow_id,
        flow_code=flow_code,
        flow_name=flow_name,
        password=password,
        priority=priority,
        state=state,
        account=account,
        creater=creater,
        create_time=create_time,
        update_time=update_time
    )
    response = [{"code": "200", "msg": "测试流添加成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def editPerformanceFlow(request):
    flow_id = json.loads(request.body)["pk"]
    PerformanceFlow.objects.filter(flow_id=flow_id).update(
        flow_name=json.loads(request.body)["flow_name"],
        password=json.loads(request.body)["password"],
        priority=json.loads(request.body)["priority"],
        state=json.loads(request.body)["state"],
        account=json.loads(request.body)["account"],
        creater=json.loads(request.body)["creater"],
        update_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    response = [{"code": "200", "msg": "测试流保存成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def deletePerformanceFlow(request):
    flow_id = json.loads(request.body)["flow_id"]
    print('flow_id=', flow_id)
    PerformanceFlow.objects.filter(flow_id=flow_id).delete()
    response = [{"code": "200", "msg": "测试流删除成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def deletePerformanceNode(request):
    node_id = json.loads(request.body)["node_id"]
    print("node_id", node_id)
    PerformanceNode.objects.filter(node_id=node_id).delete()
    response = [{"code": "200", "msg": "接口删除成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def addPerformanceNode(request):
    flow_id = json.loads(request.body)["flow_id"]
    order_id = json.loads(request.body)["order_id"]
    node_id = PerformanceNode.objects.all().order_by("-node_id")[0].node_id + 1
    node_code = PerformanceFlow.objects.filter(flow_id=flow_id)[0].flow_code.replace("TEST_",
                                                                                     "") + "_" + "NODE_0" + order_id
    node_name = json.loads(request.body)["node_name"]
    method = json.loads(request.body)["method"]
    path = json.loads(request.body)["path"]
    parameter = json.loads(request.body)["parameter"]
    pre_keys = json.loads(request.body)["pre_keys"]
    sleep_time = json.loads(request.body)["sleep_time"]
    expect_response = json.loads(request.body)["expect_response"]
    state = json.loads(request.body)["state"]
    isexcute_pre_sql = json.loads(request.body)["isexcute_pre_sql"]
    pre_sql_out = json.loads(request.body)["pre_sql_out"]
    pre_sql_str = json.loads(request.body)["pre_sql_str"]
    pre_sql_para = json.loads(request.body)["pre_sql_para"]
    expect_db = json.loads(request.body)["expect_db"]
    ischechdb = json.loads(request.body)["ischechdb"]
    sql_para = json.loads(request.body)["sql_para"]
    sql_str = json.loads(request.body)["sql_str"]
    post_keys = json.loads(request.body)["post_keys"]
    post_keys_extractor = json.loads(request.body)["post_keys_extractor"]
    post_keys_default = json.loads(request.body)["post_keys_default"]
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    PerformanceNode.objects.create(
        node_id=node_id,
        order_id=int(order_id),
        flow_id=flow_id,
        node_code=node_code,
        node_name=node_name,
        method=method,
        path=path,
        parameter=parameter,
        pre_keys=pre_keys,
        sleep_time=sleep_time,
        expect_response=expect_response,
        state=state,
        isexcute_pre_sql=isexcute_pre_sql,
        pre_sql_out=pre_sql_out,
        pre_sql_para=pre_sql_para,
        pre_sql_str=pre_sql_str,
        expect_db=expect_db,
        ischechdb=ischechdb,
        sql_para=sql_para,
        sql_str=sql_str,
        post_keys=post_keys,
        post_keys_extractor=post_keys_extractor,
        post_keys_default=post_keys_default,
        create_time=create_time,
        update_time=update_time
    )
    response = [{"code": "200", "msg": "接口添加成功", "node_id": node_id}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def editPerformanceNode(request):
    order_id = json.loads(request.body)["order_id"]
    flow_id = json.loads(request.body)["flow_id"]
    node_id = json.loads(request.body)["pk"]
    node_code = PerformanceFlow.objects.filter(flow_id=flow_id)[0].flow_code.replace("TEST_", "") + "NODE_0" + str(
        order_id)
    node_name = json.loads(request.body)["node_name"]
    method = json.loads(request.body)["method"]
    path = json.loads(request.body)["path"]
    parameter = json.loads(request.body)["parameter"]
    expect_response = json.loads(request.body)["expect_response"]
    pre_keys = json.loads(request.body)["pre_keys"]
    sleep_time = json.loads(request.body)["sleep_time"]
    state = json.loads(request.body)["state"]
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("node_id", node_id)
    PerformanceNode.objects.filter(node_id=node_id).update(
        node_id=node_id,
        order_id=order_id,
        flow_id=flow_id,
        node_code=str(node_code),
        node_name=node_name,
        method=method,
        path=path,
        parameter=parameter,
        expect_response=expect_response,
        pre_keys=pre_keys,
        sleep_time=sleep_time,
        state=state,
        update_time=update_time
    )
    response = [{"code": "200", "msg": "接口添加成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def actionPerformanceFlow(request):
    flow_id = json.loads(request.body)["flow_id"]
    newStr = 'flow_id = ' + str(flow_id)
    changeAciton(newStr, paths)
    removeFile(paths+"Report\\html\\")
    removeFile(paths+"Report\\jtl\\")
    os.chdir(paths)
    os.system("ant")
    response = [{"code": "200", "msg": "接口触发允许成功，请查收邮件"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def actionPerformanceAllFlow(request):
    newStr = "1=1"
    changeAciton(newStr, paths)
    removeFile(paths+"Report\\html\\")
    removeFile(paths+"Report\\jtl\\")
    os.chdir(paths)
    os.system("ant")
    response = [{"code": "200", "msg": "接口触发允许成功，请查收邮件"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getPerformanceDefaultVar(request):
    varList = getDefaultVariable(paths)
    response = [{"code": "200", "msg": "默认变量获取成功", "varList": varList}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def addPerformanceDefaultVar(request):
    argumentName = json.loads(request.body)["argumentName"]
    argumentValue = json.loads(request.body)["argumentValue"]
    result = addDefaultVariable(argumentName, argumentValue, paths)
    if result == 200:
        response = [{"code": "200", "msg": "默认变量添加成功"}]
        return JsonResponse(response, safe=False)
    elif result == 601:
        response = [{"code": "601", "msg": "变量已存在"}]
        return JsonResponse(response, safe=False)


@csrf_exempt
def editPerformanceDefaultVar(request):
    oldKey = json.loads(request.body)["argumentName"]
    newKey = json.loads(request.body)["argumentNameNew"]
    value = json.loads(request.body)["argumentValue"]
    result = editDefaultVariable(oldKey, newKey, value, paths)
    if result == 200:
        response = [{"code": "200", "msg": "默认变量修改成功"}]
        return JsonResponse(response, safe=False)
    elif result == 601:
        response = [{"code": "601", "msg": "变量不存在"}]
        return JsonResponse(response, safe=False)


@csrf_exempt
def deletePerformanceDefaultVar(request):
    argumentName = json.loads(request.body)["argumentName"]
    result = deleteDefaultVariable(argumentName, paths)
    if result == 200:
        response = [{"code": "200", "msg": "默认变量删除成功"}]
        return JsonResponse(response, safe=False)
    elif result == 601:
        response = [{"code": "601", "msg": "变量不存在"}]
        return JsonResponse(response, safe=False)


@csrf_exempt
def getPerformanceConfig(request):
    config = Config.objects.filter(id=1).order_by("pk")[0]
    testenv = Testenv.objects.filter(env_code=config.env_code).order_by("pk")[0]
    serverName = testenv.host
    formList = []
    formList.insert(10000, {
        "pk": config.pk,
        "email": config.email,
        "protocol": testenv.protocol,
        "serverName": testenv.env_code,
        "port": testenv.port,
        "num_threads": config.numthreads,
        "ramp_time": config.ramptime,
        "loops": config.loops,
    })
    changeEmail(config.email, paths)
    changeServiceInfo(serverName, testenv.port, testenv.protocol, paths)
    changeSThread(str(config.loops), str(config.numthreads), str(config.ramptime), paths)
    response = [{"code": "200", "msg": "配置获取成功", "formList": formList}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def savePerformanceConfig(request):
    form = json.loads(request.body)["form"]
    protocol = form["protocol"]
    email = form["email"]
    port = form["port"]
    env_code = form["serverName"]
    configId = form["pk"]
    num_threads = form["num_threads"]
    ramp_time = form["ramp_time"]
    loops = form["loops"]
    serverName = Testenv.objects.filter(env_code=env_code)[0].host
    Testenv.objects.filter(env_code=env_code).update(
        port=port,
        protocol=protocol,
        env_code=env_code
    )
    Config.objects.filter(id=configId).update(
        env_code=env_code,
        loops=loops,
        numthreads=num_threads,
        email=email,
        ramptime=ramp_time,
    )
    changeEmail(email, paths)
    changeServiceInfo(serverName, str(port), str(protocol), paths)
    changeSThread(str(loops), str(num_threads), str(ramp_time), paths)
    response = [{"code": "200", "msg": "配置获取成功", "formList": [form]}]
    return JsonResponse(response, safe=False)
