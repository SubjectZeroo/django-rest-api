from rest_framework import generics
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListApiView


class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
    
    # def get_queryset(self):
    #    return MeasureUnit.objects.filter(state = True)
    
        
class IndicatortListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer
    
    # def get_queryset(self):
    #     return Indicator.objects.filter(state = True)
            
class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
    
    # def get_queryset(self):
    #     return CategoryProduct.objects.filter(state = True)
    
    