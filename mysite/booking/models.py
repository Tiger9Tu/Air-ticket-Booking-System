from django.db import models

# Create your models here.
class Mytable(models.Model):
    mytable_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
