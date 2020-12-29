from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # Note, we create a model manager that will help us filter and return data (instead of returning all data available in db!):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        # Note, PROTECT means if user deletes a category, posts will be unaffected:
        Category, on_delete=models.PROTECT, default=1
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        # Note, CASCADE means if we delete a user, the posts for that user will also be deleted:
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        # Note, we can specify if data should be returned in ascending/descending order by default:
        ordering = ('-published',)

    def __str__(self):
        return self.title
