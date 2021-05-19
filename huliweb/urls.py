from django.urls import path
from . import views

app_name = 'huliweb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('request/', views.SubView.as_view(),name='request')

]
