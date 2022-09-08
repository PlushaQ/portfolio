from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField()
