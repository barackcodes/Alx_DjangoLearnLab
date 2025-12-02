from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request,"Registration successful. You're now logged in.")
            return redirect('blog:idex')
        else:
            messages.error(request, "Please correct the errors below.")
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
def profile_edit(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form()
            
            messages.success(request, "Your profile has been updated.")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'blog/profile_edit.html', context)
        