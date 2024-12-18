from rest_framework import serializers
from .models import martprices
 
class martserializers(serializers.ModelSerializer):
    class Meta:
        model = martprices
        fields = ['id','costomername','product_1','product_2','product_3','product_4','product_5','product_6','product_7']