from django.contrib import admin

# Register your models here.
from .models import Hotels,Rooms,Reservation, Contact, Category, Property

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'add_date')
    search_fields = ('title',)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','cat','post_date',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneno',)
    search_fields = ('email',)


# Register your models here.
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Property, PropertyAdmin)