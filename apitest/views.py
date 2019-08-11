import datetime
import json

import numpy as np
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from apitest.models import TestdataNode, TestdataFlow


@csrf_exempt
def apitest(request):
    return render_to_response('apitest.html', {})


@csrf_exempt
def getFlowData(request):
    flowDataList = []
    for e in TestdataFlow.objects.all():
        flowDataList.insert(10000,
                            {
                                'pk': e.pk,
                                'flow_name': e.flow_name,
                                'account': e.account,
                                'password': e.password,
                                'priority': e.priority,
                                'creater': e.creater,
                                'state': e.state,
                                'operation': "1",
                            })
    return JsonResponse(flowDataList, safe=False)


@csrf_exempt
def getNodeData(request):
    flow_id = json.loads(request.body)["flow_id"]
    data = TestdataNode.objects.filter(flow_id__exact=flow_id).order_by("order_id")
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
            'dbcheck': {
                "ischechdb": e.ischechdb,
                "sql_str": e.sql_str,
                "sql_para": e.sql_para,
                "expect_db": e.expect_db
            },
            'pre_keys': e.pre_keys,
            'sleep_time': e.sleep_time,
            'presql': {
                "isexcute_pre_sql": e.isexcute_pre_sql,
                "pre_sql_str": e.pre_sql_str,
                "pre_sql_para": e.pre_sql_para,
                "pre_sql_out": e.pre_sql_out
            },
            'post_keys': e.post_keys,
            'post_keys_extractor': e.post_keys_extractor,
            'post_keys_default': e.post_keys_default,
            'state': e.state
        })
    print(nodeDataList)
    return JsonResponse(nodeDataList, safe=False)
    # return HttpResponse(listToJson(nodeDataList), content_type="application/json,charset=utf-8")


@csrf_exempt
def getOutSql(request):
    node_id = json.loads(request.body)["node_id"]
    data = TestdataNode.objects.filter(node_id__exact=node_id)
    outSqlDataList = []
    print(data)
    outSqlDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "ischechdb": data[0].ischechdb,
        "sql_str": data[0].sql_str,
        "sql_para": data[0].sql_para,
        "expect_db": data[0].expect_db,

    })
    print(outSqlDataList)
    return JsonResponse(outSqlDataList, safe=False)

@csrf_exempt
def editOutSql(request):
    print(json.loads(request.body)["ischechdb"])
    node_id = json.loads(request.body)["node_id"]
    ischechdb = json.loads(request.body)["ischechdb"]
    sql_str = json.loads(request.body)["sql_str"]
    sql_para = json.loads(request.body)["sql_para"]
    expect_db = json.loads(request.body)["expect_db"]
    TestdataNode.objects.filter(node_id=node_id).update(
        ischechdb=ischechdb,
        sql_str=sql_str,
        sql_para=sql_para,
        expect_db=expect_db
    )
    response = [{"code": "200", "msg": "后置SQL校验配置成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getPreSql(request):
    node_id = json.loads(request.body)["node_id"]
    data = TestdataNode.objects.filter(node_id__exact=node_id)
    preSqlDataList = []
    print(data)
    preSqlDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "isexcute_pre_sql": data[0].isexcute_pre_sql,
        "pre_sql_str": data[0].pre_sql_str,
        "pre_sql_para": data[0].pre_sql_para,
        "pre_sql_out": data[0].pre_sql_out,

    })
    print(preSqlDataList)
    return JsonResponse(preSqlDataList, safe=False)

@csrf_exempt
def editPreSql(request):
    node_id = json.loads(request.body)["node_id"]
    isexcute_pre_sql = json.loads(request.body)["isexcute_pre_sql"]
    pre_sql_str = json.loads(request.body)["pre_sql_str"]
    pre_sql_para = json.loads(request.body)["pre_sql_para"]
    pre_sql_out = json.loads(request.body)["pre_sql_out"]
    TestdataNode.objects.filter(node_id=node_id).update(
        isexcute_pre_sql=isexcute_pre_sql,
        pre_sql_para=pre_sql_para,
        pre_sql_str=pre_sql_str,
        pre_sql_out=pre_sql_out
    )
    response = [{"code": "200", "msg": "前置SQL查询配置成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def savePostKey(request):
    node_id = json.loads(request.body)["node_id"]
    post_keys = json.loads(request.body)["post_keys"]
    post_keys_extractor = json.loads(request.body)["post_keys_extractor"]
    post_keys_default = json.loads(request.body)["post_keys_default"]
    TestdataNode.objects.filter(node_id=node_id).update(
        post_keys=post_keys,
        post_keys_extractor=post_keys_extractor,
        post_keys_default=post_keys_default
    )
    response = [{"code": "200", "msg": "后置变量提取配置成功"}]
    return JsonResponse(response, safe=False)

@csrf_exempt
def getPostKey(request):
    node_id = json.loads(request.body)["node_id"]
    data = TestdataNode.objects.filter(node_id__exact=node_id)
    postKeyDataList = []
    print(data)
    postKeyDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "post_keys": data[0].post_keys,
        "post_keys_extractor": data[0].post_keys_extractor,
        "post_keys_default": data[0].post_keys_default,
    })
    print(postKeyDataList)
    return JsonResponse(postKeyDataList, safe=False)


@csrf_exempt
def getParameter(request):
    node_id = json.loads(request.body)["node_id"]
    data = TestdataNode.objects.filter(node_id__exact=node_id)
    parameterDataList = []
    print(data)
    parameterDataList.insert(10000, {
        "pk": data[0].pk,
        "flow_id": data[0].flow_id,
        "parameter": data[0].parameter,
    })
    print(parameterDataList)
    return JsonResponse(parameterDataList, safe=False)


