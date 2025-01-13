from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    # Home and User Authentication
    path('', views.home, name='home'),  # Home page route
    path('signup/', views.signup, name='signup'),  # User signup route
    path('login/', views.login_user, name='login'),  # User login route
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Redirect to home after logout
     path('accounts/signup/', RedirectView.as_view(url='/signup/', permanent=False)),
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=False)),

    # HTML views for Post list, creation, and details
    path('posts/', views.post_list, name='post-list'),  # Post list page
    path('post/create/', views.post_create, name='post-create'),  # Post create page
    path('post/<int:id>/', views.post_detail, name='post-detail'),  # Post detail page (with dynamic ID)
    path('posts-and-create/', views.post_list, name='post-list-create'),  # Post list with creation route (you can modify this if needed)
    
]

