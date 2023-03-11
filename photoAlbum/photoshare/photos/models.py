from django.db import models

# Create your models here.

class Categorey(models.Model):
      name = models.CharField(max_length=150,null=False,blank=False)

      def __str__(self) -> str:
            return self.name

class Photo(models.Model):
      categorey = models.ForeignKey(Categorey,null=True,blank=True,on_delete=models.SET_NULL)
      image = models.ImageField(null=False,blank=False)
      description = models.CharField(max_length=500,null=False,blank=False)

      def __str__(self) -> str:
            return self.description