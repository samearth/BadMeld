from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(profile)
admin.site.register(inventory)
admin.site.register(issue_item)
admin.site.register(complaints_posted)