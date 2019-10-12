from django.db import models

# Create your models here.

from django.db import models

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
