from rest_framework import routers
from .views import (
    UsersViewSets,
    ProductViewSets,
    CategoryViewSets)
app_name = "acq_test"

router = routers.DefaultRouter()
router.register(r"users", UsersViewSets)
router.register(r"product", ProductViewSets)
router.register(r"category", CategoryViewSets)

urlpatterns = []
urlpatterns += router.urls
