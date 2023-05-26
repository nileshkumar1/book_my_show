from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(booking)
class bookingModelAdmin(admin.ModelAdmin):
    class Meta:
        model = booking
        fields = ['name','age','row_num', 'col_num','show', 'user','status','session']