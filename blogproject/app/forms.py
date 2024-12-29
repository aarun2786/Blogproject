from .models import Post,Tag,Bloger
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
def getChoice(self):
    return 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tag' ,'title', 'content']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':"Title"}),
            'tag':forms.SelectMultiple(attrs={'class':"form-select mb-2"},choices=[(tag.tag_name,tag.id)  for tag in Tag.objects.all()]),
            'content':forms.Textarea(attrs={"class":"tt"})
        }


class SignupForm(forms.ModelForm):
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input mb-2','placeholder':"Enter the Password"}))

    class Meta:
        model = User
        fields = ['username', 'email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input mb-2', 'placeholder': ' Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-input mb-2', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input mb-2', 'placeholder': 'Password'}),
        }

    def clean_username(self):
        data = super().clean().get('username')
        if User.objects.filter(username=data).exists():
            print("is it ture")
            raise forms.ValidationError("This User name is already exits")
        return data
    
    def clean_password2(self):
        data = super().clean()
        password = data.get('password')
        password2 = data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Pasword are not Matching")
        return password2


    def save(self, commit =True):
        user =  super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Bloger.objects.create(user=user)
        return user
    
