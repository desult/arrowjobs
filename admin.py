from django.contrib import admin

from .models import Asp, Contact

class AspAdmin(admin.ModelAdmin):
    list_display = ['design_id', 'description', 'date_in']
    list_filter = ['date_in']
    search_fields = ['description']
    class Meta:
        model = Asp


admin.site.register(Asp, AspAdmin)
admin.site.register(Contact)
