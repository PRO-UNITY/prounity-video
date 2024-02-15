from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return self.title
