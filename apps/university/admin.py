from django.contrib import admin

from apps.university.models import OTM

#
# class StudentWalletAdmin(admin.ModelAdmin):
#     list_display = ('id', 'student', 'degree', 'contract_amount', 'talabaga_tolangan_tolov', 'allocated_amount')
#     readonly_fields = ('talabaga_tolangan_tolov', 'allocated_amount')


admin.site.register(OTM)
# # admin.site.register(SponsorWallet)
# # admin.site.register(StudentWallet)
# admin.site.register(Tolov)
# admin.site.register(AmountSpent)
