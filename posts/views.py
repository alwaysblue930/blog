from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def create_get(request):
    return render(request, 'create.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PostForm()
        
    return render(request, 'create.html', {'form': form})
def delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        post.delete()

    return redirect('index')
    
def update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        return render(request, 'update.html', {'post': post}) 