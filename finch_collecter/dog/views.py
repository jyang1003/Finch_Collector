#Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DogSerializer
from .models import Dog

class DogsView(APIView):
  def get(self, request):
        dogs = Dog.objects.all()
        data = DogSerializer(dogs, many=True).data
        return Response(data)
  def post(self, request):
        print(request.data)
        dog = DogSerializer(data=request.data)
        if dog.is_valid():
            dog.save()
            return Response(dog.data, status=status.HTTP_201_CREATED)
        else:
            return Response(dog.errors, status=status.HTTP_400_BAD_REQUEST)
class DogDetailView(APIView):
    def get(self, request, pk):
        """show one dog"""
        dogs = get_object_or_404(Dog, pk=pk)
        data = DogSerializer(dogs).data
        return Response(data)
    def delete(self, request, pk):
        """Delete a dog"""
        dog = get_object_or_404(Dog, pk=pk)
        data = DogSerializer(dog).data
        return Response(data)
    def patch(self, request, pk):
        """Update a dog"""
        #first we locate the dog
        dog = get_object_or_404(Dog, pk=pk)
        updated_dog = DogSerializer(dog, data=request.data)
        if updated_dog.is_valid():
            updated_dog.save()
            return Response(updated_dog.data)
        return Response(updated_dog.errors, status=status.HTTP_400_BAD_REQUEST)

