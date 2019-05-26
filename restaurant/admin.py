from django.contrib import admin

# Register your models here.
from .models import(
    client,
    ofitsiant,
    oshpaz,
    kassa
)
admin.site.register(client)
admin.site.register(ofitsiant)
admin.site.register(oshpaz)
admin.site.register(kassa)