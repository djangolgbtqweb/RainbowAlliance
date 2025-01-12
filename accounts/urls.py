from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Define the namespace here if needed

urlpatterns = [
    # Home and User Authentication
    path('', views.home, name='home'),  # Home page route
    path('signup/', views.signup, name='signup'),  # User signup route
    path('login/', views.login_user, name='login'),  # User login route
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # User logout route

    # HTML views for Post list, creation, and details
    path('posts/', views.post_list, name='post-list'),  # Post list page
    path('post/create/', views.post_create, name='post-create'),  # Post create page
    path('post/<int:id>/', views.post_detail, name='post-detail'),  # Post detail page (with dynamic ID)
    path('posts-and-create/', views.post_list, name='post-list-create'),  # Post list with creation route (you can modify this if needed)
    

    
]
