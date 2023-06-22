from rest_framework import serializers

from api.v1.user.models import Seller
from .models import (
    ImportProductToWarehouse,
    ImportToWarehouseCart,
    Warehouse
)


class ImportToWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportProductToWarehouse
        fields = ('product', 'warehouse', 'seller', 'import_price', 'sell_price', 'quantity')


class ImportToWarehouseCartSerialzier(serializers.ModelSerializer):
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all(), required=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all(), required=True)

    class Meta:
        model = ImportToWarehouseCart
        fields = ('warehouse', 'seller')

