from django.db import models

# Create your models here.
from django.db import models


class JgPushRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    push_token = models.CharField(max_length=50, blank=True, null=True)
    record_id = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    push_time = models.DateTimeField(blank=True, null=True)
    jg_req = models.CharField(max_length=1000, blank=True, null=True)
    organ = models.CharField(max_length=10, blank=True, null=True)
    msg_id = models.CharField(max_length=30, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    return_msg = models.CharField(max_length=500, blank=True, null=True)
    click_state = models.CharField(max_length=10, blank=True, null=True)
    click_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jg_push_record'


class JpushRegisterInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    devicetagapp = models.CharField(max_length=50, blank=True, null=True)
    pushtoken = models.CharField(max_length=50, blank=True, null=True)
    errormessage = models.CharField(max_length=255, blank=True, null=True)
    registid = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    devicetype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jpush_register_info'


class SmsVoicePushRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)
    push_request = models.CharField(max_length=500, blank=True, null=True)
    push_response = models.CharField(max_length=500, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms_voice_push_record'


class ThirdpartyErrorRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    alarm_status = models.IntegerField(blank=True, null=True)
    alarm_staff = models.TextField(blank=True, null=True)
    alarm_type = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thirdparty_error_record'


class VerificationCode(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    channel_name = models.CharField(max_length=50, blank=True, null=True)
    channel_type = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=10)
    created = models.DateTimeField(blank=True, null=True)
    device_model = models.CharField(max_length=500, blank=True, null=True)
    device_tag = models.CharField(max_length=200, blank=True, null=True)
    device_type = models.CharField(max_length=5, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=20)
    os_version = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    sms_org = models.CharField(max_length=5)
    state = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'verification_code'


class VerificationEmailCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    state = models.CharField(max_length=1, blank=True, null=True)
    device_model = models.CharField(max_length=200, blank=True, null=True)
    device_type = models.CharField(max_length=1, blank=True, null=True)
    device_tag = models.CharField(max_length=200, blank=True, null=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    os_version = models.CharField(max_length=20, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    channel_type = models.CharField(max_length=50, blank=True, null=True)
    channel_name = models.CharField(max_length=50, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    apitype = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'verification_email_code'


class WtCityWeatherRecord(models.Model):
    area_id = models.CharField(max_length=50, blank=True, null=True)
    area_name = models.CharField(max_length=100, blank=True, null=True)
    area_weather = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wt_city_weather_record'


class WxPushRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    openid = models.CharField(max_length=50, blank=True, null=True)
    todo_id = models.BigIntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    push_state = models.IntegerField(blank=True, null=True)
    push_request = models.CharField(max_length=500, blank=True, null=True)
    push_response = models.CharField(max_length=500, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wx_push_record'


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app_version = models.CharField(max_length=32, blank=True, null=True)
    birth_day = models.IntegerField(blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    channel = models.CharField(max_length=32, blank=True, null=True)
    channel_name = models.CharField(max_length=128, blank=True, null=True)
    channel_type = models.CharField(max_length=128, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField()
    device_tag = models.CharField(max_length=50, blank=True, null=True)
    device_type = models.CharField(max_length=32)
    email = models.CharField(unique=True, max_length=128, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    id_card = models.CharField(max_length=128, blank=True, null=True)
    job = models.CharField(max_length=32, blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    leap_month = models.CharField(max_length=32, blank=True, null=True)
    lunar = models.CharField(max_length=32, blank=True, null=True)
    mobile = models.CharField(unique=True, max_length=32)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    old_mobile = models.CharField(max_length=32)
    openid = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    pwd_error_count = models.IntegerField(blank=True, null=True)
    qq_name = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=1024, blank=True, null=True)
    signature = models.CharField(max_length=1024, blank=True, null=True)
    telecom_operators = models.CharField(max_length=32, blank=True, null=True)
    unionid = models.CharField(max_length=128, blank=True, null=True)
    unique_key = models.CharField(max_length=50)
    updated = models.DateTimeField()
    user_code = models.IntegerField(blank=True, null=True)
    user_image = models.CharField(max_length=1024, blank=True, null=True)
    user_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserAction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    ip = models.CharField(max_length=20, blank=True, null=True)
    old_user_code = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    config = models.CharField(max_length=20, blank=True, null=True)
    config_date = models.DateTimeField(blank=True, null=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    app_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_action'


class UserAppManage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    app_code = models.CharField(max_length=50, blank=True, null=True)
    visit_count = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    user_code = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_app_manage'


class UserConfigPush(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    ip = models.CharField(max_length=20, blank=True, null=True)
    old_user_code = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    config = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_config_push'


class UserConfigShow(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    config = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_config_show'


class UserCustom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    config = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_custom'
        unique_together = (('user_id', 'type'),)


class UserDataBackup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.IntegerField(blank=True, null=True)
    devicetagapp = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_data_backup'


class UserDataExportApply(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.IntegerField(blank=True, null=True)
    datatype = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    begintime = models.DateTimeField()
    endtime = models.DateTimeField()
    applydate = models.DateTimeField()
    status = models.CharField(max_length=32)
    filename = models.CharField(max_length=200, blank=True, null=True)
    dealsttime = models.DateTimeField(blank=True, null=True)
    dealetime = models.DateTimeField(blank=True, null=True)
    sendstime = models.DateTimeField(blank=True, null=True)
    sendetime = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    updated = models.DateTimeField()
    deleted = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    ip = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_data_export_apply'


class UserDataExportLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.IntegerField()
    devicetagapp = models.CharField(max_length=50)
    exportinfostring = models.CharField(max_length=500, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_data_export_log'


class UserDevice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    address = models.CharField(max_length=1024, blank=True, null=True)
    app_version = models.CharField(max_length=32, blank=True, null=True)
    area = models.CharField(max_length=32, blank=True, null=True)
    channel = models.CharField(max_length=32, blank=True, null=True)
    channel_name = models.CharField(max_length=128, blank=True, null=True)
    channel_type = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    device_model = models.CharField(max_length=200, blank=True, null=True)
    device_tag = models.CharField(max_length=100, blank=True, null=True)
    device_tag_app = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.CharField(max_length=32, blank=True, null=True)
    ip = models.CharField(max_length=128, blank=True, null=True)
    is_root = models.IntegerField(blank=True, null=True)
    lat = models.CharField(max_length=128, blank=True, null=True)
    lng = models.CharField(max_length=128, blank=True, null=True)
    mac = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=128, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField()
    user_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_device'
        unique_together = (('user_id', 'device_tag_app'),)


class UserDeviceActivite(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    address = models.CharField(max_length=1024, blank=True, null=True)
    app_version = models.CharField(max_length=32, blank=True, null=True)
    area = models.CharField(max_length=32, blank=True, null=True)
    channel = models.CharField(max_length=32, blank=True, null=True)
    channel_name = models.CharField(max_length=128, blank=True, null=True)
    channel_type = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    device_model = models.CharField(max_length=200, blank=True, null=True)
    device_tag = models.CharField(max_length=100, blank=True, null=True)
    device_tag_app = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.CharField(max_length=32, blank=True, null=True)
    is_root = models.IntegerField(blank=True, null=True)
    lat = models.CharField(max_length=128, blank=True, null=True)
    lng = models.CharField(max_length=128, blank=True, null=True)
    mac = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=128, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=512, blank=True, null=True)
    activite_count = models.IntegerField()
    activite_day = models.IntegerField()
    version = models.BigIntegerField()
    ip = models.CharField(max_length=128, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_device_activite'


class UserDeviceCopy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    address = models.CharField(max_length=1024, blank=True, null=True)
    app_version = models.CharField(max_length=32, blank=True, null=True)
    area = models.CharField(max_length=32, blank=True, null=True)
    channel = models.CharField(max_length=32, blank=True, null=True)
    channel_name = models.CharField(max_length=128, blank=True, null=True)
    channel_type = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    device_model = models.CharField(max_length=200, blank=True, null=True)
    device_tag = models.CharField(max_length=100, blank=True, null=True)
    device_tag_app = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.CharField(max_length=32, blank=True, null=True)
    ip = models.CharField(max_length=128, blank=True, null=True)
    is_root = models.IntegerField(blank=True, null=True)
    lat = models.CharField(max_length=128, blank=True, null=True)
    lng = models.CharField(max_length=128, blank=True, null=True)
    mac = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=128, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField()
    user_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_device_copy'
        unique_together = (('user_id', 'device_tag_app'),)


class UserEverydayMotto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    ip = models.CharField(max_length=20, blank=True, null=True)
    template_id = models.BigIntegerField(blank=True, null=True)
    old_user_code = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    en_content = models.CharField(max_length=500, blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    creator = models.CharField(max_length=100, blank=True, null=True)
    motto_date = models.DateTimeField(blank=True, null=True)
    push_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    bg_img = models.CharField(max_length=200, blank=True, null=True)
    user_content = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_everyday_motto'


class UserEverydayShow(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    ip = models.CharField(max_length=20, blank=True, null=True)
    old_user_code = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    config = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_everyday_show'


class UserExtend(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    add_check_num = models.IntegerField(blank=True, null=True)
    add_check_num_month = models.IntegerField(blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    channel_name = models.CharField(max_length=50, blank=True, null=True)
    channel_type = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    msg_num = models.IntegerField(blank=True, null=True)
    phone_num = models.IntegerField(blank=True, null=True)
    share_time = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField()
    user_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_extend'


class UserLoginLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    app_version = models.CharField(max_length=32, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    channel_name = models.CharField(max_length=50, blank=True, null=True)
    channel_type = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    device_tag_app = models.CharField(max_length=50, blank=True, null=True)
    device_type = models.CharField(max_length=5, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    login_type = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    token = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField()
    user_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_log'


class UserMsgListCheck(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    link_id = models.BigIntegerField(blank=True, null=True)
    check_day = models.CharField(max_length=10, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    ip = models.CharField(max_length=128, blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_msg_list_check'


class UserMsgListSysMsg(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.BigIntegerField(blank=True, null=True)
    link_id = models.BigIntegerField(blank=True, null=True)
    content = models.CharField(max_length=2000, blank=True, null=True)
    unread = models.IntegerField()
    day = models.IntegerField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    temp_code = models.CharField(max_length=20, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    ip = models.CharField(max_length=128, blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_msg_list_sys_msg'


class UserPopupWindowRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    app_name = models.CharField(max_length=20, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_popup_window_record'


class UserSetting(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    zone = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_setting'


class UserShareCode(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    share_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    user_code = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_share_code'


class UserShareCodeLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    created = models.DateTimeField(blank=True, null=True)
    friend_id = models.BigIntegerField(blank=True, null=True)
    friend_mobile = models.CharField(max_length=20, blank=True, null=True)
    msg_num = models.IntegerField(blank=True, null=True)
    share_code = models.CharField(max_length=20, blank=True, null=True)
    updated = models.DateTimeField()
    user_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_share_code_log'


class UserThirdParty(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    access_token = models.CharField(max_length=1024, blank=True, null=True)
    app_version = models.CharField(max_length=32, blank=True, null=True)
    auth_type = models.CharField(max_length=32, blank=True, null=True)
    avatar = models.CharField(max_length=1024, blank=True, null=True)
    channel = models.CharField(max_length=32, blank=True, null=True)
    channel_name = models.CharField(max_length=32, blank=True, null=True)
    channel_type = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    device_tag = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=32, blank=True, null=True)
    info = models.CharField(max_length=3120, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    nick_name = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=32, blank=True, null=True)
    unique_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    updated = models.DateTimeField()
    user_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_third_party'


class UserVersionUpdate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version_code = models.CharField(max_length=50, blank=True, null=True)
    version_name = models.CharField(max_length=50, blank=True, null=True)
    update_notice = models.CharField(max_length=200, blank=True, null=True)
    download_url = models.CharField(max_length=1000, blank=True, null=True)
    app_size = models.CharField(max_length=20, blank=True, null=True)
    app_type = models.CharField(max_length=20, blank=True, null=True)
    force_update = models.IntegerField()
    device_type = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField()
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_version_update'


class WxUserInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app_name = models.CharField(max_length=50, blank=True, null=True)
    avatar_url = models.CharField(max_length=1000, blank=True, null=True)
    can_subscribe_time = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    group_id = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(db_column='LANGUAGE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    last_subscribe_time = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    openid = models.CharField(max_length=200, blank=True, null=True)
    province = models.CharField(max_length=40, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    session_key = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    subscribe = models.CharField(max_length=5, blank=True, null=True)
    tag = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    unionid = models.CharField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wx_user_info'

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


class ChecklistAttachment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    checklist_id = models.BigIntegerField()
    checklist_finish_id = models.BigIntegerField()
    media_type = models.IntegerField()
    url = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=128, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist_attachment'
        unique_together = (('checklist_finish_id', 'media_type', 'user_id'),)


class ChecklistExt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    checklist_finish_id = models.BigIntegerField(unique=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    district = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist_ext'


class ChecklistFinish(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    checklist_id = models.BigIntegerField()
    finish_state = models.IntegerField()
    finish_time = models.DateTimeField(blank=True, null=True)
    complete_time = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist_finish'


class ChecklistSort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    sort = models.TextField()
    version = models.BigIntegerField()
    ip = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist_sort'


class ChecklistTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    checklist_id = models.BigIntegerField()
    title = models.CharField(max_length=1024, blank=True, null=True)
    todo_time = models.DateTimeField(blank=True, null=True)
    next_time = models.DateTimeField(blank=True, null=True)
    remind_id = models.BigIntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist_task'


class ChecklistTaskFinish(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    checklist_finish_id = models.BigIntegerField()
    checklist_task_id = models.BigIntegerField()
    finish_state = models.IntegerField()
    finish_time = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist_task_finish'


class ChecklistTaskSort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    checklist_id = models.BigIntegerField()
    sort_key = models.CharField(max_length=50)
    sort = models.TextField()
    version = models.BigIntegerField()
    ip = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checklist_task_sort'


class DelayInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    todo_type = models.IntegerField()
    todo_id = models.BigIntegerField()
    task_id = models.BigIntegerField(blank=True, null=True)
    todo_time = models.DateTimeField(blank=True, null=True)
    new_todo_time = models.DateTimeField(blank=True, null=True)
    offset = models.IntegerField(blank=True, null=True)
    next_time = models.DateTimeField(blank=True, null=True)
    short_title = models.CharField(max_length=255)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delay_info'


class RecordSearchSetting(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.CharField(max_length=255)
    value = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'record_search_setting'


class RecordSort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    sort = models.TextField()
    version = models.BigIntegerField()
    ip = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    dsfds = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_sort'


class RecordTabSort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    sort = models.TextField()
    version = models.BigIntegerField()
    ip = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'record_tab_sort'


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


class TodoAttachment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    todo_id = models.BigIntegerField()
    todo_finish_id = models.BigIntegerField()
    media_type = models.IntegerField()
    url = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=128, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_attachment'


class TodoClassify(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    classify_icon = models.CharField(max_length=50, blank=True, null=True)
    classify_name = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_classify'


class TodoClassifySort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    classify_sort_list = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_classify_sort'


class TodoCustomizeTime(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    version = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    ip = models.CharField(max_length=20, blank=True, null=True)
    advance_minute = models.IntegerField()
    source = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'todo_customize_time'


class TodoDayCheckin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    user_code = models.IntegerField(blank=True, null=True)
    check_day = models.DateField(blank=True, null=True)
    todo_id = models.BigIntegerField(blank=True, null=True)
    todo_old_id = models.IntegerField(blank=True, null=True)
    impression = models.CharField(max_length=128, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_day_checkin'


# class TodoExt(models.Model):
#     id = models.BigIntegerField()
#     user_id = models.BigIntegerField()
#     todo_id = models.BigIntegerField(blank=True, null=True)
#     longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
#     latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
#     country = models.CharField(max_length=128, blank=True, null=True)
#     province = models.CharField(max_length=32, blank=True, null=True)
#     city = models.CharField(max_length=32, blank=True, null=True)
#     district = models.CharField(max_length=32, blank=True, null=True)
#     address = models.CharField(max_length=128, blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     ip = models.CharField(max_length=255, blank=True, null=True)
#     version = models.BigIntegerField()
#     deleted = models.IntegerField()
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'todo_ext'
#
#
class TodoFinish(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    todo_id = models.BigIntegerField()
    todo_time = models.DateTimeField(blank=True, null=True)
    finish_state = models.IntegerField()
    finish_time = models.DateTimeField(blank=True, null=True)
    ahead_type = models.CharField(max_length=512, blank=True, null=True)
    durations = models.IntegerField(blank=True, null=True)
    complete_time = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_finish'
        unique_together = (('todo_id', 'todo_time', 'created'),)


class TodoIgnore(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    todo_id = models.BigIntegerField(blank=True, null=True)
    todo_old_id = models.IntegerField(blank=True, null=True)
    user_code = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_ignore'


class TodoRepeatRule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    todo_id = models.BigIntegerField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    rules_json = models.TextField(blank=True, null=True)
    attach_datetimes_json = models.TextField(blank=True, null=True)
    detach_datetimes_json = models.TextField(blank=True, null=True)
    interval_type = models.IntegerField()
    duration = models.TextField(blank=True, null=True)
    close_state = models.IntegerField(blank=True, null=True)
    repeat_type = models.IntegerField()
    todo_time = models.DateTimeField(blank=True, null=True)
    offset = models.IntegerField(blank=True, null=True)
    next_time = models.DateTimeField(blank=True, null=True)
    zone = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_repeat_rule'


class TodoTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    todo_id = models.BigIntegerField()
    title = models.CharField(max_length=1024, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    todo_time = models.DateTimeField(blank=True, null=True)
    next_time = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_task'

#
# class TodoTaskFinish(models.Model):
#     id = models.BigIntegerField()
#     user_id = models.BigIntegerField()
#     todo_finish_id = models.BigIntegerField()
#     todo_task_id = models.BigIntegerField()
#     finish_state = models.IntegerField()
#     finish_time = models.DateTimeField(blank=True, null=True)
#     remark = models.TextField(blank=True, null=True)
#     ip = models.CharField(max_length=255, blank=True, null=True)
#     version = models.BigIntegerField()
#     deleted = models.IntegerField()
#     created = models.DateTimeField()
#     updated = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'todo_task_finish'


class TodoTaskSort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    todo_type = models.IntegerField()
    todo_id = models.BigIntegerField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    sort = models.TextField()
    version = models.BigIntegerField()
    ip = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todo_task_sort'
