from django.contrib import admin
from django.urls import path,include
from accounts.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("accounts.urls")),
    path("",IndexView.as_view()),
    path("manager/",include("manager.urls"))
]
