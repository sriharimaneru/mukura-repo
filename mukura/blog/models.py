from django.db import models


class PostCategory(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    ordering = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/categories/%s" % (self.slug,)
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    time_stamp = models.DateTimeField(null=True, blank=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(PostCategory, null=True, blank=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/%s" % (self.slug,)