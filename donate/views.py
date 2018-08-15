from django.shortcuts import render, redirect
from .forms import DonorSignupForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def index(request):
    return render(request,'donor/index.html')


def donorsignup(request):
    if request.method == 'POST':
        form = DonorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active =True
            user.save()
            return redirect('/')
    else:
        form = DonorSignupForm()
    return render(request,'donor/donorsignup.html',{"form":form})
