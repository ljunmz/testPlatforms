import os

from gevent import thread

import django
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from task.models import Task

os.environ.setdefault('DJANGO_SETTING_MODULE', 'MyDjango.settings')
django.setup()



@csrf_exempt
def startWork(request):
    os.system("F:&&cd F:\\code\\testPlatforms&&celery -A task.apitestTask worker -l info -P eventlet")
    response = [{"code": "200", "msg": "sss"}]
    return JsonResponse(response, safe=False)

@csrf_exempt
def startBeat(request):
    path = os.path.abspath(os.path.dirname(__file__)).split('testPlatforms')[0]+"testPlatforms\\"
    if os.path.exists(path +"celerybeat.pid"):
        print("文件存在,删除文件")
        os.remove(path +"celerybeat.pid")
    os.system("F:&&cd F:\\code\\testPlatforms&&celery -A task beat -l info")
    response = [{"code": "200", "msg": "sss"}]
    return JsonResponse(response, safe=False)

@csrf_exempt
def test(request):
    taskQuery = Task.objects.filter(status__exact=1).order_by("taskid")
    print(taskQuery[0].status)
    response = [{"code": "200", "msg": taskQuery[0].status}]
    return JsonResponse(response, safe=False)
