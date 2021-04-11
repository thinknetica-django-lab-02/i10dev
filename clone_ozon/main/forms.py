from django import forms

class ProfileForm(forms.Form):
    firstname = forms.CharField(max_length=255, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=255, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class': 'form-control'}))

  