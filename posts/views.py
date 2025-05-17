from django.shortcuts import render, redirect  
from .forms import ProfileForm  
from django.contrib import messages  
from django.contrib.messages import constants as messages_constants 

def upload_profile(request):  
    if request.method == 'POST':  
        form = ProfileForm(request.POST, request.FILES)  # Include request.FILES!  
        if form.is_valid():  
            form.save()  
            return  messages.success(request, 'Your message was sent successfully!')  
    else:  
        form = ProfileForm()  
    return render(request, 'posts/upload.html', {'form': form})  