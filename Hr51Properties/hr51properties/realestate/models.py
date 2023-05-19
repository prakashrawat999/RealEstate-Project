from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
# Create your models here.

    
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="HR51")
    owner = models.CharField(max_length=20, default="Karan Bhadana")
    location = models.CharField(max_length=50, default="Faridabad")
    state = models.CharField(max_length=50,default="Haryana")
    country = models.CharField(max_length=50,default="India")
    url = models.CharField(max_length=100, null=True)
    owner_image = models.ImageField(upload_to='user/', null=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:5%;"  />'.format(self.owner_image))

    def __str__(self):
        return self.name + "   |   " + self.owner + "   |   " + self.location


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "Available"), 
    ("2", "Not Available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    PROP_ROOM = ( 
    ("1", "1BHK"), 
    ("2", "2BHK"), 
    ("3", "3BHK"), 
    ("4", "4BHK"), 
    ("5", "5BHK"), 
    ("6", "6BHK"), 
    ("7", "7BHK"), 
    )

    ROOMOWNERSHIP = (
    ("1", "First Owner"), 
    ("2", "Second Owners"),
    ("3", "Third Owners"),    
    ("4", "FreeHold"),    
    ("5", "Multiple Owners"),  
    )

    SIZERATE = (
    ("1", "1"), 
    ("2", "2"),
    ("3", "3"),    
    ("4", "4"),  
    ("5", "5"),  
    ("6", "6"),  
    ("7", "7"),  
    ("8", "8"),  
    )

    PROP_STATUS = ( 
    ("1", "For Sell"), 
    ("2", "For Rent/lease"), 
    ("3", "Not Available"),    
    ) 

    PROP_TYPE = ( 
    ("1", "Independent Builder Floor"), 
    ("2", "Builder Floor"), 
    ("3", "Not Available"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    title = models.CharField(max_length=50,null=True)
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    prop_status = models.CharField(max_length=50,choices = ROOM_STATUS, null=True)
    prop_sell = models.CharField(max_length=50,choices = PROP_STATUS, null=True)
    prop_type = models.CharField(max_length=50,choices = PROP_TYPE, null=True)
    property_bhk = models.CharField(max_length=50,choices = PROP_ROOM, null=True)
    capacity = models.IntegerField(null=True)
    propety_code = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField(null=True)
    yearbuild = models.IntegerField(null=True)
    address = models.CharField(max_length=150, null=True)
    ownership = models.CharField(max_length=150, null=True, choices= ROOMOWNERSHIP)
    Configuration = models.CharField(max_length = 800, null=True)
    content = models.CharField(max_length = 1500, null=True)
    flooring = models.CharField(max_length = 50, null=True)
    parking = models.CharField(max_length = 100, null=True)
    water_source = models.CharField(max_length = 100, null=True)
    widthroad = models.CharField(max_length = 100, null=True)
    powerbackup = models.CharField(max_length = 100, null=True)
    consider = models.CharField(max_length = 2000, null=True)
    nearby = models.CharField(max_length = 200, null=True)
    facing = models.CharField(max_length = 50, null=True)
    property_age = models.CharField(max_length = 10, null=True)
    furnished_details = models.CharField(max_length = 2000, null=True)
    loan_available = models.CharField(max_length=450, null=True)
    image = models.ImageField(upload_to='post/', null=True)
    image1 = models.ImageField(upload_to='post/', null=True)
    image2 = models.ImageField(upload_to='post/', null=True)
    image3 = models.ImageField(upload_to='post/', null=True)
    image4 = models.ImageField(upload_to='post/', null=True)
    url = models.CharField(max_length=100, null=True)
    map = models.CharField(max_length=450, null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:30px;height:30px;border-radius:10%;"  />'.format(self.image))

    def __str__(self):
        return self.hotel.name + self.title

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False, null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phoneno = models.IntegerField()
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name + ' - ' + self.email

class Feedback(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name + ' - ' + self.message