
from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/',blank=True,null=True)
    bio = models.TextField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class DiaryEntry(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy'),
        ('Excited', 'Excited'),
        ('Calm', 'Calm'),
        ('Neutral', 'Neutral'),
        ('Sad', 'Sad'),
        ('Angry', 'Angry'),]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    mood = models.CharField(max_length=20,choices=MOOD_CHOICES,default='Neutral')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.title