from django.contrib.auth import get_user_model
from django.db import models
from slugify import slugify

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=30, unique=True
    )
    slug = models.SlugField(
        max_length=30, primary_key=True, blank=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Tag(models.Model):
    title = models.CharField(max_length=15,
                             unique=True)
    slug = models.SlugField(max_length=15,
                    primary_key=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Post(models.Model):
    author = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='posts')
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/')
    slug = models.SlugField(max_length=30,
        primary_key=True, blank=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category,
         on_delete=models.CASCADE,
        related_name='posts')
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    body = models.CharField(max_length=30)
    post = models.ForeignKey(Post,
            on_delete=models.CASCADE,
            related_name='comments')
    author = models.ForeignKey(User,
                on_delete=models.CASCADE,
                related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-created_at']


class Rating(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='ratings'
    )

    def __str__(self):
        return f'{self.rating} -> {self.post}'


class Like(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='likes'
    )
    is_liked = models.BooleanField(
        default=False)

    def __str__(self):
        return f'{self.post} Liked by ' \
               f'{self.author.name}'







