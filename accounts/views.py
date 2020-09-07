from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
class IndexView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        return redirect("login")


class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request,"accounts/login.html")

    def post(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        user = auth.authenticate(username=request.POST.get("username"),password=request.POST.get('password'))
        if user:
            auth.login(request,user)
            messages.success(request,"Login Successfully")
            return redirect("/")
        messages.error(request,"Username Or Password is Incorrect")
        return redirect("/")

class RegisterView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request,"accounts/register.html")

    def post(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        if request.POST.get("password") != request.POST.get("password1"):
            messages.error("Password Doesn't Match")
            return redirect("/")
        user = User.objects.create(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password")
        )
        auth.login(request,user)
        return redirect("/")


class LogoutView(View):
    def get(self,request):
        if request.user.is_authenticated:
            auth.logout(request)
            messages.success(request,"Logout Successfully")
            return redirect("/")
        messages.error(request,"Already LoggedOut")
        return redirect("/")

