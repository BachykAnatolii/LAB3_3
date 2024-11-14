# serializers.py
from rest_framework import serializers
from .models import Appraiser, Role


class AppraiserSerializer(serializers.ModelSerializer):
    # Specify the role field to accept a primary key (integer ID)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = Appraiser
        fields = '__all__'

