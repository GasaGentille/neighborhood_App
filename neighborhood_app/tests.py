from django.test import TestCase
from .models import Neighbor,Profile,Business,Event

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        # Creating a new profile and saving it
        self.new_profile= Profile( f_name ='jacky')

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

   # Testing Save Method
    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles) > 0) 

    #test delete
    def test_delete_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.filter(f_name ='jacky').first()
        delete = Profile.objects.filter().delete()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles)==1)

class BusinessTestClass(TestCase):

    def setUp(self):
        # Creating a new profile and saving it
        self.new_business= Business( business_name ='Beaty saloon')

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

   # Testing Save Method
    def test_save_business(self):
        self.new_business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0) 

    #test delete
    def test_delete_business(self):
        self.new_business.save_business()
        business = Business.objects.filter(business_name ='Beaty saloon').first()
        delete = Business.objects.filter().delete()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses)==1)