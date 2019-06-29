from django.db import models


class Student(models.Model):

    name = models.CharField(verbose_name='Name', max_length=100)
    phone = models.CharField(verbose_name='Phone number', max_length=100)
    login_datetime = models.DateTimeField(verbose_name='Login date')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
