from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_inages', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", self.pk)