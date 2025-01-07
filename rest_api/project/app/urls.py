from django.urls import path
from .views import *
from django.contrib import admin


urlpatterns=[
    path('admin/', admin.site.urls),
    path('', get),
    path('add',add),
    path('put/<int:id>/',put),
    path('patch/<int:id>/',patch),
    path('delete/<int:id>/',delete)
]