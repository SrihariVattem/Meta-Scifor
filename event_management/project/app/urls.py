from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/category/', views.events_category, name='events_category'),
    path('register_event/<int:event_id>/', views.register_event, name='register_event'),
    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('user_dashboard',views.user_dashboard,name= 'user_dashboard')
]
