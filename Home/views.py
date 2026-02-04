from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import authenticate,login as auth_login
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import logout
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
    if request.method == "POST":
        raw = request.POST.get("due_date")  # "2026-02-04T18:20"
        if raw:
            naive = datetime.fromisoformat(raw)
            aware = timezone.make_aware(naive)

        Todo.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            due_date=aware,
            user=request.user,
            audio=request.FILES.get("audio"),
            video=request.FILES.get("video"),
        )


    todos = Todo.objects.filter(user=request.user)
    return render(request, "todo-dashboard.html", {"todos": todos})
def complete_task(request, id):
    todo = Todo.objects.get(id=id, user=request.user)

    # Delete from S3
    if todo.audio:
        todo.audio.delete(save=False)
    if todo.video:
        todo.video.delete(save=False)

    # Delete DB row
    todo.delete()

    return redirect('dashboard')



def reschedule(request, id):
    new_date = request.GET.get('d')
    Todo.objects.filter(id=id).update(due_date=new_date)
    return redirect('dashboard')



def logout_view(request):
    logout(request)
    return redirect("login")
