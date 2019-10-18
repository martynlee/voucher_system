from django.contrib import admin
from .models import Voucher
# Register your models here.


class VoucherAdmin(admin.ModelAdmin):
    list_dislpay = ['code', 'discount_value', 'discount_type']


admin.site.register(Voucher, VoucherAdmin)
