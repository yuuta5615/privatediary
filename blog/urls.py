from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index3"),
    path('/inquiry2/', views.InquiryView.as_view(), name = "inquiry2")
]