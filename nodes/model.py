
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiStatistics(models.Model):
    service = models.CharField(max_length=255, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    inner_cell = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    isauto = models.CharField(db_column='isAuto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(max_length=255, blank=True, null=True)
    rmark = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_statistics'


class Col(models.Model):
    col_list = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'col'


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


class PerformanceUserinfo(models.Model):
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'performance_userinfo'


class Plan(models.Model):
    plan_name = models.CharField(max_length=255, blank=True, null=True)
    statistics = models.CharField(max_length=1024, blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class Row(models.Model):
    col_id = models.IntegerField(blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)
    row_list = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'row'


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


class TestdataFlow(models.Model):
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
        db_table = 'testdata_flow'


class TestdataNode(models.Model):
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
        db_table = 'testdata_node'


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
