from .models import Post,Tag
from django import forms

def getChoice(self):
    return 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tag' ,'title', 'content']#
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':"Title"}),
            'tag':forms.SelectMultiple(attrs={'class':"form-select mb-2"},choices=[(tag.tag_name,tag.id)  for tag in Tag.objects.all()]),
            'content':forms.Textarea(attrs={"class":"tt"})
        }
        label  ={'tag':""}
