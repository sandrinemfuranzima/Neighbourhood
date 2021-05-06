from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Neighbourhood(models.Model):
    HOODS = (
    ('Rwamagana','Rwamagana',),
    ('kigali','kigali'),
    ('kicukiro','kicukiro'),
    ('Nyamirambo','Nyamirambo'), 
    )
    hood_name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50,choices=HOODS)
    hood_description  = models.TextField(max_length=100)
    hood_count = models.IntegerField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="" )
    

    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()
    
    @classmethod
    def search_hood(cls, search_term):
        hoods = cls.objects.filter(hood_location__icontains = search_term)
        return hoods

    
    def __str__(self):
        return self.hood_name

    
class Business(models.Model):
    biz_name = models.CharField(max_length=50)
    biz_email = models.EmailField()
    biz_description = models.CharField(max_length=1000)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_biz(self):
        self.save()

    def delete_biz(self):
        self.delete()


    @classmethod
    def search_biz(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    def __str__(self):
        return self.biz_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=200,default = "Awesome bio will appear here")

    def __str__(self):
        return self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

class Join(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    hood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id

class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length = 1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment



