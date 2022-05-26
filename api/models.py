from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name


class InflectionTime(models.Model):
    data_field = models.CharField(max_length=30)

    def __str__(self):
        return self.data_field


class Component(models.Model):
    component_url = models.FileField(upload_to='media', null=True)
    types = models.CharField(max_length=20)
    sub_type = models.CharField(max_length=30)
    length = models.FloatField()
    business = models.ManyToManyField(Business)
    inflection_time = models.ManyToManyField(InflectionTime)

    def __str__(self):
        return self.types


# Create your models here.
