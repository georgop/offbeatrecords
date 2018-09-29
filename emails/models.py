from django.db import models


class info(models.Model):
    email=models.EmailField(max_length=500)
    def __str__(self):
        return '{}'.format(self.email)
