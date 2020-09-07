from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import Detail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password

# Create your views here.

class HomeView(View):

    @method_decorator(login_required)
    def get(self,request):
        data = {
            "details" :Detail.objects.filter(user=request.user),
        }
        return render(request,"manager/home.html",data)


class CreateDetail(View):

    @method_decorator(login_required)
    def get(self,request):
        return render(request,"manager/detail.html")

    @method_decorator(login_required)
    def post(self,request):
        data = Detail.objects.create(
            title=request.POST.get("title"),
            website=request.POST.get("website"),
            username=request.POST.get("username"),
            password=make_password(request.POST.get("password")),
            user=request.user
        )
        return redirect("home")
