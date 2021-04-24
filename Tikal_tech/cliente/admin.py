from django.contrib import admin
from .models import Client
from .models import Telephone
from .models import Email


admin.site.register(Client)
admin.site.register(Telephone)
admin.site.register(Email)