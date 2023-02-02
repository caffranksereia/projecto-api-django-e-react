from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [

            "id",
            "uuid",
            "name",
            "mobile_number",
            "birth_date",
            "is_superuser",
            "is_staff",
            "is_active",
        ]

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name",
            "mobile_number",
            "birth_date",
            "is_superuser",
            "is_staff",
            "is_active",
        ]

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name",
            "mobile_number",
            "birth_date",
            "is_superuser",
            "is_staff",
            "is_active",
           
        ]

