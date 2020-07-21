from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestView.as_view(), name="test"),
    path('<slug:param>/', views.TestApiGetView.as_view(), name='paramTest')
]
