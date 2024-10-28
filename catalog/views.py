from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import AddleadForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, 'lead/dasboard.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            userprofile = UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()

    data = {'form': form}
    return render(request, 'userprofile/signup.html', data)


@login_required
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    data = {'form': form}
    return render(request, 'userprofile/loginup.html', data)


def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddleadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            return redirect('dash')
    else:
        form = AddleadForm()

    data = {'form': form}
    return render(request, 'lead/lead_add.html', data)


