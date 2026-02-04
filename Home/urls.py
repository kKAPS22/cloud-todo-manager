from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('done/<int:id>/', views.complete_task, name='done'),
    path('reschedule/<int:id>/', views.reschedule, name='reschedule'),
    path("logout/", views.logout_view, name="logout"),
]