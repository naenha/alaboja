from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(default="매입다가구", max_length=20, help_text="단지명")
    address = models.CharField(default="서울특별시 종로구 대학로5가길", max_length=100, help_text="주소")
    latitude = models.FloatField(default=0, help_text="위도")
    longitude = models.FloatField(default=0, help_text="경도")
    category =  models.CharField(default="기존주택매입임대", max_length=20, help_text="공급유형")
    area = models.FloatField(default=0, help_text="공급면적")
    num = models.IntegerField(default=0, help_text="세대수")
    people = models.CharField(default="00-00", max_length=10, help_text="가구원수")
    target = models.CharField(default="수급자", max_length=10, help_text="공급대상")
    rating = models.CharField(default=1, max_length=10, help_text="소득분위")
    income = models.CharField(default="50% 이하", max_length=15, help_text="소득/자산")
