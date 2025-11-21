from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    rejissor = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.FileField(upload_to='media')




    def __str__(self):
        return self.title
    

    