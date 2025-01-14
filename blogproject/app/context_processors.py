from .models import Post, Tag,Bloger

def sidebar_data(request):
    context_data ={}
    if not 'recent_post' in request.session:
        request.session['recent_post'] = []
    
    posts = request.session.get('recent_post')
    posts= Post.objects.filter(slug__in=posts)
    tags = Tag.objects.all()
    
    context_data['recent_post']= posts
    context_data['tags']=tags
    
    if  request.user.is_authenticated:
        context_data['user'] = Bloger.objects.get(user__username=request.user)
    else:
        context_data['user'] = False
    return context_data