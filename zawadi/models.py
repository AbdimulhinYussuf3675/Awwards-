from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField


# Create your models here.

class Profile(models.Model):
  profile_pic = models.ImageField(default='../static/images/defaul.jpg',upload_to='media/')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  
  @receiver(post_save , sender = User)
  def create_profile(instance,sender,created,**kwargs):
    if created:
      Profile.objects.create(user = instance)

  @receiver(post_save,sender = User)
  def save_profile(sender,instance,**kwargs):
    instance.profile.save()
    
class Projects(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/')
    project_description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    site = models.URLField()
    country = CountryField(default='NBO')

    def save_project(self):
        self.save()
    
    @classmethod
    def get_all_projects(cls):
        projects = Projects.objects.all()
        return projects
        
    @classmethod
    def get_post(cls, id):
        projects = Projects.objects.filter(user=id)
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects   

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title 