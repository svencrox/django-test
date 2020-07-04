from django.db import models

class uploaded_file(models.Model):
    title = models.CharField(max_length = 200)
    content = models.FileField()

    def __str__(self):
        return self.title