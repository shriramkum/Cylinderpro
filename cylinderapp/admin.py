from django.contrib import admin
from.models import cylinder

class Cylinderadmin(admin.ModelAdmin):
    list_display = ['id','address','Business_Name','person_Name','contact','Verified_status','TimeStamp']

admin.site.register(cylinder,Cylinderadmin)