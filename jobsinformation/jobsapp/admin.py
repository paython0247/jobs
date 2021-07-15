from django.contrib import admin
from jobsapp.models import Hydjobs
from jobsapp.models import Punejobs
from jobsapp.models import Chennaijobs
from jobsapp.models import Banglorejobs
from jobsapp .models import Student
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','email','phonenumber']
admin.site.register(Hydjobs,HydjobsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','email','phonenumber']
admin.site.register(Punejobs,PunejobsAdmin)




class ChennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','email','phonenumber']
admin.site.register(Chennaijobs,ChennaijobsAdmin)



class BanglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','email','phonenumber']
admin.site.register(Banglorejobs,BanglorejobsAdmin)



class StudentAdmin(admin.ModelAdmin):
	list_display=['name','marks','add','mobile','email']
admin.site.register(Student,StudentAdmin)
