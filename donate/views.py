from django.shortcuts import render, redirect

from donate.models import Profile
from .forms import DonorSignupForm,BankSignupForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    return render(request,'registration/index.html')

def banksignup(request):
    if request.method == 'POST':
        form = BankSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active =True
            user.save()
            return redirect('/')
    else:
        form = BankSignupForm()
    return render(request,'registration/banksignup.html', { "form":form })
def donorsignup(request):
    if request.method == 'POST':
        form = DonorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active =True
            user.save()
            return redirect('/')
    else:
        form = DonorSignupForm()
    return render(request,'registration/donorsignup.html', { "form":form })


def showdonorprofile(request,user_id):
    users = User.objects.filter(id=user_id)
    profiles = Profile.objects.filter(user=users)
    print(profiles)
    return render(request,'don/showdon.html',{"profiles":profiles,"users":users})