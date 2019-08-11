from django.db import models

# Create your models here.
class TestdataFlow(models.Model):
    flow_id = models.IntegerField(primary_key=True, max_length=36)
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
    node_id = models.IntegerField(primary_key=True, max_length=36)
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

