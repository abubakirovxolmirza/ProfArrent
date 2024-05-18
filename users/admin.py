from django.contrib import admin
from .models import CustomUser, Admin, Moderator, User
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Moderator)
admin.site.register(User)