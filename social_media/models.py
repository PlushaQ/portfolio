from django.db import models

# Create your models here.


class SocialMedia(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title
