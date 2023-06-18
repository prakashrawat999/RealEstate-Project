from django.contrib import admin

# Register your models here.
from .models import Realator,PropertyView,Reservation, Contact, Feedback

admin.site.site_header = 'HR51 Properties'
admin.site.index_title = 'HR51 Properties'                
admin.site.site_title = 'HR51 Properties'

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
    list_filter = ('title','prop_status', 'property_bhk',)
    list_per_page = 25

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','timeStamp')
    list_filter = ('timeStamp',)
    search_fields = ('email',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')
    list_filter = ('timeStamp',)
    search_fields = ('name',)

class ReservAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'check_out', 'room', 'guest',)
    list_filter = ('booking_id', 'check_out',)
    search_fields = ('booking_id',)

# Register your models here.
admin.site.register(Realator, RealatorAdmin)
admin.site.register(PropertyView, PropertyAdmin)
admin.site.register(Reservation, ReservAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Feedback, FeedbackAdmin)