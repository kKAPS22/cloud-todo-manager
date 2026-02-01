from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import authenticate,login as auth_login
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST.get('fnm')
        email=request.POST.get('email')
        password=request.POST.get('Pwd')
    
        if User.objects.filter(username=username).exists():
         messages.error(request,"Username already exists")
         return redirect('signup')
        
    
        user=User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    
        user.save()
        return redirect('login')
    
    
    return render(request,'signup.html')

def login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            auth_login(request,user)#session create
            return redirect('dashboard')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
        
    return render(request,'login.html')

@login_required
def dashboard(request):
    if request.method=="POST":
        Todo.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            due_at=request.POST.get("due_at"),
            user=request.user
        )
        
    todos = Todo.objects.filter(user=request.user)#Database se sirf wahi todo nikkalo jo current logged in user ke hain 
    return render(request, "todo-dashboard.html", {"todos": todos})

