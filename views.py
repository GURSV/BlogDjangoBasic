from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def protected_view(request):
    posts = Post.objects.all()
    return render(request, '', {'posts': posts})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, '')

def profile_view(request):
    # Logic for the profile view
    return render(request, '')

def search_view(request):
    query = request.GET.get('q')  # Get the search query from the request

    if query:
        # Perform the search query using the title and content fields of the Post model
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        results = []

    context = {
        'query': query,
        'results': results
    }

    return render(request, 'blog/search_results.html', context)
    