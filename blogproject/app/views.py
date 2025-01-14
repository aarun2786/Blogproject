from django.shortcuts import render,HttpResponse,redirect
from .forms import PostForm,SignupForm,AuthenticationForm,CommentForm
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate,aauthenticate,login,logout
from django import forms
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView,FormView
from .models import *
import json
from datetime import datetime
# Create your views here.

class ProfileView(ListView):
    model = Bloger
    template_name='profile.html'
    context_object_name ='bloger'
    
    def get_queryset(self):
        bloger = Bloger.objects.get(user=self.request.user)
        
        return bloger

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bloger = self.get_queryset()
        context['user_posts'] = posts = Post.objects.filter(bloger=bloger.id)
        return context

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
        content = form.cleaned_data.get('content')
        bloger = Bloger.objects.get(user__username=self.request.user)
        post = form.save(commit=False)
        post.text_content = content
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
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = Bloger.objects.get(user__username=self.request.user)
            context['user'] =  user
        return context

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


    def get_object(self, queryset = None):
        slug = self.kwargs.get('slug')
        return self.model.objects.get(slug=slug)

    def get_bloger(self):
        return Bloger.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = self.get_object()
        
        # Get No of vist to post only other user not author
        if str(post.bloger) != str(self.request.user) :
            post.views = post.views + 1
            post.save()
            context['post'] = post        
        
        # User Activity
        recent_activity = self.request.session.get('recent_post')
        if slug not in recent_activity:
            recent_activity.append(slug)
            self.request.session['recent_posts'] = recent_activity
        else:
            self.request.session['recent_posts'] = ""
        
        # get all comments for particuler post
        context['all_comments'] = post.comments.all()
        cm = context.get('all_comments')
        for c in cm:
            print(c.bloger.profile_image.url)
        context['commentform'] = CommentForm()
        return context
    
    def post(self,request,*args,**kwargs):
        commentForm = CommentForm(request.POST)
        current_post = self.get_object()

        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.post = self.get_object()
            comment.bloger = self.get_bloger()
            comment.save()
        return redirect('post_view', slug=self.get_object().slug)

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
