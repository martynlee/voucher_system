from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import VoucherForm


# Create your views here.
class VoucherView(FormView):
    template_name = 'voucher.html'
    form_class = VoucherForm
    success_url = '/thanks/'
    # fail_url = '/sorry/'

    def form_valid(self, form):
        form.apply()
        return super().form_valid(form)
