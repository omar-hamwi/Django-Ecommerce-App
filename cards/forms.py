from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField , PasswordChangeForm
from django.contrib.auth.models import User
from .models  import Customer 


#this class for login
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password' , 'class':'form-control'}))


#This class for registration
class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

# Why do we use meta class?
# In object-oriented programming, a metaclass is a class whose instances are classes. 
# Just as an ordinary class defines the behavior 
# of certain objects, a metaclass defines the behavior of certain classes 
# and their instances. Not all object-oriented programming languages support metaclasses.

class MyPasswordResetForm(PasswordChangeForm):
    pass 

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['id','user','locality','city','state','zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality' :forms.TextInput(attrs={'class':'form-control'}),
            'city' :forms.TextInput(attrs={'class':'form-control'}),
            'mobile' :forms.NumberInput(attrs={'class':'form-control'}),
            'state' :forms.Select(attrs={'class':'form-control'}),
            'zipcode' :forms.NumberInput(attrs={'class':'form-control'}),
             

        }
