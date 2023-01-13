from django.db import models

# Create your models here.
class Text(models.Model):
    plaintext=models.CharField(max_length=500)
    #latextext=models.CharField(max_length=100)
    finaltext=models.CharField(max_length=500,default="")