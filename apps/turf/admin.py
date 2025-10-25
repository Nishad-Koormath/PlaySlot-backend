from django.contrib import admin
from .models import Turf, TurfImage

class TurfImageInline(admin.TabularInline):
    model = TurfImage
    extra = 1
    
@admin.register(Turf)
class TrufAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'location', 'day_price_per_hour', 'night_price_per_hour',
                    'day_start_time', 'night_start_time', 'is_active')
    list_filter = ('is_active', 'location')
    search_fields = ('name', 'location', 'owner__username')
    inlines = [TurfImageInline]
    
admin.site.register(TurfImage)