from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
# Create your models here.

# Category model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:5%;"  />'.format(self.image))

    def __str__(self):
        return self.title


# Post Mode
class Property(models.Model):
    PROP_STATUS = ( 
    ("1", "For Sell"), 
    ("2", "For Rent/lease"), 
    ("3", "Not Available"),    
    ) 

    PROP_TYPE = ( 
    ("1", "Semi Furnished"), 
    ("2", "Fully Furnished"),
    ("3", "Luxury"),    
    ("4", "Basic"),    
    )

    PROP_OWNER = ( 
    ("1", "First Owner"), 
    ("2", "Second Owners"),
    ("3", "Third Owners"),    
    ("4", "Multiple Owners"),    
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

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(max_length=50, choices = PROP_TYPE)
    status = models.CharField(max_length = 15, choices = PROP_STATUS)
    rooms = models.CharField(max_length = 15, choices = PROP_ROOM)
    ownership = models.CharField(max_length = 15, choices = PROP_OWNER)
    location = models.CharField(max_length=50, default="faridabad")
    property_price = models.IntegerField()
    property_size = models.IntegerField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    post_date = models.DateTimeField(auto_now_add=True, null=True)


    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:30px;height:30px;border-radius:10%;"  />'.format(self.image))

    def __str__(self):
        return self.title
    
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="hr51")
    owner = models.CharField(max_length=20, default="karan bhadana")
    location = models.CharField(max_length=50, default="faridabad")
    state = models.CharField(max_length=50,default="haryana")
    country = models.CharField(max_length=50,default="india")
    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
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
