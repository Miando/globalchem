from django.db import models

class Tovar(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    bezpeka = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
