from rest_framework import serializers
from .models import (
    Customer,
    ImportProductToWarehouse
)


class CustomerSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'phone_number')


class ImportToWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportProductToWarehouse
        fields = ('product', 'warehouse', 'customer', 'import_price', 'sell_price', 'quantity')
