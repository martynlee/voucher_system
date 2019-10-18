from django import forms


class VoucherForm(forms.Form):
    code = forms.CharField()

    def apply(self):
        pass
