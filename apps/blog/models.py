# coding=utf-8
from django.db import models
import uuid
from django.utils.html import format_html

# 自定义验证器


def validate_email(email):
    import re
    from django.core.exceptions import ValidationError
    from django.utils.translation import gettext_lazy as _
    if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
        raise ValidationError(
            _('%(email)s format is wrong!'),
            params={'email': email}
        )


# Create your models here.
class user_info(models.Model):
    """
    1.null=True 数据库中字段是否可以为空
        
    2.blank=True django的Admin中添加数据时是否可以允许空值
        
    3.primary_key=False 主键，对AutoField设置主键后，就会代替原来的自增id列
        
    4.auto_now和auto_now_add
        auto_now 自动创建，无论添加或修改，都是当前操作的时间
        auto_now_add 自动创建，用于都是创建时的时间
        
    5.choices用于页面上的选择框标签，需要先提供一个二维的二元元组，第一个元素表示存在数据库内真实的值，第二个表示页面上显示的具体内容。在浏览器页面上将显示第二个元素的值
        gender_choice = (
            (u'M', u'Male'),
            (u'F', u'Female')
        )
        gender = models.CharField(max_length=2, choices=gender_choice)  
        
    6.max_length 最大长度
    
    7.default 默认值
    
    8.verbose_name Admin中字段的显示名称
    
    9.name|db_column 数据库中的字段名称
    
    10.unique=True 不允许重复
    
    11.db_index=True 数据库索引
    
    12.editable=True 在Admin里是否可编辑
    
    13.error_message=None 错误提示
    
    14.auth_created=True 自动创建
    
    15.help_text 在Admin中提示帮助信息
    
    16.validators=[] 验证器

    17.upload-to="image" 指定文件存放的前缀路径
    """

    """
    1.models.AutoField 自增列=int(11)
        如果没有的话，默认生成一个名称为id的列，如果要显示的自定义的一个自增列，必须将列设置为主键primary_key=True
        
    2.models.CharField 字符串字段
        必须max_length参数
        
    3.models.BooleanField 布尔类型=tinyint(1)
        不能为空，Blank=True
        
    4.models.CommaSeparatedIntegerField 用逗号分隔的数字=varchar
        继承CharField，所以必须max_length参数
        
    5.models.DateField 日期类型 date
        对于参数，auto_now=True则每次更新都会更新这个时间；auto_now_add则只是第一次创建添加，之后的更新不再改变
        
    6、models.DateTimeField　　日期类型 datetime
    　　同DateField的参数
    
    7、models.Decimal　　十进制小数类型 = decimal
    　　必须指定整数位max_digits和小数位decimal_places
    
    8、models.EmailField　　字符串类型（正则表达式邮箱） =varchar
    　　对字符串进行正则表达式
    
    9、models.FloatField　　浮点类型 = double
    
    10、models.IntegerField　　整形
    
    11、models.BigIntegerField　　长整形
    　　integer_field_ranges = {
    　　　　'SmallIntegerField': (-32768, 32767),
    　　　　'IntegerField': (-2147483648, 2147483647),
    　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
    　　　　'PositiveSmallIntegerField': (0, 32767),
    　　　　'PositiveIntegerField': (0, 2147483647),
    　　}
    
    12、models.IPAddressField　　字符串类型（ip4正则表达式）
    
    13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
    　　参数protocol可以是：both、ipv4、ipv6
    　　验证时，会根据设置报错
    
    14、models.NullBooleanField　　允许为空的布尔类型
    
    15、models.PositiveIntegerField　　正Integer
    
    16、models.PositiveSmallIntegerField　　正smallInteger
    
    17、models.SlugField　　减号、下划线、字母、数字
    
    18、models.SmallIntegerField　　数字
    　　数据库中的字段有：tinyint、smallint、int、bigint
    
    19、models.TextField　　字符串=longtext
    
    20、models.TimeField　　时间 HH:MM:ss
    
    21、models.URLField　　字符串，地址正则表达式
    
    22、models.BinaryField　　二进制
    
    23、models.ImageField   图片
    
    24、models.FilePathField 文件                    
    """
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1(), unique=True)
    name = models.CharField(max_length=30, verbose_name=u'姓名')
    email = models.EmailField(verbose_name=u'电子邮件')
    memo = models.TextField(verbose_name=u'简介')
    user_type_choice = (
        (0, u'普通用户'),
        (1, u'高级用户')
    )
    user_type = models.IntegerField(choices=user_type_choice, default=0, verbose_name=u'用户类型')
    add_time = models.DateTimeField(verbose_name=u'添加时间', auto_now=True)

    class Meta:
        verbose_name = u'个人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_readonly_fields(self, request):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user_info = models.OneToOneField("user_info", verbose_name=u'用户信息', on_delete=models.CASCADE)
    username = models.CharField(max_length=64, verbose_name=u'用户名称')
    password = models.CharField(max_length=64, verbose_name=u'用户密码')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=64, verbose_name=u'说明')
    user_info = models.ManyToManyField('user_info', verbose_name=u'用户信息')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.caption


class Host(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=64, verbose_name=u'主机名')
    ip = models.GenericIPAddressField(verbose_name=u'ip地址')
    user_group = models.ForeignKey('UserGroup', on_delete=models.CASCADE, verbose_name=u'用户组')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'站点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hostname


class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.FileField(upload_to='./upload/')
    add_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.avatar

