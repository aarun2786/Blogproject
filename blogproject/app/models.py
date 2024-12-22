from django.db import models
from django.urls import reverse
from django_summernote.fields import SummernoteTextField
from django.contrib.auth.models import User
# Create your models here.
class Bloger(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio_data = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    tag = models.ManyToManyField("Tag",related_name='posts')
    bloger = models.ForeignKey(Bloger,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = SummernoteTextField()
    pub_date = models.DateTimeField()
    slug = models.SlugField()
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    
    def get_tag(self):
        return ",".join(tg.tag_name for tg in self.tag.all())
    
    def get_slug(self):
        return reverse("post_view",kwargs={'slug':self.slug_fiedl})


class Comment(models.Model):
    bloger = models.ForeignKey(Bloger,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name
    
    def taged_post(self):
        return ",".join(f"{pt.title} {pt.bloger.user.username}" for pt in self.posts.all())