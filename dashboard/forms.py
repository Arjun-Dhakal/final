from django import forms
from main.models import Slide, Client, About, Service, Contact, Media

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['title', 'description', 'message', 'image']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'logo']


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'description', 'image']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'icon']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'maps']


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = [
            'office_description', 'office_phone', 'office_address', 'office_email',
            'facebook', 'twitter', 'instagram', 'linkedin'
        ]
