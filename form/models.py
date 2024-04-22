from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_img/")

    def __str__(self):
        return "{},{}".format(self.pk, self.title)
