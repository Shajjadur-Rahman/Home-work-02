from django.db import models

class District(models.Model):
    name = models.CharField(max_length=150)
    dis_info = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
