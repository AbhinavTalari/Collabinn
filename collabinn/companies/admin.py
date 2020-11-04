from .models import Company,CollabRequest,Company_Profile
from django.contrib import admin
# Register your models here.




# admin.py


class RelationshipInline(admin.StackedInline):
    model = CollabRequest
    fk_name = 'from_user'

class CompanyAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Company_Profile)




