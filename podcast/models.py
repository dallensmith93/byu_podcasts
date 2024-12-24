from django.db import models

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='podcast_covers/')

    def __str__(self):
        return self.title

class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    audio_file = models.FileField(upload_to='podcast_episodes/')
    published_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.podcast.title})"


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
