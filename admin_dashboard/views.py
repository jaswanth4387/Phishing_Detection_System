from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from client_portal.models import Prediction
from admin_dashboard.rbac import is_provider

import subprocess
import os


# =========================
# 📊 DASHBOARD (FIXED)
# =========================
@login_required
def dashboard(request):

    # 🔐 RBAC CHECK
    if not is_provider(request.user):
        return redirect('profile')

    # 📊 DATA
    total_users = User.objects.count()
    total_predictions = Prediction.objects.count()

    phishing_count = Prediction.objects.filter(result="Phishing URL").count()
    safe_count = Prediction.objects.filter(result="Legitimate URL").count()

    phishing_ratio = round((phishing_count / total_predictions) * 100, 2) if total_predictions else 0

    return render(request, 'admin/dashboard.html', {
        'total_users': total_users,
        'total_predictions': total_predictions,
        'phishing_ratio': phishing_ratio,
        'phishing_count': phishing_count,
        'safe_count': safe_count
    })


# =========================
# 👥 USERS PAGE
# =========================
@login_required
def view_users(request):

    if not is_provider(request.user):
        return redirect('profile')

    users = User.objects.all()

    return render(request, 'admin/users.html', {
        'users': users
    })


# =========================
# 📋 PREDICTIONS PAGE
# =========================
@login_required
def view_predictions(request):

    if not is_provider(request.user):
        return redirect('profile')

    predictions = Prediction.objects.select_related('user').all().order_by('-created_at')

    return render(request, 'admin/predictions.html', {
        'predictions': predictions
    })


# =========================
# ⚖️ RATIO PAGE
# =========================
@login_required
def ratio_view(request):

    if not is_provider(request.user):
        return redirect('profile')

    total = Prediction.objects.count()

    phishing = Prediction.objects.filter(result="Phishing URL").count()
    safe = Prediction.objects.filter(result="Legitimate URL").count()

    phishing_ratio = round((phishing / total) * 100, 2) if total else 0
    safe_ratio = 100 - phishing_ratio

    return render(request, 'admin/ratio.html', {
        'phishing_ratio': phishing_ratio,
        'safe_ratio': safe_ratio
    })


# =========================
# 📊 CHARTS PAGE
# =========================
@login_required
def charts_view(request):

    if not is_provider(request.user):
        return redirect('profile')

    phishing = Prediction.objects.filter(result="Phishing URL").count()
    safe = Prediction.objects.filter(result="Legitimate URL").count()

    return render(request, 'admin/charts.html', {
        'phishing_count': phishing,
        'safe_count': safe
    })


# =========================
# 🎯 ACCURACY PAGE
# =========================
@login_required
def accuracy_view(request):

    if not is_provider(request.user):
        return redirect('profile')

    # Static accuracy (you can improve later)
    accuracy = 95.5

    return render(request, 'admin/accuracy.html', {
        'accuracy': accuracy
    })


# =========================
# 🤖 TRAIN MODEL
# =========================
@login_required
@require_http_methods(["GET", "POST"])
def train_model(request):

    if not is_provider(request.user):
        return redirect('profile')

    message = None

    if request.method == "POST":
        try:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            train_script = os.path.join(BASE_DIR, 'ml_model', 'train.py')

            subprocess.run(['python', train_script], check=True)

            message = "✅ Model trained successfully!"

        except Exception as e:
            message = f"❌ Error: {str(e)}"

    return render(request, 'admin/train.html', {
        'message': message
    })