from django.contrib import admin
from quiz.models import Quiz


# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at', 'updated_at']
    list_display_links = ['pk', 'title']