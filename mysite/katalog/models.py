from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def dodaty(self):
        self.save()
    def __str__(self):
        return self.name

class Tovar(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    bezpeka = models.TextField()
    category = models.ManyToManyField(Category)
    def publish(self):
        self.save()
    def __str__(self):
        return self.title
