from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', 'content')}


admin.site.register(Article, ArticleAdmin)
