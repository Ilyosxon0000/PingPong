from django.contrib import admin
from webapp.models import Table,Order,TableLog
# Register your models here.
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(TableLog)
