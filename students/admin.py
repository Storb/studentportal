from django.contrib import admin
from students.models import Group, Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name']}),
        (None,{'fields':['elder']}),
    ]
    inlines = [StudentInline]

admin.site.register(Group, GroupAdmin)
