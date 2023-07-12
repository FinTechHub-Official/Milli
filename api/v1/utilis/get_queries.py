from api.v1.product.models import (
    Product,
    Category,
    Brand,
    Country
)


# Product app tables ===================================================

def get_category_queryset():
    return Category.objects.select_related("parent").order_by("-id")

def get_product_queryset():
    return Product.objects.select_related('seller', 'category', 'brand', 'country').order_by("-id")

def get_brand_queryset():
    return Brand.objects.order_by("-id")

def get_country_queryset():
    return Country.objects.order_by("-id")


# Product app active object in tables ====================================

def get_active_category_queryset():
    return get_category_queryset().filter(is_active=True, is_deleted=False)

def get_active_product_queryset():
    return get_product_queryset().filter(is_active=True, is_deleted=False)

def get_active_brands():
    return get_brand_queryset().filter(is_active=True, is_deleted=False)

def get_active_countries():
    return get_country_queryset().filter(is_active=True, is_deleted=False)
