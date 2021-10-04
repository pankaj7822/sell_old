from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone



# Create your models here.
'''
If null is True, Django will store empty values as NULL in the database. Default is False
null is purely database-related, whereas blank is validation-related. If a field has blank=True
validation on Django’s admin site will allow entry of an empty value. If a field has blank=False, the field will be required. 

The related_name attribute specifies the name of the reverse relation
for more:
https://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
 '''

class Catagory(models.Model):
    title=models.CharField(max_length=200,blank=False,null=False)
    class Meta:
         verbose_name_plural = "Catagories"
    def __str__(self):
        return self.title

class Subcatagory(models.Model):
    title=models.CharField(max_length=200,blank=False,null=False)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE, related_name="subcatagories")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Subcatagories"
    



 
class Ad(models.Model):
    title=models.CharField(max_length=200,blank=True,null=False)
    description=models.CharField(max_length=500,blank=True,null=False)
    time_added=models.DateTimeField(editable=False) #Note that editable=False Doest not appers in admin panel
    time_updated=models.DateTimeField()
    price=models.IntegerField(blank=True,null=False)
    published=models.BooleanField(default=False)
    subcatagory=models.ForeignKey(Subcatagory,on_delete=models.CASCADE, related_name="ads",blank=True)
    images=ArrayField(models.CharField(max_length=200), blank=True,null=True)
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.time_added=timezone.now()
        self.time_updated=timezone.now()
        return super(Ad,self).save(*args,**kwargs)
            
        
    
    
    class Meta:
        verbose_name_plural="Ads"
    def __str__(self):
        return self.title