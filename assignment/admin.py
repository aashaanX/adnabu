from django.contrib import admin

# Register your models here.
from assignment.models import URequest, UUrl

admin.site.register(URequest)
admin.site.register(UUrl)
