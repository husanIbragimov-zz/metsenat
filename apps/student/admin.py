from django.contrib import admin

from apps.student.models import StudentWallet


class SA(admin.ModelAdmin):
    list_display = ('id', 'student', 'donates')


admin.site.register(StudentWallet, SA)
