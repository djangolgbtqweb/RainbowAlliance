from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home and User Authentication
    path('', views.home, name='home'),  # Home page route
    path('signup/', views.signup, name='signup'),  # User signup route
    path('login/', views.login_user, name='login'),  # User login route
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Redirect to home after logout
    path('accounts/signup/', RedirectView.as_view(url='/signup/', permanent=False)),
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=False)),
    
    path('mental-health-guides/', views.mental_health_guides, name='mental-health-guides'),
    path('support-groups/', views.support_groups, name='support-groups'),
    path('self-care-tips/', views.self_care_tips, name='self-care-tips'),


    path('resources/', views.educational_resources, name='educational-resources'),
    path('upload-resource/', views.upload_resource, name='upload-resource'),
    
    path('upload/', views.upload_health_resource, name='upload-health-resource'),
    path('resources/', views.health_resources_list, name='health-resources'),
    path('community-groups/', views.community_groups, name='community-groups'),

    # HTML views for Post list, creation, and details
    path('posts/', views.post_list, name='post-list'),  # Post list page
    path('post/create/', views.post_create, name='post-create'),  # Post create page
    path('post/<int:id>/', views.post_detail, name='post-detail'),  # Post detail page (with dynamic ID)
    path('posts-and-create/', views.post_list, name='post-list-create'),  # Post list with creation route (you can modify this if needed)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

