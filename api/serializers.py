from rest_framework import serializers
from myapp.models import Role, Appraiser, Client, LoanStatus, Loan, Collateral, Payment

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class AppraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraiser
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class LoanStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanStatus
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class CollateralSerializer(serializers.ModelSerializer):  # Ensure this is defined
    class Meta:
        model = Collateral
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):  # Ensure this is defined
    class Meta:
        model = Payment
        fields = '__all__'
