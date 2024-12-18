from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Event, Registration, EventCategory

# Home View
def home(request):
    category_name = request.GET.get('category', 'all')
    if category_name != 'all':
        # Use EventCategory to filter by name
        category = get_object_or_404(EventCategory, name=category_name)
        events = Event.objects.filter(category=category)
    else:
        events = Event.objects.all()

    categories = EventCategory.objects.all()  # Fetch all categories for the dropdown
    return render(request, 'home.html', {'events': events, 'category': category_name, 'categories': categories})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

# Register Event View
@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        Registration.objects.create(
            user=request.user,
            event=event,
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            gender=request.POST['gender'],
            description=request.POST['description']
        )
        return redirect('home')
    return render(request, 'register_event.html', {'event': event})

# Events by Category View
def events_category(request):
    categories = EventCategory.objects.all()
    selected_category = request.GET.get('category')
    events = Event.objects.filter(category__name=selected_category) if selected_category else Event.objects.all()
    return render(request, 'events_category.html', {'categories': categories, 'events': events})


# Admin Dashboard
@staff_member_required
def admin_dashboard(request):
    registrations = Registration.objects.select_related('event', 'user')
    return render(request, 'admin_dashboard.html', {'registrations': registrations})

# User Dashboard
@login_required
def user_dashboard(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'user_dashboard.html', {'registrations': registrations})

# User Registration
def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'registration.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'registration.html')
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('home')
    return render(request, 'registration.html')

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('home')



# View for displaying events based on selected category
def event_by_category_view(request, category_id):
    category = get_object_or_404(EventCategory, id=category_id)  # Get the selected category
    events = Event.objects.filter(category=category)  # Filter events by category
    return render(request, 'events_by_category.html', {'category': category, 'events': events})