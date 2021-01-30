from django.db import models

class Count(models.Model):
    counting_text = models.TextField(max_length=10000,blank=False,null=True,verbose_name='Enter text')
    result = models.CharField(max_length=100,blank=False,null=True)

    class Meta:
        ordering = ['id']

