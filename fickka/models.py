from django.db import models
from django.shortcuts import reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    likes = models.ManyToManyField(User, related_name='blog_post', null=True, blank=True, default=None)
    image_1 = models.ImageField(null=True, blank=True, default=None)
    image_2 = models.ImageField(null=True, blank=True, default=None)
    image_3 = models.ImageField(null=True, blank=True, default=None)
    To_homepage = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=100, null=True, blank=True)
    views = models.IntegerField(default=0, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField()
    post_number = models.IntegerField(null=True, blank=True, default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title) + ' by ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    likes = models.ManyToManyField(User, blank=True, related_name='comment_like')

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-date').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


class Thread(models.Model):
    post = models.ForeignKey(Post, related_name='thread', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    threads = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    image_1 = models.ImageField(null=True, blank=True, default=None)
    image_2 = models.ImageField(null=True, blank=True, default=None)
    image_3 = models.ImageField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('article', args=[self.id])


class Profile(models.Model):
    Gender = (
        ('Male','Male'),
        ('Female', 'Female')
    )

    Occupation = (
        ('Student', 'Student'),
        ('Employed', 'Employed'),
        ('Self Employed', 'Self Employed'),
        ('Unemployed', 'Unemployed')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Biography = models.TextField(max_length=100)
    Gender = models.CharField(max_length=50, choices=Gender)
    State = models.CharField(max_length=20)
    Occupation = models.CharField(max_length=30, choices=Occupation)
    Contact = models.IntegerField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    confirmed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' profile'


class About(models.Model):
    about = models.TextField()






