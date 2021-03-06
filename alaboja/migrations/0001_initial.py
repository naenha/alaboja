# Generated by Django 2.0.13 on 2021-02-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='매입다가구', help_text='단지명', max_length=20)),
                ('address', models.CharField(default='서울특별시 종로구 대학로5가길', help_text='주소', max_length=100)),
                ('latitude', models.FloatField(default=0, help_text='위도')),
                ('longitude', models.FloatField(default=0, help_text='경도')),
                ('category', models.CharField(default='기존주택매입임대', help_text='공급유형', max_length=20)),
                ('area', models.FloatField(default=0, help_text='공급면적')),
                ('num', models.IntegerField(default=0, help_text='세대수')),
                ('people', models.CharField(default='00-00', help_text='가구원수', max_length=10)),
                ('target', models.CharField(default='수급자', help_text='공급대상', max_length=10)),
                ('rating', models.CharField(default=1, help_text='소득분위', max_length=10)),
                ('income', models.CharField(default='50% 이하', help_text='소득/자산', max_length=15)),
            ],
        ),
    ]
