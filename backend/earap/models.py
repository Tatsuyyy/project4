from django.db import models


class ActionElement(models.Model):
    action = models.ForeignKey('Actions', models.DO_NOTHING)
    elem = models.ForeignKey('Elems', models.DO_NOTHING)

    class Meta:
        db_table = 'action_element'


class Actions(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'actions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Collects(models.Model):
    output = models.ForeignKey('Outputs', models.DO_NOTHING)

    class Meta:
        db_table = 'collects'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


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
