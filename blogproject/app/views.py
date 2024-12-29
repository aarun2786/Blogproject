from django.shortcuts import render,HttpResponse,redirect
from .forms import PostForm,SignupForm,AuthenticationForm
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate,aauthenticate,login,logout
from django import forms
from django.views.generic.edit import CreateView
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
            bloger = Bloger.objects.get(user__username=request.user)
            post = Post.objects.create(bloger=bloger,title=title,content=html,pub_date=datetime.now())
            post.tag.set(tag)
            return redirect('home')

    form = PostForm(initial={'content':"Write something"})
    return render(request,'make_post.html',{'form':form})

class PostCreateView(CreateView):
    model = Post
    template_name = 'make_post.html'
    form_class = PostForm
    success_url= "/"

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['content'].initial = "Write something"
        return form
        


    def form_valid(self, form):
        action = self.request.POST.get('action')        
        
        bloger = Bloger.objects.get(user__username=self.request.user)
        post = form.save(commit=False)
        post.bloger = bloger
        post.pub_date = datetime.now()
        
        if action == 'save':
            post.is_publish = False
        else:
            post.is_publish = True
        
        post.save()
        
        return super().form_valid(form)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = '-pub_date'

    def get_queryset(self):
        ojb =  Bloger.objects.all()
        return Post.objects.filter(is_publish=True)

class TagView(ListView):
    model =Tag
    template_name = 'tag_view.html'
    context_object_name = 'taged_post'
    pk_url_kwarg = 'tag'

    def get_queryset(self):
        Post_tag = Tag.objects.get(tag_name=self.kwargs['tag'])
        posts = Post_tag.posts.filter(is_publish=True)
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


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = '/login'


class Loginview(LoginView):
    template_name = "login_page.html"
    form_class = AuthenticationForm
    success_url = "/"

    def get_form(self, form_class = None):
        form =  super().get_form(form_class)
        form.fields['username'].widget =forms.TextInput(attrs={'class': 'form-input mb-2', 'placeholder': ' Username'})
        form.fields['password'].widget =forms.PasswordInput(attrs=({'class': 'form-input mb-2', 'placeholder': ' Password'}))
        return form

    def form_valid(self, form):
        login(self.request,form.get_user())
        return redirect('home')



class Logoutview(LogoutView):
    next_page = '/'

