from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from donate.models import Profile, Donation
from .forms import DonorSignupForm, DonationForm,BankSignupForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def home(request):
    return render(request,'home.html')

def donorsignup(request):
    if request.method == 'POST':
        form = DonorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active =True
            user.is_donor = True
            user.is_bbank = False
            user.save()
            return redirect('/')
    else:
        form = DonorSignupForm()
    return render(request,'registration/donorsignup.html', { "form":form })

def banksignup(request):
    if request.method == 'POST':
        form = BankSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active =True
            user.is_donor = False
            user.is_bbank = True
            user.save()
            return redirect('/')
    else:
        form = BankSignupForm()
    return render(request,'registration/banksignup.html', { "form":form })


def donation(request):
    current_user = request.user
    if request.method == 'POST':
        form = DonationForm(request.POST,request.FILES)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = current_user
            donation.save()
    else:
        form = DonationForm()
    return render(request, 'dashboard.html', {'form':form})

def showdonorprofile(request,user_id):
    users = User.objects.filter(id=user_id)
    profiles = Profile.objects.filter(user=users)
    print(profiles)
    return redirect('/')
@login_required
def index(request):
    drives = Donation.objects.all()
    print(drives)
    return render(request,'index.html',{"drives":drives})
