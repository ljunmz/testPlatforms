from django.db import models

# Create your models here.




class ApiStatistics(models.Model):
    service = models.CharField(max_length=255, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    inner_cell = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    isauto = models.CharField(db_column='isAuto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_statistics'



class TestdataFlow(models.Model):
    flow_id = models.IntegerField(primary_key=True)
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
    node_id = models.IntegerField(primary_key=True)
    flow_id = models.CharField(max_length=36)
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
    post_keys = models.CharField(max_length=255, blank=True, null=True)
    post_keys_extractor = models.CharField(max_length=255, blank=True, null=True)
    post_keys_default = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testdata_node'

class Checklist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=1024, blank=True, null=True)
    short_title = models.CharField(max_length=1024, blank=True, null=True)
    classify_id = models.BigIntegerField()
    importance = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    user_code = models.IntegerField(blank=True, null=True)
    old_todo_info_id = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist'

class Todo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=1024)
    short_title = models.CharField(max_length=1024, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    classify_id = models.BigIntegerField()
    importance = models.IntegerField()
    ahead_type = models.CharField(max_length=512, blank=True, null=True)
    todo_type = models.IntegerField()
    is_forever = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    user_code = models.IntegerField(blank=True, null=True)
    old_todo_info_id = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo'