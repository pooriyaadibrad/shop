from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.category)
admin.site.register(models.customer)
admin.site.register(models.product)
admin.site.register(models.order)