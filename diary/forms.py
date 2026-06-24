from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DiaryEntry
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]


class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['title','content','mood',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control','rows': 8,}),
            'mood': forms.Select(attrs={'class': 'form-control'}),
                                 }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio',]
        widgets = {'bio': forms.Textarea(attrs={'class': 'form-control','rows': 5, }),}


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email',]