from django.db import models


class Actions(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'actions'


class Collects(models.Model):
    output = models.ForeignKey('Outputs', models.DO_NOTHING)

    class Meta:
        db_table = 'collects'

class Elems(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'elems'


class Operations(models.Model):
    repeat_num = models.SmallIntegerField()

    class Meta:
        db_table = 'operations'


class Outputs(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'outputs'


class Projects(models.Model):
    url = models.CharField(db_column='URL', max_length=256)  # Field name made lowercase.
    draft_flag = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        db_table = 'projects'


class ScrLogs(models.Model):
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    success_flag = models.IntegerField()

    class Meta:
        db_table = 'scr_logs'


class Steps(models.Model):
    xpath = models.CharField(max_length=256)
    action = models.ForeignKey(Actions, models.DO_NOTHING)
    elem = models.ForeignKey(Elems, models.DO_NOTHING)
    value = models.CharField(max_length=50)
    order_num = models.SmallIntegerField()
    project_id = models.PositiveIntegerField()

    class Meta:
        db_table = 'steps'


class TestItems(models.Model):
    name = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    verification = models.ForeignKey('Verifications', models.DO_NOTHING)
    order_num = models.SmallIntegerField()
    webtest = models.ForeignKey('Webtests', models.DO_NOTHING)

    class Meta:
        db_table = 'test_items'


class Users(models.Model):
    username = models.CharField(max_length=16)
    mail = models.CharField(max_length=256)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'


class Verifications(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'verifications'


class Webtests(models.Model):

    class Meta:
        db_table = 'webtests'
