from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import martprices
from .serializers import martserializers
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def martbilling(request):
    if request.method == 'POST':
        serializer = martserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET'])
def billing_id(request,id):
    martprice = martprices.objects.get(pk=id)

    if request.method == 'GET':
        serializer = martserializers(martprice)
        print(serializer.data["costomername"])
        total_prize = serializer.data["product_1"] + serializer.data["product_2"] + serializer.data["product_3"] + serializer.data["product_4"] + serializer.data["product_5"] + serializer.data["product_6"] + serializer.data["product_7"]
        print(f"total price =  {total_prize}")
        
        actual_price = total_prize
        discount_above_1000 = total_prize - 100 
        discount_above_1500 = total_prize - 225
        discount_above_2500 = total_prize - 500
        discount_above_5000 = total_prize - 1500

        if (total_prize > 1000 and total_prize < 1500):
            total_prize = discount_above_1000
        elif (total_prize > 1500 and total_prize < 2500):
            total_prize = discount_above_1500
        elif (total_prize > 2500 and total_prize < 5000):
            total_prize = discount_above_2500
        elif (total_prize > 5000):
            total_prize = discount_above_5000
        
        final_bill = total_prize
        print(f"Final bill after Discount = {final_bill}")
        data = {}
        data["costomername"] = serializer.data["costomername"]
        data["product_1"] = serializer.data["product_1"]
        data["product_2"] = serializer.data["product_2"]
        data["product_3"] = serializer.data["product_3"]
        data["product_4"] = serializer.data["product_4"]
        data["product_5"] = serializer.data["product_5"]
        data["product_6"] = serializer.data["product_6"]
        data["product_7"] = serializer.data["product_7"]
        data["total price"] = actual_price
        data["final bill after discount"] = final_bill

        return Response(data)



