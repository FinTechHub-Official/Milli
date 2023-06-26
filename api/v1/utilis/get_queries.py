from api.v1.product.models import (
    Product,
    Category
)

def get_category_queryset():
    return Category.objects.select_related("parent")


def get_active_category_queryset():
    return get_category_queryset().filter(is_active=True, is_deleted=False)


def get_active_product_queryset():
    return Product.objects.select_related('seller', 'category')
