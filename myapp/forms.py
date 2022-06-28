from django import forms
from .models import*


class UsercreateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['name','email','phone','password']
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'phone':forms.TextInput(attrs={'class':'form-control','id':'phoneid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'}),
            
        }
        

class EditUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['name','email','phone','password']
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'phone':forms.TextInput(attrs={'class':'form-control','id':'phoneid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'}),
            
        }