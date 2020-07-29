from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics

class TestView(APIView):

    def get(self, request, *args, **kwargs):
        # data = {
        #     'name'  :   'marzooq',
        #     'time'  :   timezone.now(),
        # }
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serial = PostSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return serial.errors

class TestApiGetView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        title = kwargs['param']
        qs = Post.objects.get(title=title)
        post = PostSerializer(qs)
        return Response(post.data)

class newPage(generics.ListAPIView):
    """
    instead of specifying the get method in TestView we just specify the queryset and 
    serializer class in newPage which extends ListAPIView which extends generic APIView
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class newPage2(generics.CreateAPIView):
    serializer_class = PostSerializer

class NewPageThree(generics.DestroyAPIView):
    """
    Less code for deleting a Post object
    """
    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.queryset = Post.objects.filter(pk=pk) #it works with filter but not with get
        return self.destroy(request, *args, **kwargs)