from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.TestView.as_view(), name="test"),
    path('<slug:param>/', views.TestApiGetView.as_view(), name='paramTest'),
    path('api/token', obtain_auth_token, name='getToken')
]
