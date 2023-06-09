from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Realator, PropertyView, Reservation, Contact, Feedback
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
import random
# Create your views here.


def allpost(request):
    posts = PropertyView.objects.all()[:11]
    categories = Realator.objects.all()
    data = {
        'posts': posts,
        'categories': categories
    }
    return render(request, "allpost.html", data)


def page401(request):
    return render(request, "401.html")


def page404(request):
    return render(request, "404.html")


def page500(request):
    return render(request, "500.html")


def privacypage(request):
    return render(request, "privacy.html")


def termspage(request):
    return render(request, "terms.html")


def propertydetails(request, url):
    room = PropertyView.objects.get(url=url)
    # print(post)
    return render(request, 'propertydetails.html', {'room': room, })


# homepage
def homepage(request):
    all_location = Realator.objects.values_list(
        'location', 'id').distinct().order_by()
    posts = PropertyView.objects.all()[:11]
    categories = Realator.objects.all()
    if request.method == "POST":
        try:
            print(request.POST)
            hotel = Realator.objects.all().get(
                id=int(request.POST['search_location']))
            rr = []

            # for finding the reserved PropertyView on this time period for excluding from the query set
            for each_reservation in Reservation.objects.all():
                if str(each_reservation.check_in) < str(request.POST['cin']) and str(each_reservation.check_out) < str(request.POST['cout']):
                    pass
                elif str(each_reservation.check_in) > str(request.POST['cin']) and str(each_reservation.check_out) > str(request.POST['cout']):
                    pass
                else:
                    rr.append(each_reservation.room.id)

            room = PropertyView.objects.all().filter(
                hotel=hotel, capacity__gte=int(request.POST['capacity'])).exclude(id__in=rr)
            if len(room) == 0:
                messages.warning(
                    request, "Sorry No Properties are Available on this time period")
            data = {'rooms': room, 'all_location': all_location, 'flag': True}
            response = render(request, 'index.html', data)
        except Exception as e:
            messages.error(request, e)
            response = render(request, 'index.html', {
                              'all_location': all_location})
    else:
        reveiw = Feedback.objects.all()
        data = {
            'all_location': all_location,
            'posts': posts,
            'categories': categories,
            'own': reveiw
            }
        response = render(request, 'index.html', data)
    return HttpResponse(response)

# about


def aboutpage(request):
    return HttpResponse(render(request, 'about.html'))

# property


def propertypage(request):
    all_location = Realator.objects.values_list(
        'location', 'id').distinct().order_by()
    if request.method == "POST":
        try:
            print(request.POST)
            hotel = Realator.objects.all().get(
                id=int(request.POST['search_location']))
            rr = []

            # for finding the reserved rooms on this time period for excluding from the query set

            room = PropertyView.objects.all().filter(
                hotel=hotel, capacity__gte=int(request.POST['capacity'])).exclude(id__in=rr)
            if len(room) == 0:
                messages.warning(
                    request, "Sorry No Properties are Available on this time period")
            data = {'rooms': room, 'all_location': all_location, 'flag': True}
            response = render(request, 'property.html', data)
        except Exception as e:
            messages.warning(request, "Please Select All Section | Area | Location ")
 #           messages.error(request, e)
            response = render(request, 'property.html', {
                              'all_location': all_location})
    else:
        data = {'all_location': all_location}
        response = render(request, 'property.html', data)
    return HttpResponse(response)

# reveiw


def reveiwpage(request):
    return HttpResponse(render(request, 'reveiw.html'))

# contact page


def contactpage(request):
    if request.method == 'POST':
        print("submitted")
        name = request.POST['name']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        content = request.POST['content']
        if len(name) < 4 or len(email) < 5 or len(phoneno) < 9 or len(content) < 6:
            messages.error(request, "Please Enter Correct Details")
        else:
            contact = Contact(name=name, email=email,
                              phoneno=phoneno, content=content)
            contact.save()
            messages.success(request, "Successfully Sent")
    # return render(request, 'contact.html')
    return HttpResponse(render(request, 'contact.html'))


# contact page
def feedbackpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['content']
        if len(name) < 4 or len(message) < 10:
            messages.error(request, "Invalid Form Data")
        else:
            feedback = Feedback(name=name, message=message)
            feedback.save()
            messages.success(request, "Successfully Sent")
    # return render(request, 'contact.html')
    return HttpResponse(render(request, 'feedback.html'))

# user sign up


