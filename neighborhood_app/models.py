from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbor(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length=30,null=True)
    occupants_count = models.IntegerField(default=0,null=True)
    admin = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    
    def __str__(self):
        return self.name

    @classmethod
    def create_neighborhood(self):
        self.save()
      
    @classmethod
    def delete_neighborhood(self):
        self.delete()
    
    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood
    
    def update_neighborhood():
        self.update()

    def update_occupants():
        occupants = self.update_occupants.update()
        return occupants

class Profile(models.Model):
    f_name  = models.CharField(max_length= 30,null=True)
    l_name  = models.CharField(max_length= 30, null=True)
    general_location = models.CharField(max_length= 30,null=True)
    neighborhood= models.ForeignKey(Neighbor,null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)

   
    def __str__(self):
        return self.f_name

    def save_profile(self):
        self.save
    
    def delete_profile(self):
        self.delete()

    def update_profile(self):  
        self.update() 

class Business(models.Model):
    business_name = models.CharField(max_length= 30,null=True)
    neighborhood = models.ForeignKey(Neighbor,null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    email= models.EmailField(max_length= 30,null=True)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()
    
    @classmethod
    def search_by_name(cls,search_term):
        business_name = cls.objects.filter(business_name__icontains=search_term)
        return business_name
    
    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighbor=neighborhood.id
        neighbor1 = cls.objects.get(neighbor=neighborhood_id)
        return neighbor

class Event(models.Model):
    description = models.CharField(max_length= 30)
    neighborhood = models.ForeignKey(Neighbor)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()
   
     


