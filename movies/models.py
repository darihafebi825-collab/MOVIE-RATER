from django.db import models
from django.contrib.auth.models import User

# ----------------------
# Movie Models
# ----------------------
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.reactions.filter(reaction='like').count()

    def dislikes_count(self):
        return self.reactions.filter(reaction='dislike').count()

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 1)
        return 0


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1-5

    class Meta:
        unique_together = ('movie', 'user')  # one rating per user

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title}: {self.rating}"


class MovieReaction(models.Model):
    movie = models.ForeignKey(Movie, related_name='reactions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=10, choices=[('like', 'Like'), ('dislike', 'Dislike')])

    class Meta:
        unique_together = ('movie', 'user')  # one reaction per user

    def __str__(self):
        return f"{self.user.username} reacted {self.reaction} to {self.movie.title}"


# ----------------------
# Contact Model
# ----------------------
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