def user_sign_up(request):
    if request.method == "POST":
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.warning(request, "Password didn't matched")
            return redirect('userloginpage')
        
        if len(user_name)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')
        
        if not user_name.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        try:
            if User.objects.all().get(username=user_name):
                messages.warning(request, "Username Not Available")
                return redirect('userloginpage')
        except:
            pass

        new_user = User.objects.create_user(
            username=user_name, email=email, password=password1)
        new_user.is_superuser = False
        new_user.is_staff = False
        new_user.save()
        messages.success(request, "Registration Successfull")
        return redirect("userloginpage")
    return HttpResponse('Access Denied')
# staff sign up


def staff_sign_up(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.success(request, "Password didn't Matched")
            return redirect('staffloginpage')
        try:
            if User.objects.all().get(username=user_name):
                messages.warning(request, "Username Already Exist")
                return redirect("staffloginpage")
        except:
            pass

        new_user = User.objects.create_user(
            username=user_name, password=password1)
        new_user.is_superuser = False
        new_user.is_staff = True
        new_user.save()
        messages.success(request, " Staff Registration Successfull")
        return redirect("staffloginpage")
    else:

        return HttpResponse('Access Denied')
# user login and signup page


def user_log_sign_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pswd']

        user = authenticate(username=email, password=password)
        try:
            if user.is_staff:
                login(request, user)
                messages.success(request, "successful logged in")
                return redirect('staffpanel')
            # if user.is_staff:

                # messages.error(request,"Incorrect username or Password")
                # return redirect('staffloginpage')
        except:
            pass

        if user is not None:
            login(request, user)
            messages.success(request, "successful logged in")
            print("Login successfull")
            return redirect('homepage')
        else:
            messages.warning(request, "Incorrect username or password")
            return redirect('userloginpage')

    response = render(request, 'user/userlogsign.html')
    return HttpResponse(response)

# logout for admin and user


def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        messages.success(request, "Logged out successfully")
        print("Logged out successfully")
        return redirect('homepage')
    else:
        print("logout unsuccessfull")
        return redirect('userloginpage')

# staff login and signup page


def staff_log_sign_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user.is_staff:
            login(request, user)
            return redirect('staffpanel')
        

        else:
            messages.success(request, "Incorrect username or password")
            return redirect('staffloginpage')
    response = render(request, 'staff/stafflogsign.html')
    return HttpResponse(response)

# staff panel page


@login_required(login_url='/staff')
def panel(request):

    if request.user.is_staff == False:
        return HttpResponse('Access Denied')

    rooms = PropertyView.objects.all()
    total_rooms = len(rooms)
    available_rooms = len(PropertyView.objects.all().filter(status='1'))
    unavailable_rooms = len(PropertyView.objects.all().filter(status='2'))
    reserved = len(Reservation.objects.all())

    hotel = Realator.objects.values_list(
        'location', 'id').distinct().order_by()

    response = render(request, 'staff/panel.html', {'location': hotel, 'reserved': reserved, 'rooms': rooms,
                      'total_rooms': total_rooms, 'available': available_rooms, 'unavailable': unavailable_rooms})
    return HttpResponse(response)

# for editing room information


@login_required(login_url='/staff')
def edit_room(request):
    if request.user.is_staff == False:
        return HttpResponse('Access Denied')
    if request.method == 'POST' and request.user.is_staff:
        print(request.POST)
        old_room = PropertyView.objects.all().get(
            id=int(request.POST['roomid']))
        hotel = Realator.objects.all().get(id=int(request.POST['hotel']))
        old_room.room_type = request.POST['roomtype']
        old_room.capacity = int(request.POST['capacity'])
        old_room.price = int(request.POST['price'])
        old_room.size = int(request.POST['size'])
        old_room.hotel = hotel
        old_room.status = request.POST['status']
        old_room.room_number = int(request.POST['roomnumber'])

        old_room.save()
        messages.success(request, "Property Details Updated Successfully")
        return redirect('staffpanel')
    else:

        room_id = request.GET['roomid']
        room = PropertyView.objects.all().get(id=room_id)
        response = render(request, 'staff/editroom.html', {'room': room})
        return HttpResponse(response)

# for adding room


@login_required(login_url='/staff')
def add_new_room(request):
    if request.user.is_staff == False:
        return HttpResponse('Access Denied')
    if request.method == "POST":
        total_rooms = len(PropertyView.objects.all())
        new_room = PropertyView()
        hotel = Realator.objects.all().get(id=int(request.POST['hotel']))
        print(f"id={hotel.id}")
        print(f"name={hotel.name}")

        new_room.roomnumber = total_rooms + 1
        new_room.room_type = request.POST['roomtype']
        new_room.capacity = int(request.POST['capacity'])
        new_room.size = int(request.POST['size'])
        new_room.hotel = hotel
        new_room.status = request.POST['status']
        new_room.price = request.POST['price']
        new_room.title = request.POST['title']
        new_room.prop_type = request.POST['proptype']
        new_room.prop_sell = request.POST['sell']
        new_room.property_bhk = request.POST['bhk']
        new_room.propety_code = int(request.POST['code'])
        new_room.yearbuild = int(request.POST['build'])
        new_room.address = request.POST['address']
        new_room.ownership = request.POST['ownership']
        new_room.Configuration = request.POST['Configuration']
        new_room.content = request.POST['content']
        new_room.flooring = request.POST['flooring']
        new_room.parking = request.POST['parking']
        new_room.water_source = request.POST['water']
        new_room.powerbackup = request.POST['powerbackup']
        new_room.consider = request.POST['consider']
        new_room.nearby = request.POST['nearby']
        new_room.facing = request.POST['facing']
        new_room.property_age = request.POST['age']
        new_room.furnished_details = request.POST['furnished']
        new_room.loan_available = request.POST['loan']
        new_room.image = request.POST['image']
        new_room.image1 = request.POST['image1']
        new_room.image2 = request.POST['image2']
        new_room.image3 = request.POST['image3']
        new_room.image4 = request.POST['image4']
        new_room.map = request.POST['map']
        new_room.url = request.POST['url']

        new_room.save()
        messages.success(request, "New Property Added Successfully")

    return redirect('staffpanel')

# booking room page


@login_required(login_url='/user')
def book_room_page(request):
    room = PropertyView.objects.all().get(id=int(request.GET['roomid']))
    return HttpResponse(render(request, 'user/bookroom.html', {'room': room}))

# For booking the room


@login_required(login_url='/user')
def book_room(request):

    if request.method == "POST":

        room_id = request.POST['room_id']

        room = PropertyView.objects.all().get(id=room_id)
        # for finding the reserved PropertyView on this time period for excluding from the query set
        for each_reservation in Reservation.objects.all().filter(room=room):
            if str(each_reservation.check_out) < str(request.POST['check_out']):
                pass
            elif str(each_reservation.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(
                    request, "Sorry This Property is unavailable for Booking")
                return redirect("homepage")

        current_user = request.user
        # total_p = int( request.POST['person'])
        booking_id = str(room_id) + str(datetime.datetime.now())

        reservation = Reservation()
        # generate random number
        book_id_generate = random.random()

        reservation.booking_id = book_id_generate
        room_object = PropertyView.objects.all().get(id=room_id)
        room_object.status = '2'

        user_object = User.objects.all().get(username=current_user)

        reservation.guest = user_object
        reservation.room = room_object
        # person = total_p
        # reservation.check_in = request.POST['check_in']
        reservation.check_out = request.POST['check_out']

        reservation.save()

        messages.success(request, "Booking Successfull")

        return redirect("homepage")
    else:
        return HttpResponse('Access Denied')


def handler404(request):
    return render(request, '404.html', status=404)


@login_required(login_url='/staff')
def view_room(request):
    room_id = request.GET['roomid']
    room = PropertyView.objects.all().get(id=room_id)

    reservation = Reservation.objects.all().filter(room=room)
    return HttpResponse(render(request, 'staff/viewroom.html', {'room': room, 'reservations': reservation}))


@login_required(login_url='/user')
def user_bookings(request):
    if request.user.is_authenticated == False:
        return redirect('userloginpage')
    user = User.objects.all().get(id=request.user.id)
    print(f"request user id ={request.user.id}")
    bookings = Reservation.objects.all().filter(guest=user)
    if not bookings:
        messages.warning(request, "No Bookings Found")
    return HttpResponse(render(request, 'user/mybookings.html', {'bookings': bookings}))


@login_required(login_url='/staff')
def add_new_location(request):
    if request.method == "POST" and request.user.is_staff:
        owner = request.POST['new_owner']
        location = request.POST['new_city']
        state = request.POST['new_state']
        country = request.POST['new_country']

        hotels = Realator.objects.all().filter(location=location, state=state)
        if hotels:
            messages.warning(
                request, "Sorry City at this Location already exist")
            return redirect("staffpanel")
        else:
            new_hotel = Realator()
            new_hotel.owner = owner
            new_hotel.location = location
            new_hotel.state = state
            new_hotel.country = country
            new_hotel.save()
            messages.success(
                request, "New Location Has been Added Successfully")
            return redirect("staffpanel")

    else:
        return HttpResponse("Not Allowed")

# for showing all bookings to staff


@login_required(login_url='/staff')
def all_bookings(request):

    bookings = Reservation.objects.all()
    if not bookings:
        messages.warning(request, "No Bookings Found")
    return HttpResponse(render(request, 'staff/allbookings.html', {'bookings': bookings}))
