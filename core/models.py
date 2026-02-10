from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


def _get_default_admin_pk():
    User = get_user_model()
    try:
        admin = User.objects.filter(is_superuser=True).order_by('id').first()
        return admin.pk if admin else None
    except Exception:
        return None

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    content = models.TextField(help_text='HTML allowed')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, default=_get_default_admin_pk)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.subject}"
