from django.urls import path
from vouchers.views import VoucherView

urlpatterns = [
    path('', VoucherView.as_view(), name='index'),
]
