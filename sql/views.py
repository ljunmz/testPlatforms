import json
import time

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from sql.models import VerificationCode, User, Todo, Checklist, VerificationEmailCode, UserLoginLog, TodoFinish, \
    TodoRepeatRule, UserBehaviorLog
from sql.requestUitls import doRequest


@csrf_exempt
def sqlIndex(request):
    return render_to_response('sqlOperation.html', {})


@csrf_exempt
def register(request):
    mobile = json.loads(request.body)["mobile"]
    devicesAndroid = {"deviceType": "1", "appVersion": "1.4.7", "deviceTag": "90:f0:52:5d:75:a4", "isRoot": "false",
                      "osVersion": 27, "ip": "172.16.11.21", "channel": "xiaomi", "deviceModel": "Meizu-16th Plus",
                      "channelName": "android", "channelType": "sgx", "deviceTagApp": "90:f0:52:5d:75:a4"}
    method = "POST"
    header = {}
    datas = {}
    sendMessageUrl = 'http://47.112.0.183:8801/web/thirdparty/sendSmsMessage'
    sendMessageJson = {'device': devicesAndroid, 'mobile': mobile, 'productName': '时光序', 'type': 3}

    """清除验证码记录"""
    VerificationCode.objects.using("thirdparty").filter(device_model="Meizu-16th Plus").delete()

    sendMessageRe = doRequest(method, sendMessageUrl, datas, sendMessageJson, header)
    json_sendMessage = json.loads(sendMessageRe)
    print(json_sendMessage['msg'])

    registUrl = 'http://47.112.0.183:8801/base/user/register'

    if json_sendMessage['msg'] == '短信验证码发送成功':
        time.sleep(3)
        code = VerificationCode.objects.using("thirdparty").filter(mobile=mobile).order_by("-created")[0].code
        print(code)
        registJson = {'appType': '2', 'code': code, 'device': devicesAndroid, 'mobile': mobile, 'password': '123456',
                      'shareCode': '', 'type': 3}
        registRe = doRequest(method, registUrl, datas, registJson, header)
        json_regist = json.loads(registRe)
        if json_regist['code'] == 200 and json_regist['msg'] == '操作成功':
            response = [{"code": "200", "msg": "注册成功"}]
            return JsonResponse(response, safe=False)
        else:
            response = [{"code": "602", "msg": "注册失败"}]
            return JsonResponse(response, safe=False)
    else:
        response = [{"code": "601", "msg": "注册失败"}]
        return JsonResponse(response, safe=False)


