from django.contrib import admin

from ohs_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Register)
admin.site.register(models.worker_register)
admin.site.register(models.complaints)
admin.site.register(models.schedule)
admin.site.register(models.take_appoinments)
admin.site.register(models.Bill)
admin.site.register(models.CreditCard)