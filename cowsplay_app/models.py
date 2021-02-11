from django.db import models

class Cow_Model(models.Model):
    text = models.TextField(max_length=50)

    def __str__(self):
        return self.text
