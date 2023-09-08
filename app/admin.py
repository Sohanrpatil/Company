from django.contrib import admin

# Register your models here.
from .models import Company,Problems,Student,Solution,Sol_progress

class CompanyAdmin(admin.ModelAdmin):

    list_display=['C_name','Owner_name','C_type']
    search_fields=['C_name']

admin.site.register(Company,CompanyAdmin)

class ProblemsAdmin(admin.ModelAdmin):

    list_display=['problem','image']


admin.site.register(Problems,ProblemsAdmin)
class StudentAdmin(admin.ModelAdmin):

    list_display=['Name','mob_no','branch']
    search_fields=['branch','Name']

admin.site.register(Student,StudentAdmin)

class SolutionAdmin(admin.ModelAdmin):
    list_display=['S_name','sol_name','Problem']

admin.site.register(Solution,SolutionAdmin)

class ProgressAdmin(admin.ModelAdmin):

    list_display=['sol','progress']

admin.site.register(Sol_progress,ProgressAdmin)
