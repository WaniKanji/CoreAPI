from django.contrib import admin
from .models import Kana
from .models import Kanji
from .models import KanjiReadings


class KanaAdmin(admin.ModelAdmin):
    list_display = ('writing', 'kana_type',)
    search_fields = ['writing',]
    list_filter = ('kana_type',)


class KanjiReadingInlineAdmin(admin.TabularInline):
    model = KanjiReadings
    extra = 1


class KanjiAdmin(admin.ModelAdmin):
    list_display = ('writing', 'meaning', 'date_created', 'date_updated')
    search_fields = ['writing', 'meaning']
    inlines = [KanjiReadingInlineAdmin,]

admin.site.register(Kanji, KanjiAdmin)
admin.site.register(Kana, KanaAdmin)
