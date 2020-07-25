from django.contrib import admin
from .models import TimeTableModel

@admin.register(TimeTableModel)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_workout', 'description', 'date']
    fieldsets = (
        ('General info', {
         'fields': ('name_workout', 'description')
         }),
    )
