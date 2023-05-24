from django.contrib import admin
from .models.cases import (
    CaseResultText,
    Cases,
    CaseTaskText
)
from .models.podcasts import Podcasts, PodcastLink


class PodcastLinkInline(admin.TabularInline):
    model = PodcastLink


class CaseResultTextInline(admin.TabularInline):
    model = CaseResultText


class CaseTaskTextInline(admin.TabularInline):
    model = CaseTaskText


@admin.register(Podcasts)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'listening_count', 'published_at')
    list_filter = ('published_at', )

    inlines = [PodcastLinkInline]


@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    list_display = ('title', 'case_type', 'desc')
    list_filter = ('case_type', )

    inlines = [CaseTaskTextInline, CaseResultTextInline]
