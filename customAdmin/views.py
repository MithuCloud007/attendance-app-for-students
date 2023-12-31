from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def backend(request):
    return render(request, 'customAdmin/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('customAdmin:backend_dashboard')

    return render(request, 'customAdmin/login.html')

def logoutuser(request):
    logout(request)
    return redirect('customAdmin:login_page')