from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from accounts.models import User
from django.core.exceptions import ValidationError
from rest_framework import generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .forms import CommentForm
from django.views.generic import ListView
from django.conf import settings
import random  # For simulating payment success
from .models import EducationalResource
from .forms import EducationalResourceForm
from .forms import HealthResourceForm
from .models import HealthResource
from .models import CommunityGroup


# Home view
def home(request):
    return render(request, 'home.html')

# Signup view
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '')  # Optional
        last_name = request.POST.get('last_name', '')    # Optional

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, 'Signup successful! Please log in.')
            return redirect('login')
        except ValidationError as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('signup')

    return render(request, 'signup.html')

# Login view
def login_user(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user = None
        if '@' in username_or_email:
            user = authenticate(request, email=username_or_email, password=password)
        else:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'login.html')

# Post views
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post-list')
    return render(request, 'post_create.html')

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def educational_resources(request):
    if request.method == 'POST':
        form = EducationalResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Optionally, redirect or show a success message
        else:
            messages.error(request, "Please provide a description for the resource.")
    else:
        form = EducationalResourceForm()

    resources = EducationalResource.objects.all()  # Retrieve all uploaded resources
    return render(request, 'accounts/educational_resources.html', {'form': form, 'resources': resources})



def upload_resource(request):
    if request.method == 'POST':
        form = EducationalResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the resource list page or show a success message
            return redirect('educational-resources')  # Assuming this is the name of the page showing resources
    else:
        form = EducationalResourceForm()
    
    return render(request, 'accounts/upload_resource.html', {'form': form})



def upload_health_resource(request):
    if request.method == 'POST':
        form = HealthResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('health-resources')
    else:
        form = HealthResourceForm()
    return render(request, 'accounts/upload.html', {'form': form})

def health_resources_list(request):
    resources = HealthResource.objects.all().order_by('-uploaded_at')
    return render(request, 'accounts/resources_list.html', {'resources': resources})

from django.shortcuts import render
from .models import CommunityGroup  # Assuming you have a model for community groups

def community_groups(request):
    location = request.GET.get('location')
    group_type = request.GET.get('group_type')
    groups = CommunityGroup.objects.all()

    if location:
        groups = groups.filter(location__icontains=location)
    if group_type:
        groups = groups.filter(group_type=group_type)

    return render(request, 'accounts/community_groups.html', {'groups': groups})


def mental_health_guides(request):
    return render(request, 'accounts/mental_health_guides.html')

def support_groups(request):
    return render(request, 'accounts/support_groups.html')

def self_care_tips(request):
    return render(request, 'accounts/self_care_tips.html')