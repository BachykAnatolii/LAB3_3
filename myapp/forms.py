# forms.py
from django import forms
from .models import Role, Appraiser, Client, LoanStatus, Loan, Collateral, Payment

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class AppraiserForm(forms.ModelForm):
    class Meta:
        model = Appraiser
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class LoanStatusForm(forms.ModelForm):
    class Meta:
        model = LoanStatus
        fields = '__all__'

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

class CollateralForm(forms.ModelForm):
    class Meta:
        model = Collateral
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
