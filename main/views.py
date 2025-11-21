from django.shortcuts import render,redirect

from .models import Slide,Contact,Service,About,Media
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
   slide=Slide.objects.all()
   service=Service.objects.all()
   about=About.objects.first()
   media=Media.objects.last()
   
 
   context={
      'about':about,
      'slide':slide,
      'service':service,
      'media':media
   }
   return render(request, "core/index.html",context)

def contact(request):

   if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      subject=request.POST.get('subject')
      message=request.POST.get('message')
      data=Contact(name=name,email=email,subject=subject,message=message,)
      data.save()
      return render(request,'core/contact.html',{'success':'Your message has been sent successfully.'})
   return render(request,'core/contact.html')







# for admin

def log_in(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Please enter both username and password")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid credentials")
            return redirect('log_in')

    return render(request, "admin/login.html")


@login_required(login_url='log_in')
def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('log_in')