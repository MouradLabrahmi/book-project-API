from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    #id = models.IntegerField(auto_create=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']
    def __str__(self):
        return self.title


