from .models import Company,CollabRequest,Company_Profile
from django.contrib import admin
# Register your models here.




# admin.py


class RelationshipInlineTo(admin.StackedInline):
    model = CollabRequest
    fk_name = 'to_user'

class RelationshipInlineFrom(admin.StackedInline):
    model = CollabRequest
    fk_name = 'from_user'

class CompanyAdmin(admin.ModelAdmin):
    inlines = [RelationshipInlineTo, RelationshipInlineFrom]
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        unfiltered = super(CompanyAdmin, self).get_inline_instances(request, obj)
        if obj.relationships.all():
            return [x for x in unfiltered if isinstance(x,RelationshipInlineTo)]
        else:
            return [x for x in unfiltered if isinstance(x,RelationshipInlineFrom)]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Company_Profile)
