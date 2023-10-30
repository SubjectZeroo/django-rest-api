from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()
    
    class Meta:
        model = Product
        exclude = ('state','created_at', 'updated_at', 'deleted_at')
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image or "",
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else '',
        }