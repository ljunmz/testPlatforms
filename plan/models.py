
from django.db import models


class Col(models.Model):
    col_list = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'col'



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
    row_list = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'row'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    username = models.CharField(db_column='userName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
