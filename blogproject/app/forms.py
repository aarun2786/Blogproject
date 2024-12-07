from .models import Post,Tag
from django import forms

def getChoice(self):
    return 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tag' ,'title', 'content']#
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'tag':forms.SelectMultiple(attrs={'class':"form-select"},choices=[(tag.tag_name,tag.id)  for tag in Tag.objects.all()]),
            'content':forms.Textarea(attrs={"class":"tt"})
        }

