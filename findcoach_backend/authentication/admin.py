from django.contrib import admin
from .models import User, Profile, Coach, Client, CoachClient, CoachCategory

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Coach)
admin.site.register(Client)
admin.site.register(CoachClient)
admin.site.register(CoachCategory)