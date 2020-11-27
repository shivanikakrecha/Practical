from rest_framework import serializers
from .models import User, Category, Product
import uuid
from django.contrib.auth.hashers import make_password


def create_hashed_token():
    email_verification_token = uuid.uuid4().hex
    return email_verification_token


def create_hashed_token():
    email_verification_token = uuid.uuid4().hex
    return email_verification_token


class Usersserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "is_owner",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
        )
        read_only_fields = ("id",)
        write_only_fields = ("password",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user_email = validated_data.get("email", "").lower().strip()
        username = validated_data.get("username", "").lower().strip()
        is_owner = validated_data.get("is_owner", False)
        raw_password = validated_data.pop("password", "")
        user = User.objects.create(
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            username=username,
            email=user_email,
            password=make_password(raw_password),
            is_owner=is_owner
        )
        user.save()
        user_data = Usersserializer(instance=user)
        data = user_data.data
        return data


class Subdispproduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "parent_category",
        )


class Productcreateserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "product_code",
            "price",
            "category",
            "manufacture_date",
            "expiry_date",
            "owner",
            "status",
        )


class Subserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "parent_category",
        )


class Usersserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "is_owner",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
        )
        read_only_fields = ("id",)
        write_only_fields = ("password",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user_email = validated_data.get("email", "").lower().strip()
        username = validated_data.get("username", "").lower().strip()
        is_owner = validated_data.get("is_owner", False)
        raw_password = validated_data.pop("password", "")
        user = User.objects.create(
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            username=username,
            email=user_email,
            password=make_password(raw_password),
            is_owner=is_owner
        )
        user.save()
        user_data = Usersserializer(instance=user)
        data = user_data.data
        return data


class Subdispproduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "parent_category",
        )


class Productlistserializer(serializers.ModelSerializer):
    category = Subdispproduct()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "product_code",
            "price",
            "category",
            "manufacture_date",
            "expiry_date",
            "owner",
            "status",
            "category"
        )


class Productcreateserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "product_code",
            "price",
            "category",
            "manufacture_date",
            "expiry_date",
            "owner",
            "status",
        )


class Subserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "parent_category",
        )
