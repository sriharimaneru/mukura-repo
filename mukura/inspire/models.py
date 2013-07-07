from django.db import models
from blog.models import Post


RELATION = 0
FIELD = 1
INSPIRE_CATEGORY_CHOICES = ((RELATION, "Relation"),
                            (FIELD, "Field Of Work"), )

class InspireCategory(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    ordering = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)
    category_type = models.IntegerField(choices = INSPIRE_CATEGORY_CHOICES)
    
    class Meta:
        verbose_name = "Inspire Category"
        verbose_name_plural = "Inspire Categories"
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/inspire/categories/%s" % (self.slug,)
    
    
class InspireProfile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(null=True, blank=True)
    time_stamp = models.DateTimeField(null=True, blank=True)
    thumbnail = models.FileField(upload_to="inspire/thumbnails", null=True, blank=True)
    one_liner = models.CharField(max_length=100, null=True, blank=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(InspireCategory, null=True, blank=True)
    posts = models.ManyToManyField(Post, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/inspire/%s" % (self.slug,)