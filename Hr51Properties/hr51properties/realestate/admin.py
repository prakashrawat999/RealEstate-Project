from django.contrib import admin

# Register your models here.
from .models import Realator,PropertyView,Reservation, Contact

# for configuration of Category admin
class RealatorAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'owner', 'name', 'add_date')
    list_display_links = ('image_tag', 'name',)
    list_filter = ('owner', 'name',)
    search_fields = ('name',)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'is_published', 'prop_status','post_date',)
    search_fields = ('title',)
    list_editable = ('prop_status',)
    list_filter = ('hotel', 'prop_status', 'property_bhk',)
    list_per_page = 25

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneno', 'timeStamp')
    list_filter = ('timeStamp',)
    search_fields = ('email',)

class ReservAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'check_out', 'room', 'guest',)
    list_filter = ('booking_id', 'check_out',)
    search_fields = ('booking_id',)

# Register your models here.
admin.site.register(Realator, RealatorAdmin)
admin.site.register(PropertyView, PropertyAdmin)
admin.site.register(Reservation, ReservAdmin)
admin.site.register(Contact, ContactAdmin)