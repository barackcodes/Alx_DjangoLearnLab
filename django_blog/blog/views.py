from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login

from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # FIXED
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5 


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user   # FIXED typo
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'

    def test_func(self):
        post = self.get_object() 
        return self.request.user == post.author


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful. You're now logged in.")
            return redirect('blog:post-list')   # FIXED
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})  # FIXED TEMPLATE


@login_required
def profile(request):
    return render(request, 'blog/profile.html')


@login_required
def profile_edit(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()  
            messages.success(request, "Your profile has been updated.")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please fix the errors below.")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'blog/profile_edit.html', context)
