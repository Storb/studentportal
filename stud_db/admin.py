from django.contrib import admin
from stud_db.models import Group, Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

admin.site.register(Group, GroupAdmin)
