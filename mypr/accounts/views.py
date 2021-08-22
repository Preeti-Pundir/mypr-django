from django.shortcuts import render

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

'''def signup(request):
    return render(request, 'signup.html')'''

def signup(request):
    form = UserCreationForm()
    #return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
    if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})