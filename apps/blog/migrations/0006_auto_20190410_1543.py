# Generated by Django 2.2 on 2019-04-10 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190410_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='user_type',
            field=models.IntegerField(choices=[(0, '普通用户'), (1, '高级用户')], default=0),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=64, verbose_name='用户名称')),
                ('password', models.CharField(max_length=64, verbose_name='用户密码')),
                ('add_time', models.DateTimeField(auto_now=True)),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.user_info', verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '用户资料',
                'verbose_name_plural': '用户资料',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('caption', models.CharField(max_length=64)),
                ('add_time', models.DateTimeField(auto_now=True)),
                ('user_info', models.ManyToManyField(to='blog.user_info')),
            ],
            options={
                'verbose_name': '用户组',
                'verbose_name_plural': '用户组',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('hostname', models.CharField(max_length=64)),
                ('ip', models.GenericIPAddressField()),
                ('add_time', models.DateTimeField(auto_now=True)),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserGroup')),
            ],
            options={
                'verbose_name': '站点',
                'verbose_name_plural': '站点',
            },
        ),
    ]
