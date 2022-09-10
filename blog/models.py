from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) < 150:
            return self.body
        else:
            return self.body[:150]+"..."

    def publish_time(self):
        return self.publish_date.strftime("%e %b %Y")