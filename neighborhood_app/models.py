from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NeighborHood(models.Model):
    name=models.CharField(max_length =50)
    location=models.CharField(max_length =50)
    occupants_count=models.IntegerField(default=0)
    admin=models.ForeignKey(User,on_delete=models.CASCADE)

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
        occupants=self.update_occupants.update()       
        return occupants

class Profile(models.Model):
    
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    neighborhood=models.ForeignKey(NeighborHood)
    user=models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()     

    def update_profile(self):
        self.update()       


class BusinessClass(models.Model):
    business_name=models.CharField(max_length =50)
    neighborhood=models.ForeignKey(NeighborHood)
    profile=models.ForeignKey(Profile)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email_address=models.EmailField()


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        biz=cls.objects.filter(id=business_id)
        return biz

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighbor=neighborhood.id
        neighbor1 = cls.objects.get(neighbor=neighborhood_id)
        return neighbor   

    def update_business(self):
        self.update()

class Event(models.Model):
    description=models.CharField(max_length =50)
    neighborhood=models.ForeignKey(NeighborHood,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    


    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete() 

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighbor=neighborhood.id
        neighbor1 = cls.objects.get(neighbor=neighborhood_id)
        return neighbor   


