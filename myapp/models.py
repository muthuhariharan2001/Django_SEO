from django.db import models

class Admin():
    name = models.TextField(max_length = 20)
    email = models.EmailField()
    age = models.IntegerField(default=18, blank=True)
