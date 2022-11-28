from django.contrib import admin
from .models import Task

# admin.site.register(Task)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_complete', 'created')
    list_filter = ['is_complete']
    actions = ['completed']

    def completed(self, request, queryset):
        queryset.update(is_complete=True)

