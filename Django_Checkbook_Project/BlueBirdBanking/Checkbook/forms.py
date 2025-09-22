from django import forms
from django.forms import ModelForm
from .models import Account, Transaction


# Creates Account Form based on Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Creates Transaction Form based on Transaction Model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class AccountChoiceForm(forms.Form):
    account = forms.ModelChoiceField(
        queryset=None,   # don't set it yet!
        empty_label="Select an account"
    )

    def __init__(self, *args, **kwargs):
        from .models import Account   # import here to avoid early evaluation
        super().__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.all()
