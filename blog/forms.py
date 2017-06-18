from django import forms
from .models import Post
from .models import Device

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['DeviceID', 'CustomerProduct', 'Tester', 'NoPara', 'ProductType']
