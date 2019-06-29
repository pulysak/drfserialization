from django.contrib import admin

from student.models import Student, Address


@admin.register(Student)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'login_datetime')
    search_fields = ('name', )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = ('city', 'street', 'house_num')
    search_fields = ('city', )
