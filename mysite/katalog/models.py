from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def dodaty(self):
        self.save()
    def __str__(self):
        return self.name

class Tovar(models.Model):
    title = models.CharField(max_length=200)
    zastosuvannya = models.CharField(max_length=200)
    opys = models.TextField()
    category = models.ManyToManyField(Category)
    opublikovaty = models.BooleanField(default=False)
    def publish(self):
        self.save()
    def __str__(self):
        return self.title
