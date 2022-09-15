from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index"),
    path('good', views.IndexView2.as_view(), name = "index2"),
    path('inquiry/', views.InquiryView.as_view(), name = "inquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name = "diary_list"),
]


