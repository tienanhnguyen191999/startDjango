from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm
# Create your views here.


def register(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            # hash password and save to database
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}!')
            return redirect('blog-home')

    else:
        form = UserRegisterForm()
    return render(req, 'register.html', {'form': form})
