from django.urls import path
from .views import user_dashboard
from . import views

urlpatterns = [
    path('', user_dashboard, name='dashboard'),
    path('logout/', views.custom_logout_view, name='logout'),
]
