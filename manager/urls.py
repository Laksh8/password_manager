from django.urls import path
from .views import HomeView,CreateDetail

urlpatterns = [
    path("home/",HomeView.as_view(),name="home"),
    path("detail/",CreateDetail.as_view(),name="detail")
]

