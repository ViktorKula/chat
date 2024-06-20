from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Profile
from .forms import SignUpForm, AvatarForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import AvatarForm, UserEditForm
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()


def user_list(request):
    users = Profile.objects.all()
    return render(request, 'core/users.html', {'users': users})

def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'core/frontpage.html')


def user_page_view(request):
    return render(request, 'core/User_Page.html')


User = get_user_model()


def avatar_edit(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_page')
    else:
        form = AvatarForm(instance=request.user.profile)
    return render(request, 'core/avatar_edit.html', {'form': form})


def username_edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_page')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'core/username_edit.html', {'form': form})
