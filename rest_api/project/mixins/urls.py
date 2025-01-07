from django.db import router
from django.urls import path,include
from django.views.generic import DeleteView

from .myviews import Listview, Creatview, Retrieveview, Updateview, lsview, rudview, ruview, rdview
from rest_framework.mixins import RetrieveModelMixin

from .views import Startuplist, Createstartup, Deletestartup, Retrivestartup, Updatestartup

from rest_framework.routers import DefaultRouter
from .viewset_view import Startupviews


'''
urlpatterns=[
This are path to views.py
    path('',Startuplist.as_view()),
    path('add',Createstartup.as_view()),
    path('delete/<int:pk>/',Deletestartup.as_view()),
    path('get/<int:pk>/',Retrivestartup.as_view()),
    path('update/<int:pk>/',Updatestartup.as_view())
]''',

'''
# This are path ot myviews.py
urlpatterns=[
    path('',Listview.as_view()),
    path('add/',Creatview.as_view()),
    path('get/<int:pk>/',Retrieveview.as_view()),
    path('update/<int:pk>/',Updateview.as_view()),
    path('delete/<int:pk/',DeleteView.as_view()),
    path('ls/',lsview.as_view()),
    path('ru/<int:pk>/',ruview.as_view()),
    path('rd/<int:pk>/',rdview.as_view()),
    path('rud/<int:pk>/',rudview.as_view()),


]
'''

# This is path for the  viewset_myview file
router=DefaultRouter()
router.register(r'api',Startupviews,basename='Startup')

urlpatterns=[
    path('',include(router.urls))
]