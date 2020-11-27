from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name=_('Created At'))
    modified_at = models.DateTimeField(auto_now=True, db_index=True,
                                       verbose_name=_('Modified At'))

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Username"),
        error_messages={"unique": _(
            "A user with that username already exists."), },
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_("Last Name")
    )
    email = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    password = models.CharField(max_length=100)
    reset_password_token = models.CharField(max_length=50,
                                            null=True, blank=True)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.username)


class Category(BaseModel):
    name = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name=_("Name"))
    parent_category = models.ForeignKey('self', null=True, blank=True,
                                        on_delete=models.SET_NULL,
                                        verbose_name=_("Parent Category"))

    def __str__(self):
        return '{}'.format(self.name)


class Product(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True,
                            verbose_name=_("Name"))
    product_code = models.CharField(max_length=100, null=True, blank=True,
                                    verbose_name=_("Product Code"))
    price = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name=_("price"))
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("Category"))
    manufacture_date = models.DateTimeField(
        null=False, blank=False, db_index=True,
        verbose_name=_("Manufacture Date"))
    expiry_date = models.DateTimeField(null=False, blank=False, db_index=True,
                                       verbose_name=_("Expiry Date"))
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name=_("Owner")
                              )
    status = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_("Status")
    )

    def __str__(self):
        return '{}'.format(self.name)
