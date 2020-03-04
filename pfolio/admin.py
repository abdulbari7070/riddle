from django.contrib import admin

# Register your models here.
from .models import Pfolio,About,Contact


admin.site.register(Pfolio)
admin.site.register(About)
admin.site.register(Contact)