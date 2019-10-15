from celery import Celery
from datetime import timedelta

from celery.schedules import crontab

app = Celery('my_task')

app.config_from_object("task.celeryconfig")

taskList = {
    # "tast1": {
    #     'task': "task.apitestTask.everySeconds",
    #     'schedule': timedelta(seconds=20),  # 每 30 秒执行一次
    #     'args': ()  # 任务函数参数
    # },
    "tast2": {
        'task': "task.apitestTask.everyDay",
        'schedule': crontab(hour=9, minute=40),  # 每 30 秒执行一次
        'args': ()  # 任务函数参数
    },
}