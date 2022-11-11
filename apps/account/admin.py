from django.contrib import admin

from apps.account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'phone', 'gender', 'date_login', 'date_created', 'is_active',)
    readonly_fields = ('date_login', 'date_created')


admin.site.register(Account, AccountAdmin)
