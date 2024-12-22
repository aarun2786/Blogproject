from .models import Post, Tag

def sidebar_data(request):
    if not 'recent_post' in request.session:
        request.session['recent_post'] = []
    posts = request.session.get('recent_post')
    posts= Post.objects.filter(slug__in=posts)
    tags = Tag.objects.all()
    return {'recent_post':posts,'tags':tags}