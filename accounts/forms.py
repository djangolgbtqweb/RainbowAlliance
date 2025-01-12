from django import forms
from .models import User, Post, Comment

# Form for User creation
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

# Form for Post creation
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# Form for Comment creation
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Add a comment...'}),
        }


