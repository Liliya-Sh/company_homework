from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    position = models.CharField(max_length=25, verbose_name='Должность')
    phone = models.CharField(max_length=35, null=True, blank=True, verbose_name='Номер телефон')
    birth_date = models.DateField(blank=False, null=False, verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Почта',  null=True, blank=True)
    name_department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Название отдела')

class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название отдела')
    storey = models.IntegerField(verbose_name='Этаж')
    name_branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, verbose_name='Название филиала',  null=True)

class Branch(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес филиала', null=True, blank=True)
    short_name = models.CharField(max_length=255, verbose_name='Короткое название филиала', null=True, blank=True)