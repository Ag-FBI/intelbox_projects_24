from django.db import models

# Create your models here.
class Info(models.Model):
    text = models.CharField(max_length=100)
    bbox = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Info"

    def __str__(self):
        return self.text
