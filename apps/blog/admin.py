# coding=utf-8
from django.contrib import admin
from .models import user_info as UserInfo, UserProfile, UserGroup, Host, Banner


# Register your models here.
@admin.register(UserInfo)
class userInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'memo', 'user_type', 'add_time')  # 设置显示的字段
    list_filter = ('name', 'email', 'memo', 'user_type', 'add_time')  # 设置用于过滤的字段
    search_fields = ('name', 'email', 'memo', 'user_type')  # 设置搜索字段
    # list_display_links = ('name', )  # 设置哪些字段可以点击进入编辑页面
    list_per_page = 5  # 设置每页显示多少条记录，默认是100
    # ordering = ('email', 'memo', 'user_type')  # 设置可排序的字段
    # list_editable = ('email', 'memo', 'user_type')  # 设置可编辑的字段
    date_hierarchy = 'add_time'  # 详细时间分层筛选
    # readonly_fields = ('id',) # 设置只读属性
    actions_on_top = True  # 显示顶部的选项
    actions_on_bottom = True  # 显示底部的选项
    fields = ['name', 'email', 'memo', 'user_type']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'add_time')
    list_filter = ('username', 'password', 'add_time')
    search_fields = ('username',)
    list_display_links = ('username', 'password', 'add_time')


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('caption', 'add_time')
    list_filter = ('caption', 'add_time')
    search_fields = ['caption']
    list_display_links = ('caption', 'add_time')


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip', 'user_group', 'add_time')
    list_filter = ('hostname', 'ip', 'user_group', 'add_time')
    search_fields = ('hostname', 'ip', 'user_group')
    list_display_links = ('hostname', 'ip', 'user_group', 'add_time')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('avatar', 'add_time')
    list_filter = ('avatar', 'add_time')
    list_display_links = ('avatar', 'add_time')


admin.site.site_header = "好医生运维资源管理系统"  # 修改页面头部显示内容
admin.site.site_title = '好医生运维资源管理系统'  # 还守着你页面标题
