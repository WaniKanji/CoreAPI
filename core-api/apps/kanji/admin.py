from django.contrib import admin
from apps.kanji.models import Kanji
from apps.kanji.models import KanjiReadings


class KanjiReadingInlineAdmin(admin.TabularInline):
    model = KanjiReadings
    extra = 1


class KanjiAdmin(admin.ModelAdmin):
    list_display = ('writing', 'meaning', 'date_created', 'date_updated')
    search_fields = ['writing', 'meaning']
    inlines = [KanjiReadingInlineAdmin,]

admin.site.register(Kanji, KanjiAdmin)
