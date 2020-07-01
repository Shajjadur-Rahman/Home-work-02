from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    blog_text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
