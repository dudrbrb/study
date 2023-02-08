from django.contrib import admin
from .models import Works, Stacks
# Register your models here.

class WorksAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Works information', {'fields': ['title', 'link', 'description', 'date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'link', 'description', 'date')
   
    # 검색 필터링
    search_fields = ['title']
    

admin.site.register(Works, WorksAdmin)
admin.site.register(Stacks)