import os
import django
django.setup()
from apitest.readJmx import changeAciton
from task import app
from task.taskDao import findStatusById

paths = os.path.abspath(os.path.dirname(__file__)).split('testPlatforms')[0]+"testPlatforms\\data\\auto\\API-Test\\"

@app.task
def everySeconds():
    print("----------开始执行间隔秒定时任务---------")
    status = findStatusById("1")[0][5]
    if status==1 or status =="1":
        print("允许执行定时任务")
        newStr = "state = 1 and 1=1"
        changeAciton(newStr, paths)
        os.chdir(paths)
        os.system("ant")

@app.task
def everyDay():
    print("----------开始执行每日定时任务---------")
    status = findStatusById("2")[0][5]
    if status==1 or status =="1":
        print("允许执行定时任务")
        # newStr = "1=1"
        # changeAciton(newStr, paths)
        # os.chdir(paths)
        # os.system("ant")
