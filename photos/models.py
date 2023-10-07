from django.db import models

# Create your models here.
class Photo(models.Model):
    upload = models.ImageField(upload_to="photos/% Y/% m/% d/")
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)