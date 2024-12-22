from django.shortcuts import render,HttpResponse,redirect
from .forms import PostForm
from django.views import View
from django.views.generic import ListView,DetailView
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



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = '-pub_date'

    def get_queryset(self):
        return Post.objects.all()

class TagView(ListView):
    model =Tag
    template_name = 'tag_view.html'
    context_object_name = 'taged_post'
    pk_url_kwarg = 'tag'

    def get_queryset(self):
        Post_tag = Tag.objects.get(tag_name=self.kwargs['tag'])
        posts = Post_tag.posts.all()
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_view.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        post = self.model.objects.get(slug=slug)
        post.views = post.views + 1
        post.save()
        
        context = super().get_context_data(**kwargs)
        context['post'] = post
        
        recent_activity = self.request.session.get('recent_post')
        if slug not in recent_activity:
            recent_activity.append(slug)
            self.request.session['recent_posts'] = recent_activity
        else:
            self.request.session['recent_posts'] = ""
        
        return context

# def post(request,slug):
#     post = Post.objects.get(slug_fiedl=slug)
#     post.views = post.views + 1
#     post.save()

#     recent_activity = request.session.get('recent_post')
#     if slug not in recent_activity:
#         recent_activity.append(slug)
#         request.session['recent_posts'] = recent_activity
#     else:
#         request.session['recent_posts'] = ""
#     return render(request,'post_view.html',{"post":post})
