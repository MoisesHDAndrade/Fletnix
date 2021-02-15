from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from Fletnix.apps.accounts.models import UserProfile
from .forms import UserProfileForm

def register(request):
    if request.user.is_authenticated:
        # return redirect('accounts:detail')
        print('esta autenticado')
    if request.method !='POST':
        return render(request, 'register.html')

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('user')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if not first_name and not last_name and not username and not email and not password and not confirm_password:
        messages.error(request, 'All fields must be filled')
        return render(request, 'register.html')

    if password != confirm_password:
        messages.error(request, 'Password does not match')
        return render(request, 'register.html')

    if len(password) < 5:
        messages.error(request, 'Password must have 6 characters at least')
        return render(request, 'register.html')

    if len(username) < 4:
        messages.error(request, 'Username must have 5 characters at least')
        return render(request, 'register.html')
    
    if User.objects.filter(username=username).exists():
        messages.error(request, 'This username has been taken already')
        return render(request, 'register.html')	

    if User.objects.filter(email=email).exists():
        messages.error(request, 'This e-mail address has been taken already')
        return render(request, 'register.html')
    try:
        validate_email(email)
    except:
        messages.error(request, 'Invalid Email')
        return render(request, 'register.html')
        
def login(request):
    return render(request, 'login.html')

def profile_detail(request):
    user = request.user.user_profile
    return render(request, 'user_profile.html', {'user':user})

def profile_update(request):
    profile = request.user.user_profile
    form = UserProfileForm(request.POST or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        profile.save()
        messages.success(request, 'User settings was updated')
        return redirect('user_profile:profile_detail')
