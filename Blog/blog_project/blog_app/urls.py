from django.urls import path
from .views import UserRegisterView, UserLoginView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),  # Redirect to registration
    path('login/', UserLoginView.as_view(), name='login'),  # Login page
    path('home/', PostListView.as_view(), name='post_list'),  # Blog home page
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
