from django.db import models

class StudentInfo(models.Model):
    name = models.CharField(max_length=200)
    std_cls = models.CharField(max_length=100)
    std_roll = models.IntegerField()

    def __str__(self):
        return self.name
