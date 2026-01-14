from django.contrib import admin
from .models import Movie, Comment, MovieRating, MovieReaction

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_rating', 'likes_count', 'dislikes_count')
    search_fields = ('title',)
    readonly_fields = ('likes_count', 'dislikes_count', 'average_rating')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'text', 'created_at')
    search_fields = ('user__username', 'movie__title', 'text')

@admin.register(MovieRating)
class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating')
    search_fields = ('user__username', 'movie__title')

@admin.register(MovieReaction)
class MovieReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'reaction')
    search_fields = ('user__username', 'movie__title')
