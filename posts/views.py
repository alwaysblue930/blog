from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def read(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'read.html', {'post': post})

def listall(request):
    posts = Post.objects.all()
    return render(request, 'listall.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
        else:
            print(form.errors)
             
    return render(request, 'create.html')

def delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        post.delete()

    return redirect('home')
    
def update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        return render(request, 'update.html', {'post': post}) 
    
def contact(request):
    return render(request, 'contact.html')