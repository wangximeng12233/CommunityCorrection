# Generated by Django 2.0 on 2022-04-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('username', models.CharField(max_length=255, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
                ('phone', models.CharField(max_length=255, verbose_name='手机号')),
                ('trueName', models.CharField(max_length=255, verbose_name='真实姓名')),
                ('auth', models.CharField(max_length=255, verbose_name='角色')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='职位')),
                ('headpic', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像地址')),
            ],
        ),
    ]
