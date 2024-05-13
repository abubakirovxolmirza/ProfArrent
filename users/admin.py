from django.contrib import admin
from .models import User, Admin, Moderator
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Moderator)