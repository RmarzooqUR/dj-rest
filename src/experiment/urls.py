from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.TestView.as_view(), name="test"),
    path('one/', views.newPage.as_view(), name="testListapiview"),
    path('two/', views.newPage2.as_view() , name="testCreateapiview"),
    path('three/<int:pk>/', views.NewPageThree.as_view(), name="testDeleteapiview"),
    path('<slug:param>/', views.TestApiGetView.as_view(), name='paramTest'),
    path('api/token', obtain_auth_token, name='getToken'),
]
