from datetime import timedelta

from celery.schedules import crontab

from task import taskList

BROKER_URL = 'redis://127.0.0.1:6379'  # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend

CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

CELERY_IMPORTS = (  # 指定导入的任务模块
    'task.apitestTask',
)

#有些情况可以防止死锁
CELERYD_FORCE_EXECV=True
# 设置并发worker数量
CELERYD_CONCURRENCY=4
#允许重试
CELERY_ACKS_LATE=True
# 每个worker最多执行100个任务被销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD=100
# 超时时间
CELERYD_TASK_TIME_LIMIT=12*30

CELERYBEAT_SCHEDULE = taskList
