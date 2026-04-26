from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Prediction
from ml_model.predict import predict_url


# 🔹 HOME PAGE
def home_view(request):
    return render(request, 'base.html')


# 🔹 REGISTER
def register_view(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        from django.contrib.auth.models import User

        if User.objects.filter(username=username).exists():
            return render(request, 'client/register.html', {'error': 'Username already exists'})

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return redirect('login')

    return render(request, 'client/register.html')


# 🔹 LOGIN
def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('post_login_redirect')   # 🔥 IMPORTANT

        return render(request, 'client/login.html', {'error': 'Invalid credentials'})

    return render(request, 'client/login.html')


# 🔹 ROLE-BASED REDIRECT
def post_login_redirect(request):

    if request.user.is_superuser:
        return redirect('dashboard')

    if request.user.has_perm('admin_dashboard.can_train_model'):
        return redirect('dashboard')

    return redirect('profile')


# 🔹 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# 🔹 PROFILE
@login_required
def profile_view(request):
    return render(request, 'client/profile.html')


# 🔹 PREDICT
@login_required
def predict_view(request):

    result = None

    if request.method == "POST":
        url = request.POST.get('url')

        result = predict_url(url)

        # Save to DB
        Prediction.objects.create(
            user=request.user,
            url=url,
            result=result
        )

    return render(request, 'client/predict.html', {
        'objs': result
    })

from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# 🔹 FORGOT PASSWORD
def forgot_password(request):
    return render(request, 'client/forgot.html')


# 🔹 VERIFY OTP
def verify_otp(request):
    return render(request, 'client/verify_otp.html')


# 🔹 RESET PASSWORD
def reset_password(request):
    return render(request, 'client/reset.html')

from admin_dashboard.rbac import is_provider

def admin_login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and is_provider(user):
            login(request, user)
            return redirect('dashboard')

        return render(request, 'client/admin_login.html', {
            'error': 'Invalid Provider Credentials'
        })

    return render(request, 'client/admin_login.html')