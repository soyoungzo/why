from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    body = models.TextField()
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body [:10]

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="images/")
    body = models.CharField(max_length=200)
    like_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# Create your models here.
