import json
import time

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from sql.models import VerificationCode, User, Todo, Checklist, VerificationEmailCode, UserLoginLog
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
    
    
        print(user.email)
    
        if not VerificationCode.objects.using("thirdparty").filter(mobile=mobile).order_by("-created").exists():
            phoneCode = '无手机验证码'
        else:
            phoneCode = VerificationCode.objects.using("thirdparty").filter(mobile=mobile).order_by("-created")[0].code
        
        if user.email is None:
            emailCode = VerificationEmailCode.objects.using("thirdparty").all().order_by("-created")[0].code
            email = '未绑定邮箱'
        else:
            email = user.email
            if not VerificationEmailCode.objects.using("thirdparty").filter(email=email).order_by("-created").exists():
                emailCode = '无邮箱验证码'
            else:
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
    response = [{"code": "200", "msg": "事项当日100条限制清除成功","data":tokenInfo}]
    return JsonResponse(response, safe=False)