from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

class TestView(APIView):
    data = {
        'name'  :   'marzooq',
        'time'  :   timezone.now(),
    }

    def get(self, request, *args, **kwargs):
        return Response(self.data)