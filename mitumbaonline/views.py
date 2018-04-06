from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product,Category
from .serializer import ProductSerializer,CategorySerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework import generics


def Index(request):
    return render(request,'index.html')

   

class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class CategoryList(APIView):
    def get(self,request,format=None):
        all_cat=Category.objects.all()
        serializers=CategorySerializer(all_cat,many=True)
        return Response({'Categories': serializers.data})

    def post(self,request,format=None):
        serializers=CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)  
