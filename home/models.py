from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50,verbose_name="Basliq")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True,verbose_name="Vaxt")

    def __str__(self):
        return self.title