@csrf_exempt
def clearModelCodeRecords(request):
    device_model = json.loads(request.body)["device_model"]
    result = VerificationCode.objects.using("thirdparty").filter(device_model=device_model).delete()
    print(result)
    response = [{"code": "200", "msg": "设备获取短信验证码记录清除成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def clearPhoneCodeRecords(request):
    mobile = json.loads(request.body)["mobile"]
    result = VerificationCode.objects.using("thirdparty").filter(mobile=mobile).delete()
    print(result)
    response = [{"code": "200", "msg": "手机号获取短信验证码记录清除成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def changeCreatedTime(request):
    mobile = json.loads(request.body)["mobile"]
    user_id = User.objects.using("user").filter(mobile=mobile)[0].id
    print(user_id)
    Todo.objects.using("plan").filter(Q(user_id=user_id) | Q(created__gte='2019-08-26 00:00:01')).update(
        created='2019-08-14 00:00:01'
    )
    Checklist.objects.using("plan").filter(Q(user_id=user_id) | Q(created__gte='2019-08-26 00:00:01')).update(
        created='2019-08-14 00:00:01'
    )
    response = [{"code": "200", "msg": "事项当日100条限制清除成功"}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getUserInfo(request):
    mobile = json.loads(request.body)["mobile"]
    if not User.objects.using("user").filter(mobile=mobile).exists():
        response = [{"code": "600", "msg": "手机号未注册", "data": ""}]
        return JsonResponse(response, safe=False)
    else:
        user = User.objects.using("user").filter(mobile=mobile)[0]
        if not VerificationCode.objects.using("thirdparty").filter(mobile=mobile).order_by("-created").exists():
            print("无手机验证码")
            phoneCode = '无手机验证码'
        else:
            phoneCode = VerificationCode.objects.using("thirdparty").filter(mobile=mobile).order_by("-created")[0].code
            print("有手机验证码")
        if user.email is None:
            print("未绑定邮箱")
            email = '未绑定邮箱'
            if not VerificationEmailCode.objects.using("thirdparty").all().order_by("-created").exists():
                emailCode = "无邮箱验证码"
            else:
                emailCode = VerificationEmailCode.objects.using("thirdparty").all().order_by("-created")[0].code
        else:
            print("已绑定邮箱")
            email = user.email
            if not VerificationEmailCode.objects.using("thirdparty").filter(email=email).order_by("-created").exists():
                print("无邮箱验证码")
                emailCode = '无邮箱验证码'
            else:
                print("有邮箱验证码")
                emailCode = VerificationEmailCode.objects.using("thirdparty").filter(email=email).order_by("-created")[0].code

        userInfo = {
            "user_id": str(user.pk),
            "user_name": user.user_name,
            "email": email,
            "phoneCode": phoneCode,
            "emailCode": emailCode,

        }
        print(userInfo)
        response = [{"code": "200", "msg": "获取信息成功", "data": userInfo}]
        return JsonResponse(response, safe=False)


@csrf_exempt
def getTokenInfo(request):
    token = json.loads(request.body)["token"]
    loginLog = UserLoginLog.objects.using("user").filter(token=token)[0]
    moblie = User.objects.using("user").filter(id=loginLog.user_id)[0].mobile
    tokenInfo = {
        "user_id": str(loginLog.user_id),
        "device_tag_app": loginLog.device_tag_app,
        "moblie": moblie,
        "updated": loginLog.updated,
    }
    response = [{"code": "200", "msg": "事项当日100条限制清除成功", "data": tokenInfo}]
    return JsonResponse(response, safe=False)


@csrf_exempt
def getTodoInfo(request):
    todo_id = json.loads(request.body)["todo_id"]
    todo = Todo.objects.using("plan").filter(id=todo_id)[0]
    rule = TodoRepeatRule.objects.using("plan").filter(Q(todo_id=todo_id) | Q(repeat_type=0)).order_by('-updated')[0]
    print(rule.todo_time)
    print(rule.next_time)
    print(rule.todo_time)
    print(TodoFinish.objects.using("plan").filter(todo_id=todo_id))
    if not TodoFinish.objects.using("plan").filter(todo_id=todo_id).exists():
        finish_State = '0'
    else:
        finish_State = TodoFinish.objects.using("plan").filter(todo_id=todo_id).order_by('-updated')[0].finish_state
    todoInfo = {
        "user_id": str(todo.user_id),
        "short_title": todo.short_title,
        "todo_type": todo.todo_type,
        "status": todo.status,
        "finish_state": finish_State,
        "deleted": todo.deleted,
        "todo_time": rule.todo_time,
        "next_time": rule.next_time,
        "created": todo.created,
        "ahead_type": todo.ahead_type,
    }
    response = [{"code": "200", "msg": "日程信息查询成功", "data": todoInfo}]
    return JsonResponse(response, safe=False)

@csrf_exempt
def getBuriedInfo(request):
    print("aaaaaaaaaaaa")
    mobile = json.loads(request.body)["phone"]
    user_id = User.objects.using("user").filter(mobile=mobile)[0].id
    buriedInfoList = UserBehaviorLog.objects.using("user").filter(user_id=user_id).order_by('-created')[0]
    buriedInfo = {
        "user_id": str(buriedInfoList.user_id),
        "device_tag": buriedInfoList.device_tag,
        "event_type": buriedInfoList.event_type,
        "event_param": buriedInfoList.event_param,
        "ip": buriedInfoList.ip,
        "channel": buriedInfoList.channel,
        "os_type": buriedInfoList.os_type,
        "network_type": buriedInfoList.network_type,
        "created": buriedInfoList.created,
        "app_version": buriedInfoList.app_version
    }
    response = [{"code": "200", "msg": "埋点信息查询成功", "data": buriedInfo}]
    return JsonResponse(response, safe=False)


# @csrf_exempt
# def getDevice(request):
#     print("sssssssssssssssssssss")
#     device_tag = json.loads(request.body)["device_tag"]
#     buriedInfoList = UserBehaviorLog.objects.using("user").filter(device_tag=device_tag).order_by('-created')[0]
#     mobile = User.objects.using("user").filter(id=buriedInfoList.user_id)[0].mobile
#     buriedInfoByDevice = {
#         "user_id": str(buriedInfoList.user_id),
#         "mobile": mobile,
#         "device_tag": buriedInfoList.device_tag,
#         "event_type": buriedInfoList.event_type,
#         "event_param": buriedInfoList.event_param,
#         "ip": buriedInfoList.ip,
#         "channel": buriedInfoList.channel,
#         "os_type": buriedInfoList.os_type,
#         "network_type": buriedInfoList.network_type,
#         "created": buriedInfoList.created,
#         "app_version": buriedInfoList.app_version
#     }
#     response = [{"code": "200", "msg": "埋点信息查询成功", "data": buriedInfoByDevice}]
#     return JsonResponse(response, safe=False)