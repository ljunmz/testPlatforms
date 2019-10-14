
from django.db import models


class Config(models.Model):
    email = models.CharField(max_length=1024, blank=True, null=True)
    env_code = models.CharField(max_length=255, blank=True, null=True)
    numthreads = models.BigIntegerField(db_column='numThreads', blank=True, null=True)  # Field name made lowercase.
    ramptime = models.BigIntegerField(db_column='rampTime', blank=True, null=True)  # Field name made lowercase.
    loops = models.BigIntegerField(blank=True, null=True)
    continueforever = models.IntegerField(db_column='continueForever', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'config'

class PerformanceFlow(models.Model):
    flow_id = models.AutoField(primary_key=True)
    flow_code = models.CharField(max_length=20)
    flow_name = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_flow'


class PerformanceNode(models.Model):
    node_id = models.AutoField(primary_key=True)
    flow_id = models.IntegerField()
    node_code = models.CharField(max_length=20)
    node_name = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.IntegerField()
    method = models.CharField(max_length=4)
    path = models.CharField(max_length=255)
    parameter = models.TextField(blank=True, null=True)
    expect_response = models.TextField(blank=True, null=True)
    ischechdb = models.IntegerField(blank=True, null=True)
    sql_str = models.TextField(blank=True, null=True)
    sql_para = models.CharField(max_length=255, blank=True, null=True)
    expect_db = models.TextField(blank=True, null=True)
    pre_keys = models.CharField(max_length=255, blank=True, null=True)
    sleep_time = models.BigIntegerField(blank=True, null=True)
    isexcute_pre_sql = models.IntegerField(blank=True, null=True)
    pre_sql_str = models.TextField(blank=True, null=True)
    pre_sql_para = models.CharField(max_length=255, blank=True, null=True)
    pre_sql_out = models.CharField(max_length=255, blank=True, null=True)
    post_keys = models.CharField(max_length=1024, blank=True, null=True)
    post_keys_extractor = models.TextField(blank=True, null=True)
    post_keys_default = models.CharField(max_length=1024, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_node'


class Task(models.Model):
    taskid = models.AutoField(db_column='taskId', primary_key=True)  # Field name made lowercase.
    taskname = models.CharField(db_column='taskName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    task = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    args = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class Testenv(models.Model):
    id = models.IntegerField(primary_key=True)
    env_code = models.CharField(max_length=10)
    env_name = models.CharField(max_length=255, blank=True, null=True)
    protocol = models.CharField(max_length=10, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    port = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testenv'




class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    username = models.CharField(db_column='userName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'