from rest_framework import serializers
from django.db import transaction
from api.v1.user.models import Seller
from .models import (
    ImportPriceProductInWarehouse,
    ImportProductToWarehouse,
    ImportQuantityProductInWarehouse,
    ImportToWarehouseCart,
    ProductInWarehouse,
    QuantityProductInWarehouse,
    Warehouse
)


class ImportToWarehouseSerializer(serializers.ModelSerializer):
    characteristics = serializers.ListField(write_only=True)

    class Meta:
        model = ImportProductToWarehouse
        fields = ('product', 'import_to_warehouse_cart', "characteristics")

    def create_characteristic(self, characteristics, import_to_warehouse):
        import_price = []
        import_quantity = []
        product_id = import_to_warehouse.product.id
        warehouse_id = import_to_warehouse.import_to_warehouse_cart.warehouse.id
        seller_id = import_to_warehouse.product.seller.id

        with transaction.atomic():
            for characteristic in characteristics:
                product_in_warehouse, _ = ProductInWarehouse.objects.get_or_create(
                    product_id=product_id, 
                    warehouse_id=warehouse_id,
                    seller_id=seller_id
                )
                import_price.append(
                    ImportPriceProductInWarehouse(
                        import_product_to_warehouse=import_to_warehouse,
                        product_in_warehouse=product_in_warehouse,
                        characteristic_id=characteristic['characteristic'],
                        import_price=characteristic['import_price']
                    )
                )
                import_quantity.append(
                    ImportQuantityProductInWarehouse(
                        import_product_to_warehouse=import_to_warehouse,
                        product_in_warehouse=product_in_warehouse,
                        characteristic_id=characteristic['characteristic'],
                        quantity=characteristic['quantity']
                    )
                )
                product_in_warehouse_quantity, _ = QuantityProductInWarehouse.objects.get_or_create(
                    product_in_warehouse=product_in_warehouse,
                    characteristic_id=characteristic['characteristic'],
                )
                product_in_warehouse_quantity.quantity += characteristic['quantity']
                product_in_warehouse_quantity.save()
            ImportPriceProductInWarehouse.objects.bulk_create(import_price)
            ImportQuantityProductInWarehouse.objects.bulk_create(import_quantity)


    def create(self, validated_data):
        characteristics = validated_data.pop('characteristics', [])
        instance = super().create(validated_data)
        if characteristics:
            self.create_characteristic(characteristics, instance)
        return instance


class ImportToWarehouseCartSerialzier(serializers.ModelSerializer):
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all(), required=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all(), required=True)

    class Meta:
        model = ImportToWarehouseCart
        fields = ('warehouse', 'seller')

