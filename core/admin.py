from django.contrib import admin
from . import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Item)
admin.site.register(models.Order)