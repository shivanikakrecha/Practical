from celery.decorators import task
from practical.models import Product


@task()
def remove_deleted_products():

    # Remove all deleted products
    product.objects.filter(status='deleted').delete()
    return
