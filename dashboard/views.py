from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SlideForm,ClientForm, AboutForm, ServiceForm, ContactForm, MediaForm
from main.models import Slide, Client, About, Service, Contact, Media
from django.contrib import messages
# Create your views here.
@login_required(login_url='log_in')
def dashboard(request):
    if not request.user.is_staff:
        return redirect('log_in')
    return render(request, "admin/dashboard.html", {'user': request.user})

# slide

def slide_list(request):
    if not request.user.is_staff:
        return redirect('log_in')
    slides = Slide.objects.all()  # all slides
    return render(request, 'admin/slide_list.html', {'slides': slides})


def slide_create(request):
    form = SlideForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Slide created successfully!')
        return redirect('slide_list')
    return render(request, 'admin/slide_form.html', {'form': form, 'model_name': 'Slide', 'action': 'Create'})


def slide_update(request, pk):
    slide = Slide.objects.get(pk=pk)
    form = SlideForm(request.POST or None, request.FILES or None, instance=slide)
    if form.is_valid():
        form.save()
        messages.success(request, 'Slide updated successfully!')
        return redirect('slide_list')
    return render(request, 'admin/slide_form.html', {'form': form, 'model_name': 'Slide', 'action': 'Update'})


def slide_delete(request, pk):
    slide = Slide.objects.get(pk=pk)
    slide.delete()
    messages.success(request, 'Slide deleted successfully!')
    return redirect('slide_list')



@login_required
def aboutus_list(request):
    aboutus = About.objects.all().order_by('id')
    return render(request, 'admin/aboutus.html', {'aboutus': aboutus})

def aboutus_create(request):
    form = AboutForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'About Us created successfully!')
        return redirect('aboutus_list')
    return render(request, 'admin/aboutus_form.html', {'form': form, 'model_name': 'About Us', 'action': 'Create'})

def aboutus_update(request, pk):
    aboutus = About.objects.get(pk=pk)
    form = AboutForm(request.POST or None, request.FILES or None, instance=aboutus)
    if form.is_valid():
        form.save()
        messages.success(request, 'About Us updated successfully!')
        return redirect('aboutus_list')
    return render(request, 'admin/aboutus_form.html', {'form': form, 'model_name': 'About Us', 'action': 'Update'})

def aboutus_delete(request, pk):    
    aboutus = About.objects.get(pk=pk)
    aboutus.delete()
    messages.success(request, 'About Us deleted successfully!')
    return redirect('aboutus_list')

def contactus_list(request):
    contacts = Contact.objects.all().order_by('id')
    return render(request, 'admin/contact_form.html', {'contacts': contacts})


def media_list(request):
    media = Media.objects.all()
    return render(request, 'admin/media.html', {'media': media})

def media_create(request):
    form= MediaForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Media created successfully!')
        return redirect('media')
    else:
        form= MediaForm()
        return render(request, 'admin/media_form.html', {'form': form, 'model_name': 'Media', 'action': 'Create'})
    
def media_update(request, pk):
    media = Media.objects.get(pk=pk)
    if request.method == 'POST':
        form = MediaForm(request.POST or None, instance=media)
        if form.is_valid():
            form.save()
        messages.success(request, 'Media updated successfully!')
        return redirect('media_list')
    else:
        form = MediaForm(instance=media)
    return render(request, 'admin/media.html', {'form': form})

def media_delete(request, pk):
    media = Media.objects.get(pk=pk)
    if request.method == 'POST':
        media.delete()
        messages.success(request, 'Media deleted successfully!')
        return redirect('media')
    return render(request, 'admin/media_delete.html', {'media': media})    

    
def service_list(request):
    services = Service.objects.all()
    return render(request, 'admin/service.html', {'services': services})


def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service created successfully!')
            return redirect('service')
    else:
        form = ServiceForm()

    return render(request, 'admin/service_form.html', {
        'form': form,
        'action': 'Add'
    })


def service_update(request, pk):
    service = Service.objects.get(pk=pk)

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully!')
            return redirect('service')
    else:
        form = ServiceForm(instance=service)

    return render(request, 'admin/service_form.html', {
        'form': form,
        'action': 'Update'
    })


def service_delete(request, pk):
    service = Service.objects.get(pk=pk)
    service.delete()
    messages.success(request, 'Service deleted successfully!')
    return redirect('service')
