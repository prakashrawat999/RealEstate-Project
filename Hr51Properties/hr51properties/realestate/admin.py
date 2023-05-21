from django.contrib import admin

# Register your models here.
from .models import Hotels,Rooms,Reservation, Contact

# for configuration of Category admin
class HotelAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'owner','add_date')
    list_display_links = ('image_tag', 'name',)
    search_fields = ('name',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'is_published', 'prop_status','post_date',)
    list_display_links = ('image_tag', 'title',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('room_type',)
    list_per_page = 25

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneno',)
    search_fields = ('email',)


# Register your models here.
admin.site.register(Hotels, HotelAdmin)
admin.site.register(Rooms, RoomAdmin)
admin.site.register(Reservation)
admin.site.register(Contact, ContactAdmin)