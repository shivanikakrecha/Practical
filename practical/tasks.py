from celery.decorators import task
from practical.models import Product


@task()
def remove_deleted_products():
    product.objects.filter(status='deleted').delete()
    return