@csrf_exempt
def editParameter(request):
    node_id = json.loads(request.body)["node_id"]
    parameter = json.loads(request.body)["parameter"]
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    TestdataNode.objects.filter(node_id=node_id).update(
        node_id=node_id,
        parameter=parameter,
        update_time=update_time
    )
    response = [{"code": "200", "msg": "请求参数配置成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def addFlow(request):
    flow_id = TestdataFlow.objects.all().order_by("-flow_id")[0].flow_id + 1
    flow_code = "TEST_FLOW_0" + str(flow_id)
    flow_name = json.loads(request.body)["flow_name"]
    password = json.loads(request.body)["password"]
    priority = json.loads(request.body)["priority"]
    creater = json.loads(request.body)["creater"]
    state = json.loads(request.body)["state"]
    account = json.loads(request.body)["account"]
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    addFlowData = TestdataFlow.objects.create(
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
    print(addFlowData)
    response = [{"code": "200", "msg": "测试流添加成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def editFlow(request):
    flow_id = json.loads(request.body)["pk"]
    TestdataFlow.objects.filter(flow_id=flow_id).update(
        flow_name=json.loads(request.body)["flow_name"],
        password=json.loads(request.body)["password"],
        priority=json.loads(request.body)["priority"],
        state=json.loads(request.body)["state"],
        account=json.loads(request.body)["account"],
        creater=json.loads(request.body)["creater"],
        update_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    # obj = TestdataFlow.objects.get(flow_id=flow_id)
    # obj.flow_name = flow_name,
    # obj.password = password,
    # obj.priority = priority,
    # obj.state = state,
    # obj.account = account,
    # obj.update_time = update_time
    # obj.save()
    response = [{"code": "200", "msg": "测试流保存成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def deleteFlow(request):
    flow_id = json.loads(request.body)["pk"]
    TestdataFlow.objects.filter(flow_id=flow_id).delete()
    response = [{"code": "200", "msg": "测试流删除成功"}]
    return JsonResponse(response, safe=False)

@csrf_exempt
def deleteNode(request):
    node_id = json.loads(request.body)["pk"]
    TestdataNode.objects.filter(node_id=node_id).delete()
    response = [{"code": "200", "msg": "接口删除成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def addNode(request):
    global isexcute_pre_sql, pre_sql_out, pre_sql_str, expect_db, sql_para, sql_str, pre_sql_para, ischechdb
    flow_id = json.loads(request.body)["flow_id"]
    order_id = json.loads(request.body)["order_id"]
    node_id = TestdataNode.objects.all().order_by("-node_id")[0].node_id + 1
    node_code = TestdataFlow.objects.filter(flow_id=flow_id)[0].flow_code.replace("TEST_", "") + "NODE_0" + order_id
    node_name = json.loads(request.body)["node_name"]
    method = json.loads(request.body)["method"]
    path = json.loads(request.body)["path"]
    parameter = json.loads(request.body)["parameter"]
    pre_keys = json.loads(request.body)["pre_keys"]
    sleep_time = json.loads(request.body)["sleep_time"]
    presql = json.loads(request.body)["presql"]
    ischechdb = json.loads(request.body)["dbcheck"]

    for key, value in presql.items():
        if key == "isexcute_pre_sql":
            isexcute_pre_sql = value
        elif key == "pre_sql_out":
            pre_sql_out = value
        elif key == "pre_sql_str":
            pre_sql_str = value
        elif key == "pre_sql_para":
            pre_sql_para = value

    for key, value in ischechdb.items():
        if key == "expect_db":
            expect_db = value
        elif key == "ischechdb":
            ischechdb = value
        elif key == "sql_para":
            sql_para = value
        elif key == "sql_str":
            sql_str = value

    post_keys = json.loads(request.body)["post_keys"]
    post_keys_extractor = json.loads(request.body)["post_keys_extractor"]
    post_keys_default = json.loads(request.body)["post_keys_default"]
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    addNodeData = TestdataNode.objects.create(
        node_id=node_id,
        order_id=order_id,
        flow_id=flow_id,
        node_code=node_code,
        node_name=node_name,
        method=method,
        path=path,
        parameter=parameter,
        pre_keys=pre_keys,
        sleep_time=sleep_time,
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
    response = [{"code": "200", "msg": "接口添加成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def editNode(request):
    global isexcute_pre_sql, pre_sql_out, pre_sql_str, expect_db, sql_para, sql_str, pre_sql_para, ischechdb
    order_id = json.loads(request.body)["order_id"]
    flow_id = json.loads(request.body)["flow_id"]
    node_id = json.loads(request.body)["pk"]
    node_code = TestdataFlow.objects.filter(flow_id=flow_id)[0].flow_code.replace("TEST_", "") + "NODE_0" + str(
        order_id)
    node_name = json.loads(request.body)["node_name"]
    method = json.loads(request.body)["method"]
    path = json.loads(request.body)["path"]
    parameter = json.loads(request.body)["parameter"]
    pre_keys = json.loads(request.body)["pre_keys"]
    sleep_time = json.loads(request.body)["sleep_time"]
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    addNodeData = TestdataNode.objects.filter(node_id=node_id).update(
        node_id=node_id,
        order_id=order_id,
        flow_id=flow_id,
        node_code=str(node_code),
        node_name=node_name,
        method=method,
        path=path,
        parameter=parameter,
        pre_keys=pre_keys,
        sleep_time=sleep_time,
        update_time=update_time
    )
    response = [{"code": "200", "msg": "接口添加成功"}]
    return JsonResponse(response, safe=False)
