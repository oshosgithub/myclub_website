from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    #customized fields that's not part of build in User
    work_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',}))
    age = forms.CharField(max_length=5,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Age'}))

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email',
            'work_email',
            'username', 
            'password1', 
            'password2',
            'age',
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

    