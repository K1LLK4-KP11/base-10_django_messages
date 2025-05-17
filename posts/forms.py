from django import forms  
from .models import Post
class ProfileForm(forms.ModelForm):  
    class Meta:  
        model = Post
        fields = ['title', 'content', 'avatar']  