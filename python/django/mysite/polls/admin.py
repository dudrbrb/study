from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # 우측 목록 필터링
    list_filter = ['pub_date']
    # 검색 필터링
    search_fields = ['question_text']
    # 선택목록 추가
    inlines = [ChoiceInline]
    

admin.site.register(Question, QuestionAdmin)