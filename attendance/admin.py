from django.contrib import admin
from .models import AttendanceRecord

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status', 'remarks')
    list_filter = ('status', 'date')
    search_fields = ('student__username',)
    ordering = ('-date',)

admin.site.register(AttendanceRecord, AttendanceAdmin)