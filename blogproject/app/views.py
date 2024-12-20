from django.shortcuts import render,HttpResponse,redirect
from .forms import PostForm
from django.views import View
from .models import *
import json
from datetime import datetime
# Create your views here.

def Main(request):
    if request.POST:
        fm = PostForm(request.POST,request.FILES)
        if fm.is_valid():
            title =fm.cleaned_data.get('title')
            #html =fm.cleaned_data['content']
            html = fm.cleaned_data.get('content')
            tag = fm.cleaned_data.get('tag')
            bloger = Bloger.objects.get(id=1)
            post = Post.objects.create(bloger=bloger,title=title,content=html,pub_date=datetime.now())
            post.tag.set(tag)
            return redirect('home')

    form = PostForm(initial={'content':"Write something"})
    return render(request,'make_post.html',{'form':form})


def home(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    #recent_post
    if not 'recent_post' in  request.session:
        request.session['recent_post'] = []
    recent_posts = request.session.get('recent_post')
    recent_post = Post.objects.filter(slug_fiedl__in=recent_posts)
    #return HttpResponse(posts.content)
    return render(request,'home.html',{'posts':posts,'tags':tags,"recent_post":recent_post})


def TagsPost(request,tag):
    Post_tag = Tag.objects.get(tag_name=tag)
    posts = Post_tag.posts.all()
    all_tag = Tag.objects.all()
    return render(request,'tag_view.html',{'posts':posts,"tags":all_tag})
    
def post(request,slug):
    post = Post.objects.get(slug_fiedl=slug)
    
    recent_activity = request.session.get('recent_post')
    if slug not in recent_activity:
        recent_activity.append(slug)
    request.session['recent_posts'] = recent_activity
    return render(request,'post_view.html',{"post":post})
