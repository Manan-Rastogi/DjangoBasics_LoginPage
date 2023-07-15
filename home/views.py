from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

# Create your views here.


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        return render(request=request, template_name='index.html')
    
    return redirect('login')



def loginUser(request):
    if request.method == 'POST':
        # Authenticate user
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            return redirect('/')

        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html')
    
    if request.method == 'GET':
        return render(request, 'login.html')


def logoutUser(request):
    logout(request=request)
    return redirect('/login')
