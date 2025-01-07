from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Post  # Assuming you still want your blog views
from django.shortcuts import redirect, render

# User Registration View

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        print("Inside form_valid method")  # Debug statement
        response = super().form_valid(form)
        return redirect(self.success_url)

    def post(self, request, *args, **kwargs):
        print("Received POST request")  # Debug statement
        return super().post(request, *args, **kwargs)


# User Login View
class UserLoginView(LoginView):
    template_name = 'login.html'  # Specify your login template

# Blog Views (for context, keep this if you need it)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
