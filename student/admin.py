from django.contrib import admin

from student.models import Student


@admin.register(Student)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'login_datetime')
    search_fields = ('name', )
