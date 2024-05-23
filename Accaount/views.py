from django.shortcuts import render,redirect
from.forms import*
from django.contrib import messages
# Create your views here.
def Login(request):
    return render(request,'login.html')

def Registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered.')
            return redirect('login')
        else:
            messages.warning(request, 'Please enter valid information and ensure the password is 8+ characters.')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

