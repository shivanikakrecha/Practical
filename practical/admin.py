from django.contrib import admin
from practical.models import User, Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'modified_at')
    search_fields = ('name', 'price', 'owner__username', 'category__name')
    list_filter = ('name', 'price', 'owner__username', 'category__name')


admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
