from django.db import models


class Address(models.Model):

    city = models.CharField(verbose_name='City', max_length=100)
    street = models.CharField(verbose_name='Street', max_length=256)
    house_num = models.IntegerField('House number')

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.city} {self.street} {self.house_num}'


class Student(models.Model):

    name = models.CharField(verbose_name='Name', max_length=100)
    phone = models.CharField(verbose_name='Phone number', max_length=100)
    login_datetime = models.DateTimeField(verbose_name='Login date')

    address = models.OneToOneField('student.Address', verbose_name='Address', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name
