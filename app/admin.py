from django.contrib import admin
from .models import Evenement
from .models import Visitor
from .models import PlayedTrack

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin')
    search_fields = ('titre', 'description')
    list_filter = ('date_debut', 'date_fin')

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'path', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('ip_address', 'path')

admin.site.register(Visitor, VisitorAdmin)

class PlayedTrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'played_at', 'cover_preview')
    list_filter = ('artist', 'played_at')
    search_fields = ('title', 'artist')
    readonly_fields = ('cover_preview',)

    def cover_preview(self, obj):
        if obj.cover:
            return f'<img src="{obj.cover.url}" width="50" height="50" />'
        return "No cover"
    cover_preview.allow_tags = True
    cover_preview.short_description = 'Cover Preview'

admin.site.register(PlayedTrack, PlayedTrackAdmin)
