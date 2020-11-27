from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import User, Product, Category
from .serializers import Usersserializer, Productlistserializer, Subserializer, Productcreateserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from acqu_practical import authentication
from django.utils.translation import gettext as _
from .permissions import ProductPermission, SubPermission
from rest_framework import filters as rest_filters
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated


class UsersViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Usersserializer
    permission_classes = [IsAuthenticated]

    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.instance)
        return Response(
            data=serializer.instance, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(methods=['POST'], detail=False)
    def login(self, request, pk=None):
        email = request.data.get("email").lower()
        password = request.data.get("password")
        is_owner = request.data.get("is_owner", False)

        if email:
            username = email

        if not (username and password):
            content = {"detail": _("Please provide required parameter.")}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return authentication.authenticate_user(
            self, request, username, password, is_owner
        )


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productlistserializer
    permission_classes = (ProductPermission,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter,
        OrderingFilter,
    )
    ordering_fields = ("name",)
    search_fields = ["name",
                     "product_code",
                     "price",
                     "category",
                     "manufacture_date",
                     "expiry_date",
                     "owner",
                     "status", ]

    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return Productlistserializer
        elif self.action == "create":
            return Productcreateserializer
        else:
            return Productlistserializer

    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        updated_price = int(request.data.get('price', 0))
        actual_price = int(instance.price)

        diff_price = int(int(instance.price) * 10 / 100)
        if updated_price is not 0:
            if not ((actual_price + diff_price == updated_price) or
                    (actual_price - diff_price == updated_price)):

                return Response({'detail': 'You can not update '
                                 'the product. Please enter the 10% variation price.'},
                                status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Product updated successfully'},
                        status=status.HTTP_200_OK)


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Subserializer
    permission_classes = (SubPermission,)

    filter_backends = (
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter,
        OrderingFilter,
    )
    ordering_fields = ("sub_category_name", "sub_category_description")
    search_fields = ["sub_category_name", "sub_category_description"]
    http_method_names = ["get", "post", "patch", "delete"]
